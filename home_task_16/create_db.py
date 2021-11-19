from sqlalchemy import create_engine
from models import User, Group, Task

if __name__ == '__main__':
    engine = create_engine('postgresql://postgres:postgres@localhost:5433/postgres')

    User.metadata.drop_all(engine)
    Group.metadata.drop_all(engine)
    Task.metadata.drop_all(engine)

    User.metadata.create_all(engine)
    Group.metadata.create_all(engine)
    Task.metadata.create_all(engine)
