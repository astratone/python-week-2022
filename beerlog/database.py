from sqlmodel import create_engine, Session
from beerlog.config import settings
from beerlog import models
import warnings
from sqlalchemy.exc import SAWarning
from sqlmodel.sql.expression import Select, SelectOfScalar

warnings.filterwarnings("ignore", category=SAWarning)
SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

engine = create_engine(settings.database.url, echo=False)
models.SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
