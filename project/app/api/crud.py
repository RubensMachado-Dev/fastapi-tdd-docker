# project/app/api/crud.py
from typing import List, Union

from sqlalchemy.orm import Session

from app.models.pydantic import SummaryPayloadSchema
from app.models.sqlalchemy_model import TextSummary


async def post(db: Session, payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        summary="dummy summary",
    )
    db.add(summary)
    db.commit()
    db.refresh(summary)
    return summary.id


async def get(db: Session, id: int) -> Union[dict, None]:
    summary = db.query(TextSummary).filter(TextSummary.id == id).first()
    if summary:
        return summary
    return None


async def get_all(db: Session) -> List:
    summaries = db.query(TextSummary).all()
    return summaries
