from apscheduler.schedulers.background import BackgroundScheduler
from scraper import scrape_product
from database import SessionLocal, ProductPrice
from datetime import datetime

tracked_urls = [
    "https://www.amazon.in/dp/B0BZCR6TNK"
]

def job():
    print("Running scheduled job...")
    db = SessionLocal()
    try:
        for url in tracked_urls:
            result = scrape_product(url)
            new_entry = ProductPrice(
                url=url,
                name=result["name"],
                price=result["price"],
                timestamp=datetime.utcnow()
            )
            db.add(new_entry)
        db.commit()
        print("Data saved to DB.")
    except Exception as e:
        print("Error in scheduler job:", str(e))
    finally:
        db.close()

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, "interval", minutes=30)
    scheduler.start()
    print("Scheduler started.")
