import factory
from factory import fuzzy


class BrewerFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'beer.Brewer'

    name = fuzzy.FuzzyText()


class BeerFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'beer.Beer'

    brewer = factory.SubFactory(BrewerFactory)
    name = fuzzy.FuzzyText()
    abv = fuzzy.FuzzyDecimal(low=1, high=100)
