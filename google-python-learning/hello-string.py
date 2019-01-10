import sys;

def main():

    s="mystring"
    print ("this is length of string",len(s)) ## 8
    print ("this is the first letter of string",s[0]) ## m
    print ("hi "+s) ## hi mystring
    
    # Unlike Java or JavaScript, the '+' does not automatically convert numbers or other types to string form.
    # The str() function converts values to a string form so they can be combined with other strings.
    num=500
    ## print (this is the number "+num     ## NO, does not work
    print ("this is the number "+str(num))


    a=50
    b=3
    print (a/b)
    print (a//b)
    ## print a++  ## NO, ++ does not work
    a+=10
    print( a)
    a-=10
    print (a)


    # A "raw" string literal is prefixed by an 'r' and passes all the chars through without special treatment of backslashes,
    # so r'x\nx' evaluates to the length-4 string 'x\nx'.

    raw=r'x\nx'
    print (raw)

    ## multi line string
    multi = """It was the best of times.  
    It was the worst of times."""
    print (multi)

    ## String Methods

    s="PYTHON IS COOL!"
    s=s.lower()
    print ("s.lower() ",s)
    s=s.upper()
    print ("s.upper() ",s)
    #s.strip() -- returns a string with whitespace removed from the start and end
    s=" "+s+"  "
    print ("s.strip() ",s.strip())
    s=s.strip()
    #s.isalpha()/s.isdigit()/s.isspace()... -- tests if all the string chars are in the various character classes
    print ("s.isalpha() ",s.isalpha())
    print ("s.isdigit() ",s.isdigit())
    print ("s.isspace() ",s.isspace())
    print ("s.isdigit() ",s.isdigit())

    #s.startswith('other'), s.endswith('other') -- tests if the string starts or ends with the given other string
    print (s)
    print ("s.startswith() ",s.startswith('PYTHON'))
    print ("s.endswith() ",s.endswith('PYTHON'))

    # s.find('other') -- searches for the given other string (not a regular expression) within s, 
    # and returns the first index where it begins or -1 if not found
    print ("s.find('PYTHON') ",s.find('PYTHON'))

    # s.replace('old', 'new') -- returns a string where all occurrences of 'old' have been replaced by 'new'
    s=s.replace('COOL','SEXY')
    print ("s.replace",s)

    # s.split('delim') -- returns a list of substrings separated by the given delimiter. 
    # The delimiter is not a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. 
    # As a convenient special case s.split() (with no arguments) splits on all whitespace chars.
    print ("s.split(" ")",s.split(" "))
    s=s.split(" ")
    # s.join(list) -- opposite of split(), joins the elements in the given list together using the string as the delimiter. 
    # e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc
    print ("s.join(" ")",' '.join(s))
    s=' '.join(s)
    s="Hello"
    ######## S L I C E #########
    #       H   e   l   l   o
    #       0   1   2   3   4
    #      -5  -4   -3  -2  -1
    ############################
    #s[1:4] is 'ell' -- chars starting at index 1 and extending up to but not including index 4
    print (s[1:4])
    # s[1:] is 'ello' -- omitting either index defaults to the start or end of the string
    print (s[1:])
    # s[:] is 'Hello' -- omitting both always gives us a copy of the whole thing (this is the pythonic way to copy a sequence like a string or list)
    print (s[:])
    # s[1:100] is 'ello' -- an index that is too big is truncated down to the string length
    print (s[1:100] )
    # s[-1] is 'o' -- last char (1st from the end)
    print (s[-1])
    # s[-4] is 'e' -- 4th from the end
    print (s[-4])
    # s[:-3] is 'He' -- going up to but not including the last 3 chars.
    print (s[:-3])
    # s[-3:] is 'llo' -- starting with the 3rd char from the end and extending to the end of the string.
    print (s[-3:])

    # It is a neat truism of slices that for any index n, s[:n] + s[n:] == s
    print (s[:2] + s[2:] == s)

 # Add parentheses to make the long line work:
    text = (
     "%d little pigs come out,"
      "or I'll %s, and I'll %s," 
      "and I'll blow your %s down."
      % (3, 'huff', 'puff', 'house'))
    print (text)

if __name__ == "__main__":
    main()