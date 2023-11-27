from menu import products


def get_product_by_id(idProduct):
    if not isinstance(idProduct, int):
        raise TypeError("product id must be an int")
    for product in products:
        if product["_id"] == idProduct:
            return product
    return {}


def get_products_by_type(type):
    if not isinstance(type, str):
        raise TypeError("product type must be a str")
    product_by_type = [
        product for product in products if product["type"] == type
        ]
    return product_by_type


def add_product(menu, **product):
    if not menu:
        product["_id"] = 1
    else:
        max_id = max(product["_id"] for product in menu)
        product["_id"] = max_id + 1
    menu.append(product)
    return product


def menu_report():
    product_count = len(products)

    total_price = sum(product["price"] for product in products)
    average_price = round(total_price / product_count, 2)

    types_count = {}
    for product in products:
        if product["type"] in types_count:
            types_count[product["type"]] += 1
        else:
            types_count[product["type"]] = 1

    most_common_type = max(types_count, key=types_count.get)

    report = f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {most_common_type}"

    return report
