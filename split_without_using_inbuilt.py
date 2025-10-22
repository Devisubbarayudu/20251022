sentence="emma-is-a-data-scientist"

space=""
for word in sentence:
    if word!="-":
        space=space+word
    else:
        print(space)
        space=""
print(space)