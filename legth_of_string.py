def lengthOfString(s):
    print("Length:", len(s))


def access(s):
    for ch in s:
        print(ch)


def assign(s):
    new_str = s
    new_str += " World"
    return new_str


original = "Hello"

lengthOfString(original)

print("\nCharacters:")
access(original)

result = assign(original)

print("\nOriginal:", original)
print("Returned:", result)