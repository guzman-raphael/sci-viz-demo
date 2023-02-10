import datajoint as dj
import os
from faker import Faker


fake = Faker()
Faker.seed("datajoint")

dj.conn(
    host=os.getenv("PHARUS_HOST"),
    user=os.getenv("PHARUS_USER"),
    password=os.getenv("PHARUS_PASSWORD"),
)

schema = dj.Schema("demo")


@schema
class Scientist(dj.Lookup):
    definition = """
    id: int
    ---
    name: varchar(50)
    """
    contents = [(i, fake.first_name()) for i in range(50)]
