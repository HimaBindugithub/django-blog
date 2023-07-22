from django.contrib.auth.models import User #user modle was created by django itself,
#by default it comes with django
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('email','username','password1','password2')