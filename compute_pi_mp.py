from multiprocessing import Process
import sys
import os

NUM_THREADS = int(sys.argv[1])
threads = []
def calc_pi(itterations):
    print("Start process %s" % os.getpid())
    # Leibnizs formula
    k = 1
    s = 0
    for i in range(itterations):
        if i % 2 == 0:
            s += 4/k
        else:
            s -= 4/k
        k += 2
    print("(%i) Result: %s" % (os.getpid(), s))

if __name__ =="__main__":
    # creating thread
    for t in range(0, NUM_THREADS):
        threads.append(Process(target=calc_pi, args=(100000000,)))

    for t in threads:
        t.start()
    for t in threads:
        t.join()
    # both threads completely executed
    print("Done!")
