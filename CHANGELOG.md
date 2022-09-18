# Change Log

## [1.0.12] 2022-09-18
### Improvements

- Dynamic DataTables:
  - Server-Side Pagination, Search, Export 

## [1.0.11] 2022-09-17
### Improvements

- API Generator 
  - the code is generated on top of DRF
  - Mutating requests secured by JWT

## [1.0.10] 2022-09-17
### Improvements

- Added **Github OAuth** via AllAuth. requires in `.env`:
  - `GITHUB_ID`=<YOUR_GITHUB_ID>
  - `GITHUB_SECRET`=<YOUR_GITHUB_SECRET>

## [1.0.9] 2022-09-17
### Improvements

- Bump Codebase & UI version
- Docker scripts update

## [1.0.8] 2022-06-21
### Improvements

- UI Update: `Soft UI Dashboard` v1.0.6
- Enhanced version:
  - `Dark Mode`

## [1.0.7] 2022-05-25
### Improvements

- Built with [Soft UI Dashboard Generator](https://appseed.us/generator/soft-ui-dashboard/)
  - Timestamp: `2022-05-25 10:16`
- Added CDN/Static Server management
  - `ASSETS_ROOT` env variable

## [1.0.6] 2022-05-24
### Improvements 

- UI Update: `Soft UI Dashboard` v1.0.5
  - upgrade Bootstrap version to v5.1.3
  - upgrade ChartJs plugin version to v3.7.1
  - fix running 'npm install' issue
  - fix SCSS compiling issues
  - update sidebar height
  - fix sidebar button on Safari
  - update dropdown text on RTL page
  - fix navbar scroll error on example pages

## [1.0.5] 2022-01-16
### Improvements

- Bump Django Codebase to [v2stable.0.1](https://github.com/app-generator/boilerplate-code-django-dashboard/releases)
- Dependencies update (all packages) 
  - Django==4.0.1
- Settings update for Django 4.x
  - `New Parameter`: CSRF_TRUSTED_ORIGINS
    - [Origin header checking isn`t performed in older versions](https://docs.djangoproject.com/en/4.0/ref/settings/#csrf-trusted-origins)  

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
