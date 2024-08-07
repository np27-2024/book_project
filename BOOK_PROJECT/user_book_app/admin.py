from django.contrib import admin

# Register your models here.

from user_book_app.models import Cart,CartItem

admin.site.register(Cart)
admin.site.register(CartItem)