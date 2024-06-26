from random import choice, randint

import sys
sys.setrecursionlimit(10000000)

def genereate_braces(n:int, max:int = 10) -> str:
    def do_subtree():
        nonlocal n
        nonlocal sequence
        brace = choice(["()","{}","[]"])
        sequence.append(brace[0])
        count = randint(0 if n==0 else 1, min(max,n))
        n -= count
        for _ in range(count):
            do_subtree()
        sequence.append(brace[1])
    sequence = []
    do_subtree()
    return " ".join(sequence)

for size in range(1,7):
    size = 10 ** size
    print(f"Generating datasets with size {size}", end="")
    for count in range(10):
        print(".", end="")
        with open(f"testdata/{size}_dataset_{count}.txt", "w") as f:
            f.write(genereate_braces(size, 2**count))
    print(" done.")
