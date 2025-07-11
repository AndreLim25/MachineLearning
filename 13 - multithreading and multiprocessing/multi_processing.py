import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i * i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i * i * i}")

if __name__ == "__main__":
    ## create 2 processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    start_time = time.time()

    ## start the processes
    p1.start()
    p2.start()

    ## wait for the processes to complete
    p1.join()
    p2.join()

    end_time = time.time()
    print(end_time - start_time)