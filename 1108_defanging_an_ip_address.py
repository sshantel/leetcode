"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

"""


def defangIPaddr(address);
    defanged = ''
    for char in address:
        if char == '.':
            defanged += '[.]'
        else:
            defanged += char
    return defanged
                
print(defangIPaddr)