from fastapi import FastAPI

from psyncly import models
from psyncly.api import core_routes
from psyncly.api.v1 import (
    playlist_routes as v1_playlists,
    account_routes as v1_accounts,
    service_playlist_routes as v1_service_playlists,
    track_routes as v1_tracks,
    user_routes as v1_users,
    worker_routes as v1_workers,
)
from psyncly.database import engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(v1_users.router, prefix="/v1")
app.include_router(v1_playlists.router, prefix="/v1")
app.include_router(v1_tracks.router, prefix="/v1")
app.include_router(v1_accounts.router, prefix="/v1")
app.include_router(v1_service_playlists.router, prefix="/v1")
app.include_router(v1_workers.router, prefix="/v1")

app.include_router(core_routes.router)
