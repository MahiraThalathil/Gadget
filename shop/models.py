from django.urls import reverse

from django.db import models
from django.template.defaultfilters import slugify


class catag(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug=models.CharField(max_length=200,unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='catagory'
        verbose_name_plural='catagories'

    def get_url(self):
        return reverse('prod_cat',args=[self.slug])
    
    def __str__(self):
        return '{}'.format(self.name)

    

class products(models.Model):
    brand=models.CharField(max_length=200)
    name=models.CharField(max_length=200,unique=True)
    slug=models.CharField(max_length=200,unique=True)
    img=models.ImageField(upload_to='products')
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    price=models.IntegerField()
    catagory=models.ForeignKey(catag,on_delete=models.CASCADE)

    def get_url(self):
        return reverse('details',args=[self.catagory.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)
