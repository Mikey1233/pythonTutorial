def convertHexDec(value):
    result = 0
    afterDecRes = 0
    
    newValue = value.split('.')
    length = len(newValue[0]) - 1
    negLength = -1
    print(newValue)
    alphabetsHex = {
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
    }
    for char in newValue[0]:
        # Convert hex character to decimal if it's a letter
        if char in alphabetsHex:
            char = alphabetsHex[char]
        else:
            char = int(char)  # Convert numeric characters to integers

        # Update result using the hexadecimal to decimal formula
        result += char * (16 ** length)
        length -= 1  # Decrement the power of 16
    print(result)
    if len(newValue) == 2 : 
         for char2 in newValue[1] :
            if char2 in alphabetsHex :
                char2= alphabetsHex[char2]
            else :
                char2= int(char2)
            result += char2 * (16 ** negLength)
            negLength -= 1
    return result

# Test the function
ans = convertHexDec("B3F.A1")
ans2= convertHexDec("3A.2F")

print(ans)
print(ans2)
