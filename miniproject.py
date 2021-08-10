import csv,json,re,logging
import getpass
import pymongo
# try:
client=pymongo.MongoClient("mongodb://localhost:27017")
mydatabase=client["DogDb"]
collection_name=mydatabase['dogs']
username="kanchana"
password="Kanchana@8+"
headerContent=["dogName","dogId","dogAge","dogprice"]
class DogDetails:
    def _init_(self,dogName,dogId,dogAge,dogPrice):
        self.dogName=''
        self.dogId=''
        self.dogAge=''
        self.dogPrice=''
    
    def adddogdetail(self,dogName,dogId,dogAge,dogPrice):
        dict1={"dogName":dogName,"dogId":dogId,"dogAge":dogAge,"dogprice":dogPrice}
        
        return dict1

def validate(dogName): 
    valname=re.search("[A-Z]{1}[^A-Z]{0,25}$",dogName) 
    if valname:
        return True
    else:
        return False 
obj=DogDetails()
doglist=[]
doglist2=[]
Price_list=[]
Age_list=[]
if(__name__=="__main__"):     
    user_name=input("please enter your username:")
    pass_word=getpass.getpass(prompt='Please enter your password:')
    if user_name==username and pass_word==password:
        while True:
            print("1.add dog details")
            print("2.view all dogs")
            print("3.search a dog by name")
            print("4.delete a dog by name")
            print("5 update the dog name by id")
            print("6.List of dogs whoes name is start with greater than A")
            print("7.exit") 
            choice=int(input("Enter your choice : "))
            
            if choice==1:
                dogName=input("Enter the dogname : ")
                dogId=int(input("Enter the dogId : "))
                
                dogAge=int(input("Enter the Age:"))
                dogPrice=int(input("Enter the dog price:"))
                a=validate(dogName)
                if a:
                    data=obj.adddogdetail(dogName,dogId,dogAge,dogPrice)
                    doglist.append(data)
                    result=collection_name.insert_many(doglist)
                    print(result.inserted_ids) 
                else:
                    logging.error("invalid data enter a valid data")
                     
            if choice==2:
                result=collection_name.find({},{"_id":0})
                for i in result:
                    doglist2.append(i)
                print(doglist2)
                doglist2.clear()
            if choice==3:
                name=input("Enter the dogName to search : ")
                result=collection_name.find({"dogName":name})
                for i in result:
                    print(i)
            if choice==4:
                name=input("Enter the dogName that you want to delete:")
                result=collection_name.delete_many({"dogName":name})
                print(result.deleted_count)
            if choice==5:
                DogId=int(input("Enter the dogId where u want to update:"))
                DogName=input("Enter the DogName update:")
                result=collection_name.update_many({"dogId=":DogId},{"$set":{"dogName":DogName}})
                print(result.modified_count)
                
            if choice==6:

                result1=collection_name.find({"dogName":{"$gt":"Q"}},{"_id":0})
                for i in result1:
                    print(i)
            if choice==7:
                break
    else:
        logging.error("username or password is incorrect please try again")
# except:
#     logging.error("unable to process")