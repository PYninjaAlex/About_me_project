from django.shortcuts import render

def main(request):
    return render(request, template_name="main.html")

def database(request):
    return render(request, template_name="database.html")
