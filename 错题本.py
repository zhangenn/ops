#1
def common_chars(s1, s2):
    """ (str, str) -> str

    Return a new string containing all characters from s1 that appear at least
    once in s2.  The characters in the result will appear in the same order as
    they appear in s1.

    >>> common_chars('abc', 'ad')
    'a'
    >>> common_chars('a', 'a')
    'a'
    >>> common_chars('abb', 'ab')
    'abb'
    >>> common_chars('abracadabra', 'ra')
    'araaara'
    """
    res=' '
    for char in s1:
        if char in s2:
            res=res+char
    return res


#2
def while_loop1():
    for ch in '123456789':
        num=int(ch)
        if num % 2==0:
            print num
            
#    return num
#figure out why output 9
#while_loop1()=while_loop2()
def while_loop2():
    i=0
    while i<8:
        i=i+2
        print(i)

#3
def vowel_aeiou():
    for vowel in 'aeiou':
        print("I'd like to buy a", vowel)


#4
def has_vowel(s):
    """(str) -> bool 
    Return True if and only if s has at least one vowel, not including y.
    >>> has_vowel("Anniversary")
    True
    >>> has_vowel("xyz")
    False
    """
    vowel_found=False
    for char in s:
        if char in 'aeiouAEIOU':
            vowel_found=True
    return vowel_found
    
#5
def last_vowel(s):
    """(str) -> str
    Return the last vowel in s if one exists; otherwise, return None.
    >>> last_vowel("cauliflower")
    "e"
    >>> last_vowel("pfft")
    None
    """
    i=len(s)-1
    while i>=0:
        if s[i] in 'aeiouAEIOU':
            return s[i]
        i=i-1
    return None

#6
def is_IP_address(address):
    for char in address:
        if char not in '0123456789.':
            return False
    return True
    




        
        
