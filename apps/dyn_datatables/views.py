import json
import math
import random
import string

from django.core.exceptions import ValidationError
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from apps.models import Utils

from core.settings import DYNAMIC_DATATB
from django.db.models.fields import DateField

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import base64
import os


# TODO: 404 for wrong page number
def data_table_view(request, **kwargs):
    try:
        model_class = Utils.get_class(DYNAMIC_DATATB, kwargs.get('model_name'))
    except KeyError:
        return render(request, '404.html', status=404)
    headings = [field.name for field in model_class._meta.get_fields()]

    page_number = int(request.GET.get('page', 1))
    search_key = request.GET.get('search', '')
    entries = int(request.GET.get('entries', 10))

    if page_number < 1:
        return render(request, '404.html', status=404)

    filter_options = Q()
    for field in headings:
        filter_options = filter_options | Q(**{field + '__icontains': search_key})
    all_data = model_class.objects.filter(filter_options)
    data = all_data[(page_number - 1) * entries:page_number * entries]
    if all_data.count() != 0 and not 1 <= page_number <= math.ceil(all_data.count() / entries):
        return render(request, '404.html', status=404)
    return render(request, 'index.html', context={
        'model_name': kwargs.get('model_name'),
        'headings': headings,
        'data': [[getattr(record, heading) for heading in headings] for record in data],
        'is_date': [True if type(field) == DateField else False for field in model_class._meta.get_fields()],
        'total_pages': range(1, math.ceil(all_data.count() / entries) + 1),
        'has_prev': False if page_number == 1 else (
            True if all_data.count() != 0 else False),
        'has_next': False if page_number == math.ceil(all_data.count() / entries) else (
            True if all_data.count() != 0 else False),
        'current_page': page_number,
        'entries': entries,
        'search': search_key,
    })


@csrf_exempt
def add_record(request, **kwargs):
    try:
        model_manager = Utils.get_manager(DYNAMIC_DATATB, kwargs.get('model_name'))
    except KeyError:
        return HttpResponse(json.dumps({
            'message': 'this model is not activated or not exist.',
            'success': False
        }), status=400)
    body = json.loads(request.body.decode("utf-8"))
    try:
        thing = model_manager.create(**body)
    except Exception as ve:
        return HttpResponse(json.dumps({
            'detail': str(ve),
            'success': False
        }), status=400)
    return HttpResponse(json.dumps({
        'id': thing.id,
        'message': 'Record Created.',
        'success': True
    }), status=200)


@csrf_exempt
def delete_record(request, **kwargs):
    try:
        model_manager = Utils.get_manager(DYNAMIC_DATATB, kwargs.get('model_name'))
    except KeyError:
        return HttpResponse(json.dumps({
            'message': 'this model is not activated or not exist.',
            'success': False
        }), status=400)
    to_delete_id = kwargs.get('id')
    try:
        to_delete_object = model_manager.get(id=to_delete_id)
    except Exception:
        return HttpResponse(json.dumps({
            'message': 'matching object not found.',
            'success': False
        }), status=404)
    to_delete_object.delete()
    return HttpResponse(json.dumps({
        'message': 'Record Deleted.',
        'success': True
    }), status=200)


@csrf_exempt
def edit_record(request, **kwargs):
    try:
        model_manager = Utils.get_manager(DYNAMIC_DATATB, kwargs.get('model_name'))
    except KeyError:
        return HttpResponse(json.dumps({
            'message': 'this model is not activated or not exist.',
            'success': False
        }), status=400)
    to_update_id = kwargs.get('id')

    body = json.loads(request.body.decode("utf-8"))
    try:
        model_manager.filter(id=to_update_id).update(**body)
    except Exception as ve:
        return HttpResponse(json.dumps({
            'detail': str(ve),
            'success': False
        }), status=400)
    return HttpResponse(json.dumps({
        'message': 'Record Updated.',
        'success': True
    }), status=200)


@csrf_exempt
def export(request, **kwargs):
    try:
        model_class = Utils.get_class(DYNAMIC_DATATB, kwargs.get('model_name'))
    except KeyError:
        return render(request, '404.html', status=404)
    request_body = json.loads(request.body.decode('utf-8'))
    search_key = request_body.get('search', '')
    hidden = request_body.get('hidden_cols', [])
    export_type = request_body.get('type', 'csv')
    filter_options = Q()

    headings = filter(lambda field: field.name not in hidden,
                      [field for field in model_class._meta.get_fields()])
    headings = list(headings)
    for field in headings:
        field_name = field.name
        try:
            filter_options = filter_options | Q(**{field_name + '__icontains': search_key})
        except Exception as _:
            pass

    all_data = model_class.objects.filter(filter_options)
    table_data = []
    for data in all_data:
        this_row = []
        for heading in headings:
            this_row.append(getattr(data, heading.name))
        table_data.append(this_row)

    df = pd.DataFrame(
        table_data,
        columns=tuple(heading.name for heading in headings))
    if export_type == 'pdf':
        base64encoded = get_pdf(df)
    elif export_type == 'xlsx':
        base64encoded = get_excel(df)
    elif export_type == 'csv':
        base64encoded = get_csv(df)
    else:
        base64encoded = 'nothing'

    return HttpResponse(json.dumps({
        'content': base64encoded,
        'file_format': export_type,
        'success': True
    }), status=200)


def get_pdf(data_frame, ):
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=data_frame.values, colLabels=data_frame.columns, loc='center',
             colLoc='center', )
    random_file_name = get_random_string(10) + '.pdf'
    pp = PdfPages(random_file_name)
    pp.savefig(fig, bbox_inches='tight')
    pp.close()
    bytess = read_file_and_remove(random_file_name)
    return base64.b64encode(bytess).decode('utf-8')


def get_excel(data_frame, ):
    random_file_name = get_random_string(10) + '.xlsx'

    data_frame.to_excel(random_file_name, index=False, header=True, encoding='utf-8')
    bytess = read_file_and_remove(random_file_name)
    return base64.b64encode(bytess).decode('utf-8')


def get_csv(data_frame, ):
    random_file_name = get_random_string(10) + '.csv'

    data_frame.to_csv(random_file_name, index=False, header=True, encoding='utf-8')
    bytess = read_file_and_remove(random_file_name)
    return base64.b64encode(bytess).decode('utf-8')


def read_file_and_remove(path):
    with open(path, 'rb') as file:
        bytess = file.read()
        file.close()

    # ths file pointer should be closed before removal
    os.remove(path)
    return bytess


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
