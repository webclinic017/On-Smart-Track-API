import pytest

from ontrack.market.api.logic.endofdata import EndOfDayData
from ontrack.market.api.tests.test_base import assert_record_creation, test_date
from ontrack.market.models.lookup import Exchange
from ontrack.market.models.participant import (
    ParticipantActivity,
    ParticipantStatsActivity,
)


class TestPullParticipantData:
    @pytest.fixture(autouse=True)
    def injector(self):
        self.exchange_qs = Exchange.backend.get_queryset()
        self.participant_qs = ParticipantActivity.backend.get_queryset()
        self.participant_stats_qs = ParticipantStatsActivity.backend.get_queryset()

    @pytest.fixture(autouse=True)
    def equity_data_fixture(self, exchange_fixture):
        self.exchange_fixture = exchange_fixture
        self.endofdaydata = EndOfDayData(exchange_fixture.symbol)

    @pytest.mark.integration
    @pytest.mark.eod_data_pull
    def test_pull_parse_eod_data(self):
        assert self.exchange_fixture is not None
        assert self.exchange_fixture.symbol is not None

        date = test_date
        result = self.endofdaydata.load_participant_eod_data(date)
        records_stats = self.endofdaydata.create_or_update(result, ParticipantActivity)
        assert_record_creation((result, records_stats))

        # check update logic
        date = test_date
        result = self.endofdaydata.load_participant_eod_data(date)
        assert isinstance(result, str)

    @pytest.mark.integration
    @pytest.mark.eod_data_pull
    def test_pull_parse_eod_stats_data(self):
        assert self.exchange_fixture is not None
        assert self.exchange_fixture.symbol is not None

        date = test_date
        result = self.endofdaydata.load_participant_stats_eod_data(date)
        records_stats = self.endofdaydata.create_or_update(
            result, ParticipantStatsActivity
        )
        assert_record_creation((result, records_stats))

        # check update logic
        date = test_date
        result = self.endofdaydata.load_participant_stats_eod_data(date)
        assert isinstance(result, str)