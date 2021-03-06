import time
import pyupbit
import datetime

access = "fHpE3fxFWxbHWztM0VBRlFRGWa2yt7CZwLFT3SBY"
secret = "mb9vr8paf8kOMaI20Oqx3j7mD1qhmllMBvYXZMnC"

upbit = pyupbit.Upbit(access, secret)

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0

target_price_bch = get_target_price("KRW-BCH", 0.5)
target_price_ltc = get_target_price("KRW-LTC", 0.5)
target_price_btt = get_target_price("KRW-BTT", 0.5)
target_price_doge = get_target_price("KRW-DOGE", 0.5)

print(target_price_bch)
print(target_price_ltc)
print(target_price_btt)
print(target_price_doge)