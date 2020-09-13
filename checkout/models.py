from django.db import models

# Create your models here.

user_profile = models.Charfield()
first_name = models.Charfield()
last_name = models.Charfield()
email = models.Emailfield()
address_line_1 = models.Charfield()
address_line_2 = models.Charfield()
town_or_city = models.Charfield()
county_or_state = models.Charfield()
postcode = models.Charfield()
order_date = models.DateTimefield()
delivery_cost = models.Decimalfield()
delivery_type = models.Charfield()
order_total = models.Decimalfield()
grand_total = models.Decimalfield()
is_gift_wrapping = models.Booleanfield()
original_bag = models.Textfield()
stripe_pid = models.Charfield()