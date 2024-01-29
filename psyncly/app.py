from fastapi import FastAPI

from psyncly import models
from psyncly.api import core, v1
from psyncly.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(core.router)

app.include_router(v1.tracks.router, prefix="/v1")
app.include_router(v1.playlists.router, prefix="/v1")
app.include_router(v1.users.router, prefix="/v1")
