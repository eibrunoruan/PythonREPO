import datetime
# Carregue a data atual do computador e, com base na data atual,
# apresente a data de dois dias no futuro

date = datetime.datetime.now()
newdate = date + datetime.timedelta(2)
print(newdate)

# Carregue a data atual do computador e apresente somente a data
print(datetime.date.today())