# Generated by Django 2.1.5 on 2019-03-18 20:28

import core.managers
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [("auth", "0009_alter_user_last_name_max_length")]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        unique=True,
                        verbose_name="uuid",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        unique=True,
                        verbose_name="email address",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=30, unique=True, verbose_name="username"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=30, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=30, verbose_name="last name"
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(auto_now_add=True, verbose_name="date joined"),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="active")),
                (
                    "avatar",
                    models.ImageField(blank=True, null=True, upload_to="avatars/"),
                ),
                (
                    "is_staff",
                    models.BooleanField(default=False, verbose_name="staff status"),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={"verbose_name": "user", "verbose_name_plural": "users"},
            managers=[("objects", core.managers.UserManager())],
        )
    ]
