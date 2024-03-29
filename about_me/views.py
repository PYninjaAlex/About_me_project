from django.shortcuts import render
from django.shortcuts import redirect
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
        """
        Db updating func().
        :param request:
        :return:
        """
        terms = AboutMeDatabase.objects.all()
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("../database")
