from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    phone= PhoneNumberField()
    def __str__(self):
        return self.username

class Elec_provider(models.Model):
    name=models.CharField(max_length=200)
    cost_per_unit=models.IntegerField()
    def __str__(self):
        return self.name
class User_electricity(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateTimeField()
    reading=models.IntegerField()
    def __str__(self):
        return u'%s' %((str(self.user)))
class Subscription(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    e_provider=models.ForeignKey(Elec_provider, on_delete=models.CASCADE)
    def __str__(self):
        return u'%s' %((str(self.user)))
