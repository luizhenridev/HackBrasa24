import psycopg2

def connetDatabase(database, user, password, host, port) -> psycopg2.extensions.connection:
    database = "auroradb"
    user = "aurora"
    password = "aurora123"
    host="localhost"
    port="5432"

    try:
        con = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port
        )

        return con
    except psycopg2.Error as e:
        print(f"Error connecting with the database")
        return None
    


