from django.db import connection

def create_partition_triggers(**kwargs):
    print('(re)creating partition triggers for tickets...')
    file = open("tickets/create_triggers.sql","r")
    sql = file.read()    
    cursor = connection.cursor()
    cursor.execute(sql)
    print ('Done creating partition triggers.')