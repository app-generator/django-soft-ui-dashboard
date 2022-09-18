# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import importlib
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from core.settings import API_GENERATOR

from api_generator import manager

def generate():

    manager.generate_serializer_file()
    manager.generate_views_file()
    manager.generate_urls_file()

class Command(BaseCommand):
    help = 'API Code generator'

    def add_arguments(self, parser):
        pass
        parser.add_argument(
            '-f',
            action='store_true',
            help='Generate API for all models without checking migrated in database or not.',
        )

    def handle(self, *args, **options):
        not_migrated_models = []
        for model_name in API_GENERATOR.values():
            models = importlib.import_module('apps.models')

            try:
                model = getattr(models, model_name)
            except:
                self.stdout.write(f'Error [' + model_name + ' Model]: NOT_FOUND or not migrated in DB.' )
                self.stdout.write(f' > Hint: Update core/settings.py -> API_GENERATOR Section')
                exit(1)

            try:
                model.objects.last()
            except OperationalError:
                not_migrated_models.append(model_name)
        if len(not_migrated_models) > 0:
            self.stderr.write(f"There are some models that aren't migrated:\n{not_migrated_models}")
            if options['f']:
                generate()
                self.stdout.write(f"API codes forced to generate. operation is successful.")
        else:
            generate()
            self.stdout.write(f"API codes successfully generated.")
