from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from .models import Administrator
from .models import Klient
from .models import Miasto
from .models import Mieszkanie
from .models import Rezerwacja
from .models import Status
from .forms import RezerwacjaForm
from .forms import MiastoForm

def admin_view(request):
    administratorzy = Administrator.objects.all()
    klienci = Klient.objects.all()
    miasta = Miasto.objects.all()
    mieszkania = Mieszkanie.objects.all()
    form = MiastoForm()
    form2 = RezerwacjaForm()
    return render(request, 'blog/post_list.html', {'miasta': miasta,'form': form, 'form2': form2})

