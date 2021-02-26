import pymongo

db_client = pymongo.MongoClient("mongodb://localhost:27017")
db = db_client["databasemining"]
collection = db["magnit_products"]


for item in collection.find({"$or": [{"promo_name": " Скидка", "title": {"$regex": " Таблетки"}},
                                     {"title": {"$regex": "Пиво"}}]}):
    print(item)