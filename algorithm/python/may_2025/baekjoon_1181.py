import sys

input = sys.stdin.readline

N = int(input().strip())

word_set = set()

for _ in range(N):
    word_set.add(input().strip()) 


sorted_words = sorted(word_set, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)