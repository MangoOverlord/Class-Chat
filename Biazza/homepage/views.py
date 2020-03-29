from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import RegisterForm

class HomePageView(TemplateView):
    template_name = 'home.html'

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/accounts/login")
    else:
        form = RegisterForm()

    return render(response, "register.html", {"form":form})




# Create your views here.
