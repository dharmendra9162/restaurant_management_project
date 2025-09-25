from django.db import models

class Coupon(models.Model):
    code = models.charField(max_length=20, unique=True)
    discount = models.DecimalField(max_digits=5, Decimal_places=2, help_text="Discount percentage")
    active = models.BoolenField(default=True)
    def __str__ (self):
        return self.code
