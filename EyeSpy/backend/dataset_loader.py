import json
from database import EyeSpyDatabase
from datetime import datetime

def create_sample_dataset():
    """Create sample fake news dataset"""
    
    fake_news_samples = [
        "BREAKING: Scientists discover shocking truth about vaccines that Big Pharma doesn't want you to know!",
        "URGENT: Secret government documents leaked revealing hidden agenda to control population",
        "EXCLUSIVE: Celebrity caught in massive scandal - you won't believe what happened next!",
        "SHOCKING: This one weird trick will make you rich overnight - doctors hate it!",
        "LEAKED: Internal emails expose conspiracy to manipulate election results",
        "BREAKING: Miracle cure for cancer discovered but medical industry is hiding it",
        "URGENT: Aliens have been living among us for decades - government finally admits",
        "EXCLUSIVE: Social media giants caught secretly monitoring your private conversations",
        "SHOCKING: This simple home remedy can cure diabetes in just 3 days",
        "LEAKED: Politicians caught planning to raise taxes by 500% next year"
    ]
    
    real_news_samples = [
        "According to a study published in Nature journal, researchers have identified new genetic markers for Alzheimer's disease.",
        "The World Health Organization announced new guidelines for COVID-19 prevention based on recent scientific evidence.",
        "Economic data released by the Federal Reserve shows inflation rates have stabilized at 2.1% this quarter.",
        "University researchers conducted a comprehensive study on climate change effects over the past decade.",
        "The Department of Education released official statistics showing improved literacy rates in public schools.",
        "Medical experts from Johns Hopkins published findings on the effectiveness of new cancer treatments.",
        "Government officials confirmed the budget allocation for infrastructure improvements next fiscal year.",
        "Scientific research indicates that regular exercise can reduce the risk of heart disease by 30%.",
        "The Environmental Protection Agency reported significant improvements in air quality standards.",
        "Academic institutions collaborated on a peer-reviewed study about renewable energy efficiency."
    ]
    
    # Extended dataset with more samples
    extended_fake = [
        "You won't believe this one simple trick that banks don't want you to know about money",
        "BREAKING: Celebrity death hoax spreads rapidly on social media platforms",
        "Secret society controls world governments - insider reveals shocking details",
        "Miracle weight loss pill melts fat overnight without diet or exercise",
        "URGENT: Asteroid heading toward Earth - government hiding the truth from public",
        "EXCLUSIVE: Time traveler from 2050 warns about upcoming disasters",
        "SHOCKING: Your smartphone is secretly recording everything you say",
        "LEAKED: Pharmaceutical companies suppress natural cures to increase profits",
        "BREAKING: Ancient aliens built pyramids - new evidence proves it",
        "URGENT: Tap water contains mind control chemicals - expert whistleblower speaks out"
    ]
    
    extended_real = [
        "Research team at MIT develops new battery technology for electric vehicles",
        "Clinical trial results show promising outcomes for new Alzheimer's treatment",
        "NASA announces successful launch of Mars exploration rover mission",
        "Supreme Court ruling affects federal regulations on environmental protection",
        "International trade agreement signed between multiple countries for economic cooperation",
        "Medical breakthrough in gene therapy offers hope for rare genetic disorders",
        "Educational reform bill passes through Congress with bipartisan support",
        "Archaeological discovery sheds new light on ancient civilization practices",
        "Renewable energy project creates thousands of jobs in rural communities",
        "Public health officials recommend updated vaccination schedule for children"
    ]
    
    return {
        "fake_news": fake_news_samples + extended_fake,
        "real_news": real_news_samples + extended_real
    }

def populate_database():
    """Populate MongoDB with sample dataset"""
    db = EyeSpyDatabase()
    
    # Clear existing data
    db.news_dataset.delete_many({})
    
    dataset = create_sample_dataset()
    
    # Insert fake news
    fake_documents = []
    for text in dataset["fake_news"]:
        fake_documents.append({
            "text": text,
            "label": "fake",
            "source": "sample_dataset",
            "created_at": datetime.utcnow()
        })
    
    # Insert real news
    real_documents = []
    for text in dataset["real_news"]:
        real_documents.append({
            "text": text,
            "label": "real", 
            "source": "sample_dataset",
            "created_at": datetime.utcnow()
        })
    
    # Bulk insert
    if fake_documents:
        db.news_dataset.insert_many(fake_documents)
    if real_documents:
        db.news_dataset.insert_many(real_documents)
    
    print(f"Dataset populated: {len(fake_documents)} fake news, {len(real_documents)} real news")
    return len(fake_documents) + len(real_documents)

if __name__ == "__main__":
    from datetime import datetime
    populate_database()