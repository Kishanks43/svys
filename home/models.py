from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    phone= models.CharField(max_length=12)
    descr=models.TextField()
    date= models.DateField()

    def __str__(self) :
        return self.name    
    
class Add(models.Model) :
    name=models.CharField(max_length=122)
    shop=models.CharField(max_length=122)
    other=models.CharField(max_length=150)
    type=models.CharField(max_length=100)
    location=models.TextField()
    reference=models.TextField()
    amount=models.IntegerField()
    city=models.CharField(max_length=122)
    state=models.CharField(max_length=122)
    pin=models.CharField(max_length=122)
    date= models.DateField()
    
    def __str__(self):
        return self.shop

