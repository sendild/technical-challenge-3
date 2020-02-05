#!/usr/bin/python3

"""
Challenge #3

Function to generate the key from a nested object.
The nested object is stripped off it's special characters and a list (new_list) is created with the characters from the nested object.
The validation key is stripped off it's special characters a list (validation_list) is created.
As long as the keys matches with the nested object in the same sequence, the value is returned
"""

import string

class mydict:
    def __init__(self, string1):
        self.string1 = string1

    def myparser(self, validationkey):
        self.validationkey = validationkey
          
        #parse1 = (self.string1.replace('{',''))
        #parse2 = (parse1.replace('}',''))
        #parse3 = (parse2.replace('\'',''))
        #print(parse3)

        new_list = []
        
        for x in self.string1:
            if (x in string.ascii_lowercase or x in string.ascii_uppercase):          
                new_list.append(x)
        
        #print(new_list) 
        #print(self.validationkey)

        validation_list = []
        for x in self.validationkey:
            if (x in string.ascii_lowercase or x in string.ascii_uppercase):                
                validation_list.append(x)
        
        #print(validation_list)

        # Return the value for the keys
        if (new_list[0] == validation_list[0]):
            if (new_list[1] == validation_list[1]):
                if (new_list[2] == validation_list[2]):
                    print(new_list[3])
        


# Some tests for the function...

mystring = '{“a”:{“b”:{“c”:”d”}}}'
mykey = "a/b/c"
parse_mystring = mydict(mystring)
parse_mystring.myparser(mykey)

teststring1 = '{“x”:{“y”:{“z”:”a”}}}'
testkey1 = "x/y/z"
parse_teststring1 = mydict(teststring1)
parse_teststring1.myparser(testkey1)

teststring2 = '{“i”:{“j”:{“k”:”l”}}}'
testkey2 = "i/j/k"
parse_teststring2 = mydict(teststring2)
parse_teststring2.myparser(testkey2)