import sys;

def main():
    colors=['green','red','blue']
    print (colors[0])
    print (colors[2])
    b = colors   ## b is pointing to the same list that colors is pointing to
    ## Does not copy the list Assignment with an = on lists does not make a copy. 
    ## Instead, assignment makes the two variables point to the one list in memory.
    print(b)  
    colors.append('black')  # if we will make any changes to colors that will be reflected in b also
    print(colors)
    print(b)
    colors.insert(0, 'white') #it will insert into position 0 and shift the array
    print(colors)
    colors.extend(['pink', 'brown'])  ## add list of elems at end   
    print(colors)
    print (colors.index('pink'))
    colors.remove('brown')         ## search and remove that element
    print(colors)
    print(colors.pop(1) )                ## remove element at position 1 and returns 'green'
    print(colors)


    list = ['a', 'b', 'c', 'd']
    print (list[1:-1])   ## ['b', 'c']
    list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
    print (list)         ## ['z', 'c', 'd']\


    # A tuple is a fixed size grouping of elements, such as an (x, y) co-ordinate. 
    # Tuples are like lists, except they are immutable and do not change size 
    # (tuples are not strictly immutable since one of the contained elements could be mutable).
    tuple = (1, 2, 'hi')
    print (len(tuple))  ## 3
    print (tuple[2])   ## hi
    #tuple[2] = 'bye'  ## NO, tuples cannot be changed
    tuple = (1, 2, 'bye')  ## this works
    print (tuple)
    tuple1 = ('hi',)   ## size-1 tuple
    print (tuple1)
    (x, y, z) = (42, 13, {'a':"asdfaf"})
    print (z)  ## {'a':"asdfaf"}


    ########## List Comprehensions ##########
    #### The syntax is [ expr for var in list ]
    nums = [1, 2, 3, 4]
    squares = [ n * n for n in nums ]   ## [1, 4, 9, 16]
    print(squares)
    cubes =[ n*n*n for n in nums]
    print(cubes)
    strs = ['hello', 'and', 'goodbye']
    shouting = [ s.upper() + '!!!' for s in strs ]
    print(shouting) ## ['HELLO!!!', 'AND!!!', 'GOODBYE!!!']

    # You can add an if test to the right of the for-loop to narrow the result. 
    # The if test is evaluated for each element, including only the elements where the test is true.

    ## Select values <= 2
    nums = [2, 8, 1, 6]
    small = [ n for n in nums if n <= 2 ]  ## [2, 1]
    print(small)
    ## Select fruits containing 'a', change to upper case
    fruits = ['apple', 'cherry', 'banana', 'lemon']
    afruits = [ s.upper() for s in fruits if 'a' in s ]
    print(afruits)    ## ['APPLE', 'BANANA']


if __name__ == "__main__":
    main()