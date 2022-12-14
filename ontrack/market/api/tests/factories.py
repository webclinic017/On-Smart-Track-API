from factory.django import DjangoModelFactory

from ontrack.market.models.lookup import Equity, Exchange, Index


class ExchangeFactory(DjangoModelFactory):

    name = "National Stock Exchange of India Ltd"
    symbol = "nse"
    start_time = "09:15:00"
    end_time = "15:30:00"
    data_refresh_time = "20:00:00"
    time_zone = "Asia/Kolkata"

    class Meta:
        model = Exchange
        django_get_or_create = [
            "name",
            "symbol",
            "start_time",
            "end_time",
            "data_refresh_time",
            "time_zone",
        ]


class EquityFactory(DjangoModelFactory):

    name = "Reliance"
    symbol = "reliance"
    chart_symbol = "reliance"
    lot_size = 50
    strike_difference = 100
    is_active = True
    exchange = ExchangeFactory

    class Meta:
        model = Equity
        django_get_or_create = [
            "name",
            "symbol",
            "chart_symbol",
            "lot_size",
            "strike_difference",
            "is_active",
        ]


class IndexFactory(DjangoModelFactory):

    name = "Nifty 50"
    symbol = "nifty"
    chart_symbol = "nifty"
    lot_size = 50
    strike_difference = 100
    is_active = True
    exchange = ExchangeFactory
    ordinal = 1

    class Meta:
        model = Index
        django_get_or_create = [
            "name",
            "symbol",
            "chart_symbol",
            "lot_size",
            "strike_difference",
            "is_active",
            "ordinal",
        ]
