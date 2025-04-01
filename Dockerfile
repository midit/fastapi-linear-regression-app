# 1. Wybór oficjalnego obrazu Pythona
FROM python:3.10-slim

# 2. Ustawienie katalogu roboczego w kontenerze
WORKDIR /app

# 3. Skopiowanie pliku requirements.txt do kontenera
COPY requirements.txt /app/

# 4. Instalowanie zależności Pythona
RUN pip install --no-cache-dir -r requirements.txt

# 5. Skopiowanie wszystkich plików aplikacji do kontenera
COPY . /app/

# 6. Ustawienie komendy uruchamiającej serwer (przykład dla aplikacji FastAPI)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
