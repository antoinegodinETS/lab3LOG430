# from common.database import init_db


# if __name__ == "__main__":
#     init_db()
#     print("✅ Base de données initialisée avec succès.")

# src/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import magasin_api, maison_mere_api, logistique_api

app = FastAPI(title="API Multi-Magasins - LOG430")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # à restreindre pour production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(magasin_api.router)
app.include_router(logistique_api.router)
app.include_router(maison_mere_api.router)

