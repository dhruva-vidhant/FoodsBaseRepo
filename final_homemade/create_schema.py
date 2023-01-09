import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="food_db",
        user='food',
        password='food')

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS food')
cur.execute('CREATE TABLE food (id serial PRIMARY KEY,'
								'name varchar NOT NULL,'
								'description varchar NOT NULL,'
								'price_cents integer NOT NULL,'
								'zipcode varchar NOT NULL,'
								'quantity integer NOT NULL,'
								'seller_name varchar NOT NULL,'
								'email varchar NOT NULL,'
								'keywords varchar[] NOT NULL,'
								'ingredients varchar[] NOT NULL,'
								'address varchar NOT NULL);'
								)


cur.execute('DROP TABLE IF EXISTS orders')
cur.execute('DROP TYPE IF EXISTS status')
cur.execute('CREATE TABLE orders (id serial PRIMARY KEY,'
	                              'seller_name varchar NOT NULL,'
								  'food_name varchar NOT NULL,'
								  'quantity integer NOT NULL,'
								  'comments varchar NOT NULL,'
								  'buyer_email varchar NOT NULL);'
								)

cur.execute('DROP TABLE IF EXISTS sellers')

	                               
cur.execute('DROP TABLE IF EXISTS buyers')


conn.commit()

cur.close()
conn.close()