import settings
import csv
import datetime
import pyodbc

# read csv
with open(settings.CSV_PATH, encoding='utf-8-sig', errors='ignore') as f:
    reader = csv.reader(f, delimiter=";")
    l = [row for row in reader]

print('Number of elements:', len(l)-1)

# connect to DB
connect = pyodbc.connect('DRIVER='+settings.DRIVER+';SERVER='+settings.SERVER+';DATABASE='+settings.DATABASE +
                         ';UID='+settings.USER+';PWD=' + settings.PASSWORD + ';Encrypt=yes;TrustServerCertificate=yes', autocommit=True)
cursor = connect.cursor()

count = 0
records = ''

print('Processing started...')

for i in range(1, len(l)):

    d = {'id': settings.TYPE_ID + ':' + l[i][0], 'typeId': settings.TYPE_ID, 'name': l[i][1],
         'birth_date': datetime.datetime.strptime(l[i][2], "%d.%m.%Y").strftime("%Y-%m-%d"),
         'fav_animal': l[i][3], 'source': settings.SOURCE, 'actionType': 'INSERT'}

    SQL = "INSERT INTO my_db.dbo.my_table\
        (ID , TypeID , AttName , AttValue , source, Action)\
        VALUES\
        (\'" + d['id'] + '\', \'' + d['typeId'] + "\', \'name\', \'" + d['name'] + '\',\' ' + d['source']+'\', \'' + d['actionType'] + "\')\
        ,(\'" + d['id'] + '\', \'' + d['typeId'] + "\', \'birth.date\', \'" + d['birth_date'] + '\',\' ' + d['source']+'\', \'' + d['actionType'] + "\')\
        ,(\'" + d['id'] + '\', \'' + d['typeId'] + "\', \'favorite.animal\', \'" + d['fav_animal'] + '\',\' '+d['source']+'\', \'' + d['actionType'] + "\')"

    cursor.execute(SQL)
    count += 1

    if settings.DEBUG == 'TRUE':
        # if 10 elements was processed: print 10 IDs, else: add ID into string
        if count % 10 == 0:
            print(records)
            records = ''
        else:
            records += l[i][0] + ', '


connect.commit()

cursor.close()
connect.close()

print('Processing completed:', count, 'elements have been processed.')
