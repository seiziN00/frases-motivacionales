from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, Quote

app = FastAPI()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/quotes")
def get_quotes(db: Session = Depends(get_db)):
    return db.query(Quote).all()

@app.get("/quotes/{quote_id}")
def get_quote(quote_id: int, db: Session = Depends(get_db)):
    quote = db.query(Quote).filter(Quote.id == quote_id).first()
    if quote is None:
        raise HTTPException(status_code=404, detail="Quote not found")
    return quote

from pydantic import BaseModel

class QuoteCreate(BaseModel):
    text: str

@app.post("/quotes")
def add_quote(quote: QuoteCreate, db: Session = Depends(get_db)):
    db_quote = Quote(text=quote.text)
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    return {"message": "Quote added successfully", "quote": db_quote}

@app.delete("/quotes/{quote_id}")
def delete_quote(quote_id: int, db: Session = Depends(get_db)):
    quote = db.query(Quote).filter(Quote.id == quote_id).first()
    if quote is None:
        raise HTTPException(status_code=404, detail="Quote not found")
    db.delete(quote)
    db.commit()
    return {"message": "Quote deleted", "quote_id": quote_id}