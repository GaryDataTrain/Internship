#!/usr/bin/env python
# coding: utf-8

# # Regular Expressions homework Gary Hickey

# ## Question 1- Write a RegEx pattern in python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)

# In[152]:


import re

def strings (s):
    
    pattern = r"^[a-z, A-Z, 0-9]+$"
    
    if re.match(pattern, s):
        return True
    else:
        return False

strings = ["space included", "spaceexcluded", "COUNT",
           "Gary", "@dt.com", "1234", 'lowercase', 'WoLpA5s']

for s in strings:
    if check_valid_string (s):
        print(f"'{s}' matches pattern.")
    else:
        print(f"'{s}' doesnt match pattern.")




# ## Question 2- Write a RegEx pattern that matches a string that has an a followed by zero or more b's
# 

# In[153]:


import re

#define pattern
pattern2 = r"ab*"

#create string
string_with_AB = ["a", "ab", "abb", "ab1", "1abbb", "2bac", "!ac", "abc"]

#test string using match
for s in string_with_AB:
    if re.match(pattern2, s):
        print(f"'{s}' matches the string.")
    else:
        print(f"'{s}' does not match the string.")


# ## Question 3-  Write a RegEx pattern that matches a string that has an a followed by one or more b's

# In[154]:


import re
#define pattern
pattern3 = r'ab+'
#create string
string_with_AandB = ["a", "ab", "Ab1", "1ab", "bA", "!abbc", "abc"]

#test string using match
for s3 in string_with_AandB:
    if re.match(pattern3, s3):
        print(f"'{s3}' matches the string.")
    else:
        print(f"'{s3}' does not match the string.")




# ## Question 4- Write a RegEx pattern that matches a string that has an a followed by zero or one 'b'.

# In[155]:


# define pattern using ?
pattern4 = r'ab?' 

#create string
string_with_AZeroB_orOneB = ["a", "ab", "Ab1", "1ab", "bAb", "!abbc", "abc", "acb", "access b string"]

#test string using match
for s4 in string_with_AZeroB_orOneB:
    if re.search(pattern4, s4):
        print(f"'{s4}' matches the string.")
    else:
        print(f"'{s4}' does not match the string.")


# ## Question 5- Write a RegEx pattern in python program that matches a string that has an a followed by three 'b'.

# In[156]:


#define pattern using {} with \b for maximum of 3b
pattern5 = r'ab{3}\b'

# Test the pattern with some example strings
string_with_a_followedby3b = ["abbb", "abb", "abbbb", "abc", "ac"]

for s5 in string_with_a_followedby3b:
    if re.match(pattern5, s5):
        print(f"'{s5}' matches the pattern.")
    else:
        print(f"'{s5}' does not match the pattern.")



# ## Question 6- Write a RegEx pattern in python program that matches a string that has an a followed by two to three 'b'.

# In[157]:


#define pattern using {} with \b for maximum of 3b
pattern6 = r'ab{2,3}\b'

# create a string
string_with_a_followedby2or3b = ["abbb", "abb", "abbbb", "abc", "ac"]

# Test the pattern with the example string
for s6 in string_with_a_followedby2or3b:
    if re.match(pattern6, s6):
        print(f"'{s6}' matches the pattern.")
    else:
        print(f"'{s6}' does not match the pattern.")


# ## Question 7- Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

# In[158]:


#define pattern using {} with  for anything ending in 'b'with $,
# *looks for a and b in the string
pattern7 = r'.*a.*b$'

# create a string
string_that_has_a_followedby_anything_endingb = ["a bib", "a bit", "the bib", "ab", "grab", "grade b", "ac"]

# Test the pattern with the example string
for s7 in string_that_has_a_followedby_anything_endingb:
    if re.match(pattern7, s7):
        print(f"'{s7}' matches the pattern.")
    else:
        print(f"'{s7}' does not match the pattern.")


# ## Question 8- Write a RegEx pattern in python program that matches a word at the beginning of a string.

# In[159]:


# Define the RegEx pattern for matching word at beginning of string ^\b
pattern8 = r"^{word}\b"
    
   
# create some example strings. 
match_word_beginningofstring = ["Hello", "goodbye", "see you again", "how are you", "see you soon"]

# define word 
word_to_match = "see"
for s8 in match_word_beginningofstring:
    if match_word_at_beginning(s8, word_to_match):
        print(f"'{s8}' starts with '{word_to_match}'.")
    else:
        print(f"'{s8}' does not start with '{word_to_match}'.")



# ## Question 9- Write a RegEx pattern in python program that matches a word at the end of a string.

# In[160]:


# Define the RegEx pattern for matching word at end of string $\b
pattern9 = r"${word}\b"
    
   
# some example strings. 
match_word_endofstring = ["Hello", "goodbye", "see you again", "how are you", "see you soon"]

# define word 
word_to_match = "you"

#create check
for s9 in match_word_endofstring:
    if match_word_at_end(s9, word_to_match):
        print(f"'{s9}' ends with '{word_to_match}'.")
    else:
        print(f"'{s9}' does not end with '{word_to_match}'.")







# ## Question 10- Write a RegEx pattern in python program to find all words that are 4 digits long in a string.
# ## Sample text- '01 0132 231875 1458 301 2725.'
# ## Expected output- ['0132', '1458', '2725']

# In[150]:


# Define the pattern for four digits words in a string, \b for boundaries, {4} for length of digits
pattern10 = r'\b\d{4}\b'

# now we use the sample text 
sample_text = '01 0132 231875 1458 301 2725 word play.'
    
# Find all matches in the text
matches = re.findall(pattern10, sample_text)
    

# Find four-digit words
result = find_four_digit_words(sample_text)
print("Expected output:", result)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




