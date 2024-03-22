from django.contrib import admin
from .models import User, client, product, order, sale
# Register your models here.

admin.site.register(User)
admin.site.register(client)
admin.site.register(product)
admin.site.register(order)
admin.site.register(sale)

