import os.path
import dj_database_url
import dj_email_url

PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

SECRET_KEY = 't8954dpsfgvhser89y34t89yhsdfw4erf'

ALLOWED_HOSTS = ['*']

DEBUG = True
CURRENT_PROJECT_LOCATION = 'local'

if CURRENT_PROJECT_LOCATION == 'production':
    SITE_URL = 'http://www.preptechmed.com'
else:
    SITE_URL = 'http://127.0.0.1:8000'

DATABASES = {
    "default": dj_database_url.config(
        default="postgres://preptechmed:preptechmed4life@127.0.0.1:5432/preptechmed", conn_max_age=600
    )
}

EMAIL_URL = os.environ.get("EMAIL_URL")
SENDGRID_USERNAME = os.environ.get('xxx')
SENDGRID_PASSWORD = os.environ.get('xxx')
SENDGRID_API_KEY = os.environ.get('xxx')
if not EMAIL_URL and SENDGRID_USERNAME and SENDGRID_PASSWORD:
    EMAIL_URL = "smtp://%s:%s@smtp.sendgrid.net:587/?tls=True" % (
        SENDGRID_USERNAME,
        SENDGRID_PASSWORD,
    )
email_config = dj_email_url.parse(EMAIL_URL or "console://")

EMAIL_FILE_PATH = email_config['EMAIL_FILE_PATH']
EMAIL_HOST_USER = 'xxx'
EMAIL_HOST_PASSWORD = 'xxx'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = '587'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", EMAIL_HOST_USER)
ORDER_FROM_EMAIL = os.getenv("ORDER_FROM_EMAIL", DEFAULT_FROM_EMAIL)

INSTALLED_APPS = [
    'preptechmed',
    'tinymce',
    'ckeditor',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'preptechmed.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'preptechmed.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = os.environ.get('STATIC_URL', '/static/')
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder']

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = os.environ.get('MEDIA_URL', '/media/')

TINYMCE_DEFAULT_CONFIG = {
    'branding': False,
    'plugins': 'lists',
    'toolbar': 'undo redo | styleselect | bullist numlist | bold italic removeformat | alignleft aligncenter alignright alignjustify | outdent indent | link image | code',
    'toolbar_location': 'bottom',
    'menubar': False,
    'height': "480"
}

CKEDITOR_CONFIGS = {
    'default': {
        'mode': "textareas",
        'force_br_newlines': 'true',
        'force_p_newlines': 'false',
        'forced_root_block': "",
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter',
             'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ]
    }
}
