import queue
import multiprocessing
from multiprocessing import Process
from typing import List
from datetime import datetime 



def result():
    while True:
        if queue.empty():
            continue
        a, b = queue.get()
        end = a ** b
        end1=end        
        sum =0        
        while end1 != 0:
            sum=sum+end1
            end1=end1-1   
        dateTime = datetime.now()        
        with open("file.txt", "a", encoding='utf8') as file:
            file.write(str(dateTime) + " >> " + str(a) + " ^ " + str(b) + " = " + str(end) + ": Сумма чисел= " + str(sum) + "\n")

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process = Process(target=result)
    process.start()
    while True:
        try:
            str = input("Введите a и b: ")
            a1, b1 = (str.split(' '))
            a: int = int(a1)
            b: int = int(b1)
            datat = [a, b]
            queue.put(datat)
        except:
            print("Возникла ошибка при вводе")
