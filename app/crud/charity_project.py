from typing import Optional, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, extract
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject
from app.schemas.charity_project import (CharityProjectCreate,
                                         CharityProjectUpdate)


class CRUDCharityProject(
    CRUDBase[
        CharityProject,
        CharityProjectCreate,
        CharityProjectUpdate
    ]
):

    async def get_charity_project(
        self,
        object_id: int,
        session: AsyncSession
    ) -> Optional[CharityProject]:
        charityproject_db = await session.execute(
            select(CharityProject).where(
                CharityProject.id == object_id
            )
        )
        return charityproject_db.scalars().first()

    async def get_charity_project_id_by_name(
        self,
        project_name: str,
        session: AsyncSession
    ) -> Optional[int]:
        charity_project = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        return charity_project.scalars().first()

    async def get_charity_project_close_date(
        self,
        project_id: int,
        session: AsyncSession
    ):
        project_close_date = await session.execute(
            select(CharityProject.close_date).where(
                CharityProject.id == project_id
            )
        )
        return project_close_date.scalars().first()

    async def get_charity_project_invested_amount(
        self,
        project_id: int,
        session: AsyncSession
    ):
        project_invested_amount = await session.execute(
            select(CharityProject.invested_amount).where(
                CharityProject.id == project_id
            )
        )
        return project_invested_amount.scalars().first()

    async def update(
        self,
        db_object,
        object_in,
        session: AsyncSession
    ):
        obj_data = jsonable_encoder(db_object)
        update_data = object_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_object, field, update_data[field])

        session.add(db_object)
        await session.commit()
        await session.refresh(db_object)
        return db_object

    async def remove(
        self,
        db_object,
        session: AsyncSession
    ):
        await session.delete(db_object)
        await session.commit()
        return db_object

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession,
    ) -> List[CharityProject]:
        """
        Получение всех завершенных проектов с сортировкой по времени закрытия.
        """
        projects = await session.execute(
            select([CharityProject.name,
                    CharityProject.description,
                    CharityProject.create_date,
                    CharityProject.close_date]).where(
                CharityProject.fully_invested.is_(True)
            ).order_by(
                extract('year', CharityProject.close_date) -
                extract('year', CharityProject.create_date),
                extract('month', CharityProject.close_date) -
                extract('month', CharityProject.create_date),
                extract('day', CharityProject.close_date) -
                extract('day', CharityProject.create_date),
                extract('hour', CharityProject.close_date) -
                extract('hour', CharityProject.create_date),
                extract('minute', CharityProject.close_date) -
                extract('minute', CharityProject.create_date),
                extract('second', CharityProject.close_date) -
                extract('second', CharityProject.create_date),
            )
        )
        return projects.all()


charityproject_crud = CRUDCharityProject(CharityProject)
