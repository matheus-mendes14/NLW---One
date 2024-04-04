from sqlalchemy import creat_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler: 
    def __init__(self) -> None:
        self .__connection_string = "{}:///{}".format(
            "sqlite",
            "storage.db"
        )

        self .engine = None
        self.__session = None

    def connect_to_db(self) -> None:
        self.__engine = creat_engine(self.__connection_string)

    def get_engine(self):
        return self.__engine
    
    def __enter__ (self):
        session_maker = sessionmaker()
        self.__session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__session.close()