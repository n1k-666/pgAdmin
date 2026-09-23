import psycopg2
from config import host, user, password, db_name

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT version();'
        )

        print(f'server version: {cursor.fetchone()}')

    # создание таблицы
    """with connection.cursor() as cursor:
        cursor.execute(
            '''CREATE TABLE users(
                id serial PRIMARY KEY,
                first_name varchar(50) NOT NULL,
                nock_name varchar(50) NOT NULL);'''
        )

        print("[INFO] table created")"""

    # ввод данных
    """with connection.cursor() as cursor:
        cursor.execute(
            '''INSERT INTO users (first_name, nick_name) VALUES
            ('Oleg','abobus');'''
        )

        print("[INFO] data created")"""

    # извлечение данных
    with connection.cursor() as cursor:
        cursor.execute(
            '''SELECT nick_name FROM users WHERE first_name = 'Oleg';'''
        )
        print(cursor.fetchone())

    # удаление
    with connection.cursor() as cursor:
        cursor.execute(
            '''DROP TABLE users;'''
        )

        print("[INFO] table was deleted")

except Exception as _ex:
    print('[INFO] error: ', _ex)
finally:
    if connection:
        connection.close()
        print('[INFO] Connect closs')