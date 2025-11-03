from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from api.routes import articles, bookmark, readstatus, article_search
from db import article

app = FastAPI(title= "커뮤니티 인기글 fastAPI")

# 모든 도메인 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # 모든 도메인 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록g
app.include_router(articles.router, prefix="/api/articles")
app.include_router(bookmark.router, prefix="/api/bookmarks")
app.include_router(readstatus.router, prefix="/api/readstatus")
app.include_router(article_search.router, prefix="/api/search")

@app.on_event("startup")
def startup_event():
    print("[Server] FastAPI server started")