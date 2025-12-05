# fast_crawl

**간단한 설명**

`fast_crawl`는 FastAPI 기반의 가벼운 크롤러/수집기 및 API 서버입니다. 커뮤니티 인기 글을 수집하고, 북마크/읽음 상태를 관리하며 검색 기능을 제공합니다.

**주요 기능**

- 커뮤니티 게시글 크롤링 및 저장
- 게시글 목록 제공 및 검색 API
- 북마크(즐겨찾기) 관리
- 읽음 상태 관리
- 스케줄러(정기 크롤링) 연동

**요구사항**

- Python 3.13 이상 권장
- 의존성은 `requirements.txt`를 사용합니다.

**빠른 시작**

1. 레포지토리 루트에서 가상환경 생성 및 활성화 (PowerShell 예시):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. 의존성 설치:

```powershell
pip install -r requirements.txt
```

3. 환경변수 설정

프로젝트는 데이터베이스 연결 문자열과 같은 설정을 환경변수 또는 `.env` 파일로 관리합니다. 예: `DATABASE_URL` (Postgres 등).

웹 브라우저에서 `http://localhost:8000/docs`로 접속하면 자동 생성된 OpenAPI 문서를 확인할 수 있습니다.

**주요 엔드포인트(라우터)**

- `GET/POST/PUT/DELETE` 등은 각 라우터 파일을 확인하세요.
- 등록된 라우터 프리픽스:
  - `/api/articles` - 게시글 관련 API (`api/routes/articles.py`)
  - `/api/bookmarks` - 북마크 관련 API (`api/routes/bookmark.py`)
  - `/api/readstatus` - 읽음 상태 관련 API (`api/routes/readstatus.py`)
  - `/api/search` - 게시글 검색 (`api/routes/article_search.py`)

세부 엔드포인트와 스키마는 각 파일(`api/routes/*.py`, `db/article/`, `bookmark/`, `read_status/`)을 참고하세요.

**디렉터리 구조(요약)**

```
.
├─ main.py
├─ api/
│  └─ routes/
│     ├─ articles.py
│     ├─ bookmark.py
│     ├─ readstatus.py
│     └─ article_search.py
├─ crawler/
├─ db/
│  ├─ session.py
│  └─ article/
│     ├─ article_models.py
│     ├─ crud.py
│     └─ schemas.py
├─ bookmark/
├─ read_status/
└─ scheduler/
   └─ task.py
```

**데이터베이스**

`SQLAlchemy`와 `psycopg2`를 사용합니다. DB 연결 및 세션은 `db/session.py`를 확인하시고, 적절한 `DATABASE_URL` 환경변수를 설정

**개발/배포 관련 팁**

- 로컬 개발 시 `--reload` 플래그로 `uvicorn` 사용
- 운영 환경에서는 `uvicorn` 조합 사용 권장
- 스케줄러는 `APScheduler`로 구현되어 있으며 `scheduler/task.py`에서 작업을 확인

---

더 구체적인 실행/설정 정보가 필요하면 말씀해 주세요. 예: 데이터베이스 초기화 스크립트나 예제 환경변수 파일(.env) 작성 도와드릴게요.
