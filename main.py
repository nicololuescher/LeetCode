import time

from p15 import Solution

def main():
    start = time.time()
    print(Solution().test())
    print(f"Time: {time.time() - start}")


if __name__ == "__main__":
    main()