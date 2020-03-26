import talib


def macd(close, previous_macds=[], fast_period=12, slow_period=26, signal_period=9):
    """
    MACD - Moving Average Convergence Divergence
    previous_macd: numpy.ndarray of previous MACDs
    Returns:
        - macd
        - macd_line
    """
    dataset_size = close.size
    if dataset_size < slow_period-1:
        print('Error in macd.py: passed not enough data! Required: ' + str(slow_period) +
              ' passed: ' + str(dataset_size))
        return None, None

    try:
        ema_slow = talib.EMA(close, timeperiod=slow_period)[-1]
        ema_fast = talib.EMA(close[-fast_period:], timeperiod=fast_period)[-1]
        macd_value = ema_fast - ema_slow

        # print('previous_macds:', previous_macds)
        if len(previous_macds) < signal_period:
            signal_line = None
        else:
            signal_line = talib.EMA(previous_macds[-signal_period:], timeperiod=signal_period)[-1]
    except Exception as e:
        print('Got Exception in macd.py. Details: ' + str(e) + '. Data: ' + str(previous_macds))
        return None, None

    return macd_value, signal_line



