import decimal
import factory

from ..test_ledger import factories as ledger_factory
from ..test_beer import factories as beer_factory


class TapFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'keg.Tap'

    location = 'Kegerator in the back room. Left handle.'


class KegFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'keg.Keg'

    beer = factory.SubFactory(beer_factory.BeerFactory)
    gallons = decimal.Decimal('10.11')
    ledger_entry = factory.SubFactory(ledger_factory.LedgerEntryFactoryRegistered)
    purchase_date = None
    tap = factory.SubFactory(TapFactory)
