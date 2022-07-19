from math import log, e
from scipy import stats


def bsm(stock_price, strike_price, rate, time, volatility, dividend=0.0):
    d1 = (log(stock_price / strike_price) + (rate - dividend + volatility ** 2 / 2) * time) / (volatility * time ** .5)
    d2 = d1 - volatility * time ** .5

    call = stats.norm.cdf(d1) * stock_price * e ** (-dividend * time) - stats.norm.cdf(d2) * strike_price * e ** (-rate * time)
    put = stats.norm.cdf(-d2) * strike_price * e ** (-rate * time) - stats.norm.cdf(-d1) * stock_price * e ** (-dividend * time)

    return call, put
