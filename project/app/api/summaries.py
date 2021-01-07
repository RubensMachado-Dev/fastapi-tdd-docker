# project/app/api/summaries.py
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import crud
from app.db import get_db
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema
from app.models.sqlalchemy_model import SummarySchema

router = APIRouter()


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(
    payload: SummaryPayloadSchema, db: Session = Depends(get_db)
) -> SummaryResponseSchema:
    summary_id = await crud.post(db, payload)
    print(summary_id)
    response_object = {"id": summary_id, "url": payload.url}
    return response_object


@router.get("/{id}/", response_model=SummarySchema)
async def read_summary(id: int, db: Session = Depends(get_db)) -> SummarySchema:
    summary = await crud.get(db, id)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")

    return summary


@router.get("/", response_model=List[SummarySchema])
async def read_all_summaries(db: Session = Depends(get_db)) -> List[SummarySchema]:
    return await crud.get_all(db)
