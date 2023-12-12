from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class item(models.Model):
    item_name = models.CharField(max_length=10)
    price = models.IntegerField()
    #picture = models.ImageField(upload_to="img", default="")

    def __str__(self):
        return self.item_name
    
class Cart(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # completed = models.BooleanField(default=False)
    item = models.ForeignKey(item, on_delete=models.CASCADE, related_name="procuctitem")
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.id}  {self.item.item_name} - price {self.item.price} - {self.quantity} "    
    # def __str__(self):
    #     return self.id self.item.item_name self.quantity

# class CartItem(models.Model):
#     item = models.ForeignKey(item, on_delete=models.CASCADE, related_name="procuctitem")
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cartitem")
#     quantity = models.IntegerField(default=0)

#     def __str__(self):
#         return self.item.item_name