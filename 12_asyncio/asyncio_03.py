import asyncio
import time
import pandas as pd
import sqlite3


async def stock_insert(stock_id):
    print(f"process stock:{stock_id}")
    df = pd.read_excel(f"tw_{stock_id}.xlsx")
    await asyncio.sleep(10)

    conn = sqlite3.connect("tw_stock.db")
    print(f"stock:{stock_id} insert...")
    for _, row in df.iterrows():
        # print(str(row.to_list())[1:-1])
        str_sql = f"""insert into tw_stock_price values (
           {str(row.to_list())[1:-1]}
        )"""
        cur = conn.cursor()
        cur.execute(str_sql)
        conn.commit()
    print(f"stock:{stock_id} insert end...")

    conn.close()


async def process_stock(stock_id):
    await stock_insert(stock_id)


async def main():
    task1 = asyncio.create_task(
        process_stock('2330'))

    task2 = asyncio.create_task(
        process_stock('0050'))

    task3 = asyncio.create_task(
        process_stock('2002'))

    start_time = time.time()

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2
    await task3

    print("--- %s seconds ---" % (time.time() - start_time))


asyncio.run(main())