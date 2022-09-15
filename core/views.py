from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.forms import formset_factory

from core.forms import *
from core.models import Hall

def home(request):
    return render(request, 'index/index.html')


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def add_video(request, pk):
    # Repetição de formulários:
    # VideoFormSet = formset_factory(VideoForm, extra=5)

    form = VideoForm()
    search_form = SearchForm()

    if request.method == "POST":
        filled_form = VideoForm(request.POST)
        if filled_form.is_valid():
            video = Video()
            video.url = filled_form.cleaned_data['url']
            video.title = filled_form.cleaned_data['title']
            video.youtube_id = filled_form.cleaned_data['youtube_id']
            
            video.hall = Hall.objects.get(pk=pk)
            video.save()

    return render(request, "video/add_video.html", {"form":form, "search_form":search_form})

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("home")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        """
        User Stay logged in after SignUp in the site
        """
        validation = super(SignUpView, self).form_valid(form) # 5. Super herda de SignUpView a presente função com o parametro do usuario autenticado
        username, password = form.cleaned_data.get("username"), form.cleaned_data.get("password1") # 1. Pega os dados dos inputs
        user = authenticate(username=username, password=password) # 2. Autentica o Usuário
        login(self.request, user) # 3. Loga com o usuário autenticado
        return validation # 4. retorna a variavel (ativa ela)


class CreateHall(generic.CreateView):
    model = Hall
    fields = ["title"]
    template_name = "halls/create_hall.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateHall, self).form_valid(form)
        return redirect("home")

class DetailHall(generic.DetailView):
    model = Hall
    template_name = "halls/detail_hall.html"

class UpdateHall(generic.UpdateView):
    model = Hall
    template_name = "halls/update_hall.html"
    fields = ["title"]
    success_url = reverse_lazy("dashboard")

class DeleteHall(generic.DeleteView):
    model = Hall
    template_name = "halls/delete_hall.html"
    success_url = reverse_lazy("dashboard")