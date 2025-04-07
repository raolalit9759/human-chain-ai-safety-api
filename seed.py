from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client.get_database()

sample_data = [
    {
        "title": "AI hallucinated text",
        "description": "Generated inappropriate content during summarization.",
        "severity": "High",
        "reported_at": datetime.utcnow().isoformat()
    },
    {
        "title": "Data leak from training set",
        "description": "Model output included personal information.",
        "severity": "Medium",
        "reported_at": datetime.utcnow().isoformat()
    },
    {
        "title": "Misinformation propagation",
        "description": "Model reinforced biased content about health advice.",
        "severity": "Low",
        "reported_at": datetime.utcnow().isoformat()
    }
]

db.incidents.insert_many(sample_data)
print(" Sample incidents inserted.")
