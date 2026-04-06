from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from django import forms
from .models import *

class AddDeck(ModelForm):
    class Meta:
        model = Deck
        fields = ["name", "sub_name"]
    
class EditCard(ModelForm):
    class Meta:
        model = Card
        fields = ["question", "answer"]

class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]