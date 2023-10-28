from pyramid.response import Response
from pyramid.request import Request
from sqlalchemy.exc import DBAPIError
from pyramid.view import view_defaults, view_config
from datetime import datetime

from ..models import Anime


@view_defaults(route_name="anime")
class AnimeView:
    def __init__(self, request):
        self.request: Request = request

    def server_error(self):
        return Response(
            status=str(500),
            content_type="application/json",
            json={"message": "Internal server error!"},
        )

    @view_config(request_method="GET", permission="view")
    def get_all_animes(self):
        try:
            animes = self.request.dbsession.query(Anime).all()
            return Response(
                status=str(200),
                content_type="application/json",
                json={
                    "data": [
                        {
                            "id": anime.id,
                            "title": anime.title,
                            "studios": anime.studios,
                            "duration": anime.duration,
                            "created_at": str(anime.created_at),
                        }
                        for anime in animes
                    ]
                },
            )
        except DBAPIError:
            self.server_error()

    @view_config(request_method="POST", permission="admin")
    def create_new_anime(self):
        try:
            title = self.request.json_body["title"]
            studios = self.request.json_body["studios"]
            duration = self.request.json_body["duration"]
            anime = Anime(title=title, studios=studios, duration=duration)
            self.request.dbsession.add(anime)

            return Response(
                status=str(201),
                content_type="application/json",
                json={"message": "Success add new anime"},
            )

        except DBAPIError:
            self.server_error()

    @view_config(route_name="anime_id", request_method="GET", permission="view")
    def get_anime_by_id(self):
        try:
            id = self.request.matchdict["id"]  # type:ignore
            anime = (
                self.request.dbsession.query(
                    Anime).filter_by(id=id).first()
            )
            if anime:
                return Response(
                    status=str(200),
                    content_type="application/json",
                    json={
                        "data": {
                            "id": anime.id,
                            "title": anime.title,
                            "studios": anime.studios,
                            "duration": anime.duration,
                            "created_at": str(anime.created_at),
                        }
                    },
                )
            else:
                return Response(
                    status=str(404),
                    content_type="application/json",
                    json={"message": "Anime not found!"},
                )
        except DBAPIError:
            self.server_error()

    @view_config(route_name="anime_id", request_method="PUT", permission="admin")
    def update_anime_by_id(self):
        try:
            id = self.request.matchdict["id"]  # type:ignore
            anime = (
                self.request.dbsession.query(
                    Anime).filter_by(id=id).first()
            )
            if anime:
                anime.title = self.request.json_body["title"]
                anime.studios = self.request.json_body["studios"]
                anime.duration = self.request.json_body["duration"]
                anime.created_at = datetime.now()

                return Response(
                    status=str(200),
                    content_type="application/json",
                    json={"message": "Success update anime!"},
                )
            else:
                return Response(
                    status=str(404),
                    content_type="application/json",
                    json={"message": "Anime not found!"},
                )
        except DBAPIError:
            self.server_error()

    @view_config(
        route_name="anime_id", request_method="DELETE", permission="admin"
    )
    def delete_anime_by_id(self):
        try:
            id = self.request.matchdict["id"]  # type:ignore
            anime = (
                self.request.dbsession.query(
                    Anime).filter_by(id=id).first()
            )
            if anime:
                self.request.dbsession.delete(anime)
                return Response(
                    status=str(200),
                    content_type="application/json",
                    json={"message": "Success delete anime!"},
                )
            else:
                return Response(
                    status=str(404),
                    content_type="application/json",
                    json={"message": "Anime not found!"},
                )
        except DBAPIError:
            self.server_error()
