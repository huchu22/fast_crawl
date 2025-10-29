from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.routes import articles, bookmark

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

@app.on_event("startup")
def startup_event():
    print("[Server] FastAPI server started")