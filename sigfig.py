import argparse
from termcolor import colored

parser = argparse.ArgumentParser()
parser.add_argument("number", help = "Number to find Significant Figure of", type = str)

args = parser.parse_args()

num = str(args.number)
digits = list(map(lambda x: "decimal" if x == '.' else int(x), num))
decimal = "decimal" in digits

def show_highlight(indices):
    final_str = list(num)
    for i in range(len(num)):
        if i in indices:
            final_str[i] = colored(num[i], 'blue')
    print(f"{len(indices)} | {''.join(final_str)}")

if all([x == 'decimal' or x != 0 for x in digits]):
    show_highlight(list(filter(lambda x: digits[x] != 'decimal', list(range(len(digits))))))
elif not decimal:
    flag = False
    indices = []
    for i, d in enumerate(digits):
        if d != 0: flag = True
        if flag: indices.append(i)

    trail_zero = len(indices)
    count = 0
    while trail_zero > 0:
        trail_zero -= 1
        if digits[indices[trail_zero]] != 0:
            break
        count += 1

    show_highlight(indices[:len(indices) - count])
elif decimal:
    flag = False
    indices = []
    for i, d in enumerate(digits):
        if d != 'decimal' and d != 0: flag = True
        if flag and d != 'decimal': indices.append(i)
    show_highlight(indices)
