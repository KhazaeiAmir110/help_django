try:
    from help_django.settings.local import *
except ImportError:
    from help_django.settings.production import *
