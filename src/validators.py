import re

from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

mobile_validator = RegexValidator(
    re.compile(r"^[6-9]\d{9}$"),
    message=_("Enter a valid mobile number"),
    code="invalid",
)
