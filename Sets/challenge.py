vowels = {'a', 'e', 'i', 'o', 'u'}

text = set(input("Please enter some text"))
text = text.difference(vowels)
print(text)
