import requests

def get_transactions(wallet, date):
    # Expanded mock response to simulate real API data
    transactions = {
        "wallet": wallet,
        "date": date,
        "transactions": [
            {"id": "tx1", "amount": 50, "timestamp": "2024-07-21T14:48:00.000Z"},
            {"id": "tx2", "amount": 100, "timestamp": "2024-07-21T15:00:00.000Z"},
            {"id": "tx3", "amount": 150, "timestamp": "2024-07-21T16:30:00.000Z"},
            {"id": "tx4", "amount": 200, "timestamp": "2024-07-21T17:00:00.000Z"},
            {"id": "tx5", "amount": 250, "timestamp": "2024-07-21T18:00:00.000Z"},
            {"id": "tx6", "amount": 300, "timestamp": "2024-07-21T19:00:00.000Z"}
        ]
    }
    return transactions
