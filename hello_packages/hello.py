"""Hello world"""
import sys

def hello_world(name: str):
    print(f"hello {name}")

if __name__ == "__main__":
    hello_world(f'from script, my params: {sys.argv}')