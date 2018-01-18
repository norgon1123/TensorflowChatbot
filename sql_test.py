import sqlite3

timeframe = '2015-01'

connection = sqlite3.connect('{}.db'.format(timeframe))
c = connection.cursor()

c.execute("SELECT * from parent_reply")
results = c.fetchall()
print (len(results))
