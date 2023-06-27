import string
def remove_punctuation(phrase):
    phrase_without_punctuation
    for letter in phrase:
        if letter not in string.punctuation:
            phrase_without_punctuation+=letter
            return phrase_without_punctuation
story=""""india is my country, all indians are my brothers and sisters!!!!"""
result=remove_punctuation(story)
print("phrase without punctuation",+result)
words=result.split()
print("list of words in the phrase",words)