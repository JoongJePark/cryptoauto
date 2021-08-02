import pyupbit

access = "fHpE3fxFWxbHWztM0VBRlFRGWa2yt7CZwLFT3SBY"          # 본인 값으로 변경
secret = "mb9vr8paf8kOMaI20Oqx3j7mD1qhmllMBvYXZMnC"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회