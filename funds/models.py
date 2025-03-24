from django.db import models


class Fund(models.Model):
    """
    Represents an individual Fund and its associated data.
    """

    STRATEGY_CHOICES = [
        ("long/short equity", "Long/Short Equity"), 
        ("global macro", "Global Macro"),
        ("arbitrage", "Arbitrage")
    ]

    name = models.CharField(verbose_name="Name", max_length=255)
    strategy = models.CharField(
        verbose_name="Strategy",
        max_length=20,
        choices=STRATEGY_CHOICES
    )
    aum = models.BigIntegerField(
        verbose_name="Assets Under Management",
        null=True,
        blank=True,
        default=None
    )
    inception_date = models.DateField(
        verbose_name="Inception Date",
        null=True,
        blank=True,
        default=None
    )
    created_at = models.DateTimeField(
        verbose_name="Created at",
        auto_now_add=True,
        editable=False
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated at",
        auto_now=True
    )

    class Meta:
        verbose_name = "Fund"
        verbose_name_plural = "Funds"
    
    def __str__(self) -> str:
        return f"{self.name} data"
