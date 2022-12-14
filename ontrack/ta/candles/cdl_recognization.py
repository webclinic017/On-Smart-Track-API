from itertools import compress

import numpy as np
import talib

from ontrack.ta.candles.cdl_ranking import candle_rankings


def recognize_candlestick(df):
    """
    Recognizes candlestick patterns and appends 2 additional columns to df;
    1st - Best Performance candlestick pattern matched by www.thepatternsite.com
    2nd - # of matched patterns
    """

    op = df["open"].astype(float)
    hi = df["high"].astype(float)
    lo = df["low"].astype(float)
    cl = df["close"].astype(float)

    candle_names = talib.get_function_groups()["Pattern Recognition"]

    # patterns not found in the patternsite.com
    exclude_items = (
        "CDLCOUNTERATTACK",
        "CDLLONGLINE",
        "CDLSHORTLINE",
        "CDLSTALLEDPATTERN",
        "CDLKICKINGBYLENGTH",
    )

    candle_names = [candle for candle in candle_names if candle not in exclude_items]

    # create columns for each candle
    for candle in candle_names:
        # below is same as;
        # df["CDL3LINESTRIKE"] = talib.CDL3LINESTRIKE(op, hi, lo, cl)
        df[candle] = getattr(talib, candle)(op, hi, lo, cl)

    df["candlestick"] = np.nan
    df["candlestick_pattern"] = np.nan
    df["candlestick_rank"] = np.nan
    for index, row in df.iterrows():

        # no pattern found
        if len(row[candle_names]) - sum(row[candle_names] == 0) == 0:
            df.loc[index, "candlestick"] = "000|NO_PATTERN|NEUTRAL|0"
            df.loc[index, "candlestick_pattern"] = "NO_PATTERN"
            df.loc[index, "candlestick_rank"] = 0
        else:
            add_candle_stick_pattern(df, row, index, candle_names)

    # clean up candle columns
    cols_to_drop = candle_names + list(exclude_items)
    df.drop(cols_to_drop, axis=1, inplace=True, errors="ignore")

    return df


def add_candle_stick_pattern(df, row, index, candle_names):
    data = compress(row[candle_names].keys(), row[candle_names].values != 0)
    patterns = list(data)
    container = []
    c_candlestick = []
    for pattern in patterns:
        if row[pattern] > 0:
            sentiment = "Bull"
            name = pattern + "_Bull"
            rank = f"{candle_rankings[name]:0>3}"
            value = str(row[pattern])
        else:
            sentiment = "Bear"
            name = pattern + "_Bear"
            rank = f"{candle_rankings[name]:0>3}"
            value = str(row[pattern])

        container.append(name)
        c_candlestick.append(f"{rank}|{pattern}|{sentiment}|{value}")

    rank_list = [candle_rankings[p] for p in container]
    if len(rank_list) == len(container):
        rank_index_best = rank_list.index(min(rank_list))
        df.loc[index, "candlestick_pattern"] = container[rank_index_best]
        df.loc[index, "candlestick_rank"] = min(rank_list)

        separator = ";"
        df.loc[index, "candlestick"] = separator.join(c_candlestick)
