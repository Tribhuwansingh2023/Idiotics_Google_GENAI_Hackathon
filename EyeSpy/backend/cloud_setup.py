#!/usr/bin/env python3
"""
EyeSpy Cloud Database Setup (MongoDB Atlas)
Alternative to local Docker setup
"""

from database import EyeSpyDatabase
from dataset_loader import populate_database

# MongoDB Atlas connection (free tier)
ATLAS_CONNECTION = "mongodb+srv://eyespy:eyespy123@cluster0.mongodb.net/eyespy?retryWrites=true&w=majority"

def setup_cloud_database():
    """Setup with MongoDB Atlas (cloud)"""
    try:
        print("🌐 Setting up EyeSpy with MongoDB Atlas (Cloud)...")
        
        # Use cloud database
        db = EyeSpyDatabase(connection_string=ATLAS_CONNECTION)
        
        # Test connection
        db.client.admin.command('ping')
        print("✅ Connected to MongoDB Atlas")
        
        # Populate with data
        total_records = populate_database()
        print(f"📊 Inserted {total_records} training samples")
        
        return True
        
    except Exception as e:
        print(f"❌ Cloud setup failed: {e}")
        return False

def setup_local_fallback():
    """Fallback to local file-based storage"""
    print("📁 Using local file-based storage (no database)...")
    return True

if __name__ == "__main__":
    print("🚀 EyeSpy Database Setup Options")
    print("=" * 40)
    
    choice = input("Choose setup:\n1. Cloud (MongoDB Atlas)\n2. Local files only\nEnter choice (1/2): ")
    
    if choice == "1":
        if setup_cloud_database():
            print("🎉 Cloud database ready!")
        else:
            setup_local_fallback()
    else:
        setup_local_fallback()
    
    print("💡 Run: python app.py")