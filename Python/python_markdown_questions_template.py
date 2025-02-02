questions = ['Find the smallest number in an array',
'Find the largest number in an array',
'Second Smallest and Second Largest element in an array',
'Reverse a given array',
'Count frequency of each element in an array',
'Rearrange array in increasing-decreasing order',
'Calculate sum of the elements of the array',
'Rotate array by K elements - Block Swap Algorithm',
'Average of all elements in an array',
'Find the median of the given array',
'Remove duplicates from a sorted array',
'Remove duplicates from unsorted array',
'Adding Element in an array',
'Find all repeating elements in an array',
'Find all non-repeating elements in an array',
'Reverse words in a string']

template = '''{
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "'''
template2 = '''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    ""
   ]
  },'''

new_text = ''

for i in questions:
    new_text += template + '## ' + i + template2

first = '''{
 "cells": ['''
 
last = '''],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
'''
new_text = first + new_text[:-1] + last
with open('hello_world.txt', 'w') as file:
    file.write(new_text)
