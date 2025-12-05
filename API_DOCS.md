# fast_crawl - API 상세 문서

이 문서는 `fast_crawl` 프로젝트의 HTTP API 엔드포인트를 요약합니다. 예시 요청/응답, 파라미터, 사용 가능한 경로를 포함합니다.

기본 베이스 경로: `/api`

참고: 서버는 `main.py`에서 `FastAPI` 인스턴스로 실행됩니다. 개발 중에는 다음 명령으로 실행하세요:

```powershell
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**응답/모델 정리**

- Article (DB 모델 `total_articles`):

  - `article_id` (string)
  - `title` (string)
  - `creationDate` (datetime 문자열, 형식: `YYYY.MM.DD HH:MM`으로 직렬화됨)
  - `siteUrl` (string)
  - `siteName` (string)
  - `collected_date` (datetime)

- Pagination (응답 모델):

  - `total` (int) - 전체 아이템 수
  - `page` (int) - 현재 페이지
  - `items` (list[Article]) - 해당 페이지의 게시글 목록

- Bookmark 모델 (`db/bookmark/models.py`):

  - `article_id` (string)
  - `site_name` (string)
  - `bookmarked_at` (datetime)

- ReadStatus 모델 (`db/read_status/models.py`):
  - `article_id` (string)
  - `site_name` (string)

---

**1) 게시글 조회 - Articles**

- 경로: `GET /api/articles`

  - 쿼리 파라미터: `page` (int, optional, 기본값: 1)
  - 설명: DB에 저장된 인기글을 페이징하여 반환합니다. 내부 `limit`은 15로 고정됩니다.
  - 응답: `Pagination` 모델
  - 예: `GET /api/articles?page=2`

- 경로: `GET /api/articles/sitename/{siteName}`
  - 경로 파라미터: `siteName` (string)
  - 쿼리 파라미터: `page` (int, optional, 기본값: 1)
  - 설명: 특정 사이트명으로 필터한 페이징 결과를 반환합니다.
  - 응답: `Pagination` 모델
  - 예: `GET /api/articles/sitename/SomeCommunity?page=1`

---

**2) 북마크(즐겨찾기) - Bookmarks**

- 경로: `POST /api/bookmarks`

  - 쿼리 파라미터: `site_name` (string, required), `article_id` (string, required)
  - 설명: 지정한 게시글을 북마크 테이블에 추가합니다. 이미 존재하면 기존 항목을 반환합니다.
  - 응답: 생성된 `Bookmark` 객체 (혹은 기존 항목)
  - 예 (curl):
    ```bash
    curl -X POST "http://localhost:8000/api/bookmarks?site_name=SomeCommunity&article_id=12345"
    ```

- 경로: `DELETE /api/bookmarks`

  - 쿼리 파라미터: `site_name` (string, required), `article_id` (string, required)
  - 설명: 해당 북마크를 삭제합니다. 항목이 없으면 404 반환.
  - 응답: 성공 시 `{ "detail": "Bookmark deleted" }` 또는 404 오류
  - 예 (curl):
    ```bash
    curl -X DELETE "http://localhost:8000/api/bookmarks?site_name=SomeCommunity&article_id=12345"
    ```

- 경로: `GET /api/bookmarks`
  - 설명: 현재 북마크된 게시글 목록을 반환합니다. 내부적으로 북마크와 `total_articles`를 조인하여 실제 게시글 데이터를 반환합니다.
  - 응답: `List[Article]`
  - 예: `GET /api/bookmarks`

---

**3) 읽음 상태(Read Status)**

- 경로: `POST /api/readstatus`

  - 쿼리 파라미터: `site_name` (string, required), `article_id` (string, required)
  - 설명: 게시글을 읽음 상태로 추가합니다. 이미 존재하면 기존 항목을 반환합니다.
  - 응답: 생성된 `ReadStatus` 객체 (혹은 기존 항목)
  - 예 (curl):
    ```bash
    curl -X POST "http://localhost:8000/api/readstatus?site_name=SomeCommunity&article_id=12345"
    ```

- 경로: `GET /api/readstatus`
  - 설명: 읽음으로 표시된 게시글들의 실제 게시글 데이터를 반환합니다. 내부적으로 `article_read_status`와 `total_articles`를 조인합니다.
  - 응답: `List[Article]`

---

**4) 검색 - Search**

- 경로: `GET /api/search`
  - 쿼리 파라미터: `keyword` (string, required)
  - 설명: 제목에서 `keyword`를 대소문자 구분 없이 검색합니다. 결과는 `creationDate` 내림차순 정렬입니다.
  - 응답: `List[Article]`
  - 예: `GET /api/search?keyword=python`

---

응답 예시 (Article 단일 항목 형태, JSON 직렬화 예):

```json
{
  "article_id": "12345",
  "title": "인기 게시글 제목",
  "creationDate": "2025.12.05 13:45",
  "siteUrl": "https://example.com/article/12345",
  "siteName": "SomeCommunity",
  "collected_date": "2025-12-05T13:45:00"
}
```

응답 예시 (Pagination):

```json
{
  "total": 120,
  "page": 2,
  "items": [
    /* Article 객체 리스트 */
  ]
}
```

---

에러 처리

- 북마크 삭제 시 항목이 없으면 `404`와 함께 `{ "detail": "Bookmark not found" }` 반환
- 기타 예외는 FastAPI 기본 HTTP 에러 형태로 반환될 수 있습니다. 필요한 경우 라우터에 명시적 예외 처리를 추가하세요.

추가 자료

- 라우터 소스 파일들:
  - `api/routes/articles.py`
  - `api/routes/bookmark.py`
  - `api/routes/readstatus.py`
  - `api/routes/article_search.py`
- 데이터 모델/스키마:
  - `db/article/article_models.py`
  - `db/article/schemas.py`
  - `db/bookmark/models.py` / `db/bookmark/schemas.py`
  - `db/read_status/models.py`

권장 다음 단계

- 각 엔드포인트에 대한 예제 요청/응답을 자동으로 생성하려면 테스트 스크립트(예: `tests/test_api.py`)를 추가해 통합 테스트를 작성하세요.
- `.env.example` 파일을 추가하여 `DATABASE_URL`의 예시를 제공하면 사용자가 빠르게 설정할 수 있습니다.

문서를 확장하거나 포맷(예: OpenAPI 마크다운, Postman 컬렉션)으로 변환해 드릴까요?
