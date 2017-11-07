import threading

from crawlers.database import Base, engine

from crawlers.schedules import fetch_data as fetch_schedules
from crawlers.positions import fetch_data as fetch_positions


def cyclic_function(fun, time):
    threading.Timer(time, cyclic_function, (fun, time)).start()
    fun()


if __name__ == "__main__":
    Base.metadata.create_all(engine)

    cyclic_function(fetch_positions, 10)
    cyclic_function(fetch_schedules, 60 * 60 * 24)





