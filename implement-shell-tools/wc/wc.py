import argparse

parser = argparse.ArgumentParser(
    prog="wc",
    description="Count lines, words, and bytes in one or more files.",
)

parser.add_argument("-l", action="store_true", help="Count lines")
parser.add_argument("-w", action="store_true", help="Count words")
parser.add_argument("-c", action="store_true", help="Count bytes")
parser.add_argument("paths", nargs="+", help="Files to process")

args = parser.parse_args()

show_lines = args.l
show_words = args.w
show_bytes = args.c

if not (show_lines or show_words or show_bytes):
    show_lines = show_words = show_bytes = True

results = []

for path in args.paths:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.count("\n")
    words = len(content.split())
    bytes_count = len(content.encode("utf-8"))

    results.append((path, lines, words, bytes_count))

if len(results) > 1:
    total = (
        sum(r[1] for r in results),
        sum(r[2] for r in results),
        sum(r[3] for r in results),
    )

for path, lines, words, bytes_count in results:
    output = []

    if show_lines:
        output.append(f"{lines:8}")
    if show_words:
        output.append(f"{words:8}")
    if show_bytes:
        output.append(f"{bytes_count:8}")

    print("".join(output), path)

if len(results) > 1:
    lines, words, bytes_count = total

    output = []

    if show_lines:
        output.append(f"{lines:8}")
    if show_words:
        output.append(f"{words:8}")
    if show_bytes:
        output.append(f"{bytes_count:8}")

    print("".join(output), "total")
