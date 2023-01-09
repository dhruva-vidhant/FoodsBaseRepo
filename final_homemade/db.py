import psycopg2
import smtplib

MY_EMAIL = "YOUR_EMAIL"
MY_PASSWORD = "YOUR_PASSWORD"

conn = psycopg2.connect(
        host="localhost",
        database="food_db",
        user='food',
        password='food')

cur = conn.cursor()

def add_order(seller_name, name, quantity, comments, buyer_email):
    cur.execute('INSERT INTO orders(seller_name, food_name, quantity, comments, buyer_email)'
                 'VALUES(%s, %s, %s, %s, %s);', (seller_name, name, quantity, comments, buyer_email))
    conn.commit()
    #cur.execute('SELECT email FROM food WHERE name = %s', name)
    #seller_email = cur.fetchone()

    #connection = smtplib.SMTP("smtp.gmail.com", 587)
    #connection.starttls()
    #connection.login(MY_EMAIL, MY_PASSWORD)
    #connection.sendmail(
            #from_addr=MY_EMAIL,
            #to_addrs=[seller_email, buyer_email],
            #msg=f"You got an order from {buyer_email} for {name}. There are {quantity} left in store. Please let them know by email on the details of this order. Here are some comments by  the buyer: {comments}")


    

def add_food(name, description, price, zipcode, quantity, seller, email, keywords, ingredients, address):
    cur.execute('INSERT INTO food(name, description, price_cents, zipcode, quantity, seller_name, email, keywords, ingredients, address)'
                 'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);', (name, description, price, zipcode, quantity, seller, email, keywords, ingredients, address))
    conn.commit()

def get_info(id):
    cur.execute('SELECT * FROM food WHERE id = %s', (id,))
    return cur.fetchone()

print(get_info(1))

#add_order('Dhruva', 'pasta', 10, 'good', "me")

#', 'good', '1000', 94566, 10, 'me', 'xyz@gmail.com', ['good', 'veg'], ['pasta', 'sauce'])

#cur.close()
#conn.close()





#psycopg2.OperationalError: connection to server at "localhost" (127.0.0.1), port 5432 failed: FATAL:  password auth failed for user «food»
#connection to server at "localhost" (127.0.0.1), port 5432 failed: FATAL:  password auth failed for user «food»

#createdb: error: failed the connection to the socket «/var/run/postgresql/.s.PGSQL.5432»: FATAL:  doesn't exist such roles «root»