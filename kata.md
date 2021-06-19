# Table of Contents
- [3 kyu](#3-kyu)
  * [Screen Locking Patterns](#screen-locking-patterns)
- [4 kyu](#4-kyu)
  * [Next bigger number with the same digits](#next-bigger-number-with-the-same-digits)
  * [parseInt() reloaded](#parseint-reloaded)
  * [Permutations](#permutations)
  * [Simplifying multilinear polynomials](#simplifying-multilinear-polynomials)
  * [Snail](#snail)
  * [Sort binary tree by levels](#sort-binary-tree-by-levels)
  * [Sum of Intervals](#sum-of-intervals)
- [5 kyu](#5-kyu)
  * [Largest product in a series](#largest-product-in-a-series)
- [6 kyu](#6-kyu)
  * [Counting Duplicates](#counting-duplicates)
  * [Even Fibonacci Sum](#even-fibonacci-sum)
  * [Last non-zero digit of factorial](#last-non-zero-digit-of-factorial)
  * [Multiples of 3 or 5](#multiples-of-3-or-5)
  * [Playing with digits](#playing-with-digits)
  * [Replace With Alphabet Position](#replace-with-alphabet-position)
  * [Take a Ten Minute Walk](#take-a-ten-minute-walk)
- [7 kyu](#7-kyu)
  * [Categorize New Member](#categorize-new-member)
  * [Descending Order](#descending-order)
  * [Disemvowel Trolls](#disemvowel-trolls)
  * [Exes and Ohs](#exes-and-ohs)
  * [Largest 5 digit number in a series](#largest-5-digit-number-in-a-series)
  * [Sum of odd numbers](#sum-of-odd-numbers)
- [8 kyu](#8-kyu)
  * [Multiply](#multiply)

# 3 kyu
## Screen Locking Pattern
[kata](https://www.codewars.com/kata/585894545a8a07255e0002f1) | Solutions: [Python](https://github.com/lcsm29/codewars/blob/main/3kyu/screen_locking_patterns.py)

You might already be familiar with many smartphones that allow you to use a geometric pattern as a security measure. To unlock the device, you need to connect a sequence of dots/points in a grid by swiping your finger **without lifting** it as you trace the pattern through the screen.

The image below has an example pattern of 7 dots/points: (A -> B -> I -> E -> D -> G -> C).

<img src="https://i.imgur.com/zmPNYdv.png">

For this kata, your job is to implement a function that returns **the number of possible patterns starting from a given first point, that have a given length**.

More specifically, for a function `countPatternsFrom(firstPoint, length)`, the parameter `firstPoint` is a single-character string corresponding to the point in the grid (i.e.: `'A'`) where your patterns start, and the parameter `length` is an integer indicating the number of points (length) every pattern must have.

For example, `countPatternsFrom("C", 2)`, should return the number of patterns starting from `'C'` that have `2` two points. The return value in this case would be `5`, because there are 5 possible patterns:

(C -> B), (C -> D), (C -> E), (C -> F) and (C -> H).

Bear in mind that this kata requires returning the **number** of patterns, **not the patterns themselves**, so you only need to count them. Also, **the name of the function might be different depending on the programming language used**, but the idea remains the same.

**Rules**
1. In a pattern, the dots/points cannot be repeated: they can only be used once, at most.
2. In a pattern, any two subsequent dots/points can only be connected with direct straight lines in either of these ways:
3. **Horizontally**: like (A -> B) in the example pattern image.
4. **Vertically**: like (D -> G) in the example pattern image.
5. **Diagonally**: like (I -> E), as well as (B -> I), in the example pattern image.
6. **Passing over a point between them that has already been 'used'**: like (G -> C) passing over E, in the example pattern image. This is the trickiest rule. Normally, you wouldn't be able to connect G to C, because E is between them, **however** when E has already been used as part the pattern you are tracing, you **can** connect G to C **passing over E**, because E is **ignored**, as it was already used once.

The sample tests have some examples of the number of combinations for some cases to help you check your code.

**Haskell Note**: A data type Vertex is provided in place of the single-character strings. See the solution setup code for more details.

**Fun fact:**

In case you're wondering out of curiosity, for the Android lock screen, the valid patterns must have between 4 and 9 dots/points. There are 389112 possible valid patterns in total; that is, patterns with a length between 4 and 9 dots/points.

# 4 kyu
## Next bigger number with the same digits
[kata](https://www.codewars.com/kata/55983863da40caa2c900004e) | Solutions: [Python](https://github.com/lcsm29/codewars/blob/main/4kyu/next_bigger_number_with_the_same_digits.py)

Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:
```
12 ==> 21
513 ==> 531
2017 ==> 2071
```
```python:
nextBigger(num: 12)   # returns 21
nextBigger(num: 513)  # returns 531
nextBigger(num: 2017) # returns 2071
```
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):
```
9 ==> -1
111 ==> -1
531 ==> -1
```
```python:
nextBigger(num: 9)   # returns -1
nextBigger(num: 111) # returns -1
nextBigger(num: 531) # returns -1
```

## parseInt() reloaded
[kata](https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5) | Solutions: [Python](https://github.com/lcsm29/codewars/blob/main/4kyu/parseint_reloaded.py)

In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

Examples:
* `"one"` => `1`
* `"twenty"` => `20`
* `"two hundred forty-six"` => `246`
* `"seven hundred eighty-three thousand nine hundred and nineteen"` => `783919`

Additional Notes:
* The minimum number is `"zero"` (inclusively)
* The maximum number, which must be supported is 1 million (inclusively)
* The `"and"` in e.g. `"one hundred and twenty-four"` is optional, in some cases it's present and in others it's not
* All tested numbers are valid, you don't need to validate them

## Permutations
[kata](https://www.codewars.com/kata/5254ca2719453dcc0b00027d) | Solutions: [Python](https://github.com/lcsm29/codewars/blob/main/4kyu/permutations.py)

In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

Examples:
```python:
permutations('a')  # ['a']
permutations('ab')  # ['ab', 'ba']
permutations('aabb')  # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
```
The order of the permutations doesn't matter.

## Simplifying multilinear polynomials
[kata](https://www.codewars.com/kata/55f89832ac9a66518f000118) | Solutions: [Python](https://github.com/lcsm29/codewars/blob/main/4kyu/simplifying_multilinear_polynomials.py)

When we attended middle school were asked to simplify mathematical expressions like "3x-yx+2xy-x" (or usually bigger), and that was easy-peasy ("2x+xy"). But tell that to your pc and we'll see!

Write a function: `simplify`, that takes a string in input, representing a multilinear non-constant polynomial in integers coefficients (like `"3x-zx+2xy-x"`), and returns another string as output where the same expression has been simplified in the following way ( `->` means application of `simplify`):

* All possible sums and subtraction of equivalent monomials ("xy==yx") has been done, e.g.:
  * `"cb+cba" -> "bc+abc"`, `"2xy-yx" -> "xy"`, `"-a+5ab+3a-c-2a" -> "-c+5ab"`

* All monomials appears in order of increasing number of variables, e.g.:
  * `"-abc+3a+2ac" -> "3a+2ac-abc"`, `"xyz-xz" -> "-xz+xyz"`

* If two monomials have the same number of variables, they appears in [lexicographic order](https://en.wikipedia.org/wiki/Lexicographic_order), e.g.:
  * `"a+ca-ab" -> "a-ab+ac"`, `"xzy+zby" -> "byz+xyz"`

* There is no leading `+` sign if the first coefficient is positive, e.g.:
  * `"-y+x" -> "x-y"`, but no restrictions for `-`: `"y-x" -> "-x+y"`

**N.B.** to keep it simplest, the string in input is restricted to represent only multilinear non-constant polynomials, so you won't find something like `-3+yx^2'. **Multilinear** means in this context: of **degree 1 on each variable**.

**Warning**: the string in input can contain arbitrary variables represented by lowercase characters in the english alphabet.

**Good Work :)**

## Snail
[kata](https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1) | Solutions: [Python](https://github.com/lcsm29/codewars/blob/main/4kyu/snail.py)

* Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
```python:
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
```
For better understanding, please follow the numbers of the next array consecutively:
```python:
array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
```
This image will illustrate things more clearly:

<img src="http://www.haan.lu/files/2513/8347/2456/snail.png">

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array `[[]]`.

## Sort binary tree by levels
[kata](https://www.codewars.com/kata/52bef5e3588c56132c0003bc) | Solutions: [Python](https://github.com/lcsm29/codewars/blob/main/4kyu/sort_binary_tree_by_levels.py)

You are given a binary tree:
```python:
class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
```
Your task is to return the list with elements from tree sorted by levels, which means the root element goes first, then root children (from left to right) are second and third, and so on.

Return empty list if root is `None`.

Example 1 - following tree:
```
                2
            8       9
          1   3   4   5
```
Should return following list:
```python:
[2,8,9,1,3,4,5]
```
Example 2 - following tree:
```
                1
            8       4
              3       5
                        7
```
Should return following list:
```python:
[1,8,4,3,5,7]
```

## Sum of Intervals
[kata](https://www.codewars.com/kata/52b7ed099cdc285c300001cd) | Solutions: [Python](https://github.com/lcsm29/codewars/blob/main/4kyu/sum_of_intervals.py)

Write a function called sumIntervals/sum_intervals() that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.

* Intervals

Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

* Overlapping Intervals

List containing overlapping intervals:
```python:
[
   [1,4],
   [7, 10],
   [3, 5]
]
```
The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.

* Examples:
```python:
sumIntervals( [
   [1,2],
   [6, 10],
   [11, 15]
] )  # => 9

sumIntervals( [
   [1,4],
   [7, 10],
   [3, 5]
] )  # => 7

sumIntervals( [
   [1,5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] )  # => 19
```
# 5 kyu
## Largest product in a series
[kata](https://www.codewars.com/kata/529872bdd0f550a06b00026e) | Solutions: [Python](https://github.com/lcsm29/codewars/blob/main/5kyu/largest_product_in_a_series.py)

Complete the `greatestProduct` method so that it'll find the greatest product of five consecutive digits in the given string of digits.

For example:
```python:
greatestProduct("123834539327238239583")  # should return 3240
```
The input string always has more than five digits.

Adapted from [Project Euler](https://projecteuler.net/).

# 6 kyu
## Counting Duplicates
[kata](https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1) | Solutions: [Python](https://github.com/lcsm29/codewars/blob/main/6kyu/counting_duplicates.py)

Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
* `"abcde"` -> `0`  # no characters repeats more than once
* `"aabbcde"` -> `2`  # `'a'` and `'b'`
* `"aabBcde"` -> `2`  # `'a'` occurs twice and `'b'` twice (`b` and `B`)
* `"indivisibility"` -> `1` # `'i'` occurs six times
* `"Indivisibilities"` -> `2` # `'i'` occurs seven times and `'s'` occurs twice
* `"aA11"` -> `2` # `'a'` and `'1'`

## Even Fibonacci Sum
[kata](https://www.codewars.com/kata/55688b4e725f41d1e9000065) | Solutions: [Python](https://github.com/lcsm29/codewars/blob/main/6kyu/even_fibonacci_sum.py)

Give the summation of all even numbers in a Fibonacci sequence up to, but not including, the maximum value.

The Fibonacci sequence is a series of numbers where the next value is the addition of the previous two values. The series starts with 0 and 1:

0 1 1 2 3 5 8 13 21...

For example:
```python:
eve_fib(0) == 0
eve_fib(33) == 10
eve_fib(25997544) == 19544084
```

## Last non-zero digit of factorial
[kata](https://www.codewars.com/kata/5f79b90c5acfd3003364a337) | Solutions: [Python](https://github.com/lcsm29/codewars/blob/main/6kyu/last_non-zero_digit_of_factorial.py)

Your task is to find the last non-zero digit of n!n!n! (factorial).

n! = 1 × 2 × 3 × ⋯ × n

* Example: If n == 12, your function should return 6 since 12! = 479001600

* Input: Non-negative integer n, Range: 0 - 2.5E6

* Output: Last non-zero digit of n!

* Note: Calculating the whole factorial will timeout.

## Multiples of 3 or 5
[kata](https://www.codewars.com/kata/514b92a657cdc65150000006) | Solutions: [Python](https://github.com/lcsm29/codewars/blob/main/6kyu/multiples_of_3_or_5.py)

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

* Note: If the number is a multiple of **both** 3 and 5, only count it once. Also, if a number is negative, return 0(for languages that do have them)

Courtesy of [projecteuler.net](https://projecteuler.net/)

## Playing with digits
[kata](https://www.codewars.com/kata/5552101f47fc5178b1000050) | Solutions: [Python](https://github.com/lcsm29/codewars/blob/main/6kyu/playing_with_digits.py)

Some numbers have funny properties. For example:
* 89 --> 8¹ + 9² = 89 * 1
* 695 --> 6² + 9³ + 5⁴ = 1390 = 695 * 2
* 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Given a positive integer `n` written as abcd... (a, b, c, d... being digits) and a positive integer `p`, we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n.

In other words:
* Is there an integer k such as : (a^p + b^(p+1) + c^(p+2) + d^(p+3) + ...) = n * k

If it is the case we will return k, if not return -1.

**Note**: n and p will always be given as strictly positive integers.
```python:
dig_pow(89, 1)     # should return 1   since 8¹ + 9² = 89 = 89 * 1
dig_pow(92, 1)     # should return -1  since there is no k such as 9¹ + 2² equals 92 * k
dig_pow(695, 2)    # should return 2   since 6² + 9³ + 5⁴= 1390 = 695 * 2
dig_pow(46288, 3)  # should return 51  since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
```

## Replace With Alphabet Position
[kata](https://www.codewars.com/kata/546f922b54af40e1e90001da) | Solutions: [Python](https://github.com/lcsm29/codewars/blob/main/6kyu/replace_with_alphabet_position.py)

Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

`"a" = 1`, `"b" = 2`, etc.

* **Example**
```
alphabet_position("The sunset sets at twelve o' clock.")
```
Should return `"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"` (as a string)

## Take a Ten Minute Walk
[kata](https://www.codewars.com/kata/54da539698b8a2ad76000228) | Solutions: [Python](https://github.com/lcsm29/codewars/blob/main/6kyu/take_a_ten_minute_walk.py)

You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. `['n', 's', 'w', 'e']`). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return `True` if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return `False` otherwise.

* Note: you will always receive a valid array containing a random assortment of direction letters (`'n'`, `'s'`, `'e'`, or `'w'` only). It will never give you an empty array (that's not a walk, that's standing still!).

# 7 kyu
## Categorize New Member
[kata](https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa) | Solutions: [Python](https://github.com/lcsm29/codewars/blob/main/7kyu/categorize_new_member.py)

The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

* Input

Input will consist of a list of lists containing two items each. Each list contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.

Note for F#: The input will be of (int list list) which is a List<List>

* Example Input
```python:
[[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
```

* Output

Output will consist of a list of string values (in Haskell: Open or Senior) stating whether the respective member is to be placed in the senior or open category.

* Example Output
```python:
["Open", "Open", "Senior", "Open", "Open", "Senior"]
```

## Descending Order
[kata](https://www.codewars.com/kata/5467e4d82edf8bbf40000155) | Solutions: [Python](https://github.com/lcsm29/codewars/blob/main/7kyu/descending_order.py)

Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:

* Input: `42145` Output: `54421`
* Input: `145263` Output: `654321`
* Input: `123456789` Output: `987654321`

## Disemvowel Trolls
[kata](https://www.codewars.com/kata/52fba66badcd10859f00097e) | Solutions: [Python](https://github.com/lcsm29/codewars/blob/main/7kyu/disemvowel_trolls.py)

Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string `"This website is for losers LOL!"` would become `"Ths wbst s fr lsrs LL!"`.

Note: for this kata `y` isn't considered a vowel.

## Exes and Ohs
[kata](https://www.codewars.com/kata/55908aad6620c066bc00002a) | Solutions: [Python](https://github.com/lcsm29/codewars/blob/main/7kyu/exes_and_ohs.py)

Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:
```python:
XO("ooxx")  # => True
XO("xooxx")  # => False
XO("ooxXm")  # => True
XO("zpzpzpp")  # => True // when no 'x' and 'o' is present should return True
XO("zzoo")  # => False
```

## Largest 5 digit number in a series
[kata](https://www.codewars.com/kata/51675d17e0c1bed195000001) | Solutions: [Python](https://github.com/lcsm29/codewars/blob/main/7kyu/largeset_5_digit_number_in_a_series.py)

In the following 6 digit number:
```
283910
```
`91` is the greatest sequence of 2 consecutive digits.

In the following 10 digit number:
```
1234567890
```
`67890` is the greatest sequence of 5 consecutive digits.

Complete the solution so that it returns the greatest sequence of five consecutive digits found within the number given. The number will be passed in as a string of only digits. It should return a five digit integer. The number passed may be as large as 1000 digits.

Adapted from [ProjectEuler.net](https://projecteuler.net/)

## Sum of odd numbers
[kata](https://www.codewars.com/kata/55fd2d567d94ac3bc9000064) | Solutions: [Python](https://github.com/lcsm29/codewars/blob/main/7kyu/sum_of_odd_numbers.py)

Given the triangle of consecutive odd numbers:
```
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
```
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.:
```python:
row_sum_odd_numbers(1)  # 1
row_sum_odd_numbers(2)  # 3 + 5 = 8
```

# 8 kyu
## Multiply
[kata](https://www.codewars.com/kata/50654ddff44f800200000004) | Solutions: [Python](https://github.com/lcsm29/codewars/blob/main/8kyu/multiply.py)
