# -*- coding: utf-8 -*-
import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(_("uuid"), default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(_("email address"), unique=True, null=True, blank=True)
    username = models.CharField(_("username"), max_length=30, unique=True)
    first_name = models.CharField(_("first name"), max_length=30, blank=True)
    last_name = models.CharField(_("last name"), max_length=30, blank=True)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    is_active = models.BooleanField(_("active"), default=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    is_staff = models.BooleanField(_("staff status"), default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")


class AbstractTrackModel(models.Model):
    is_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
