from django.shortcuts import render
from django.views.generic.base import View
from .models import AboutMeDatabase
from .form import LoginForm


def main(request):
    """
    Return main.html
    :param request:
    """
    return render(request, template_name="main.html")


class DatabaseRealisation(View):
    """
    Realise db.
    """

    @staticmethod
    def get(request):
        """
        Main db func().
        :param request:
        """
        terms = AboutMeDatabase.objects.all()
        return render(request, "database.html", {"terms_list": terms})


class AddUsers(View):
    """Users adding."""

    @staticmethod
    def post(request):
        terms = AboutMeDatabase.objects.all()
        form = LoginForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
        return render(request, 'database.html', {"terms_list": terms})
