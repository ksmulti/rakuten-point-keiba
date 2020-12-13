import rakuten_keiba_lib as RKL
import spat4_lib
import odds_park_lib

rkc = RKL.RakutenKeibaCore()
rkc.Index()
rkc.Login()
rkc.ChargeMoney()
rkc.Quit()
print("rakuten keiba end")

s4c = spat4_lib.SPAT4Core()
s4c.Index()
s4c.Login()
s4c.ChargeMoney()
s4c.Quit()
print("spat4 end")

opc = odds_park_lib.OddsParkCore()
opc.Index()
opc.Login()
opc.ChargeMoney()
opc.Quit()
print("odds park end")