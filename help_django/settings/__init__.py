"""
try to activate local settings. if it failed, we
load the production environment.
"""

try:
    from help_django.settings.base import *
    from help_django.settings.local import *
except ImportError:
    from help_django.settings.production import *
