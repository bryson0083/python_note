import threading 
import time
import pandas as pd
import sqlite3


def stock_insert(df):
    conn = sqlite3.connect("tw_stock.db")
    print(f"start insert stock {df.head(1)}")
    for _, row in df.iterrows():
        # print(str(row.to_list())[1:-1])
        str_sql = f"""insert into tw_stock_price values (
           {str(row.to_list())[1:-1]}
        )"""
        cur = conn.cursor()
        cur.execute(str_sql)
        conn.commit()

    conn.close()
    print(f"End of insert stock {df.head(1)}")


def thread_task(lock, stock_id): 
    """ 
    task for thread 
    """
    print(f"Start process stock:{stock_id}")
    df = pd.read_excel(f"tw_{stock_id}.xlsx")
    # lock.acquire()
    stock_insert(df)
    # lock.release()
    print(f"End of process stock:{stock_id}\n\n")


def main_task():
    # creating a lock 
    lock = threading.Lock() 

    # creating threads 
    t1 = threading.Thread(target=thread_task, args=(lock, "2330",)) 
    t2 = threading.Thread(target=thread_task, args=(lock, "0050",)) 
    t3 = threading.Thread(target=thread_task, args=(lock, "2002",)) 

    # start threads 
    t1.start() 
    t2.start() 
    t3.start() 

    # wait until threads finish their job 
    t1.join() 
    t2.join() 
    t3.join() 

if __name__ == "__main__":
    start_time = time.time()
    main_task()
    print("--- %s seconds ---" % (time.time() - start_time))

    # for i in range(10): 
    #     main_task() 
    #     print("Iteration {0}: x = {1}".format(i,x)) 
