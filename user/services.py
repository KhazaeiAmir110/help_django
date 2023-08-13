from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import NotFound

from user.models import User


def create_user(self, phone_number, name, password=None, is_superuser=False):
    if not phone_number:
        raise NotFound(_('Input phone number, please.'))

    user = User(phone_number=phone_number, name=name, is_superuser=is_superuser)
    user.set_password(password)
    user.save()
    return user
