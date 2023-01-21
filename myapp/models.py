from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


# Create your models here.
class Currency(models.Model):
    iso = models.CharField(max_length=3)
    long_name = models.CharField(max_length=50)

    def __repr__(self):
        return self.iso + " " + self.long_name

    def __str__(self):
        return self.iso + " " + self.long_name


class Holding(models.Model):
    iso = models.ForeignKey(Currency, on_delete=models.CASCADE)
    value = models.FloatField(default=0.0)
    buy_date = models.DateField()

    def __repr__(self):
        return self.iso.iso + " " + str(self.value) + " " + str(self.buy_date)

    def __str__(self):
        return self.iso.long_name + " " + str(self.value) + " " + str(self.buy_date)


class Rates(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    x_currency = models.CharField(max_length=3)
    rate = models.FloatField(default=1.0)
    last_update_time = models.DateTimeField()

    def __repr__(self):
        return self.currency.iso + " " + self.x_currency + " " + str(self.rate)

    def __str__(self):
        return self.currency.iso + " " + self.x_currency + " " + str(self.rate)


class User1(models.Model):
    name = models.CharField(max_length=255)
    horoscope = models.CharField(max_length=255)

    def __repr__(self):
        return self.name + " " + self.horoscope

    def __str__(self):
        return self.name + " " + self.horoscope


class CompatibleHoroscope(models.Model):
    horoscope1 = models.CharField(max_length=50)
    compatible_horoscope = models.CharField(max_length=50)
    def __repr__(self):
        return self.horoscope1 + " " + self.compatible_horoscope
    def __str__(self):
        return self.horoscope1 + " " + self.compatible_horoscope


class AccountHolder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.user.username

    def __repr__(self):
        return self.user.username

class City(models.Model):
    name = models.CharField(max_length=50)
    wiki_link = models.URLField()
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name + " " + str(self.latitude) + " " + str(self.longitude) + " " + \
            str(self.longitude) + " " + self.wiki_link
