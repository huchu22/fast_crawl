from pydantic import BaseModel
from datetime import datetime

# 기본 Table 요소
class Bookmark(BaseModel):
    article_id: str
    site_name: str