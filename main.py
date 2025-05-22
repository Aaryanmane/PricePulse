from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from scraper import scrape_product
from database import SessionLocal, ProductPrice
import scheduler

app = FastAPI()
scheduler.start()

class ProductURL(BaseModel):
    url: str

@app.post("/track")
def track_product(data: ProductURL):
    return scrape_product(data.url)

@app.get("/history")
def get_history(url: str):
    db = SessionLocal()
    records = db.query(ProductPrice).filter(ProductPrice.url == url).all()
    db.close()
    return [{"name": r.name, "price": r.price, "timestamp": r.timestamp} for r in records]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)