import threading

lock = threading.RLock()

class FileManager:
    def init(self):
        self.xd = None
    
    @staticmethod
    def rlff(content: str, dsy: str):
        print(content)
        with lock:
            with open(dsy, 'r', encoding='utf-8', errors='önemsiz') as f:
                    lines = f.readlines()

            with open(dsy, 'w', encoding='utf-8', errors='önemsiz') as f:
                for line in lines:
                    if line.strip('\n') != content:
                        f.write(line)