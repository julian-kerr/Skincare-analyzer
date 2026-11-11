import json
import sqlite3

PRODUCTS = [
    {
        "name": "SKIN1004 Madagascar Centella Ampoule Foam",
        "brand": "SKIN1004",
        "price_level": "low",
        "ingredients": [
            "centella asiatica extract",
            "sodium cocoyl isethionate"
        ],
        "goals": ["redness", "dryness", "general"],
        "sensitive_skin_safe": True,
        "url": "https://global.oliveyoung.com/product/detail?prdtNo=GA220113371"
    },
    {
        "name": "SKIN&LAB Niacinamide Recovery Serum",
        "brand": "SKIN&LAB",
        "price_level": "low",
        "category": "serum",
        "routine_step": 2,
        "usage": "Apply 2–3 drops to clean, dry skin after cleansing.",
        "frequency": "Once daily, preferably in the evening.",
        "warnings": "Patch test first. Stop using if irritation occurs.",
        "ingredients": [
            "niacinamide",
            "zinc PCA",
            "allantoin"
        ],
        "goals": [
            "oiliness",
            "blemishes"
        ],
        "sensitive_skin_safe": True,
        "url": "https://global.oliveyoung.com/product/detail?prdtNo=GA250329527"
    },
    {
        "name": "BANILA CO Clean It Zero Calming Gel Cleanser",
        "brand": "BANILA CO",
        "price_level": "medium",
        "ingredients": [
            "centella asiatica",
            "ceramides",
            "amino acids",
            "ectoin"
        ],
        "goals": ["redness", "dryness", "general"],
        "sensitive_skin_safe": True,
        "url": "https://global.oliveyoung.com/product/detail?accParam=90&prdtNo=GA250329253"
    },
    {
        "name": "Real Barrier Ceramide Moisture Cleansing Foam",
        "brand": "Real Barrier",
        "price_level": "medium",
        "ingredients": [
            "ceramide NP",
            "hyaluronic acid",
            "phytosterol",
            "fatty acids"
        ],
        "goals": ["redness", "dryness"],
        "sensitive_skin_safe": True,
        "url": "https://global.oliveyoung.com/product/detail?accParam=70&prdtNo=GA250228469"
    },
    {
        "name": "ONE THING Centella Asiatica Serum",
        "brand": "ONE THING",
        "price_level": "medium",
        "ingredients": [
            "centella asiatica",
            "madecassoside",
            "hyaluronic acid"
        ],
        "goals": ["redness", "dryness"],
        "sensitive_skin_safe": True,
        "url": "https://global.oliveyoung.com/product/detail?accParam=10&prdtNo=GA220213659"
    },
    {
        "name": "mixsoon Glacier Water Hyaluronic Acid Serum",
        "brand": "mixsoon",
        "price_level": "medium",
        "ingredients": [
            "hyaluronic acid",
            "glacial water"
        ],
        "goals": ["dryness", "general"],
        "sensitive_skin_safe": True,
        "url": "https://global.oliveyoung.com/product/detail?prdtNo=GA250228727"
    },
    {
        "name": "Isntree Ultra-Low Molecular Hyaluronic Acid Serum",
        "brand": "Isntree",
        "price_level": "medium",
        "ingredients": [
            "hyaluronic acid",
            "magnesium",
            "potassium",
            "calcium"
        ],
        "goals": ["dryness", "general"],
        "sensitive_skin_safe": True,
        "url": "https://global.oliveyoung.com/product/detail?accParam=1710&prdtNo=GA230518731"
    },
    {
        "name": "ILLIYOON Ceramide Ato Concentrate Cream",
        "brand": "ILLIYOON",
        "price_level": "medium",
        "ingredients": [
            "soy ceramide",
            "madecassoside"
        ],
        "goals": ["dryness", "redness"],
        "sensitive_skin_safe": True,
        "url": "https://global.oliveyoung.com/product/detail?prdtNo=GA251034628"
    },
    {
        "name": "Acnes Perfect Solution Foam Cleanser",
        "brand": "Acnes",
        "price_level": "low",
        "ingredients": [
            "salicylic acid",
            "tea tree",
            "centella asiatica"
        ],
        "goals": ["blemishes", "oiliness"],
        "sensitive_skin_safe": False,
        "url": "https://global.oliveyoung.com/product/detail?prdtNo=GA210003128"
    },
    {
        "name": "HEVEBLUE Salmon Caring Centella Ampoule",
        "brand": "HEVEBLUE",
        "price_level": "high",
        "ingredients": [
            "centella asiatica leaf water",
            "madecassoside"
        ],
        "goals": ["redness"],
        "sensitive_skin_safe": True,
        "url": "https://global.oliveyoung.com/product/detail?accParam=110&prdtNo=GA241126638"
    },
    {
        "name": "12GRABS My BHA Foaming Cleanser",
        "brand": "12GRABS",
        "price_level": "medium",
        "ingredients": [
            "centella asiatica",
            "BHA",
            "AHA",
            "beta-glucan",
            "allantoin"
        ],
        "goals": ["blemishes", "oiliness"],
        "sensitive_skin_safe": False,
        "url": "https://global.oliveyoung.com/product/detail?accParam=50&prdtNo=GA241126940"
    },
    {
        "name": "APLB Glutathione Niacinamide Facial Cleanser",
        "brand": "APLB",
        "price_level": "low",
        "ingredients": [
            "niacinamide",
            "glutathione",
            "centella asiatica"
        ],
        "goals": ["oiliness", "blemishes", "general"],
        "sensitive_skin_safe": True,
        "url": "https://global.oliveyoung.com/product/detail?prdtNo=GA240824958"
    }
]

