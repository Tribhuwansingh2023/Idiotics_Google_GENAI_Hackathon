# Optional database extension for EyeSpy
import sqlite3
from datetime import datetime
import json

class EyeSpyDatabase:
    def __init__(self, db_path='eyespy.db'):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Create tables if they don't exist"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Analysis history table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS analysis_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content_type TEXT NOT NULL,
                content_hash TEXT,
                is_fake BOOLEAN,
                confidence_score REAL,
                analysis_details TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def save_analysis(self, content_type, content_hash, is_fake, confidence, details):
        """Save analysis result to database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO analysis_history 
            (content_type, content_hash, is_fake, confidence_score, analysis_details)
            VALUES (?, ?, ?, ?, ?)
        ''', (content_type, content_hash, is_fake, confidence, json.dumps(details)))
        
        conn.commit()
        conn.close()
    
    def get_analysis_stats(self):
        """Get analysis statistics"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM analysis_history')
        total = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM analysis_history WHERE is_fake = 1')
        fake_count = cursor.fetchone()[0]
        
        conn.close()
        
        return {
            'total_analyses': total,
            'fake_detected': fake_count,
            'authentic_detected': total - fake_count
        }

# Usage in app.py:
# from database_extension import EyeSpyDatabase
# db = EyeSpyDatabase()
# db.save_analysis('text', hash(text), result['is_fake'], result['confidence'], result['analysis'])