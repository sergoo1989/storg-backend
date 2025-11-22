def find_duplicates(orders):
    ref_count = {}
    duplicates = []

    for o in orders:
        ref_count[o.order_reference] = ref_count.get(o.order_reference, 0) + 1

    for o in orders:
        if ref_count[o.order_reference] > 1:
            duplicates.append(o)

    return duplicates
