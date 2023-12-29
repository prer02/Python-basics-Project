#!/usr/bin/env python
# coding: utf-8

# # Python (Basics) Project:-

# In[ ]:


You are working in a bank, and you have been given two lists of the employees who worked in 2021.
Employees’ names in list 1 are Ramesh, Suresh, Mahesh, Ali, Jacob, and Saritha. List 2 contains the names of Ali, Mukesh, Mahesh, Jacob, Sai, and Sarita. Please write a program that helps to identify people who are common in both lists. 
Please do not use any in-built function. 


# In[ ]:


list1=["Ramesh","Suresh","Mahesh","Ali","JAcob","Saritha"]
list2=["Ali","Mukesh","Mahesh","Jacob","Sai","Saritha"]
for i in list1:
     if i in list2:
            print(i)





# In[ ]:


Q2. While entering data, someone entered a few names as a common string “Ramesh Suresh Mohit”.
    Please write a program which separates all the names and converts them into a list.
    Once converted into a list, please write a program that adds their age. 
Ramesh:  25
Suresh: 22
Mohit: 26


# In[5]:


inputs=input("Enter the names:")
list1=list(inputs.split())
list2=[25,22,26]
added_age=list(zip(list1,list2))
for i in added_age:
    print(i[0],":",i[1])
    


# In[ ]:


Q3. You are working in a medical store. A patient came to your medical store and asked to buy 2 strips of paracetamol, 
   3 strips of azithromycin, and 5 strips of Vitamin C. One strip of paracetamol costs Rs 35,
   one strip of azithromycin costs Rs 49, and one strip of vitamin c costs Rs. 33.
   Patient gave you Rs 2000. Please tell us what is the total cost of each medicine, 
   the total cost of all medicine, and how much money you refunded to the patient.  


# In[2]:


dict11={"paracetamol":35,"azithromycin": 49,"vitamin c": 33}
dist12={"paracetamol":2, "azithromycin":3,"vitamin c":5} 
cost=0
for i,j in dict11.items():
     for k,l in dist12.items():
            if i==k:
                cost=cost+j*l
     print(f" The cost of each medicine {cost}")   
print(f"The total cost of each medicine is {cost}")    
print(f"Money refunded to the patient is {2000-cost}")            


# In[ ]:


Q4: Accept a sentence as input and find the number of vowels in it. Assume that the sentence has no punctuation marks.
    For example, I am learning python contains 6 vowels.
    This function should be applicable for all other different sentences.



# In[6]:


ss=input("enter the string")
count=0
vowels=["a","e","i","o","u"]
for i in ss:
    if i in vowels:
        count=count+1
print(count)        
        


# In[ ]:


Q5: You have been appointed by the election commission to create a website.
    Your first task is to work on a program which tells candidates if they are eligible for voting or not. 
    If they are eligible, your output should be ‘Congrats! You are eligible’; otherwise, 
    it should tell that you have to return after X number of years.
    The eligibility criteria for voting is 18 years. 



# In[9]:


def www(ss):

 if ss>=18:
        print("Congrats! You are eligible")
 else: 
    print(f"come after {18-ss} years")


# In[14]:


ss=filter(www,[2,3,12,56,67,18])
print(list(ss))


# In[ ]:


Q6. Given a list of integers, find the cumulative sum of the elements of the list and store them in another list.
A = [1, 2, 3, 4, 5]
Output: 
[1, 3, 6, 10, 15]


# In[32]:


ss=[]
A = [1, 2, 3, 4, 5]
count=0
for i in A:
    count=count+i
    ss.append(count)
print(ss)    


# In[ ]:


Q7. Write a program to implement run length encoding of a string
RLE:Consecutive repetition of a character has to be replaced with the count of occurrences and the character.
Enter your string :aabbbccdddae
Encoded: 2a3b2c3d1a1e


# In[33]:


def run_length_encode(input_string):
    encoded_string = ""
    count = 1
    
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            encoded_string += str(count) + input_string[i - 1]
            count = 1
    
    encoded_string += str(count) + input_string[-1]
    
    return encoded_string

input_string = input("Enter your string: ")
encoded_result = run_length_encode(input_string)
print("Encoded:", encoded_result)


# In[ ]:


Q8. WAP to encode a message entered by user as per below conditions:

for every word in the sentence, 

1. If the word starts with a vowel, encode it as the first and last letter of the word.

2. If the word starts with a consonant, remove all vowels from it.

Ensure the case insensitive comparisons/checks are performed.
Please enter your text:The quick brown fox used to sleep inside this box
Encoded Msg: Th qck brwn fx ud t slp ie ths bx


# In[ ]:


def encode_message(input_text):
    vowels = "AEIOUaeiou"
    words = input_text.split()
    encoded_words = []

    for word in words:
        if word[0] in vowels:
            encoded_word = word[0] + word[-1]
        else:
            encoded_word = ''.join([char for char in word if char not in vowels])
        
        encoded_words.append(encoded_word)

    encoded_msg = ' '.join(encoded_words)
    return encoded_msg

user_input = input("Please enter your text: ")
encoded_message = encode_message(user_input)
print("Encoded Msg:", encoded_message)









# In[4]:


def aas(n):
   if n==0:
      return "Go!"
   else:
      print(n)
      return aas(n-1)
result=aas(10) 
print(result)
      


# In[ ]:


Write a Python function that takes a string of text and returns a dictionary containing the frequency of each word in the text.
The function should ignore case and punctuation.
Note:Give in the input in the code
Input:Welcome to OdinSchool
Output:{'welcome': 1, 'to': 1, 'odinschool': 1} 


# In[ ]:


def word_frequency(text):
    # Initialize an empty dictionary to store word frequencies.
    word_freq = {}
    
    # Convert the input text to lowercase and remove punctuation.
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.lower().translate(translator)
    
    # Split the cleaned text into words.
    words = cleaned_text.split()
    
    # Count the frequency of each word and update the dictionary.
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    return word_freq

# Test the function with your input.
input_text = "Welcome to OdinSchool"
result = word_frequency(input_text)
print(result)


# In[30]:


import string

def count_word_frequency(text):
    # Initialize an empty dictionary to store word frequencies
    word_frequency = {}
    
    # Split the text into words and process each word
    words = text.split()
    
    for word in words:
        # Remove punctuation and convert to lowercase
        cleaned_word = word.strip(string.punctuation).lower()
        
        # Update the word frequency dictionary
        if cleaned_word in word_frequency:
            word_frequency[cleaned_word] += 1
        else:
            word_frequency[cleaned_word] = 1
    
    print(word_frequency)

# Example usage
text = "Welcome to OdinSchool"
result = count_word_frequency(text)
print(result)





# In[ ]:




