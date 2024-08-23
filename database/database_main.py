import mysql.connector
from mysql.connector import Error

DB_NAME = 'password_db2'

##Shularni o'zizinikiga o'zgartiring
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'Abdulboriy'


def init_db():
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
        )

        if connection.is_connected():
            cursor = connection.cursor()

            create_database_script = f"create database IF NOT EXISTS {DB_NAME};"
            cursor.execute(create_database_script)
            connection.commit()

            connection.database = DB_NAME

            create_passwords_table_script = """
                create table IF NOT EXISTS passwords(
                    id bigint AUTO_INCREMENT PRIMARY KEY,
                    sayt_name varchar(250) not null UNIQUE,
                    login_user varchar(250) not null UNIQUE,
                    password varchar(250) not null,
                    created_date timestamp default CURRENT_TIMESTAMP
                );
            """
            cursor.execute(create_passwords_table_script)
            connection.commit()

            insert_passords_table_script = """
                INSERT IGNORE INTO passwords(sayt_name, login_user, password) values("Telegram", "Abdulboriy", "12345");
            """
            cursor.execute(insert_passords_table_script)
            connection.commit()

    except Error as e:
        print(f"Ma'lumotlar bazasiga ulanishda xato: {e}")
    except Exception as e:
        print(f"Databaseni yaratishda xatolik: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

    return connection
