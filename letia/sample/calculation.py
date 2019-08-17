import argparse

def calculate(number: int) -> int:
    return number * 6

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("number", type=int)
    args = parser.parse_args()
    print(calculate(args.number))

if __name__ == "__main__":
    main()
