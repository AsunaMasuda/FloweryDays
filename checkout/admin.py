from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    This inline item is going to allow us to add and edit line
    items in theadmin right from inside the order model.
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'order_date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_cart', 'stripe_pid')

    fields = ('order_number', 'user_profile', 'order_date', 'first_name',
              'last_name', 'email', 'address_line_1', 'address_line_2',
              'postcode', 'town_or_city', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_cart', 'stripe_pid')

    list_display = ('order_number', 'order_date', 'first_name',
                    'last_name', 'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-order_date',)


admin.site.register(Order, OrderAdmin)
