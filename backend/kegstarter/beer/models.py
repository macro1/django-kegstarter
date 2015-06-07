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


class Brewer(models.Model):
    """The creator (either a person or company) of the beer.

    "Beer is proof that God loves us and wants us to be happy"
        - Misquoted from Benjamin Franklin
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Beer(models.Model):
    """The specific name of the particular beer. Beers tend to have... creative names."""

    brewer = models.ForeignKey(Brewer)
    name = models.CharField(max_length=1024)  # Might not be supported on all DBs?
    abv = models.DecimalField(max_digits=5, decimal_places=2, help_text="Alcohol by Volume (in percent)")

    def __str__(self):
        return "{} - {}".format(self.brewer, self.name)
