import os

from crawlers.database import Base, engine

from crawlers.schedules import fetch_data

if __name__ == "__main__":
    print("python:", os.environ["DB_CONNECTION"])

    Base.metadata.create_all(engine)

    fetch_data()

