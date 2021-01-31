from sqlite3 import Error


def create_table_client(conn):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :return:
    """

    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            create table IF NOT EXISTS client (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                cpf TEXT NOT NULL,
                date_register DATE NOT NULL
            );
            """
        )
        conn.close()
    except Error as e:
        print(e)
