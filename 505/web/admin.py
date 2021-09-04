from django.contrib import admin
from .models import M_Users, M_Items, T_Orders, T_Order_Details

admin.site.register(M_Users)
admin.site.register(M_Items)
admin.site.register(T_Orders)
admin.site.register(T_Order_Details)
