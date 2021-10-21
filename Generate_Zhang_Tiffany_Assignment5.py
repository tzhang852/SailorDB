import mysql.connector

print ("Starting up Assignment5...")

mydb = mysql.connector.connect(
  user='testuser2',    # could be root, or a user you created, I created 'testuser2'
  passwd='thepassword',  # the password for that use
  port=3306,
  database='hw5',   # the database to connect to
  host='127.0.0.1',   # localhost
  allow_local_infile='1'  # needed so can load local files
)

print(mydb)
myc = mydb.cursor()

myc.execute('set global local_infile = 1') 

myc.execute ("show databases")  # this returns a list in myc that you can iterate over
for x in myc:
	print(x) 

myc.execute ("use hw5") 

# print out which tables are in hw5
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
  country_a_id int NOT NULL, 
  country_a_name varchar(100) NOT NULL, 
  country_a_population int, 
  country_a_gdp float NOT NULL, 
  Primary Key (country_a_id) ) ; 
""")

myc.execute("""
create table CountryB (
  country_b_id int NOT NULL, 
  country_b_name varchar(100) NOT NULL, 
  country_b_population int, 
  country_b_gdp float NOT NULL, 
  Primary Key (country_b_id) ) ;
""")

myc.execute("""
create table RawMaterial (
  raw_material_id int NOT NULL, 
  raw_material_name varchar(100) NOT NULL, 
  quantity int, 
  base_value float, 
  Primary Key (raw_material_id) ) ;
""")

myc.execute("""
create table Product (
  product_id int NOT NULL, 
  product_name varchar(100) NOT NULL, 
  price float,
  Primary Key (product_id) ) ;
""")

myc.execute("""
create table ExportsTo (
  country_a_id int NOT NULL,
  country_a_name varchar(100),
  raw_material_id int NOT NULL,
  raw_material_name varchar(100),
  transportation varchar (100),
  Primary Key (country_a_id, raw_material_id) ) ;
""")

myc.execute("""
create table ImportedBy (
  country_b_id int NOT NULL,
  country_b_name varchar(100),
  raw_material_id int NOT NULL,
  raw_material_name varchar(100),
  import_date date,
  warehouse varchar(100),
  transportation varchar (100),
  total float,
  Primary Key (country_b_id, raw_material_id) ) ;
""")


myc.execute("""
create table Creates (
  country_b_id int NOT NULL,
  country_b_name varchar(100),
  product_id int NOT NULL,
  product_name varchar(100),
  previous_product_id int,
  previous_product_name varchar(100),
  Primary Key (country_b_id, product_id) ) ;
""")

myc.execute("""
create table PurchasedBy (
  country_a_id int NOT NULL,
  country_a_name varchar(100),
  product_id int NOT NULL,
  product_name varchar(100),
  purchase_date date,
  total float,
  Primary Key (country_a_id, product_id) ) ;
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
