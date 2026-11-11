import sqlite3

DATABASE_NAME = "products.db"


def create_products_table():
    connection = sqlite3.connect(DATABASE_NAME)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            brand TEXT NOT NULL,
            price_level TEXT NOT NULL,
            category TEXT NOT NULL,
            routine_step INTEGER NOT NULL,
            usage TEXT NOT NULL,
            frequency TEXT NOT NULL,
            warnings TEXT NOT NULL,
            ingredients TEXT NOT NULL,
            goals TEXT NOT NULL,
            sensitive_skin_safe INTEGER NOT NULL,
            url TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()