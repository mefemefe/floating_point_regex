math = 'f4.0' # any string

# determine if string is a floating point number (in this example, the string CONTAINS a float but it's not a float since it has an alphabetic character)
import re
float_check = re.search('^\-*\+*[0-9]*\.[0-9]+$', math)


