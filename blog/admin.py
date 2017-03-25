from django.contrib import admin
from .models import Administrator
from .models import Klient
from .models import Miasto
from .models import Mieszkanie
from .models import Rezerwacja
from .models import Status


admin.site.register(Administrator)
admin.site.register(Klient)
admin.site.register(Miasto)
admin.site.register(Mieszkanie)
admin.site.register(Rezerwacja)
admin.site.register(Status)
