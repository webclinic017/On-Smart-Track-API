from django.db import models

from ontrack.market.managers.equity import (
    EquityDerivativeBackendManager,
    EquityEndOfDayBackendManager,
    EquityLiveDataBackendManager,
    EquityLiveOpenInterestManager,
)
from ontrack.market.models.base import (
    DerivativeEndOfDay,
    EntityCalcutatedValues,
    EntityLiveData,
    EntityLiveFuture,
    EntityLiveOpenInterest,
    EntityLiveOptionChain,
    LiveDerivativeData,
    TradingInformation,
    numeric_field_values,
)
from ontrack.market.models.lookup import Equity
from ontrack.utils.base.model import BaseModel


class EquityEndOfDay(TradingInformation):
    entity = models.ForeignKey(
        Equity, related_name="eod_data", on_delete=models.CASCADE
    )

    delivery_quantity = models.DecimalField(**numeric_field_values)
    delivery_percentage = models.DecimalField(**numeric_field_values)

    backend = EquityEndOfDayBackendManager()

    class Meta(BaseModel.Meta):
        ordering = []
        unique_together = ("entity", "date")

    def __str__(self):
        return f"{self.entity.name}-{self.date.strftime('%d/%m/%Y')}"


class EquityEodCalcutatedValues(EntityCalcutatedValues):
    entity = models.ForeignKey(
        Equity, related_name="eod_calculated_data", on_delete=models.CASCADE
    )

    average_quantity_per_trade = models.DecimalField(**numeric_field_values)
    average_volumn = models.DecimalField(**numeric_field_values)
    average_delivery_percentage = models.DecimalField(**numeric_field_values)
    average_open_interest = models.DecimalField(**numeric_field_values)

    backend = EquityEndOfDayBackendManager()

    class Meta(BaseModel.Meta):
        ordering = ["-created_at"]
        unique_together = ("entity", "date")

    def __str__(self):
        return f"{self.entity.name}-{self.date.strftime('%d/%m/%Y')}"


class EquityInsiderTrade(BaseModel):
    entity = models.ForeignKey(
        Equity, related_name="insider_trades", on_delete=models.CASCADE
    )
    category_of_person = models.CharField(max_length=100)
    no_of_shares = models.IntegerField()
    value_of_shares = models.DecimalField(**numeric_field_values)
    mode_of_acquisition = models.CharField(max_length=100)
    pull_date = models.DateField(auto_now=True)

    class Meta(BaseModel.Meta):
        ordering = ["-created_at"]

    def __str__(self):
        return self.entity.name


class EquityPledged(BaseModel):
    entity = models.ForeignKey(
        Equity, related_name="equity_pledged", on_delete=models.CASCADE
    )
    total_shares = models.IntegerField()
    total_promoter_holding = models.IntegerField()
    total_public_holding = models.IntegerField()
    total_encumbered_by_promoter = models.IntegerField()
    pull_date = models.DateField(auto_now=True)

    class Meta(BaseModel.Meta):
        ordering = ["-created_at"]

    def __str__(self):
        return self.entity.name


class EquitySast(BaseModel):
    entity = models.ForeignKey(
        Equity, related_name="equity_sast", on_delete=models.CASCADE
    )
    total_acquisition = models.IntegerField()
    total_sale = models.IntegerField()
    total_after_acquistion = models.IntegerField()
    pull_date = models.DateField(auto_now=True)

    class Meta(BaseModel.Meta):
        ordering = ["-created_at"]

    def __str__(self):
        return self.entity.name


class EquityDerivativeEndOfDay(DerivativeEndOfDay):
    entity = models.ForeignKey(
        Equity, related_name="derivative_eod_data", on_delete=models.CASCADE
    )

    backend = EquityDerivativeBackendManager()

    class Meta(BaseModel.Meta):
        ordering = ["-created_at"]
        unique_together = (
            "entity",
            "date",
            "instrument",
            "expiry_date",
            "strike_price",
            "option_type",
        )

    def __str__(self):
        return (
            f"{self.entity.name}-"
            f"{self.date.strftime('%d/%m/%Y')}-"
            f"{self.instrument}-"
            f"{self.expiry_date.strftime('%d/%m/%Y')}"
        )


class EquityLiveDerivativeData(LiveDerivativeData):
    entity = models.ForeignKey(
        Equity, related_name="derivative_live_data", on_delete=models.CASCADE
    )

    backend = EquityDerivativeBackendManager()

    class Meta(BaseModel.Meta):
        ordering = ["-created_at"]
        unique_together = (
            "entity",
            "date",
            "instrument",
            "expiry_date",
            "strike_price",
            "option_type",
        )

    def __str__(self):
        return (
            f"{self.entity.name}-"
            f"{self.date.strftime('%d/%m/%Y')}-"
            f"{self.instrument}-"
            f"{self.expiry_date.strftime('%d/%m/%Y')}"
        )


class EquityLiveData(EntityLiveData):
    entity = models.ForeignKey(
        Equity, related_name="live_data", on_delete=models.CASCADE
    )

    backend = EquityLiveDataBackendManager()

    class Meta(BaseModel.Meta):
        ordering = ["-created_at"]
        unique_together = (
            "entity",
            "date",
        )

    def __str__(self):
        return f"{self.entity.name}-{self.date.strftime('%d/%m/%Y')}"


class EquityLiveOptionChain(EntityLiveOptionChain):
    entity = models.ForeignKey(
        Equity, related_name="live_optionchain", on_delete=models.CASCADE
    )

    backend = EquityDerivativeBackendManager()

    class Meta(BaseModel.Meta):
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.entity.name}-{self.date.strftime('%d/%m/%Y')}"


class EquityLiveFuture(EntityLiveFuture):
    entity = models.ForeignKey(
        Equity, related_name="live_future", on_delete=models.CASCADE
    )

    backend = EquityDerivativeBackendManager()

    class Meta(BaseModel.Meta):
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.entity.name}-{self.date.strftime('%d/%m/%Y')}"


class EquityLiveOpenInterest(EntityLiveOpenInterest):
    entity = models.ForeignKey(
        Equity, related_name="live_openInterest", on_delete=models.CASCADE
    )

    backend = EquityLiveOpenInterestManager()

    class Meta(BaseModel.Meta):
        ordering = ["-created_at"]
        unique_together = (
            "entity",
            "date",
        )

    def __str__(self):
        return f"{self.entity.name}-{self.date.strftime('%d/%m/%Y')}"
