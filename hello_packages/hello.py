"""Hello world"""
import sys

def hello_world(name: str = 'default'):
    print(f"hello {name}")
    print(f"argv: {sys.argv}")

if __name__ == "__main__":
    hello_world(f'from script, my params: {sys.argv}')
    hello_world()