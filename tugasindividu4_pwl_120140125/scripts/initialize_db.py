import argparse
import sys

from pyramid.paster import bootstrap, setup_logging
from sqlalchemy.exc import OperationalError

from .. import models


def setup_models(dbsession):
    """
    Add or update models / fixtures in the database.

    """
    animes = [
        models.Anime(
            title="One Piece",
            studios="Toei Animation",
            duration="24 min"
        ),
        models.Anime(
            title="Gintama",
            studios="Sunrise",
            duration="24 min"
        ),
        models.Anime(
            title="Koe no Katachi",
            studios="Kyoto Animation",
            duration="2 hr. 10 min."
        ),
        models.Anime(
            title="Kimi no Na wa",
            studios="CoMix Wave Films",
            duration="1 hr. 46 min."
        ),
        models.Anime(
            title="Death Note",
            studios="Madhouse",
            duration="23 min"
        ),
        models.Anime(
            title="Boku no Hero Academia",
            studios="Bones",
            duration="24 min"
        ),
        models.Anime(
            title="Sword Art Online",
            studios="A-1 Pictures",
            duration="23 min"
        ),
        models.Anime(
            title="Naruto",
            studios="Pierrot",
            duration="23 min"
        ),
        models.Anime(
            title="Kimetsu no Yaiba",
            studios="ufotable",
            duration="23 min"
        ),
        models.Anime(
            title="Tokyo Ghoul",
            studios="Pierrot",
            duration="24 min"
        ),
    ]

    for anime in animes:
        dbsession.add(anime)


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "config_uri",
        help="Configuration file, e.g., development.ini",
    )
    return parser.parse_args(argv[1:])


def main(argv=sys.argv):
    args = parse_args(argv)
    setup_logging(args.config_uri)
    env = bootstrap(args.config_uri)

    try:
        with env["request"].tm:
            dbsession = env["request"].dbsession
            setup_models(dbsession)
    except OperationalError:
        print(
            """
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for description and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.
            """
        )
