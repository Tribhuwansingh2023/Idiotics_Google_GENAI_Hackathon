from pymongo import MongoClient
from datetime import datetime
import hashlib
import json

class EyeSpyDatabase:
    def __init__(self, connection_string="mongodb://localhost:27017/", db_name="eyespy"):
        self.client = MongoClient(connection_string)
        self.db = self.client[db_name]
        self.init_collections()
    
    def init_collections(self):
        """Initialize database collections"""
        # Collections
        self.news_dataset = self.db.news_dataset
        self.analysis_history = self.db.analysis_history
        self.user_sessions = self.db.user_sessions
        
        # Create indexes for better performance
        self.news_dataset.create_index("content_hash")
        self.analysis_history.create_index("timestamp")
    
    def save_analysis(self, content_type, content, result):
        """Save analysis result to database"""
        content_hash = hashlib.md5(content.encode()).hexdigest()
        
        analysis_record = {
            "content_type": content_type,
            "content_hash": content_hash,
            "content_preview": content[:100] if len(content) > 100 else content,
            "is_fake": result["is_fake"],
            "confidence_score": result["confidence"],
            "fake_probability": result["fake_probability"],
            "analysis_details": result["analysis"],
            "timestamp": datetime.utcnow()
        }
        
        return self.analysis_history.insert_one(analysis_record)
    
    def get_analysis_stats(self):
        """Get analysis statistics"""
        total = self.analysis_history.count_documents({})
        fake_count = self.analysis_history.count_documents({"is_fake": True})
        
        return {
            "total_analyses": total,
            "fake_detected": fake_count,
            "authentic_detected": total - fake_count,
            "accuracy_rate": round((total - fake_count) / total * 100, 2) if total > 0 else 0
        }
    
    def check_content_cache(self, content):
        """Check if content was analyzed before"""
        content_hash = hashlib.md5(content.encode()).hexdigest()
        return self.analysis_history.find_one({"content_hash": content_hash})
    
    def get_training_data(self):
        """Get training data from database"""
        fake_news = list(self.news_dataset.find({"label": "fake"}).limit(100))
        real_news = list(self.news_dataset.find({"label": "real"}).limit(100))
        
        texts = []
        labels = []
        
        for item in fake_news:
            texts.append(item["text"])
            labels.append(1)  # 1 for fake
        
        for item in real_news:
            texts.append(item["text"])
            labels.append(0)  # 0 for real
        
        return texts, labels