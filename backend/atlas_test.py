from pymongo import MongoClient

uri = "mongodb+srv://docutrustuser:2BZWreA9t-rDf9@docutrustcluster.9bidl3c.mongodb.net/?appName=DocuTrustCluster"

client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("✅ MongoDB Atlas Connected Successfully!")
except Exception as e:
    print("❌ Connection Failed")
    print(repr(e))