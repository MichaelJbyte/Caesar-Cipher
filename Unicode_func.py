# ord(), chr() functions
#   ord(character) -> Unicode code point (UCP)
#   chr(integer) -> Unicode character [reverse]

print(ord("A"))
print(ord("B"))
print(ord("C"))
print(ord("*"))

py_str = "Python"

ucp_vals = [ord(char) for char in py_str]

print(ucp_vals)


print(chr(97))
print(chr(98))
print(chr(99))

random_list = [25, 68, 43, 19]

print([chr(num) for num in random_list])
