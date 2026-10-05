```python
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

files = []
directories = []

for path in args.paths:
    if os.path.isdir(path):
        directories.append(path)
    else:
        files.append(path)

# Print files first
if files:
    if args.one:
        for file in files:
            print(file)
    else:
        print("  ".join(files))

# Print directories
for path in directories:
    if files:
        print()

    print(f"{path}:")

    directory_files = os.listdir(path)

    if not args.a:
        directory_files = [
            file for file in directory_files
            if not file.startswith(".")
        ]

    directory_files.sort()

    if args.a:
        directory_files = [".", ".."] + directory_files

    if args.one:
        for file in directory_files:
            print(file)
    else:
        print("  ".join(directory_files))
```
