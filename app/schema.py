import strawberry
from typing import List, Optional
from app.models import User as UserModel
from app.database import async_session
from sqlalchemy.future import select

@strawberry.type
class User:
    id: int
    name: str
    email: str
    is_active: bool
    created_at: str
    updated_at: str


@strawberry.type
class Query:
    @strawberry.field
    async def users(self, page: int = 1, page_size: int = 10, name: Optional[str] = None) -> List[User]:
        async with async_session() as session:
            query = select(UserModel).offset(
                (page - 1) * page_size).limit(page_size)
            if name:
                query = query.where(UserModel.name.ilike(f"%{name}%"))
            result = await session.execute(query)
            users = result.scalars().all()
            return [User(
                id=user.id,
                name=user.name,
                email=user.email,
                is_active=user.is_active,
                created_at=user.created_at.isoformat(),
                updated_at=user.updated_at.isoformat()
            ) for user in users]


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_user(self, name: str, email: str) -> User:
        async with async_session() as session:
            query = """
            INSERT INTO users (name, email, is_active) 
            VALUES (:name, :email, TRUE) 
            RETURNING id, name, email, is_active, created_at, updated_at
            """
            result = await session.execute(query, {'name': name, 'email': email})
            user = result.fetchone()
            return User(
                id=user.id,
                name=user.name,
                email=user.email,
                is_active=user.is_active,
                created_at=user.created_at.isoformat(),
                updated_at=user.updated_at.isoformat()
            )

schema = strawberry.Schema(query=Query, mutation=Mutation)
