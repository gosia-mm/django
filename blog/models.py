from django.db import models

class Administrator(models.Model):
    id_admin = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)

    def __str__(self):
        return self.imie + " " + self.nazwisko


class Klient(models.Model):
    id_klienta = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)

    def __str__(self):
        return self.imie + " " + self.nazwisko


class Miasto(models.Model):
    id_miasta = models.AutoField(primary_key=True)
    nazwa_miasta = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa_miasta


class Mieszkanie(models.Model):
    id_mieszkania = models.AutoField(primary_key=True)
    ulica = models.CharField(max_length=50)
    nr_mieszkania = models.IntegerField()
    metraz = models.IntegerField()
    id_miasta = models.ForeignKey('Miasto')
    id_admin = models.ForeignKey('Administrator')

    def __str__(self):
        return self.ulica + " " + str(self.nr_mieszkania)

class Rezerwacja(models.Model):
    id_rezerwacji = models.AutoField(primary_key=True)
    data_od = models.DateTimeField()
    data_do = models.DateTimeField()
    id_mieszkania = models.ForeignKey('Mieszkanie')
    id_klienta = models.ForeignKey('Klient')

    def __str__(self):
        return str(self.id_klienta) + " " + str(self.data_od) + " -> " + str(self.data_do)

class Status(models.Model):
    id_statusu = models.AutoField(primary_key=True)
    dostepny = models.BooleanField()
    dostepnosc_od = models.DateTimeField()
    dostepnosc_do = models.DateTimeField()
    id_mieszkania = models.ForeignKey('Mieszkanie')

    def __str__(self):
        return str(self.id_statusu) + " " + str(self.id_mieszkania)


