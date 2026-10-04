import argparse

parser = argparse.ArgumentParser(
    prog="cat",
    description="Implement my own version of cat in Python",
)

parser.add_argument("files", nargs="+", help="Files to process")
parser.add_argument("-n", action="store_true", help="Number all lines")
parser.add_argument("-b", action="store_true", help="Number non-blank lines")

args = parser.parse_args()

line_number = 1

for filename in args.files:
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if args.b:
                if line.strip() == "":
                    print(line, end="")
                else:
                    print(f"{line_number:6}\t{line}", end="")
                    line_number += 1

            elif args.n:
                print(f"{line_number:6}\t{line}", end="")
                line_number += 1

            else:
                print(line, end="")
