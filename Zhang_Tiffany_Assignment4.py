import mysql.connector

print ("Starting up Assignment4...")

mydb = mysql.connector.connect(
  user='testuser2',    # could be root, or a user you created, I created 'testuser2'
  passwd='thepassword',  # the password for that use
  port=3306,
  database='hw4',   # the database to connect to
  host='127.0.0.1',   # localhost
  allow_local_infile='1'  # needed so can load local files
)

print(mydb)
myc = mydb.cursor()

myc.execute('set global local_infile = 1') 

myc.execute ("show databases")  # this returns a list in myc that you can iterate over
for x in myc:
	print(x) 

myc.execute ("use hw4") 

# print out which tables are in hw4
myc.execute ("show tables") 
for x in myc:
	print(x) 

myc.execute("drop table if exists CountryA ;")
myc.execute("drop table if exists CountryB ;")
myc.execute("drop table if exists RawMaterial ;")
myc.execute("drop table if exists Product ;")
myc.execute("drop table if exists ExportsTo ;")
myc.execute("drop table if exists ImportedBy ;")
myc.execute("drop table if exists Creates ;")
myc.execute("drop table if exists PurchasedBy ;")

myc.execute("""    # multi-line python comment is three double quotes
create table CountryA ( 
  cid int NOT NULL, 
  name varchar(100) NOT NULL, 
  pop int, 
  gdp float NOT NULL, 
  Primary Key (cid) ) ; 
""")

myc.execute("""
create table CountryB (
  cid int NOT NULL, 
  name varchar(100) NOT NULL, 
  pop int, 
  gdp float NOT NULL, 
  Primary Key (cid) ) ;
""")

myc.execute("""
create table RawMaterial (
  iid int NOT NULL, 
  name varchar(100) NOT NULL, 
  quantity int, 
  baseval float, 
  Primary Key (iid) ) ;
""")

myc.execute("""
create table Product (
  pid int NOT NULL, 
  name varchar(100) NOT NULL, 
  price float,
  Primary Key (pid) ) ;
""")

myc.execute("""
create table ExportsTo (
  cid int NOT NULL,
  iid int NOT NULL,
  raw varchar(100),
  transportation varchar (100),
  Primary Key (cid, iid) ) ;
""")

myc.execute("""
create table ImportedBy (
  cid int NOT NULL,
  iid int NOT NULL,
  idate date,
  transportation varchar (100),
  Primary Key (cid, iid) ) ;
""")


myc.execute("""
create table Creates (
  cid int NOT NULL,
  pid int NOT NULL,
  previous varchar(100),
  Primary Key (cid, pid) ) ;
""")

myc.execute("""
create table PurchasedBy (
  cid int NOT NULL,
  pid int NOT NULL,
  pdate date,
  total float,
  Primary Key (cid, pid) ) ;
""")

myc.execute("""
load data local infile 'countrya' into table CountryA
  fields terminated by ','
  lines terminated by '\n'
  ;
  """)

myc.execute("""
load data local infile 'countryb' into table CountryB
  fields terminated by ','
  lines terminated by '\n'
  ;
  """)

myc.execute("""
load data local infile 'raw_material' into table RawMaterial
  fields terminated by ','
  lines terminated by '\n'
  ;
""")

myc.execute("""
load data local infile 'product' into table Product
  fields terminated by ','
  lines terminated by '\n'
  ;
  """)

myc.execute("""
load data local infile 'exports_to' into table ExportsTo
  fields terminated by ','
  lines terminated by '\n'
  ;
  """)

myc.execute("""
load data local infile 'imported_by' into table ImportedBy
  fields terminated by ','
  lines terminated by '\n'
  ;
""")

myc.execute("""
load data local infile 'creates' into table Creates
  fields terminated by ','
  lines terminated by '\n'
  ;
  """)

myc.execute("""
load data local infile 'purchased_by' into table PurchasedBy
  fields terminated by ','
  lines terminated by '\n'
  ;
  """)

myc.execute("""
load data local infile 'imported_by' into table ImportedBy
  fields terminated by ','
  lines terminated by '\n'
  ;
""")

# MUST commit the changes!!!!  (if you did any inserts, deletes, updates, load data.... )
mydb.commit()
mydb.close() 
