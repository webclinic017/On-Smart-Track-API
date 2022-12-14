from django.db.models import Q

from ontrack.market.querysets.base import BaseEntityQuerySet


class ExchangeQuerySet(BaseEntityQuerySet):
    pass


class EquityQuerySet(BaseEntityQuerySet):
    pass


class IndexQuerySet(BaseEntityQuerySet):
    pass


class EquityIndexQuerySet(BaseEntityQuerySet):
    def unique_search(self, index_symbol=None, equity_symbol=None):
        if equity_symbol is None or equity_symbol is None:
            return self.none()

        lookup_equity = Q(equity__symbol__iexact=equity_symbol)
        lookup_index = Q(index__symbol__iexact=index_symbol)

        return self.filter(lookup_equity & lookup_index)


class MarketDayTypeQuerySet(BaseEntityQuerySet):
    def unique_search(self, name=None):
        if name is None:
            return self.none()

        lookups = Q(name__iexact=name)
        return self.filter(lookups)


class MarketDayCategoryQuerySet(BaseEntityQuerySet):
    def unique_search(self, code=None):
        if code is None:
            return self.none()

        lookups = Q(code__iexact=code)
        return self.filter(lookups)


class MarketDayQuerySet(BaseEntityQuerySet):
    def unique_search(
        self,
        category_code=None,
        category_id=None,
        daytype_id=None,
        daytype_name=None,
        date=None,
        day=None,
    ):
        if category_code is None and category_id is None:
            return self.none()

        if daytype_name is None and daytype_id is None:
            return self.none()

        if date is None and day is None:
            return self.none()

        if category_code is not None:
            lookups = Q(category__code__iexact=category_code)
        else:
            lookups = Q(category_id=category_id)

        if daytype_name is not None:
            lookups = lookups & Q(daytype__name__iexact=daytype_name)
        else:
            lookups = lookups & Q(daytype_id=daytype_id)

        if date is not None:
            lookups = lookups & Q(date=date)
        else:
            lookups = lookups & Q(day=day)

        return self.filter(lookups)
