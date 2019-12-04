from collections import Counter
# 136760-595730

result = 0
for i in range(136760, 595730):
    digits = [int(j) for j in str(i)]
    if sorted(digits) != digits:
        continue

    # part one
    # elif len(digits) == len(set(digits)):
    #     continue
    # else:
    #     result += 1

    # part two
    # two digits not part of a larger group of matching digits
    for digit in digits:
        if digits.count(digit) == 2:
            result += 1
            break

    # bonus: only EXACTLY two of the same digits
    # most_common = [j for j in Counter(digits).most_common()[0]]
    # if most_common[1] <= 2 :
    #     result += 1

print(result)
