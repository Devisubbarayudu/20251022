sentence = "Python"
reversed_str = ""
i = len(sentence) - 1
for word in range (len(sentence),0,-1):
    reversed_str += sentence[i]
    i -= 1
print(reversed_str)