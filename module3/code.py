def encodeStr(str) :
    encode = []
    count = 0
    cur_Char = str[0]
    for item in str :
        if item == cur_Char :
            count += 1 
        else:
            encode.append((cur_Char,count))
            cur_Char = item
            
            count = 1
    encode.append((cur_Char,count))
    return encode

res = encodeStr('bookkeeping')
print(res)

def decodeStr(strLs) :
    decode =''
    for item in strLs :
            decode += item[0] * item[1]
    return decode

res2 = decodeStr(res)

print(res2)