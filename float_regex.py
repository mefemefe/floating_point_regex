math = 'f4.0' # any string

# determine if string contains a floating point number
import re
float_check = re.search('^\-*\+*[0-9]*\.[0-9]+$', math)


