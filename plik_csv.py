#odczyt pliku csv

path = 'C:\\Users\\vdi-student\\Desktop\\WSB\\rozliczenie.csv'
mode ='r'
with open (path, mode) as plik_csv_1:
    content = plik_csv_1.readlines()

print(type(content))
print(len(content))
print(content)
print(content[4])

#dane = 'mama.tata.pies'
#print(dane)
#dane = dane.split('.')
#print(dane)

for i in range (len(content)):
    content[i] = content[i].split(';')
print(content)
print(content[5])
print(content[5][3])




#with open('C:\\Users\\vdi-student\\Desktop\\WSB\\rozliczenie.cvs', 'r') as plik_csv_2: