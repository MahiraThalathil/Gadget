from django.db import models
from shop.models import *
import uuid
# Create your models here.

class cartlist(models.Model):
    cart_id=models.CharField(max_length=200,unique=True,default=uuid.uuid1)
    date_added=models.DateTimeField(auto_now_add=True)

   

    def __str__(self):
        return self.cart_id


class item(models.Model):
    prodt=models.ForeignKey(products,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quan=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        db_table='item'

    def total(self):
        return self.prodt.price*self.quan


    def __str__(self):
        return self.prodt
