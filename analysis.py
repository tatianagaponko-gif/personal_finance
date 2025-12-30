import pandas as pd
import matplotlib.pyplot as plt

def plot_expenses_over_time(transactions):
    data = {
        'date': [t.date for t in transactions],
        'amount': [t.amount for t in transactions],
        'category': [t.category for t in transactions]
    }
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df_grouped = df.groupby('date').sum()
    df_grouped['amount'].plot(kind='line')
    plt.title('Движение по расходам')
    plt.xlabel('Дата')
    plt.ylabel('Сумма')
    plt.show()

def plot_category_pie(transactions):
    data = {}
    for t in transactions:
        data[t.category] = data.get(t.category, 0) + t.amount
    plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
    plt.title('Структура расходов по категориям')
    plt.show()