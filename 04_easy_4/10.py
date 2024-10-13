def transactions_for(id, transactions):
    return [transaction for transaction in transactions if transaction.get("id") == id]

def is_item_available(item_id, transactions):
    matching_transactions = transactions_for(item_id, transactions)
    quantity = 0
    for transaction in matching_transactions:
        if transaction['movement'] == 'in':
            quantity += transaction['quantity']
        else:
            quantity -= transaction['quantity']
    return quantity > 0


transactions = [
    {"id": 101, "movement": "in", "quantity": 5},
    {"id": 105, "movement": "in", "quantity": 10},
    {"id": 102, "movement": "out", "quantity": 17},
    {"id": 101, "movement": "in", "quantity": 12},
    {"id": 103, "movement": "out", "quantity": 20},
    {"id": 102, "movement": "out", "quantity": 15},
    {"id": 105, "movement": "in", "quantity": 25},
    {"id": 101, "movement": "out", "quantity": 18},
    {"id": 102, "movement": "in", "quantity": 22},
    {"id": 103, "movement": "out", "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)  # True
