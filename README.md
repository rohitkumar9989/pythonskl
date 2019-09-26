# illustrated guide to python3

* list builtins
```python
dir(__builtins__)
```
* object's properties: 
  * identity(location in the memory)
  ```python
  one = '1'
  first = one //give same id
  id(one)
  id(first)
  ```
  * type(str, int, float, list, dict, tuple, function, type)
  ```python
  type(name)
  ```
    * value
* Mutability. mutable: dict, list. Immutable: string, tuple, int, float.
* coercing that is conversion from one type to another
* module, don't use negative signs
```python
-1%3
2
-1%-3
-1
1%-3
-2
```
* backslash 
```python
backslash = '\\'
print(backslash)
\
```
* escape symbols
```python
\\ Backslash
\' Single quote
\" Double quote
\b ASCII Backspace
\n Newline
\t Tab
\u12af Unicode 16 bit
\U12af89bc Unicode 32 bit
\N{SNAKE }Unicode character
\o84 Octal character
\xFF Hex character
```
* formatted string example
```python
"{name}".format(name="A")
"{[name]}".format({'name':"A"})
"{1}{0}".format('Zero','One')
```
* more on formatted strings
```python
:[[fill]align][sign][#][0][width][grouping_option][.precision][type]
```
   * fill - character used to fill in align, space is default
   * align - align output(< left align, > right align,^center, = put padding after sign)
   * sign - for numbers +(show sign on both positive and neg numbers), - - default(only on negative), or space(leading space for positive, sign on negative)
   * \# - prefix integers(0b, 0o, 0x)
   * 0 - enable zero padding
   * width - minimum field width
   * grouping_option - number separator(',' or _)
   * type - type for string or float
* Integers in formatted strings
   * b - binary, c - (unicode character), d - decimal, o - octal, x- hex, X - hex upper case
 * Floats in formatted strings
   * e/E - exponent, lower/upper case e
   * f - fixed point
   * g/G - General, fixed with exponent for large
   * n - with locale-specific separators
   * % multiplies by 100
* more examples
```python
"{:*^12}".format(Ringo)
# ***Ringo****
"{:b}".format(12)
# 1100
```
* f-strings. starting from python 3.6
```python
letter = 'A'
f'Letter is {letter} and {letter.capitalize()} and some calculation {2 **.5:5.3f}'
```
* dir - lists all the attributes of the object passed into it
* Dunder methods start(and end) with '__'
* help provides documentation for the method ```python help("a") ```

