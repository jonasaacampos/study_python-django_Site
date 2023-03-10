### Cobertura de testes
>Coverage report: **100%** xD
<table class="index" data-sortable="">
        <thead>
            <tr class="tablehead" title="Click to sort">
                <th class="name left" aria-sort="none" data-shortcut="n">Module</th>
                <th aria-sort="none" data-default-sort-order="descending" data-shortcut="s">statements</th>
                <th aria-sort="none" data-default-sort-order="descending" data-shortcut="m">missing</th>
                <th aria-sort="none" data-default-sort-order="descending" data-shortcut="x">excluded</th>
                <th class="right" aria-sort="none" data-shortcut="c">coverage</th>
            </tr>
        </thead>
        <tbody>
            <tr class="file">
                <td class="name left"><a href="d_57760688d1f824db_forms_py.html">core\forms.py</a></td>
                <td>15</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="15 15">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_57760688d1f824db_models_py.html">core\models.py</a></td>
                <td>54</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="54 54">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_57760688d1f824db_views_py.html">core\views.py</a></td>
                <td>24</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="24 24">100%</td>
            </tr>
        </tbody>
        <tfoot>
            <tr class="total">
                <td class="name left">Total</td>
                <td>93</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="93 93">100%</td>
            </tr>
        </tfoot>
    </table>

### Configurando ambiente e criando projeto

```bash
# install dependencies
pip install django psycopg2-binary gunicorn dj-static django-stdimage

# salvar depend??ncias em um arquivo de texto
pip freeze > requirements.txt

# iniciar projeto no diretor??rio corrente
django-admin startproject fusion .

# criar a aplica????o core
django-admin startapp core
```

### Alterar arquivos de configura????o

projeto > settings.py:

```python
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "...",
    "...",
    "core",
]
# inserir nome do diretorio de templates da aplica????o
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

# Diret??rios para arquivos est??ticos (CSS, JavaScript, Images)
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

# Criar diretorios dentro da aplica????o core
mkdir static, templates
```

### Rodar Projeto

`python manage.py runserver`

### Prepara????o do template

```django
# inserir marcador de arquivos est??ticos no cabe??alho do arquivo html
{% load static %}

# alterar todos os arquivos est??vticos (imagens, css, js, etc.)
{% static 'caminhoDoarquivo/nomeArquivo' %}

# criar arquivo de base e fatiar o template original
 {% block content %}
  {% endblock %}
 
```

### Trabalhando com Models

> Ao criar ou alterar uma classe em models, ?? preciso realizar as migra????es
 
`python manage.py makemigrations`

Para criar as tabelas do banco de dados
`python manage.py migrate`

Criar superusuario
`python manage.py createsuperuser`


### Trabalhando com imagens

> ao utilizar o StdImageField, esta biblioteca altera os nomes de arquivos de media para evitar a sobrescrita
> 
> Para fazer manualmente a altera????o com hashes nos arquivos, podemos usar a biblioteca uuid.uuid 
> 
> MAS
> 
> ?? uma boa pr??tica usar os dois m??todos em conjunto

### Testes unit??rios
> _Testar ?? preciso..._

instalar bibliotecas adicionais de teste

```console
pip install model_mommy coverage
```
- Criar na raiz do projeto o arquivo `.coveragerc`
- Inserir neste arquivo:
  
```text
[run]
source = .

omit =
    */__init__.py
    */settings.py
    */wsgi.py
    */apps.py
    */urls.py
    */admin.py
    */migrations/*
    */tests/*
```
- Para rodar o teste use `coverage run manage.py test`
- para relat??rio de testes `coverage report` ou `coverage html`
- rodar o servidor interno do python `python -m http.server`

**Excluir arquivo padr??o de testes** e **criar pacote de testes**

- criar diret??rio `tests` dentro da raiz do app
- criar arquivo vazio `__init__.py`
- criar arquivos
  - `test_forms.py`
  - `test_models.py`
  - `test_views.py`

## Refer??ncias

- [PostgreSQL download](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
- [Built-in class-based views API - Django Oficial Documentation](https://docs.djangoproject.com/en/2.2/ref/class-based-views/)
- [Classy Class-Based Views](https://ccbv.co.uk/)