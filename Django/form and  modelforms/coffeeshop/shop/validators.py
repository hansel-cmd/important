from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

def vaidate_address(value):
    if any(char.isdigit() for char in value):
            raise ValidationError(
                _("Address %(value)s must not contain numbers."),
                code='invalid_address',
                params={'value': value}
            )