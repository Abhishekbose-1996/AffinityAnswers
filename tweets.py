#function to count the no. of words in a sentence
def count_dict(s):    # accepts a string 
  lis = s.split(' ')  #converting the string into a list where each word is an element
  d = {}
  for i in lis:
    if i in dict.keys():
      d[i] += 1
    else:
      d[i] = 1
  return d            # returning a dictionary where keys are words and values are word count


'''Considering the file containing the tweets as xyz.txt and every newline contains a new tweet'''
f = open('xyz.txt', 'r')
tweets = f.readlines() # extracting the data from the file and converting it into a list
'''Let the file containg the racial slurs as rac_slr.txt'''
e = open('rac_slr.txt', 'r')
racial_slurs = e.readlines() # creating a list of all the set of words 
d = {}
for i in len(tweets):
  d[i] = count_dict(tweets[i])
  for j in d[i].keys():
    racial_count = 0
    word_count = 0
    if j in racial_slurs:
      racial_count += d[i][j]     # counting racial slur words in a tweet  
    word_count += d[i][j]         # counting total number of words in a tweet
  d[i] = (racial_count/word_count)*100  # calculating the percentage of racial words in a tweet

for i in d.keys():
  print(f' tweet No. {i} contains {d[i]}% racial slurs') # printing percentage of profanity in each tweet
