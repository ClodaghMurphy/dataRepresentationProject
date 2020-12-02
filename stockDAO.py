#Code adapated from https://github.com/andrewbeattycourseware/dataRepresenation2020
import mysql.connector
from mysql.connector import cursor
import config as config
class StockDAO:
    db = ""
#variable stores database connection,ok to leave blank
    def __init__(self):
        self.db = mysql.connector.connect(
            #host = 'localhost',
            #user= 'root',
            #password = 'success',
            #database ='datarepresentation'
            host=config.mysql['host'],
            user=config.mysql['username'],
            password=config.mysql['password'],
            database=config.mysql['database']
        )
        print ("connection @ __init__ made with stockDAO.py")


#Create function _Insert
    def create(self, item):
        cursor = self.db.cursor()
        sql = "insert into stock (description, price, provenance) values (%s,%s,%s)"
        values = [
           #item['id'],
            item['description'],
            item['price'],
            item['provenance']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid   
#Get All
    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from stock'
        cursor.execute(sql)
        results = cursor.fetchall()
        #this command will return tuples, below will convert to an array
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)#convert tuple into a Dict object
            returnArray.append(resultAsDict)
        return returnArray   
#Find One
    def findById(self,id):
        #return{}
        cursor = self.db.cursor()
        sql = 'select * from stock where id = %s'
        values = [id,]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result) 
        print (result)
#Update        
    def update(self, item):
        cursor = self.db.cursor()
        sql = "update stock set description = %s, price = %s, provenance = %s where id = %s"
#note on lines below you must change the order. It is important!
        values = [
           item['description'],
           item['price'],
           item['provenance'],
           item['id']

       ]
        cursor.execute(sql, values)
        self.db.commit()
        return item
    
#Delete
    def delete(self, id):
       cursor = self.db.cursor()
       sql = 'delete from stock where id = %s'
       values = [id]
       cursor.execute(sql, values)
       return {}

#rather than convertToDict in each individual function, they can all call this one
    def convertToDict(self, result):
        colnames = ['id','description', 'price', 'provenance']#extract the columns names as tuples and convert them too, they will appear on the printout
        item = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]#extract from the dict object
                item[colName] = value#make the item that matches the column name equal that value
        return item   

stockDao = StockDAO()