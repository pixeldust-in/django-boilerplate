from django.conf import settings
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import RedirectView

from .forms import LoginForm


# Create your views here.
def login_view(request):
    context = {}
    form = LoginForm(request.POST or None)
    context["form"] = form
    if request.POST and form.is_valid():
        user = form.authenticate(request)
        if user:
            login(request, user)
            next = request.GET.get("next")
            if next:
                return HttpResponseRedirect(next)
    return render(request, "core/login.html", context)


class LogoutView(RedirectView):
    url = settings.LOGIN_URL

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
