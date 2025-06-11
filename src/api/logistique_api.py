# src/api/logistique_api.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from common.database import get_db
from logistique import services as log_services

router = APIRouter(prefix="/api/v1/logistique", tags=["Logistique"])

@router.get("/stock")
def get_stock_logistique(db: Session = Depends(get_db)):
    return log_services.consulter_stock_logistique()

@router.get("/demandes")
def get_demandes_en_attente(db: Session = Depends(get_db)):
    return log_services.recuperer_demandes_en_attente()

@router.post("/approvisionner")
def approvisionner(produit_id: int, quantite: int, magasin_id: int, db: Session = Depends(get_db)):
    return log_services.approvisionner_magasin(produit_id, quantite, magasin_id)

@router.post("/verifier_reapprovisionnement")
def verifier(magasin_id: int, produit_id: int, quantite: int, db: Session = Depends(get_db)):
    return log_services.verifier_et_reapprovisionner(magasin_id, produit_id, quantite)
