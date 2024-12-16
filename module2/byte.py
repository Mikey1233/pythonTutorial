print(bytes(4))

stringB= bytes("hello",'utf-8') 

# emoji = bytes('👩‍🦱', 'utf-8')
print(stringB)
emoji = bytearray('👩‍🦱', 'utf-8')
print(emoji)
emoji[10]=int('32',16)
emoji = emoji.decode('utf-8')

print(emoji)
