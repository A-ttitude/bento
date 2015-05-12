from django import forms
from django.contrib.auth.models import User
from bento.models import Recette


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email :')
    password = forms.CharField(label='Mot de passe :', widget=forms.PasswordInput)

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
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ('titre', 'auteur', 'type', 'difficulte', 'cout', 'temps_preparation', 'temps_cuisson', 'temps_repos',
                  'ingredients', 'etape', 'note_moyenne', 'photo')