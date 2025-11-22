from datetime import datetime, timedelta
from app.services.duplicates import find_duplicates
from app.models.qc_error import QCError

def qc_check_orders(orders, inventory):
    errors = []

    now = datetime.utcnow()

    for o in orders:
        # 1) Missing AWB
        if not o.awb:
            errors.append(QCError(
                order_reference=o.order_reference,
                error_code="M-AWB",
                error_message="Missing AWB number",
                severity="medium"
            ))

        # 2) Missing status
        if not o.status:
            errors.append(QCError(
                order_reference=o.order_reference,
                error_code="M-STATUS",
                error_message="Missing order status",
                severity="high"
            ))

        # 3) Delivered but no delivered_at
        if o.status == "delivered" and not o.delivered_at:
            errors.append(QCError(
                order_reference=o.order_reference,
                error_code="M-POD",
                error_message="Delivered but missing delivery timestamp",
                severity="high"
            ))

        # 4) Processing delay > 24 hours
        if o.picked_at and (o.picked_at - o.created_at).total_seconds() > 24 * 3600:
            errors.append(QCError(
                order_reference=o.order_reference,
                error_code="D-PROC",
                error_message="Processing delay exceeds 24 hours",
                severity="medium"
            ))

        # 5) Delivery delay > 72 hours
        if o.delivered_at and o.picked_at:
            if (o.delivered_at - o.picked_at).total_seconds() > 72 * 3600:
                errors.append(QCError(
                    order_reference=o.order_reference,
                    error_code="D-DEL",
                    error_message="Delivery delay exceeds 72 hours",
                    severity="high"
                ))

    # 6) Duplicates
    duplicates = find_duplicates(orders)
    for d in duplicates:
        errors.append(QCError(
            order_reference=d.order_reference,
            error_code="DUP-ORDER",
            error_message="Order prepared more than once",
            severity="critical"
        ))

    return errors
