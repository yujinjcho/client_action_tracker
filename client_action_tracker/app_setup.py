import os
import psycopg2
from flask import Flask

from client_action_tracker.client_track_service import ClientTrackService
from client_action_tracker.datastore import Datastore


def create_app():
    print("Creating app")

    app = Flask(__name__)
    db_config = {
        'dbname': os.environ.get('DB_NAME', 'client-metric-track'),
        'password': os.environ.get('DB_PASSWORD', None),
        'user': os.environ.get('DB_USER', 'postgres'),
        'port': os.environ.get('DB_PORT', '5432'),
        'host': os.environ.get('DB_HOST', 'localhost')
    }
    conn = psycopg2.connect(**db_config)

    datastore = Datastore(conn)
    service = ClientTrackService(datastore)

    return app, service

