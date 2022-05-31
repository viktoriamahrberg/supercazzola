from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """ 
    Add and edit items in the order in admin panel
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Order in admin panel
    """
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date', 
                        'delivery_cost', 'order_total', 
                        'grand_total')

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'street_address', 
              'optional_address', 
              'postcode', 'city', 'country',
              'delivery_cost',
              'order_total', 'grand_total', 'original_bag', 
              'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)
    
    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)