import datetime

print (datetime.date.today())

fechaCompleta=datetime.datetime.now()
print(fechaCompleta)
print(fechaCompleta.year)
print(fechaCompleta.month)
print(fechaCompleta.day)

fechaPersonalizada=fechaCompleta.strftime("%d/%m/%Y %H: %M: %S")
print ("Mi fecha personalizada: ", fechaPersonalizada)


