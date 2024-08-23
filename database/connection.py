import mysql.connector
from mysql.connector import Error
from database.database_main import DB_NAME


def get_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Abdulboriy',
            database=DB_NAME
        )
        if connection.is_connected():
            print("Mysql ma'lumotlar bazasiga muvaffaqiyatli ulandi!")
            return connection
    except Error as e:
        print(f"Ma'lumotlar bazasiga ulanishda xato yuz berdi: {e}")
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Ma'lumotlar bazasi ulanishi yopildi.")

    return None






