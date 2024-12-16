from decimal import Decimal,getcontext

getcontext(
    
)
print(getcontext())

getcontext().prec = 2

print(Decimal(1) /Decimal(3))