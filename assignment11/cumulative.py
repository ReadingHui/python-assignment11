import pandas as pd
import matplotlib.pyplot as plt
import sqlite3


LESSON_DB = '../db/lesson.db'

def main():
    with sqlite3.connect(LESSON_DB) as conn:
        conn.execute("PRAGMA foreign_keys = 1;")
        cursor = conn.cursor()

        # Task 1: Plotting with Pandas
        query = """
        SELECT li.order_id, SUM(li.quantity * p.price) AS total_price
        FROM line_items AS li
        JOIN products AS p
        ON li.product_id = p.product_id
        GROUP BY order_id;
        """

        cursor.execute(query)
        df = pd.DataFrame(cursor.fetchall(), columns=['order_id', 'total_price'])

        def cumulative(row):
            totals_above = df['total_price'][0:row.name+1]
            return totals_above.sum()

        df['cumulative'] = df.apply(cumulative, axis=1)
        df.plot(x='order_id', y='cumulative', kind='line', 
                title='Cumulative revenue against Order ID',
                xlabel='Order ID', ylabel='Cumulative Revenue',
                legend=False)
        plt.show()


if __name__ == "__main__":
    main()