import sys
print(sys.path)

print("---------------")

import re
text = "mi número de teléfono Es 634 616 627 y el de la suerte es el 7"
result= re.findall("[0-9]+",text)
result2= re.findall("[0-9]",text)
print(result)
print(result2)

print("---------------")

import time
timestapm = time.time()
print(timestapm) 

print("---------------")

local = time.localtime()
result = time.asctime(local)
print(result)

print("---------------")
import collections
numbers = [1,2,2,3,4,6,76,542,3]
counter = collections.Counter(numbers)
print(counter)
print(type(counter))