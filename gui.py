import tkinter as tk
from tkinter import ttk, messagebox
from models import Transaction
from storage import load_transactions, save_transactions
from analysis import plot_expenses_over_time, plot_category_pie
from utils import validate_amount, validate_date

def run_app():
    transactions = load_transactions()

    def refresh_list():
        listbox.delete(0, tk.END)
        for i, t in enumerate(transactions):
            listbox.insert(tk.END, f"{i+1}. {t.date.strftime('%Y-%m-%d')} {t.category} {t.amount} {t.comment}")

    def add_transaction():
        try:
            amount = validate_amount(entry_amount.get())
            date_str = validate_date(entry_date.get())
            category = entry_category.get()
            comment = entry_comment.get()
            t = Transaction(amount, category, date_str, comment)
            transactions.append(t)
            save_transactions(transactions)
            refresh_list()
            messagebox.showinfo("Успех", "Операция добавлена.")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def delete_transaction():
        selection = listbox.curselection()
        if not selection:
            messagebox.showwarning("Удаление", "Выберите операцию для удаления.")
            return
        index = selection[0]
        del transactions[index]
        save_transactions(transactions)
        refresh_list()

    def show_expenses_over_time():
        plot_expenses_over_time(transactions)

    def show_category_structure():
        plot_category_pie(transactions)

    root = tk.Tk()
    root.title("Финансовый планер")

    frame = ttk.Frame(root)
    frame.pack(padx=10, pady=10, fill='both', expand=True)

    ttk.Label(frame, text="Сумма").grid(row=0, column=0, sticky='w')
    entry_amount = ttk.Entry(frame)
    entry_amount.grid(row=0, column=1, sticky='ew')

    ttk.Label(frame, text="Дата (YYYY-MM-DD)").grid(row=1, column=0, sticky='w')
    entry_date = ttk.Entry(frame)
    entry_date.grid(row=1, column=1, sticky='ew')

    ttk.Label(frame, text="Категория").grid(row=2, column=0, sticky='w')
    entry_category = ttk.Entry(frame)
    entry_category.grid(row=2, column=1, sticky='ew')

    ttk.Label(frame, text="Комментарий").grid(row=3, column=0, sticky='w')
    entry_comment = ttk.Entry(frame)
    entry_comment.grid(row=3, column=1, sticky='ew')

    btn_add = ttk.Button(frame, text="Добавить операцию", command=add_transaction)
    btn_add.grid(row=4, column=0, columnspan=2, pady=5)

    listbox = tk.Listbox(frame, height=10)
    listbox.grid(row=5, column=0, columnspan=2, sticky='nsew', pady=5)

    btn_delete = ttk.Button(frame, text="Удалить выбранную", command=delete_transaction)
    btn_delete.grid(row=6, column=0, columnspan=2, pady=5)

    btn_chart_time = ttk.Button(frame, text="График по времени", command=show_expenses_over_time)
    btn_chart_time.grid(row=7, column=0, pady=5)

    btn_chart_cat = ttk.Button(frame, text="Структура по категориям", command=show_category_structure)
    btn_chart_cat.grid(row=7, column=1, pady=5)

    # настройка столбцов
    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(5, weight=1)

    # инициализация списка
    refresh_list()

    root.mainloop()