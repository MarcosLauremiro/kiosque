from .product_handler import get_product_by_id


def calculate_tab(consum):
    subtotal = 0
    for consumption in consum:
        product_id = consumption["_id"]
        amount = consumption["amount"]
        product = get_product_by_id(product_id)
        subtotal += product["price"] * amount
    return {"subtotal": f"${round(subtotal, 2)}"}
