from django.db import models
from django.utils import timezone
from django import forms


# Create your models here.
class indeks(models.Model):
   nazwa = models.CharField(max_length=100,blank=True)
   barcode = models.CharField(max_length=100,blank=False)
   data = models.DateTimeField(blank=True,null=True,auto_now_add=True)
   skaner = models.CharField(max_length=20,blank=True)
   ilosc = models.IntegerField(default=0,null=True)
   nieogr_wyk = models.IntegerField(default=0,null=True)
   lokalizacja = models.CharField(max_length=100,blank=True)
   class Meta:
       verbose_name = 'indeks'
       verbose_name_plural = 'indeks(y)'
   def __str__(self):
        return "{} {}".format(self.nazwa,self.barcode)
        
class indeks_bazowy(models.Model):
   nazwa = models.CharField(max_length=100,blank=True)
   barcode = models.CharField(max_length=100,blank=False)
   data = models.DateTimeField(blank=True,null=True,auto_now_add=True)
   data_skan = models.DateTimeField(blank=True,null=True)
   skaner = models.CharField(max_length=20,blank=True)
   ilosc = models.IntegerField(default=0,null=True)
   ilosc_last = models.IntegerField(default=0,null=True)
   nieogr_wyk = models.IntegerField(default=0,null=True)
   lokalizacja = models.CharField(max_length=100,blank=True)
   class Meta:
       verbose_name = 'indeks_bazowy'
       verbose_name_plural = 'indeks(y)_bazowy(e)'
   def __str__(self):
        return "{} {}".format(self.nazwa,self.barcode)

class plik(models.Model):
    description = models.CharField(max_length=255,blank=True,default="Plik")
    path = models.FileField(upload_to='./mtinwentura/pliki')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class PlikDoPobrania(models.Model):
    name = models.CharField(max_length=255,blank=True,default="wywoz_tmp1.csv")
    path = models.FilePathField(path='./mtinwentura')

class fileform(forms.ModelForm):
    class Meta:
        model = plik
        fields = ('description','path',)



