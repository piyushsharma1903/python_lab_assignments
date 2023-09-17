sentence = input("Enter a sentence: ")
length = len(sentence)
index = 0
capital_count = 0
small_count = 0
digit_count = 0
special_count = 0

while index < length:
    char = sentence[index]
    if 'A' <= char <= 'Z':
        capital_count += 1
    elif 'a' <= char <= 'z':
        small_count += 1
    elif '0' <= char <= '9':
        digit_count += 1
    else:
        special_count += 1  

    index += 1
print("Capital letters:", capital_count)
print("Small letters:", small_count)
print("Digits:", digit_count)
print("Special characters:", special_count)
