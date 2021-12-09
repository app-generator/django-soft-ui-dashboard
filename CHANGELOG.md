# Change Log

## [1.0.4] 2021-12-09
### Improvements

- Bump UI: Soft UI Dashboard **v1.0.3**

## [1.0.3] 2021-09-20
### Improvements 

- Bump Django Codebase to [v2.0.4](https://github.com/app-generator/boilerplate-code-django-dashboard/releases)
- Codebase update
  - `assets` & `templates` moved to `apps` folder
  - `apps/base` renamed to `apps/home`
  
## [1.0.2] 2021-09-08
### Improvements & Fixes

- Bump Django Codebase to [v2.0.2](https://github.com/app-generator/boilerplate-code-django-dashboard/releases)
  - Dependencies update (all packages)
    - Use Django==3.2.6 (latest stable version)
  - Better Code formatting
  - Improved Files organization
  - Optimize imports
  - Docker Scripts Update
- Tooling: added scripts to recompile the SCSS files
  - `core/static/assets/` - gulpfile.js
  - `core/static/assets/` - package.json
  - `Update README` - [Recompile SCSS](https://github.com/app-generator/django-soft-ui-dashboard#recompile-css) (new section)
- Fixes: 
  - Patch 500 Error when authenticated users access `admin` path (no slash at the end)
  - Patch [#16](https://github.com/app-generator/boilerplate-code-django-dashboard/issues/16): Minor issue in Docker 

## [1.0.1] 2020-05-28
### Remove Media & Minor Fixes

- Patch `logout` link 
- Delete useless `media` directory

## [1.0.0] 2020-05-28
### Initial Release

- Codebase: [Django Dashboard](https://github.com/app-generator/boilerplate-code-django-dashboard) v1.0.4
- UI: [Jinja Soft UI](https://github.com/app-generator/jinja-soft-ui-dashboard) v1.0.0
- UI Kit: Soft UI Dashboard v1.0.1
