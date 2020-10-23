import sqlite3


class DatabaseContextManager(object):

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()


def create_table_coders():
    query = """CREATE TABLE IF NOT EXISTS Coders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT)"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_table_skills():
    query = """CREATE TABLE IF NOT EXISTS Skills(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    language TEXT)"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_table_coders_skills():
    query = """CREATE TABLE IF NOT EXISTS Coders_Skills(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    coders_id INTEGER,
    skills_id INTEGER,
    FOREIGN KEY (skills_id) REFERENCES Skills(id),
    FOREIGN KEY (coders_id) REFERENCES Coders(id))"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_coders(name: str):
    query = """INSERT INTO Coders(name) VALUES(?)"""
    parameters = [name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_coders():
    query = """SELECT * FROM Coders"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


def create_skills(language: str):
    query = f"""INSERT INTO Skills(language) VALUES(?)"""
    parameters = [language]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_skills():
    query = """SELECT * FROM SKills"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


def get_coders_skills():
    query = """SELECT language FROM skills
            JOIN Coders_Skills ON Skills.id = skills_id
            JOIN Coders ON coders_id = Coders.id
            WHERE name = 'joe'"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


def create_coders_skills(coders_id: int, skills_id: int):
    query = f"""INSERT INTO Coders_Skills(coders_id, skills_id) VALUES(?,?)"""
    parameters = [coders_id, skills_id]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)
