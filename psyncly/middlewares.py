from fastapi import HTTPException, Request, Response
from sqlalchemy import exc
from starlette.middleware.base import BaseHTTPMiddleware


class SQLExceptionHandler(BaseHTTPMiddleware):
    def __init__(self, app) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response:
        try:
            response = await call_next(request)
        except exc.IntegrityError as e:
            raise HTTPException(status_code=400, detail="IntegrityError")

        return response
