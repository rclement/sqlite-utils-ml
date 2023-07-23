import sqlite3
import sqlite_utils

from sqlite_ml.sqml import SQML


@sqlite_utils.hookimpl
def prepare_connection(conn: sqlite3.Connection) -> None:
    sqml = SQML()
    sqml.setup_schema(conn)
    sqml.register_functions(conn)
