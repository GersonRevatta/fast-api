from app.database import Base, engine

def test_database_connection():
    try:
        Base.metadata.create_all(bind=engine)
        assert True
    except Exception:
        assert False
