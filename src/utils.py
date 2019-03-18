# -*- coding: utf-8 -*-
from django.conf import settings


def context_processor(request):
    d = {"settings": settings}
    return d
