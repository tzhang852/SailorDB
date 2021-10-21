import numpy as np
import pandas as pd

np.random.seed(12345) 

#country names
cc = pd.read_csv('cc.csv')
countries = []
for i in range(len(cc['Country'])):
    countries.append(cc['Country'][i])
#print(countries)

#raw material names
rm = pd.read_csv('raw.csv')
raw_material = []
for i in range(len(rm['Raw'])):
    raw_material.append(rm['Raw'][i])

#product names
prod = pd.read_csv('prod.csv')
product = []
for i in range(len(prod['Product'])):
    product.append(prod['Product'][i])

#transportation names
trans = pd.read_csv('trans.csv')
transportation = []
for i in range(len(trans['Transportation'])):
    transportation.append(trans['Transportation'][i])


# Create Country Data
numCountriesa = 50000
outfile = open("countrya","w") 
for i in range(10001,numCountriesa+10001):
	outString = ''
	outString += str(i)   # id
	outString += ','
	outString += countries[np.random.randint(186)]
	outString += ','
	population = str( np.random.randint(100000000))   
	outString += population  # pop
	outString += ','
	gdp = ( np.random.uniform(1.0, 30.0))
	outString += str(gdp)   # gdp in trillions
	outString += "\n"
	outfile.write(outString)
outfile.close()

# Create Country Data
numCountriesb = 50000
outfile = open("countryb","w") 
for i in range(10001,numCountriesb+10001):
	outString = ''
	outString += str(i)   # id
	outString += ','
	outString += countries[np.random.randint(186)] # country name
	outString += ','
	population = str(np.random.randint(100000000))   
	outString += population  # pop
	outString += ','
	gdp = ( np.random.uniform(1.0, 30.0))
	outString += str(gdp)   # gdp in trillions
	outString += "\n"
	outfile.write(outString)
outfile.close()

# create the Raw Material data
numRM = 1000
outfile = open("raw_material","w") 
for i in range(101,numRM+101):
	outString = ''
	outString += str(i)   # iid
	outString += ','
	outString += raw_material[np.random.randint(39)]   # item name
	outString += ','
	quantity = str(np.random.randint(100))  # quantity in millions
	outString += quantity
	outString += ','
	baseval = np.random.uniform(0.1, 99.9)
	outString += str(baseval)   # basevalue in dollars 2011$PPP per kilo
	outString += "\n"
	outfile.write(outString)
outfile.close()

# create the Product data
numProds = 1000
outfile = open("product","w") 
for i in range(101, numProds+101):
	outString = ''
	outString += str(i)   # pid
	outString += ','
	outString += product[np.random.randint(72)]  # product name
	outString += ','
	price = np.random.uniform(0.1, 99.9)
	outString += str(price)   # basevalue per item in dollars 2011$PPP
	outString += "\n"
	outfile.write(outString)
outfile.close()

#create ExportsTo database
numExports = 10000
outfile = open('exports_to', 'w')
for i in range(101, numExports + 101):
    outString = ''
    outString += str(np.random.randint(10001, 20002)) # country id
    outString += ','
    outString += countries[np.random.randint(186)] # country a name
    outString += ','
    outString += str(i) # raw material id
    outString += ','
    outString += raw_material[np.random.randint(39)]  # raw material name
    outString += ','
    outString += transportation[np.random.randint(22)]  # type of transportation
    outString += '\n'
    outfile.write(outString)
outfile.close()

#create Imported By database
numImported = 10000
outfile = open('imported_by', 'w')
for i in range(101, numImported + 101):
    outString = ''
    outString += str(np.random.randint(10001, 20002)) # country b id
    outString += ','
    outString += countries[np.random.randint(186)] # country b name
    outString += ','
    outString += str(i) # raw material id
    outString += ','
    outString += raw_material[np.random.randint(39)]  # raw material name
    outString += ','
    date = '2011-'
    date += str( np.random.randint(12) + 1)  
    date += '-'
    date += str(np.random.randint(28) + 1)
    outString += date # date of import
    outString += ','
    outString += 'warehouse' 
    outString += str(i) # warehouse id
    outString += ','
    outString += transportation[np.random.randint(22)]  # type of transportation
    outString += ','
    total =  np.random.uniform(1.0, 999.0) # total cost in millions of dollars
    outString += str(total)
    outString += '\n'
    outfile.write(outString)
outfile.close()

#create Creates database
numCreates = 1000
outfile = open('creates', 'w')
for i in range(101, numCreates + 101):
    outString = ''
    outString += str(np.random.randint(10001, 20002)) # country b id
    outString += ','
    outString += countries[np.random.randint(186)] # country b name
    outString += ','
    outString += str(i) # product id
    outString += ','
    outString += product[np.random.randint(72)]  # product name
    outString += ','
    outString += str(i) # previous product id
    outString += ','
    previous = 'Previous product = '
    previous += product[np.random.randint(72)]  # previous product name
    outString += previous
    outString += '\n'
    outfile.write(outString)
outfile.close()

#create Purchased By database
numPurchasedby = 10000
outfile = open('purchased_by', 'w')
for i in range(101, numPurchasedby + 101):
    outString = ''
    outString += str(np.random.randint(10001, 20002)) # country a id
    outString += ','
    outString += countries[np.random.randint(186)] # country a name
    outString += ','
    outString += str(i) # product id
    outString += ','
    outString += product[np.random.randint(72)]  # product name
    outString += ','
    date = '2011-'
    date += str( np.random.randint(12) + 1)  
    date += '-'
    date += str(np.random.randint(28) + 1)
    outString += date # date of purchase
    outString += ','
    total =  np.random.uniform(1.0, 999.0) # total price in millions
    outString += str(total)
    outString += '\n'
    outfile.write(outString)
outfile.close()
