from django import forms
from .models import Administrator
from .models import Klient
from .models import Miasto
from .models import Mieszkanie
from .models import Rezerwacja
from .models import Status

class RezerwacjaForm(forms.ModelForm):
    class Meta:
        model = Rezerwacja
        fields = ('data_od', 'data_do',)

class MiastoForm(forms.ModelForm):
    class Meta:
        model = Miasto
        fields = ('nazwa_miasta',)