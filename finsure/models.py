from django.db import models
from django.core.validators import MinLengthValidator


class Lender(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    code = models.CharField(
        max_length=3,
        null=False,
        blank=False,
        validators=[MinLengthValidator(limit_value=3)]
    )
    upfront_commission_rate = models.DecimalField(
        max_digits=5,
        decimal_places=3,
        null=False,
        blank=False,
    )
    trial_commission_rate = models.DecimalField(
        max_digits=5,
        decimal_places=3,
        null=False,
        blank=False,
    )
    active = models.BooleanField(null=False)

    def __str__(self) -> str:
        return f'{self.name} ({self.code})'
