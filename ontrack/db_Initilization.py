from ontrack.lookup.api.logic.lookup import InitializeData as lookup_initialization
from ontrack.market.api.logic.endofdata import EndOfDayData
from ontrack.market.api.logic.livedata import LiveData
from ontrack.market.api.logic.lookup import MarketLookupData as market_initialization
from ontrack.utils.datetime import DateTimeHelper


def initilize_data(step=1):

    if step == 1:
        obj = market_initialization("nse")
        obj.load_initial_data()

        obj = lookup_initialization()
        obj.load_initial_data()

    if step <= 2:
        date = DateTimeHelper.get_date_time(2022, 10, 20)
        obj = EndOfDayData("nse")
        obj.load_eod_data(date)

    if step <= 3:
        obj = LiveData("nse")
        obj.load_live_data()
