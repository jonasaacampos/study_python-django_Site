### Configurando ambiente e criando projeto

```bash
# install dependencies
pip install django psycopg2-binary gunicorn dj-static django-stdimage

# salvar dependências em um arquivo de texto
pip freeze > requirements.txt

# iniciar projeto no diretorório corrente
django-admin startproject fusion .

# criar a aplicação core
django-admin startapp core
```

### Alterar arquivos de configuração

projeto > settings.py:

```python
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "...",
    "...",
    "core",
]
# inserir nome do diretorio de templates da aplicação
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "...": "...",
    }
]

#################################################################
#                      Database                                 #
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases #
#################################################################
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "fusion",
        "USER": "admin",
        "PASSWORD": "..",
        "PORT": "5432"
    }
}

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"

# Diretórios para arquivos estáticos (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
MEDIA_URL = "media/"
STATIC_ROOT = Path.joinpath(BASE_DIR, "staticfiles")
MEDIA_ROOT = Path.joinpath(BASE_DIR, "media")
```
projeto > urls.py:

```python
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

core > criar aquivo urls.py
```python
from django.urls import path

urlpatterns = [
    
]
```

```bash

# Criar diretorios dentro da aplicação core
mkdir static, templates
```

### Rodar Projeto

`python manage.py runserver`

### Preparação do template

```django
# inserir marcador de arquivos estáticos no cabeçalho do arquivo html
{% load static %}

# alterar todos os arquivos estávticos (imagens, css, js, etc.)
{% static 'caminhoDoarquivo/nomeArquivo' %}

# criar arquivo de base e fatiar o template original
 {% block content %}
  {% endblock %}
 
```


## Referências

- [PostgreSQL download](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
- [Built-in class-based views API - Django Oficial Documentation](https://docs.djangoproject.com/en/2.2/ref/class-based-views/)
- [Classy Class-Based Views](https://ccbv.co.uk/)