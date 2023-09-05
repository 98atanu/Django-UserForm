from django.db import models

# Create your models here.
class UserForm(models.Model):
    customer_name = models.CharField(max_length=200,null=False)
    product_name = models.CharField(max_length=200,null=False)
    price = models.FloatField(null=False)
    
    def __str__(self) -> str:
        return self.customer_name
