from quantplay.broker import motilal

motilal = Motilal()
motilal.generate_token()
motilal.send_otp()
# motilal.verify_otp(otp)
ltp = motilal.get_ltp("NSE", "SBIN")
print(ltp)

motilal.place_order("SBIN", "NSE", 1, "LIMIT", "BUY", "test", "NORMAL", ltp, 0)
orders_placed = motilal.get_orders()
print(orders_placed)

motilal.modify_orders_till_complete(orders_placed)