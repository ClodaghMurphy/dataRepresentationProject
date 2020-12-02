from stockDAO import stockDao
#it calls it from the file name not the class you defined *in* the file
#print ("this is a print out from testStockDao.py")

#item = {
    #'id': 122,
    #'description': '6 Free Range Eggs',
    #'price': 600,
    #'provenance': 'Magner Farm'

#}

item = {
    #'id': 107, not needed anymore because sql is giving the id numbers
   'description': '230g Wildflower Honey',
  'price': 850,
 'provenance': 'Galtee Farm'

}
#item = {
 #   'id': 5,
  #  'description': '125g Cashel Blue Cheese',
   # 'price': 5005,
    #'provenance': 'Cashel Farmhouse Cheese'
#}
#item = {
   
#    'description': '5l Apple Juice Box',
#    'price': 1250,
#    'provenance': 'The Apple Farm'
#}



#1.to check that create() works do this  
#returnValue = stockDao.create(item)
#print(returnValue) 
#returnValue = result = stockDao.getAll()
#print(returnValue) 
#returnValueCreate = stockDao.create(item)
#print("*Return from Create function is #id*",(str(returnValueCreate)))

#returnValuegetAll = stockDao.getAll()
#print("*getAll output from the stock table is as follows*\n",(str(returnValuegetAll)))
#returnValue = stockDao.findById(item[])
#returnValue = stockDao.findByRef(2)


result = stockDao.findById(2);

print("*after findById function*",(str(result)))
#print(result)
#print(returnValue)
#returnValue = stockDao.update(item)
#print("*after update function*",(str(returnValue)))

#returnValue = stockDao.delete(5)

#print("*after delete*",(str(returnValue)))