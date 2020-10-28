'''
File        : comment_conventions.py
Author      : Mark Redd
Version     : 1.0
Description :
It is common to have a header at the top of your file that has the filename, author
and a general description of the program in the file. This space may also be used
to include pertient data about the software such as its version number or the 
date it was last modified. In many cases this header may be long and detailed 
depending on the intent of the programmer.

For the purposes of this book, we will not worry about having headers in our code
until we tackle some larger, more complex problems but it's good to know that these
things exist.
'''

'''Single line comments that explain code '''
# should be in one of two places:

# This comment explains the line below
print("Here are some words") # The comment may be here as well if space permits

# If needed, the comment may span
# multiple lines. The comment is generally
# above the line or block of code
# it explains in any case.
print("Here are some words") # The comment may be here as well if space permits

"""
It is bad practice to write comments that trail off the visible screen.
Later we will explore code style and explain this convetion more fully.

Multi-line comments may be placed wherever appropriate to make general
comments or explain a large block of code.
"""
