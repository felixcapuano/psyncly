from fastapi import FastAPI

from psyncly import models
from psyncly.api import core
from psyncly.api.v1 import (
    tracks as v1_tracks,
    playlists as v1_playlists,
    users as v1_users,
    service_accounts as v1_service_accounts,
    service_playlists as v1_service_playlists,
    workers as v1_workers,
)
from psyncly.database import engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(core.router)

app.include_router(v1_users.router, prefix="/v1")
app.include_router(v1_playlists.router, prefix="/v1")
app.include_router(v1_tracks.router, prefix="/v1")
app.include_router(v1_service_accounts.router, prefix="/v1")
app.include_router(v1_service_playlists.router, prefix="/v1")
app.include_router(v1_workers.router, prefix="/v1")
