# x= 'rcaccademy'
# print(len(x))

# str():
# y=65576757635690
# z=str(y)
# print(type(z))
# print(z.find('999'))


# str.upper()
# Return a copy of the string with all the cased characters [4] converted to uppercase
# a= 'pramod'
# print(a.upper())

# count()

# a= 'pramod bansi chandan pramod bansi chandan pramod bansi chandan pramod bansi chandan '
# print(a.count('pramod',10, 50))
# print(a.count('bansi'))

# str.isupper()
# Return True if all cased characters [4] in the string are uppercase and there is at least one cased character,
# False otherwise.
# a= 'pramod bansi chandan pramod bansi chandan pramod bansi chandan pramod bansi chandan '
# b= 'pramod /bansi /chandan pramod/ bansi chandan/ pramod bansi /chandan /pramod /bansi chandan '

# print(a.isupper())
# str.isupper()
# Return True if all cased characters in the string are uppercase and there is at least one cased character, False otherwise.
# print(a.islower())


# str.split(sep=None, maxsplit=-1)
# Return a list of the words in the string, using sep as the delimiter string.
# If maxsplit is given, at most maxsplit splits are done (thus, the list will have at most maxsplit+1 elements).
# If maxsplit is not specified or -1, then there is no limit on the number of splits (all possible splits are made).

# print(a.split())
# print(b.split('/'))

# print(a.rsplit())

# str.rsplit(sep=None, maxsplit=-1)
# Return a list of the words in the string, using sep as the delimiter string.
# If maxsplit is given, at most maxsplit splits are done, the rightmost ones. If sep is not specified or None,
# any whitespace string is a separator. Except for splitting from the right,
# rsplit() behaves like split() which is described in detail below

# str.strip([chars])
# Return a copy of the string with the leading and trailing characters removed.
# The chars argument is a string specifying the set of characters to be removed. If omitted or None,
# the chars argument defaults to removing whitespace. The chars argument is not a prefix or suffix; rather,
# all combinations of its values are stripped:

a= "pramod bansi chandan pramod bansi chandan pramod bansi chandan PRAMOD pramod bansi chandan"
b ='pramod /bansi /chandan pramod/ bansi chandan/ pramod bansi /chandan /pramod /bansi chandan '
#
# print(a.strip('@;4 \''))

# str.replace(old, new[, count])
# Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument count is given,
# only the first count occurrences are replaced.

# print(a.replace('pramod','PRAMOD',1))

# str.find(sub[, start[, end]])
# Return the lowest index in the string where substring sub is found within the slice s[start:end].
# Optional arguments start and end are interpreted as in slice notation.
# Return -1 if sub is not found.
print(a.find('PRAMOD'))
print(a.find('PRAMOD',64, 100))
