#!/usr/bin/python
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","12345678","RESTAURANT")

# prepare a cursor object using cursor() method
# abstraction meant for data set traversal
cursor = db.cursor()
fid=0
cid=0
pid=0
def add_customer(cid,oid,pid):
	fname=raw_input("Enter first name: ")
	lname=raw_input("Enter last name: ")
	try:
		cursor.execute("""INSERT INTO CUSTOMER VALUES (%s,%s,%s,%s,%s);""",(cid,fname,lname,oid,pid))
def add_menu_item(foodid):
	item=raw_input("Enter the name of food item: ")
	price=int(raw_input("Enter its price: "))
	try:
	   	# Execute the SQL command
		cursor.execute("""INSERT INTO MENU VALUES (%s,%s, %s);""",(foodid,item,price))
	   	db.commit()

		###########################################################
		###########################################################

		# Fetch all rows using fetchall() method.
		# data_all = cursor.fetchall()
		# for tup in data_all :
		# 	print tup

		# ###########################################################
		# ###########################################################

		# rc = cursor.rowcount
		print "added new menu item"
		fid=fid+1
	except:
	   	# Rollback in case there is any error
	   	db.rollback()


while True:
	i=int(raw_input("enter your choice: "))
	if i==3:
		add_menu_item(fid)
	elif i==2:
		add_customer(cid,oid,pid)
	else: 
		break
#close the cursor
cursor.close()

# close the connection
db.close()
