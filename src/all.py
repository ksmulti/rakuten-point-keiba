import rakuten_keiba_lib as RKL
import spat4_lib
import odds_park_lib
import keirin_jp_lib
import boat_race_lib

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

kjpc = keirin_jp_lib.KeirinJPCore()
kjpc.Index()
kjpc.Login()
kjpc.ChargeMoney()
kjpc.Quit()
print("keirin jp end")

brc = boat_race_lib.BoatRaceCore()
brc.Index()
brc.Login()
brc.ChargeMoney()
brc.Quit()
print("boat race end")