alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

t = input("text: ").lower()
k = int(input("key: "))
r = "\n"

for char in t:
    if (char == ' '):
        r += ' ' 
        continue

    index = alphabet.index(char)
    x = (index - k) % 26
    r += alphabet[x]

print(r)