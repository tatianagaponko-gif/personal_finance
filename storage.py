import csv
from models import Transaction

DATA_FILE = 'data/transactions.csv'

def save_transactions(transactions):
    try:
        with open(DATA_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for t in transactions:
                writer.writerow([t.amount, t.category, t.date.strftime("%Y-%m-%d"), t.comment])
    except Exception as e:
        print(f"Ошибка при сохранении данных: {e}")

def load_transactions():
    transactions = []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                amount, category, date_str, comment = row
                transactions.append(Transaction(float(amount), category, date_str, comment))
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}")
    return transactions