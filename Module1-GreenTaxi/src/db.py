import os
from sqlalchemy import create_engine

def get_engine():
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    db = os.getenv("POSTGRES_DB")
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = os.getenv("POSTGRES_PORT", "5432")

    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    return create_engine(url)
