

import sys

def main():

  a = [5, 1, 4, 3]
  print (sorted(a))  ## [1, 3, 4, 5]
  print (a)  ## [5, 1, 4, 3]
  print (sorted(a,reverse=True))


  strs = ['ccc', 'aaaa', 'd', 'bb']
  print (sorted(strs, key=len))  ## ['d', 'bb', 'ccc', 'aaaa']
  ## "key" argument specifying str.lower function to use for sorting
  strs = ['aa', 'BB', 'zz', 'CC']
  print (sorted(strs, key=str.lower))  ## ['aa', 'BB', 'CC', 'zz']

  ######## You can also pass in your own MyFn as the key function, like this:######## 
  ## Say we have a list of strings we want to sort by the last letter of the string.
  strs = ['xc', 'zb', 'yd' ,'wa']

  ## Write a little function that takes a string, and returns its last letter.
  ## This will be the key function (takes in 1 value, returns 1 value).
  def MyFn(s):
    return s[-1]

  ## Now pass key=MyFn to sorted() to sort by the last letter:
  print (sorted(strs, key=MyFn))  ## ['wa', 'zb', 'xc', 'yd']



  #sort() method
  #As an alternative to sorted(), the sort() method on a list sorts that list into ascending order,
  # e.g. list.sort(). The sort() method changes the underlying list and returns None, so use it like this
  alist = [5, 1, 4, 3]
  alist.sort()            ## correct
  #alist = blist.sort()    ## NO incorrect, sort() returns None
  print(alist)


  

if __name__ == "__main__":
    main()