from django.db import models


class Order(models.Model):
    order_number = models.Charfield(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey()
    first_name = models.Charfield(max_length=32, null=False, blank=False)
    last_name = models.Charfield(max_length=32, null=False, blank=False)
    email = models.Emailfield(max_length=254, null=False, blank=False)
    address_line_1 = models.Charfield(max_length=80, null=False, blank=False)
    address_line_2 = models.Charfield(max_length=80, null=False, blank=False)
    town_or_city = models.Charfield(max_length=80, null=False, blank=False)
    county_or_state = models.Charfield(max_length=80, null=False, blank=False)
    postcode = models.Charfield(max_length=80, null=False, blank=True)
    order_date = models.DateTimefield(auto_now_add=True)
    delivery_cost = models.Decimalfield(max_digit=6, decimal_places=2,
                    null=False, default=0)
    order_total = models.Decimalfield.Decimalfield(max_digit=10,
                  decimal_places=2, null=False, default=0)
    grand_total = models.Decimalfield(max_digit=10, decimal_places=2,
                  null=False, default=0)
    is_gift_wrapping = models.Booleanfield()