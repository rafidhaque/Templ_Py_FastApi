from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./test_sql_app.db"
# SQLALCHEMY_DATABASE_URL = "sqlite:///./__temp_app__/test_sql_app.db"
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username, db_password, host_server, db_server_port,
#                                                                database_name, db_ssl_mode)

# SQLALCHEMY_DATABASE_URL = "postgresql://admin:secret@192.168.1.224:54320/postgres?sslmode=prefer"
SQLALCHEMY_DATABASE_URL = "postgresql://admin:secret@127.0.0.1:5001/postgres?sslmode=prefer"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_size=3, max_overflow=0
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()