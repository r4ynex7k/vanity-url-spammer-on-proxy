import threading
from os import get_terminal_size as _terminal_size

lock = threading.Lock()

class Logger:

    checked, succ, proxyError = 0, 0, 0

    def Print(text):
        lock = threading.Lock()
        lock.acquire()
        print(text)
        lock.release()

    def Success(text):
        lock = threading.Lock()
        lock.acquire()
        print(f'[SUCCESS] {text}')
        lock.release()

    def Error(text):
        lock = threading.Lock()
        lock.acquire()
        print(f'[ERR] {text}')
        lock.release()
