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
        SELECT last_name, SUM(price * quantity) AS revenue FROM employees e 
        JOIN orders o 
        ON e.employee_id = o.employee_id 
        JOIN line_items l 
        ON o.order_id = l.order_id 
        JOIN products p 
        ON l.product_id = p.product_id 
        GROUP BY e.employee_id;
        """

        cursor.execute(query)
        df = pd.DataFrame(cursor.fetchall(), columns=['Last Name', 'Revenue'])
        df.plot(x='Last Name', y='Revenue', kind='bar', 
                title="Employees' Revenue", 
                xlabel="Employees", ylabel="Revenue", 
                legend=False)
        plt.show()


if __name__ == "__main__":
    main()