from psyncly import models
from psyncly.crud.generic_crud import GenericCrud


class TrackCrud(GenericCrud):
    ModelClass = models.Track


class UserCrud(GenericCrud):
    ModelClass = models.User


class PlaylistCrud(GenericCrud):
    ModelClass = models.Playlist


class PlaylistTrackRelationCrud(GenericCrud):
    ModelClass = models.PlaylistTrackRelation
