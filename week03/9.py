count = {}
for i in range(int(input())):
    line = input().split(" ")
    for word in line:
        count[word] = count.get(word, 0) + 1

max_count = max(count.values())
most_frequent = [k for k, j in count.items() if j == max_count]
print(min(most_frequent))