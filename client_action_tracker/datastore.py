import json
from typing import List

import psycopg2
import psycopg2.extras
from psycopg2.errors import Error
from psycopg2.extensions import connection, cursor

from client_action_tracker.models import Event


class Datastore:
    def __init__(self, conn: connection):
        self.conn: connection = conn

    def insert_events(self, events: List[Event]):
        print(f'Inserting {len(events)} events')
        try:
            with self.conn.cursor() as cur:  # type: cursor
                events_tuples = [
                    (
                        str(event.event_id),
                        event.event_name,
                        event.event_type.value,
                        event.event_status.value,
                        event.client_created_at.isoformat(),
                        event.client_completed_at.isoformat(),
                        event.client_user_id,
                        str(event.project_id),
                        json.dumps(event.properties)  # Convert the properties to JSON string
                    )
                    for event in events
                ]
                psycopg2.extras.execute_values(
                    cur,
                    """
                    INSERT INTO events (event_id, event_name, event_type, event_status, client_created_at, client_completed_at, client_user_id, project_id, properties)
                    VALUES %s
                    """,
                    events_tuples,
                    page_size=1000
                )
                self.conn.commit()
        except Error as e:
            self.conn.rollback()
            raise e
