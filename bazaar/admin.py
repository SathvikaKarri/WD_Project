from django.contrib import admin
from .models import item, Cart

# Register your models here.
admin.site.register(item)
admin.site.register(Cart)
# admin.site.register(CartItem)