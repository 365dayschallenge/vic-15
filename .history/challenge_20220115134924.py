# // /**
# //  * @param {number} x
# //  * @return {boolean}
# //  */

def isPalindrome(x): 
  s = "" + x
  l = 0
  r = s.length - 1
  while l < r:
    if s[l] != s[r]:
      print("false")
    l+1
    r-1

  print("true")


test_number = 1212121
isPalindrome(test_number)