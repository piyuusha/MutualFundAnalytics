from sqlalchemy import create_engine
import pandas as pd
import os

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

DATABASE_PATH = f"sqlite:///{BASE_DIR}/bluestock_mf.db"

engine = create_engine(DATABASE_PATH)

def get_data(query):
    return pd.read_sql(query, engine)