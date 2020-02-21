from django.shortcuts import render, redirect
from django.http import HttpResponse
from pages.forms import SignUpForm

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from .models import Property
from .forms import PropertyForm

# Create your views here.
# def home(request):
#     return render(request, 'index.html')

class home(ListView):
    model = Property
    template_name = 'index.html'

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == 'POST':
        print('post request')
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

class PropertyCreateView(CreateView):
    model = Property
    form_class = PropertyForm


