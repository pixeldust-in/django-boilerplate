from django.conf.urls import url
from django.urls import path

from . import views

app_label = "core"

urlpatterns = [
    url(r"^login/$", views.login_view, name="login"),
    path("logout/", views.LogoutView.as_view(), name="user_logout"),
]
