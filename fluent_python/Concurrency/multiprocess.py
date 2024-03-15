from multiprocessing import Pool, Process
import multiprocessing as mp
import os


def f(x):
    return x * x


def hello(name):
    print("hello", name)


def info(title):
    print(title)
    print("module name:", __name__)
    print("parent process:", os.getppid())
    print("process id:", os.getpid())


def func_f(name):
    info("function f")
    print("hello", name)


if __name__ == "__main__":
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
    print()

    p = Process(target=hello, args=("bob",))
    p.start()
    p.join()
    print()

    info("main line")
    p = Process(target=func_f, args=("bob",))
    p.start()
    p.join()
