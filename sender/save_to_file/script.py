import sys

if __name__ == "__main__":
    data = sys.argv[1]
    with open("$", "x+") as f:
        f.write(data)
