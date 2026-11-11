import json
import sqlite3

from database import create_products_table
from products import PRODUCTS


create_products_table()

connection = sqlite3.connect("products.db")

for product in PRODUCTS:
    connection.execute("""
        INSERT INTO products (
            name,
            brand,
            price_level,
            category,
            routine_step,
            usage,
            frequency,
            warnings,
            ingredients,
            goals,
            sensitive_skin_safe,
            url
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,     (
        product["name"],
        product["brand"],
        product["price_level"],
        product.get("category", "treatment"),
        product.get("routine_step", 2),
        product.get(
            "usage",
            "Apply a small amount after cleansing."
        ),
        product.get(
            "frequency",
            "Use according to your skin's tolerance."
        ),
        product.get(
            "warnings",
            "Patch test first and stop if irritation occurs."
        ),
        json.dumps(product["ingredients"]),
        json.dumps(product["goals"]),
        int(product["sensitive_skin_safe"]),
        product["url"]
    ))

connection.commit()
connection.close()

print("Product database created successfully.")