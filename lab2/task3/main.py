import threading

class Authenticator:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

def main():
    auth1 = Authenticator()
    auth2 = Authenticator()
    print(auth1 is auth2)

if __name__ == "__main__":
    main()
