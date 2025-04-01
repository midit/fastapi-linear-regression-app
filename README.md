# Prosta Aplikacja FastAPI z Regresją Liniową

Ta aplikacja demonstruje prosty model regresji liniowej udostępniony przez API za pomocą FastAPI. Projekt zawiera konfigurację do uruchomienia za pomocą Dockera i Docker Compose.

## Wymagania

- Python 3.10+ (do uruchomienia lokalnego)
- `pip` (do instalacji zależności lokalnie)
- Docker (do uruchomienia za pomocą Dockera/Docker Compose)
- Docker Compose (do uruchomienia za pomocą Docker Compose)

## Uruchamianie Aplikacji

Istnieją trzy sposoby uruchomienia aplikacji:

### 1. Lokalnie

a. **Utwórz i aktywuj wirtualne środowisko** (zalecane):
`bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    `

b. **Zainstaluj zależności**:
`bash
    pip install -r requirements.txt
    `

c. **Uruchom serwer Uvicorn**:
`bash
    uvicorn app:app --host 0.0.0.0 --port 8001 --reload
    `
_ `--reload` jest przydatne podczas developmentu, automatycznie restartuje serwer po zmianach w kodzie. W środowisku produkcyjnym zazwyczaj się go nie używa.
_ Aplikacja będzie dostępna pod adresem `http://localhost:8001`.

### 2. Za pomocą Dockera

a. **Zbuduj obraz Docker**: W głównym katalogu projektu wykonaj:
`bash
    docker build -t fastapi-linear-regression .
    ` \* `-t fastapi-linear-regression` nadaje obrazowi nazwę `fastapi-linear-regression`.

b. **Uruchom kontener z obrazu**:
`bash
    docker run -d --name my_fastapi_app -p 8001:8000 fastapi-linear-regression
    `
_ `-d` uruchamia kontener w tle.
_ `--name my_fastapi_app` nadaje kontenerowi nazwę.
_ `-p 8001:8000` mapuje port 8001 na Twoim komputerze do portu 8000 w kontenerze (zgodnie z `CMD` w `Dockerfile`).
_ Aplikacja będzie dostępna pod adresem `http://localhost:8001`.

### 3. Za pomocą Docker Compose

a. **Uruchom serwisy**: W głównym katalogu projektu, gdzie znajduje się plik `docker-compose.yml`, wykonaj:
`bash
    docker-compose up -d --build
    `
_ `--build` (opcjonalnie, jeśli obrazy już istnieją) przebuduje obraz aplikacji.
_ `-d` uruchamia kontenery w tle.
_ Docker Compose automatycznie zbuduje obraz (jeśli trzeba), utworzy sieć i uruchomi kontenery `fastapi_app` oraz `redis_db`.
_ Aplikacja będzie dostępna pod adresem `http://localhost:8001` (zgodnie z portem zdefiniowanym w `docker-compose.yml`).

## Konfiguracja i Zasoby

### Konfiguracja

Obecnie aplikacja nie wymaga zewnętrznej konfiguracji za pomocą zmiennych środowiskowych.

- **Port**: Port, na którym nasłuchuje serwer Uvicorn wewnątrz kontenera, jest zdefiniowany w `Dockerfile` (port 8000). Mapowanie tego portu na port hosta odbywa się w komendzie `docker run` (np. `-p 8001:8000`) lub w pliku `docker-compose.yml` (sekcja `ports`).
- **Połączenie z Redis**: Gdyby aplikacja miała łączyć się z Redis (uruchomionym przez Docker Compose), kod w `app.py` powinien używać nazwy serwisu `redis` jako hosta, np. `redis.Redis(host='redis', port=6379)`. Ewentualne dane uwierzytelniające do Redis mogłyby być przekazane przez zmienne środowiskowe zdefiniowane w `docker-compose.yml`.

### Wymagane Zasoby

- **Środowisko uruchomieniowe**: Python 3.10.
- **Zależności Python**: Wymienione w pliku `requirements.txt`. Są one instalowane automatycznie podczas budowania obrazu Docker lub lokalnie za pomocą `pip install -r requirements.txt`.
- **Baza danych (opcjonalnie)**: Plik `docker-compose.yml` zawiera konfigurację dla serwera Redis, ale obecny kod `app.py` go nie wykorzystuje.
