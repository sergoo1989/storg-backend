from datetime import datetime

def calc_processing_hours(created_at, picked_at):
    if not picked_at:
        return None
    delta = picked_at - created_at
    return round(delta.total_seconds() / 3600, 2)

def calc_delivery_hours(picked_at, delivered_at):
    if not delivered_at:
        return None
    delta = delivered_at - picked_at
    return round(delta.total_seconds() / 3600, 2)
