import pg8000
import os
import sqlalchemy
from google.cloud.sql.connector import Connector, IPTypes


def connect_with_connector() -> sqlalchemy.engine.base.Engine:
    instance_connection_name = os.environ[
        "INSTANCE_CONNECTION_NAME"
    ]
    db_user = os.environ["DB_USER"]
    db_pass = os.environ["DB_PASS"]
    db_name = os.environ["DB_NAME"]

    ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC

    connector = Connector()

    def getconn() -> pg8000.dbapi.Connection:
        conn: pg8000.dbapi.Connection = connector.connect(
            instance_connection_name,
            "pg8000",
            user=db_user,
            password=db_pass,
            db=db_name,
            ip_type=ip_type,
        )
        return conn

    pool = sqlalchemy.create_engine(
        "postgresql+pg8000://",
        creator=getconn,
        # ...
    )
    return pool


def subskills_to_string(results):
    order = [0, 3, 1, 4, 2]
    prefixes = ["[Lv. 10]", "[Lv. 25]", "[Lv. 50]", "[Lv. 75]", "[Lv. 100]"]

    keys_list = list(results)
    formatted_output = []

    for i, idx in enumerate(order):
        key = keys_list[idx]
        formatted_output.append(f'{prefixes[i]} {key}: {results[key]}')

    return '\n'.join(formatted_output)
