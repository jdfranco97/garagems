from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib import messages
from users import views


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'