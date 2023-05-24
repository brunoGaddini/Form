# https://www.youtube.com/watch?v=V4nCkSKajZU&t=126s 06:14

from django.forms import ModelForm
from app.models import Carros

# Create the form class.
class CarrosForm(ModelForm):
    class Meta:
        model = Carros
        fields = ["modelo", "marca", "ani"]
