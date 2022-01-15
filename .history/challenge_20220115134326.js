// /**
//  * @param {number} x
//  * @return {boolean}
//  */
var isPalindrome = function (x) {
  var s = "" + x;
  var l = 0;
  var r = s.length - 1;
  while (l < r) {
    if (s[l] !== s[r]) return false;
    l++;
    r--;
  }
  return true;
};

test_number = 1212121
isPalindrome(test_number);