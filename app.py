from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import nest_asyncio
import asyncio
import uvicorn
from sklearn.linear_model import LinearRegression
import numpy as np
from pydantic import BaseModel, Field

# Tworzenie aplikacji FastAPI
app = FastAPI()

# Dodanie middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Zezwalaj na połączenia z dowolnego źródła
    allow_credentials=True,
    allow_methods=["*"],  # Zezwalaj na wszystkie metody HTTP
    allow_headers=["*"],  # Zezwalaj na wszystkie nagłówki
)

# Definiowanie modelu żądania do przewidywania
class PredictionRequest(BaseModel):
    feature: float = Field(..., description="Wymagana cecha wejściowa dla modelu")

# Tworzenie i trenowanie modelu regresji liniowej
model = LinearRegression()

# Dane do trenowania (cechy i wartości docelowe)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Trenowanie modelu
model.fit(X, y)

# Definiowanie głównego endpointu
@app.get("/")
async def root():
    return {"hello": "world"}

# Endpoint przewidywania
@app.post("/predict")
async def predict(request: PredictionRequest):
    try:
        # Weryfikacja, czy 'feature' została przekazana (Pydantic automatycznie to sprawdza)
        prediction = model.predict([[request.feature]])
        return {"prediction": prediction[0]}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Błąd podczas przetwarzania danych: {str(e)}"
        )

# Endpoint sprawdzający stan serwera
@app.get("/health")
async def health():
    return {"status": "ok"}

# Endpoint zwracający informacje o modelu
@app.get("/info")
async def info():
    return {
        "model_type": "Linear Regression",
        "number_of_features": 1,
        "trained_on_samples": len(X)
    }

# Zastosowanie nest_asyncio do zarządzania pętlą zdarzeń
nest_asyncio.apply()

# Uruchomienie serwera za pomocą Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="info")
