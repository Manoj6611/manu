import string
def remove_punctuation(phrase):
 phrase_without_punct = ""
 for letter in phrase:
  if letter not in string.punctuation:
   phrase_without_punct += letter
 return phrase_without_punct
my_story = """India is my country, all Indians are my "brothers and sisters"; I love my country!"""
result=remove_punctuation(my_story)
print("Phrase without punctuations:\n" + result)
words = result.split()
print("\n List of words in the phrase:\n", words)