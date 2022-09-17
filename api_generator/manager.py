# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from core.settings import API_GENERATOR

def generate_serializer_file():
    with open('api_generator/serializers/serializers_structure', 'r') as serializers_structure_file:
        serializers_structure = serializers_structure_file.read()

    with open('api_generator/serializers/library_imports', 'r') as library_imports_file:
        library_imports = library_imports_file.read()

    with open('api_generator/serializers/base_imports', 'r') as base_imports_file:
        base_imports = base_imports_file.read()

    with open('api_generator/serializers/base_serializer', 'r') as base_serializer_file:
        base_serializer = base_serializer_file.read()

    project_imports = base_imports.format(models_name=", ".join(API_GENERATOR.values()))
    serializers = '\n\n'.join(base_serializer.format(model_name=model_name) for model_name in API_GENERATOR.values())
    generation = serializers_structure.format(
        library_imports=library_imports,
        project_imports=project_imports,
        serializers=serializers
    )

    with open('apps/api/serializers.py', 'w') as serializers_py:
        serializers_py.write(generation)

    return generation


def generate_views_file():
    with open('api_generator/views/views_structure', 'r') as views_structure_file:
        views_structure = views_structure_file.read()

    with open('api_generator/views/library_imports', 'r') as library_imports_file:
        library_imports = library_imports_file.read()

    with open('api_generator/views/base_imports', 'r') as base_imports_file:
        base_imports = base_imports_file.read()

    with open('api_generator/views/base_view', 'r') as base_views_file:
        base_views = base_views_file.read()
    project_imports = base_imports.format(
        models_name=', '.join(API_GENERATOR.values()),
        serializers_name=', '.join(list(map(lambda model_name: f'{model_name}Serializer', API_GENERATOR.values())))
    )
    views = '\n\n'.join(base_views.format(
        serializer_name=f'{model_name}Serializer',
        model_name=model_name
    ) for model_name in API_GENERATOR.values())

    generation = views_structure.format(
        library_imports=library_imports,
        project_imports=project_imports,
        views=views
    )

    with open('apps/api/views.py', 'w') as views_py:
        views_py.write(generation)

    return generation


def generate_urls_file():
    urls_file_structure = """{library_imports}\n{project_imports}\nurlpatterns = [\n{paths}\n\n]"""
    with open('api_generator/urls/library_imports', 'r') as library_imports_file:
        library_imports = library_imports_file.read()

    with open('api_generator/urls/base_imports', 'r') as base_imports_file:
        base_imports = base_imports_file.read()

    with open('api_generator/urls/base_url_path', 'r') as base_urls_file:
        base_urls_path = base_urls_file.read()

    views_name = ", ".join(list(map(lambda model_name: f'{model_name}View', API_GENERATOR.values())))
    paths = ''
    for endpoint, model_name in API_GENERATOR.items():
        view_name = f'{model_name}View'
        paths = f'{paths}\n\t{base_urls_path.format(endpoint=endpoint, view_name=view_name)}'
    generation = urls_file_structure.format(
        library_imports=library_imports,
        project_imports=base_imports.format(views_name=views_name),
        paths=paths
    )
    with open('apps/api/urls.py', 'w') as urls_py:
        urls_py.write(generation)

    return generation
