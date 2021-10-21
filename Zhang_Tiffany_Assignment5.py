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
myc = mydb.cursor(buffered=True)
# #print(mydb)
# myc = mydb.cursor()

myc.execute('set global local_infile = 1') 

myc.execute ("show databases")  # this returns a list in myc that you can iterate over
# for x in myc:
# 	print(x) 

myc.execute ("use hw5") 

# print out which tables are in hw5
myc.execute ("show tables") 
# for x in myc:
# 	print(x) 

# Question 2 part 1, simple insert
#show the count of countries with population = 24512641
myc.execute("select CA.country_a_id, CA.country_a_name, CA.country_a_population from countrya CA where CA.country_a_population = 24512641;") # should display 1
for x in myc:
    print("Original: ", x)

myc.execute("insert into countrya (country_a_id, country_a_name, country_a_population, country_a_gdp)" + 
"values (99999, 'Canada', 24512641, 99.999999)")

# show new count of countries
myc.execute("select CA.country_a_id, CA.country_a_name, CA.country_a_population from countrya CA where CA.country_a_population = 24512641;") # should display 2
for x in myc:
    print("Insert New: ", x)

# Question 2 part 2, simple update
#show the count of countries with population = 24512641
myc.execute("select CA.country_a_id, CA.country_a_name, CA.country_a_population from countrya CA where CA.country_a_population = 24512641;") # should display 2
for x in myc:
    print("Original: ", x)

myc.execute("update countrya set country_a_name = 'Brazil' where country_a_id = 99999")

# show new count of countries
myc.execute("select CA.country_a_id, CA.country_a_name, CA.country_a_population from countrya CA where CA.country_a_population = 24512641;") # should display 2
for x in myc:
    print("Update New: ", x)

#Question 2 part 3, update several tuples at once
#show the count of countries with population = 24512641
myc.execute("select CA.country_a_id, CA.country_a_name, CA.country_a_population from countrya CA where CA.country_a_population = 24512641;") # should display 2
for x in myc:
    print("Original: ", x)

myc.execute("update countrya set country_a_name = 'United States of America' where country_a_population = 24512641")

# show new count of countries
myc.execute("select CA.country_a_id, CA.country_a_name, CA.country_a_population from countrya CA where CA.country_a_population = 24512641;") # should display 2
for x in myc:
    print("Update New: ", x)

