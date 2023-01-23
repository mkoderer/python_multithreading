import threading
import sys

NUM_THREADS = int(sys.argv[1])
threads = []
def print_cube(*nums):
    # function to print cube of given num
    for num in nums:
       result = (num * num * num)
       print("%s Cube: {}" .format(result) % threading.currentThread().ident)
 
 
if __name__ =="__main__":
    # creating thread
    nums = list(range(1, 1000000)) 
    for t in range(1, NUM_THREADS):
        threads.append(threading.Thread(target=print_cube, args=nums))

    for t in threads:
        t.start()
    for t in threads:
        t.join()
    # both threads completely executed
    print("Done!")
