import sqlite3


def create_connection(sqlite_file=None):

    try:
        if sqlite_file:
            conn = sqlite3.connect(sqlite_file)
        else:
            conn = sqlite3.connect('tiktok.db')
        return conn

    except sqlite3.Error as error:
        raise (
            "An error is occured while connecting to the datebase",
            error.args[0]
        )


def add_data(header, tiktok_data, db_name, file_name=""):

    db_header = ""
    conn = create_connection(file_name)
    c = conn.cursor()

    for header in header:
        db_header += header + " TEXT, "

    c.execute(f'CREATE TABLE IF NOT EXISTS {db_name}({db_header})')

    inser_values = ""
    for db in tiktok_data:
        try:
            c.execute(f"""INSERT INTO {db_name} VALUES {db}""")
        except sqlite3.Error as error:
            raise ("An error has occured", error.args[0])

    conn.commit()
    conn.close()
    c = conn.cursor()
