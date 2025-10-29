from pydantic import BaseModel
from datetime import datetime

# 기본 Table 요소
class ArticleBase(BaseModel):
    article_id: str
    title: str
    creation_date: datetime
    siteUrl: str
    siteName: str
    collected_date: datetime

# 페이지 네이션을 위한 모델
class Pagination(BaseModel):
    total: int
    page: int
    items: list[ArticleBase]
