import time
import pandas as pd
import sqlite3

def stock_insert(df):
    conn = sqlite3.connect("tw_stock.db")

    for _, row in df.iterrows():
        # print(str(row.to_list())[1:-1])
        str_sql = f"""insert into tw_stock_price values (
           {str(row.to_list())[1:-1]}
        )"""
        cur = conn.cursor()
        cur.execute(str_sql)
        conn.commit()

    conn.close()


def process_stock(stock_id):
    print(f"process stock:{stock_id}")
    df = pd.read_excel(f"tw_{stock_id}.xlsx")
    stock_insert(df)
    time.sleep(5)


def main():
    start_time = time.time()
    process_stock('2330')
    process_stock('0050')
    process_stock('2002')
    print("--- %s seconds ---" % (time.time() - start_time))


main()