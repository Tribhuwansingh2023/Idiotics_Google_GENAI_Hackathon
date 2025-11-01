#!/usr/bin/env python3
"""
EyeSpy Database Setup Script
Run this script to initialize MongoDB and populate with sample data
"""

import sys
import subprocess
from database import EyeSpyDatabase
from dataset_loader import populate_database

def check_mongodb():
    """Check if MongoDB is running"""
    try:
        db = EyeSpyDatabase()
        db.client.admin.command('ping')
        print("(success) MongoDB connection successful")
        return True
    except Exception as e:
        print(f"(error) MongoDB connection failed: {e}")
        print("\n(info) To install MongoDB:")
        print("1. Download from: https://www.mongodb.com/try/download/community")
        print("2. Or use Docker: docker run -d -p 27017:27017 mongo")
        return False

def setup_database():
    """Setup database with sample data"""
    try:
        print("(setting up) Setting up EyeSpy database...")
        
        # Initialize database
        db = EyeSpyDatabase()
        
        # Populate with sample data
        total_records = populate_database()
        
        print(f"(success) Database setup complete!")
        print(f"(inserted) Inserted {total_records} training samples")
        
        # Show statistics
        stats = db.get_analysis_stats()
        print(f"(ready) Database ready for training ML models")
        
        return True
        
    except Exception as e:
        print(f"(error) Database setup failed: {e}")
        return False

def main():
    """Main setup function"""
    print("EyeSpy Database Setup")
    print("=" * 40)
    
    # Check MongoDB connection
    if not check_mongodb():
        sys.exit(1)
    
    # Setup database
    if not setup_database():
        sys.exit(1)
    
    print("\n(completed) Setup completed successfully!")
    print("(info) You can now run: python app.py")

if __name__ == "__main__":
    main()