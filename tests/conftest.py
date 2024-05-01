import pytest
import sqlite3


@pytest.fixture
def connection():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn
