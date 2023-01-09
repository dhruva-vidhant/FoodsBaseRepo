import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="food_db",
        user='food',
        password='food')

cur = conn.cursor()

def searchByKeyword(keyword):
	list = []
	cur.execute("SELECT * FROM food")
	for i in cur.fetchall():
		if i[8][0].count(keyword)>0:
			list.append(i)
	return list

def searchByTitle(title):
	list = []
	cur.execute("SELECT * FROM food")
	for i in cur.fetchall():
		if title in i[1]:
			list.append(i)
	return list


#print(searchByTitle('pasta'))