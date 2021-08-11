##determining the length of a string
# len()
stringone="hello.world"
stringtwwo= len(stringone)
print(stringtwwo)

## Index Access
indexstring="Hamsrter"
print(indexstring[3]+indexstring[1]+indexstring[2])

## Extracting a slice Slice extraction operator: [X:Y].
# X is the beginning of the slice, and Y is the end;
# the symbol with the number Y is not included in the slice. By default,
# the first index is 0, and the second is the length of the string.


## the definition consists of a string of numbers
##  isDigit()
stringdigit="66666"
print(stringdigit.isdigit())
notquitedigitstring="668885kkdeeuueur"
print(notquitedigitstring.isdigit())


## the definition consists of a string of letters
## isAlfa
alfaStrings="spdlgkokfhikiohirtihrtkgtrt"
notquitealfastring="gkofgrty5y56i65iu8"
print(alfaStrings.isalpha())
print(notquitealfastring.isalpha())
print(notquitealfastring.isalnum())

## working with registers
lowerstring="jjjjkkooookohhigfhiio"
uperstring="RKRKOTHOTHITYHIJ5YIHI05Y0I5I0"
print(lowerstring.swapcase()+" "+uperstring.swapcase())