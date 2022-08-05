from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'index/index.html')


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('index')
