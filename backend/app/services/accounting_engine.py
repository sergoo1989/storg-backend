def detect_financial_errors(orders, transactions):
    errors = []

    order_refs = {o.order_reference for o in orders}
    tx_refs = {t.reference for t in transactions}

    # 1) Orders missing in Accounting
    missing_revenue = order_refs - tx_refs
    for ref in missing_revenue:
        errors.append({
            "reference": ref,
            "error_code": "ACC-MISS-REV",
            "message": "Order exists but not recorded in accounting",
            "severity": "high"
        })

    # 2) Duplicate transactions
    ref_count = {}
    duplicates = []
    for t in transactions:
        ref_count[t.reference] = ref_count.get(t.reference, 0) + 1
    duplicates = [r for r in ref_count if ref_count[r] > 1]

    for ref in duplicates:
        errors.append({
            "reference": ref,
            "error_code": "ACC-DUP-REV",
            "message": "Revenue recorded more than once",
            "severity": "critical"
        })

    # 3) VAT mismatch
    for t in transactions:
        if t.type == "revenue":
            expected_vat = round(t.amount * 0.15, 2)
            if t.vat != expected_vat:
                errors.append({
                    "reference": t.reference,
                    "error_code": "ACC-VAT",
                    "message": f"VAT mismatch. Expected {expected_vat}, found {t.vat}",
                    "severity": "medium"
                })

    # 4) Payment mismatch (paid but not in bank)
    paid_orders = {o.order_reference for o in orders if o.status == "delivered"}

    missing_bank = paid_orders - {
        t.reference for t in transactions if t.type == "transfer"
    }

    for ref in missing_bank:
        errors.append({
            "reference": ref,
            "error_code": "ACC-NO-BANK",
            "message": "Delivered order but no bank payment found",
            "severity": "high"
        })

    return errors
