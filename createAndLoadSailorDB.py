# first need to make sure connector is installed:
#  python3 -m pip install mysql-connector-python

# this assumes you have created a user named "testuser2" with all privileges:
#     mysql> create user 'testuser2'@'localhost' identified by 'thepassword' ;
#     mysql> grant all privileges on *.* to 'testuser2'@'localhost' ;
# to read more about how to create users: 
#  https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql


import mysql.connector

# note:  look at at end of this file - mydb.commit() and mydb.close() -> do not forget
# MUST commit the changes!!!!  (if you did any inserts, deletes, updates, load data.... )

print ("Hello - starting createAndLoadSailorDB.py")

mydb = mysql.connector.connect(
  user='testuser2',    # could be root, or a user you created, I created 'testuser2'
  password='thepassword',  # the password for that use
  port=3306,
  database='assignment_4',   # the database to connect to
  host='127.0.0.1',   # localhost
  allow_local_infile='1'  # needed so can load local files
)

print(mydb)
myc = mydb.cursor()   # myc name short for "my cursor"

# We need to reset the variable that allows loading of local files 
myc.execute('set global local_infile = 1') 

myc.execute ("show databases")  # this returns a list in myc that you can iterate over
for x in myc:
	print(x) 

myc.execute ("use assignment_4") 

# print out which tables are in assignment_4
myc.execute ("show tables") 
for x in myc:
	print(x) 




# myc.execute("drop table if exists Reserve ;")
# myc.execute("drop table if exists Sailors ;")
# myc.execute("drop table if exists Boats ;")

# myc.execute("""    # multi-line python comment is three double quotes
# create table Sailors ( 
#   sid int, 
#   name varchar(20) NOT NULL, 
#   age int, 
#   rating float NOT NULL, 
#   Primary Key (sid) ) ; 
# """)


# myc.execute("""
# create table Boats (
#   bid int,
#   name varchar(20),
#   ratingNeeded int,
#   bcolor varchar(20),
#   PRIMARY KEY (bid) ) ;
# """)

# myc.execute("""
# create table Reserve (
#   bid int,
#   sid int, 
#   rdate date,
#   PRIMARY KEY (bid,sid,rdate),
#   Foreign Key (bid) references Boats(bid),
#   Foreign Key (sid) references Sailors(sid) ) ;
# """)


# print("Before loading Sailors:  select * from sailors where sid < 10")
# myc.execute ("select * from sailors where sid < 10") ;
# for x in myc:
# 	print(x) 


# myc.execute("""
#   load data local infile 'data_sailors' into table sailors 
#   fields terminated by ',' 
#   lines terminated by '\n' ; 
# """)

# print(myc.rowcount, " tuples were inserted")

# print("After loading Sailors:  select * from sailors where sid < 10")
# myc.execute ("select * from sailors where sid < 10") ;
# for x in myc:
# 	print(x) 


# myc.execute("""
# load data local infile 'data_boats' into table boats
#   fields terminated by ','
#   lines terminated by '\n' ;
# """)

# myc.execute("""
# load data local infile 'data_reserve' into table reserve
#   fields terminated by ','
#   lines terminated by '\n' ;
# """)

myc.execute("""
set global local_infile = 1 ;
""")

myc.execute("""drop table if exists Reserve ;""")
myc.execute("""drop table if exists Sailors ;""")
myc.execute("""drop table if exists Boats ;""")

myc.execute("""create table Sailors (
  sid int,
  name varchar(20) NOT NULL,
  age int,
  rating float NOT NULL,
  Primary Key (sid) ) ;
  """)

myc.execute("""
create table Boats (
  bid int,
  name varchar(20),
  ratingNeeded int,
  bcolor varchar(20),
  PRIMARY KEY (bid) ) ;
  """)

myc.execute("""
create table Reserve (
  bid int,
  sid int, 
  rdate date,
  PRIMARY KEY (bid,sid,rdate),
  Foreign Key (bid) references Boats(bid),
  Foreign Key (sid) references Sailors(sid) ) ;
  """)

myc.execute("""
load data local infile 'data_sailors.csv' into table sailors
  fields terminated by ','
  lines terminated by '\n'
  ;
  """)

myc.execute("""
load data local infile 'data_boats.csv' into table boats
  fields terminated by ','
  lines terminated by '\n'
  ;
  """)

myc.execute("""
load data local infile 'data_reserve.csv' into table reserve
  fields terminated by ','
  lines terminated by '\n'
  ;
""")


# MUST commit the changes!!!!  (if you did any inserts, deletes, updates, load data.... )
mydb.commit()
mydb.close() 

