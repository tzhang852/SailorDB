import numpy as np


aStatement = 'drop table if exists Reserve;'
print(aStatement)
aStatement = 'drop table if exists Sailors;'
print(aStatement)
aStatement = 'drop table if exists Boats;'
print(aStatement)

aStatement = 'create table Sailors ( sid int, name varchar(20) NOT NULL, age int, rating int NOT NULL, Primary Key (sid) ) ; ' 
print(aStatement) 

aStatement = 'create table Boats ( bid int, name varchar(20), ratingNeeded int, bcolor varchar(20), PRIMARY KEY (bid) ) ;' 
print(aStatement) 

aStatement = 'create table Reserve ( bid int, sid int, rdate date, PRIMARY KEY (bid,sid,rdate), Foreign Key (bid) references Boats(bid), Foreign Key (sid) references Sailors(sid) ) ;' 
print(aStatement) 



colors = []
colors.append('red') 
colors.append('green') 
colors.append('blue') 
colors.append('yellow') 
colors.append('orange')
colors.append('purple')
colors.append('grey') 
colors.append('brown') 
colors.append('gold') 
colors.append('silver') 
colors.append('pink') 
colors.append('moss') 
colors.append('perwinkle') 
colors.append('pumpkin') 
colors.append('black') 
colors.append('citron') 
colors.append('coffee')
colors.append('chocolate') 
colors.append('olive') 
colors.append('peach')
colors.append('burnt umber') 
colors.append('salmon') 
colors.append('teal') 
colors.append('vermilion') 
colors.append('white') 
colors.append('ivory') 
colors.append('grape') 
colors.append('lemon')
colors.append('lime') 

numSailors = 10
numBoats = 10 
numReservations = 50



# lets insert a bunch of sailor tuples
for i in range(1,numSailors+1):
	aID = str(i)
	aName = 'Sue' + str(i) 
	aAge = str( np.random.randint(80) + 18)   
	aRating = str( np.random.randint(1000) + 1)   
	aStatement = 'insert into sailors values(' + aID + ',\'' + aName + '\',' + aAge + ',' + aRating + ');'
	print(aStatement) 

# lets insert a bunch of boats tuples
for i in range(101,numBoats + 101):
	bID = str(i)
	bName = 'Minnow' + str(i) 
	rNum = np.random.randint(29)
	bColor = colors[rNum]   # bcolor
	bRatingNeeded = str( np.random.randint(1000) + 1)   
	aStatement = 'insert into boats values(' + bID + ',\'' + bName + '\',' + bRatingNeeded + ',\'' + bColor + '\');' 
	print(aStatement) 


# lets insert a bunch of reserve tuples
for i in range(1,numReservations+1):
	bID = str( np.random.randint(numBoats)+101  )
	sID = str( np.random.randint(numSailors)+1 )
	rDate = '2019-05-' + str(np.random.randint(20)+10)
	aStatement = 'insert into reserve values(' + bID + ',' + sID + ',\'' + rDate + '\');' 
	print(aStatement) 


