"""
Some assumptions to keep things simple:
1. You only disconnect kegs to take them back to a vendor, so the tap they're
   on is sufficient location info.
2. Empty kegs will either be refilled or will be returned and the deposit put
   back into the keg fund, so you don't need to keep track of deposits.
3. Beer is always good; it doesn't _really_ matter what we stock. We should use
   a very basic voting system.
"""
from django.db import models


class Tap(models.Model):
    """
    A spout from which you can get a boozy beverage.
    """
    location = models.CharField(max_length=600)

    def __str__(self):
        return self.location


class Keg(models.Model):
    """
    The liquid in the keg, not the container. The container is merely an
    earthly manifestation of your deposit. The beer in the keg is the thing you
    are talking about when you say, "keg".

    Many beers change from batch to batch, which makes kegs unique by purchase.

    This is my beer. There are many like it but this one is mine.
    """

    beer = models.ForeignKey('beer.Beer')
    # django-measurements doesn't support Django 1.7, or we'd use that to make
    # a MeasurementField. We force a single
    # unit of measurement to make it easier to write a migration when
    # django-measurements gets updated.
    gallons = models.DecimalField(max_digits=4, decimal_places=2)
    ledger_entry = models.ForeignKey('ledger.LedgerEntry', blank=False, null=False,
        help_text="You bought it, there better be a trackable transaction "
            "associated with it. Don't include the keg deposit")
    purchase_date = models.DateField(blank=True, null=True)
    tap = models.ForeignKey(Tap)

    def __str__(self):
        return '{}: {} gallons of {}'.format(self.purchase_date, self.gallons,
                                             self.beer)
