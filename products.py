PRODUCTS = [
    {
        "name": "Gentle Barrier Cleanser",
        "brand": "Sample Beauty",
        "price_level": "low",
        "ingredients": ["ceramides", "glycerin"],
        "goals": ["redness", "dryness", "general"],
        "sensitive_skin_safe": True
    },
    {
        "name": "Niacinamide Balancing Serum",
        "brand": "Sample Beauty",
        "price_level": "low",
        "ingredients": ["niacinamide"],
        "goals": ["oiliness", "blemishes"],
        "sensitive_skin_safe": True
    },
    {
        "name": "Soothing Centella Serum",
        "brand": "Sample Beauty",
        "price_level": "medium",
        "ingredients": ["centella asiatica", "panthenol"],
        "goals": ["redness", "sensitive"],
        "sensitive_skin_safe": True
    },
    {
        "name": "Lightweight Gel Moisturizer",
        "brand": "Sample Beauty",
        "price_level": "low",
        "ingredients": ["glycerin", "hyaluronic acid"],
        "goals": ["oiliness", "general"],
        "sensitive_skin_safe": True
    }
]


def recommend_products(sensitive_skin: bool, budget: str):
    recommendations = []

    for product in PRODUCTS:
        matches_budget = product["price_level"] == budget
        safe_for_user = (
            not sensitive_skin or product["sensitive_skin_safe"]
        )

        if matches_budget and safe_for_user:
            recommendations.append(product)

    return recommendations