BUDGET_LIMITS = {
    "low": 1,
    "medium": 2,
    "high": 3
}

PRICE_LEVELS = {
    "low": 1,
    "medium": 2,
    "high": 3
}

def load_products_from_database():
    connection = sqlite3.connect("products.db")
    connection.row_factory = sqlite3.Row

    rows = connection.execute("""
        SELECT *
        FROM products
    """).fetchall()

    connection.close()

    products = []

    for row in rows:
        products.append({
            "name": row["name"],
            "brand": row["brand"],
            "price_level": row["price_level"],
            "category": row["category"],
            "routine_step": row["routine_step"],
            "usage": row["usage"],
            "frequency": row["frequency"],
            "warnings": row["warnings"],
            "ingredients": json.loads(row["ingredients"]),
            "goals": json.loads(row["goals"]),
            "sensitive_skin_safe": bool(row["sensitive_skin_safe"]),
            "url": row["url"]
        })

    return products


def recommend_products(
    sensitive_skin: bool,
    budget: str,
    detected_concerns: list[dict]
):

    products = load_products_from_database()
    
    max_price_level = BUDGET_LIMITS[budget]
    scored_products = []

    for product in products:
        if PRICE_LEVELS[product["price_level"]] > max_price_level:
            continue

        if sensitive_skin and not product["sensitive_skin_safe"]:
            continue

        score = 0
        matched_concerns = []

        for concern in detected_concerns:
            if concern["name"] in product["goals"]:
                score += concern["confidence"]
                matched_concerns.append(concern["name"])

        if len(matched_concerns) > 1:
            score += 0.15

        if score == 0:
            continue

        match_reasons = [
            f"Matches detected concerns: {', '.join(matched_concerns)}",
            "Suitable for sensitive skin"
            if sensitive_skin
            else "No sensitive-skin restriction applied",
            f"Within the selected {budget} budget"
        ]

        scored_products.append({
            **product,
            "match_score": round(score, 2),
            "matched_concerns": matched_concerns,
            "match_reasons": match_reasons
        })

    scored_products.sort(
        key=lambda product: product["match_score"],
        reverse=True
    )

    selected_products = []

    # Choose the best product for each detected concern first
    for concern in sorted(
        detected_concerns,
        key=lambda concern: concern["confidence"],
        reverse=True
    ):
        for product in scored_products:
            if (
                concern["name"] in product["matched_concerns"]
                and product not in selected_products
            ):
                selected_products.append(product)
                break

    # Fill remaining recommendation slots by score
    for product in scored_products:
        if product not in selected_products:
            selected_products.append(product)

        if len(selected_products) == 3:
            break

    return selected_products
