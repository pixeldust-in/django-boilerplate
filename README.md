# django-boilerplate
Barebone Django Project Starter Kit

Django + PostGresql + Post CSS + Bootstrap 

### Directory Structure

```
README.md/
base/
  manage.py         # installed to PATH via setup.py
  settings.py       # Common Settings
  wsgi.py
  urls.py           # Main URL Config
  core/             # Core app (Includes user models)
  templates/        # app specific templates
pcss/               
static/             # all other static files goes here
  pcss/             # Post-CSS files with config.js file included
config/             # Config Files
requirements.txt
package.json
build_css.sh         # Post-CSS complie script
Makefile             # Stuff
```

## pre-loaded apps
 - [django-compressor](https://django-compressor.readthedocs.io/en/latest/)
 - [django-hmin](https://pypi.python.org/pypi/django-hmin/0.3.2) (HTML Minifier)
 - [pre-commit](pre-commit.com) - With [black](https://github.com/ambv/black) as auto formatter
 - [django-user_agents](https://github.com/selwin/django-user_agents)
 - [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
 - [django-hashid-field](https://github.com/nshafer/django-hashid-field)


## Getting Started

1. Clone
2. Copy `config/settings/dev_settings.py` as `src/local_settings.py`
3. Create PSQL DB & update local_settings.py with credentials
4. `make deps`
5. migrate
6. runserver

