from typing import Optional, List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.users.models import User


async def get_user(user_id: str, db: AsyncSession) -> Optional[User]:
    query = select(User).filter_by(id=user_id)
    return await db.scalar(query)


async def sign_uo(user_model, db: AsyncSession):
    user = User(**user_model.model_dump())
    db.add(user)
    await db.commit()


async def sign_in(username: str, password: str, db: AsyncSession) -> Optional[str]:
    user: Optional[User] = await db.scalar(select(User).filter_by(username=username))
    if user:
        return user.get_token(pwd=password)