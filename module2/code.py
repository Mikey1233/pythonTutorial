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
        "F": 15,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
         "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "0": 0,
    }
    for char in newValue[0]:
        # Convert hex character to decimal if it's a letter
        if char in alphabetsHex:
            char = alphabetsHex[char]
        else:
            return None
        # Update result using the hexadecimal to decimal formula
        result += char * (16 ** length)
        length -= 1  # Decrement the power of 16
    if len(newValue) == 2 : 
         for char2 in newValue[1] :
            if char2 in alphabetsHex :
                char2= alphabetsHex[char2]
            else :
                return None
            result += char2 * (16 ** negLength)
            negLength -= 1
            
    return result

# Test the function
ans = convertHexDec("C")
# ans2= convertHexDec("3A.2F")

print(ans)
# print(ans2)

print(int(8.7))
print(bool(-1) == 1)
