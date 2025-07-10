from fastapi import APIRouter

from app.db.tournaments import db_actions


tournaments_route = APIRouter(prefix="/tournaments", tags=["tournaments"])