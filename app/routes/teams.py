from fastapi import APIRouter

from app.db.tournaments import db_actions


teams_route = APIRouter(prefix="/teams", tags=["Team"])