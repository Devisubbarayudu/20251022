string = "Hello World"
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char not in vowels:
        count += 1
print(count)