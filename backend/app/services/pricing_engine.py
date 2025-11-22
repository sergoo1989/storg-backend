def calculate_price(material_cost: float,
                    packing_cost: float,
                    operating_cost: float,
                    fulfillment_cost: float,
                    shipping_cost: float,
                    target_margin: float):

    total_cost = (
        material_cost +
        packing_cost +
        operating_cost +
        fulfillment_cost +
        shipping_cost
    )

    price = total_cost / (1 - target_margin)

    return {
        "total_cost": total_cost,
        "price": round(price, 2)
    }
