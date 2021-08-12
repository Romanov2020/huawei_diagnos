from pyModbusTCP.client import ModbusClient
c=ModbusClient(host='194.28.6.9',port=502,auto_open=True,auto_close=True)
#Напряжение фаз

data=c.read_holding_registers(32277,1)
data2=c.read_holding_registers(32278,1)
data3=c.read_holding_registers(32279,1)

#Сила тока фаз

afasA=c.read_holding_registers(32280,1)
afasB=c.read_holding_registers(32281,1)
afasC=c.read_holding_registers(32282,1)

fazA= (max(afasA))/10
fazB= (max(afasB))/10
fazC= (max(afasC))/10

#Другие параметры

freq=c.read_holding_registers(32283,1)
tempera=c.read_holding_registers(32286,1)
lastour=c.read_holding_registers(32298,3)
lastday=c.read_holding_registers(32300,2)
lastmonth=c.read_holding_registers(32302,2)
all=c.read_holding_registers(32306,2)

systime=c.read_holding_registers(32200,2)

pv1volt=c.read_holding_registers(32262,1)
pv2volt=c.read_holding_registers(32264,1)
pv3volt=c.read_holding_registers(32266,1)
pv4volt=c.read_holding_registers(32268,1)
pv5volt=c.read_holding_registers(32270,1)
pv6volt=c.read_holding_registers(32272,1)
pv7volt=c.read_holding_registers(32314,1)
pv8volt=c.read_holding_registers(32316,1)

pv1amper=c.read_holding_registers(32263,1)
pv2amper=c.read_holding_registers(32265,1)
pv3amper=c.read_holding_registers(32267,1)
pv4amper=c.read_holding_registers(32269,1)
pv5amper=c.read_holding_registers(32271,1)
pv6amper=c.read_holding_registers(32273,1)
pv7amper=c.read_holding_registers(32315,1)
pv8amper=c.read_holding_registers(32317,1)


pikpowertoday=c.read_holding_registers(32288,2)
realpower=c.read_holding_registers(32290,2)

efinv=c.read_holding_registers(32285,1)
ef=(max(efinv))/100




pik=(max(pikpowertoday))/1000
real=(max(realpower))/1000

st=(max(systime))

faza1= (max(data))/10
faza2= (max(data2))/10
faza3= (max(data3))/10
temp= (max(tempera))/10
last= (max(lastour))/100
lastd=(max(lastday))/100
lastm=(max(lastmonth))/100
allinf=(max(all))/100

print(lastmonth)


fr=(max(freq))/100


pv1=(max(pv1volt))/10
pv2=(max(pv2volt))/10
pv3=(max(pv3volt))/10
pv4=(max(pv4volt))/10
pv5=(max(pv5volt))/10
pv6=(max(pv6volt))/10
pv7=(max(pv7volt))/10
pv8=(max(pv8volt))/10

pv1a=(max(pv1amper))/10
pv2a=(max(pv2amper))/10
pv3a=(max(pv3amper))/10
pv4a=(max(pv4amper))/10
pv5a=(max(pv5amper))/10
pv6a=(max(pv6amper))/10
pv7a=(max(pv7amper))/10
pv8a=(max(pv8amper))/10

print("Напряжение фазы A: ",faza1,"Вольт")
print("Напряжение фазы B: ",faza2,"Вольт")
print("Напряжение фазы C: ",faza3,"Вольт")
print("Рабочая частота: ",fr,"Герц")

print("Температура инвертора: ",temp,"градусов")

print("Пиковая мощность сегодня: ",pik,"Kwh")
print("Текущая мощность: ",real,"Kwh")
print("Эфективность инвертора: ",ef,"%")

print("Выработано за последний час: ",last,"Kwh")
print("Выработано за день: ",lastd,"Kwh")
print("Выработано за месяц: ",lastm,"Kwh")
print("Выработано за все время: ",allinf,"Kwh")

print("PV1 напряжение",pv1,"Вольт"," PV1 сила тока",pv1a,"Ампер")
print("PV2 напряжение",pv2,"Вольт"," PV2 сила тока",pv2a,"Ампер")
print("PV3 напряжение",pv3,"Вольт"," PV3 сила тока",pv3a,"Ампер")
print("PV4 напряжение",pv4,"Вольт"," PV4 сила тока",pv4a,"Ампер")
print("PV5 напряжение",pv5,"Вольт"," PV5 сила тока",pv5a,"Ампер")
print("PV6 напряжение",pv6,"Вольт"," PV6 сила тока",pv6a,"Ампер")
print("PV7 напряжение",pv7,"Вольт"," PV7 сила тока",pv7a,"Ампер")
print("PV8 напряжение",pv8,"Вольт"," PV8 сила тока",pv8a,"Ампер") 