# // /**
# //  * @param {number} x
# //  * @return {boolean}
# //  */
import math
def isPalindrome(x): 
  if x < 0:
    print("false")
  num = x
  res = 0
  while num != 0:
    res = (res * 10) + (num % 10)
    num = math.floor(num / 10)
    print("trues")
  
  return res == x


test_number = 1212121
isPalindrome(test_number)