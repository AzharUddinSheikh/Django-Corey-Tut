from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


# clas Meta gives us nested namespace keep config in one palce so we need a field in form
# the model that ll be affected is user model lets say
#
# when form.save() its going to save in user model (ie email first name etc) and also field we ll get in
# form which is a insatnce of UserCreationForm and also in wich order

# those class attribute of meta is predefined
