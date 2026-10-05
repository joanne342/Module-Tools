import argparse
import os

parser = argparse.ArgumentParser(
    prog="ls",
    description="Implement my own version of ls",
)

parser.add_argument(
    "-1",
    "--one",
    action="store_true",
    help="List one file per line",
)

parser.add_argument(
    "-a",
    action="store_true",
    help="Show hidden files",
)

parser.add_argument(
    "paths",
    nargs="*",
    default=["."],
)

args = parser.parse_args()

if not args.paths:
    args.paths = ["."]

for path in args.paths:
    if os.path.isdir(path):
        files = os.listdir(path)

        if not args.a:
            files = [
                name for name in files
                if not name.startswith(".")
            ]

        files.sort()

        if args.a:
            files = [".", ".."] + files

        if args.one:
            for file in files:
                print(file)
        else:
            print("  ".join(files))

    else:
        print(path)

