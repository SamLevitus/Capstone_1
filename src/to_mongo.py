from base import Base
from dotenv import load_dotenv
import pymongo
import os

# Class Declaration:
class ToMongo(Base):
       
    def __init__(self, user=os.getenv('USERNAME'), password=os.getenv('PASSWORD')):
        
        load_dotenv()
        self.user = user
        self.password = password
        self.mongo_url = os.getenv('MONGO_URL')
        #Connect to PyMongo
        self.client = pymongo.MongoClient("mongodb+srv://admin:Eli2018!@capstone.ythhxvh.mongodb.net/?retryWrites=true&w=majority")
        # Create a database
        self.db = self.client.db
        # Create a collection:
        self.rest_info = self.db.rest_info
        
    def upload_collection(self):
        self.rest_info.insert_many([self.df.to_dict()])

    def upload_one_by_one(self):
        self.rest_info.drop()
        Base.__init__(self)
        
        
if __name__ == '__main__':
    c = ToMongo()
    print('Successful Connection to Client Object')
    c.upload_one_by_one()
    print('Successfully Uploaded all Restaurant Info to Mongo')