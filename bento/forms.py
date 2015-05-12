from django import forms
from django.contrib.auth.models import User
from bento.models import Recette


class LoginForm(forms.Form):
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Email',
                                                                     'class': 'pure-input-1-2',
                                                                     'style': 'display: inline;'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe',
                                                                           'class': 'pure-input-1-2',
                                                                           'style': 'display: inline;'}))

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            result = User.objects.filter(password=password, email=email)
            if len(result) != 1:
                raise forms.ValidationError("Email ou mot de passe invalide !")

        return cleaned_data


class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ('titre', 'auteur', 'type', 'difficulte', 'cout', 'temps_preparation', 'temps_cuisson', 'temps_repos',
                  'ingredients', 'etape', 'note_moyenne', 'photo')