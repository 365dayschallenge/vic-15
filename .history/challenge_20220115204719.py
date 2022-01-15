# // /**
# //  * @param {number} x
# //  * @return {boolean}
# //  */
import math
from tokenize import triple_quoted
def isPalindrome(x): 
  if x < 0:
    print("false")
  num = x
  res = 0
  while num != 0:
    res = (res * 10) + (num % 10)
    num = math.floor(num / 10)
    return True  
  return false

test_number = 1212121
isPalindrome(test_number)