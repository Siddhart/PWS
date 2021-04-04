import time
line = "--------------------------------------------------"

#variabele waarden
snelheid = 2500 # ms/s

#vaste waarden
Height = 85000 #m
massa = 100000 #kg
Tinterval = 1 #s
a = 200 #oppvervlakte
c = 0.8 #constante
straalAarde = 6371000 #straal aarde
heat = 200
jC = 0.00052656507646646

#constante atmosphere
tr = 0.0125 #kg/m3
st = 0.000125 #kg/m3
me = 0.0000125 #kg/m3
th = 0.00000000000000125 #kg/m3

count = 0
while True and (Height >= 0):
    time.sleep(1)
    #define p
    if(Height >= 85000 and Height <= 700000):
        p = th
    elif(Height >= 50000 and Height <= 85000):
        p = me
    elif(Height >= 20000 and Height <= 50000):
        p = st
    elif(Height >= 0 and Height <= 20000):
        p = tr
    
    #define deltaT
    deltaT = 0
    r1 = ((snelheid ** 2) / 9.81) 
    weerstandsKracht = (0.5 * p * (snelheid ** 2) * c * a) #bereken de weerstandskracht
    deltaV = ((weerstandsKracht * Tinterval) / massa)   
    snelheid -= deltaV
    r2 = ((snelheid ** 2) / 9.81) 
    deltaR = (r1 - r2)
    P1 = (weerstandsKracht * snelheid)

    if(count == 0):
      heat == 200
    
    P2 = (0.000000057 * a * (heat ** 4))
    PNetto = P1 - P2
    deltaQ = PNetto * Tinterval
    deltaT = (deltaQ / ( ( (a * 0.02) * 144.2) * 1200))
    heat += deltaT
    Height -= deltaR

    print(line)
    print("weerstandskracht: " + str(weerstandsKracht))
    print("delta V: " + str(deltaV))
    print("nieuwe snelheid: " + str(snelheid))
    print("Hoogte: " + str(Height))
    print("Hitte: " + str(heat))
    print(line)
    count += 1