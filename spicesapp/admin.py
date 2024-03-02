from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(AddToCart)
admin.site.register(Checkout)
admin.site.register(Contact)