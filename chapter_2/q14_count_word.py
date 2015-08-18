def word_freq(word):
    freq={}
    for i in word:
	freq[i]=freq.get(i,0)+1
    return freq

def read_file(filename):
    return open(filename).read().split()
def print_word(filename):
    freq=word_freq(read_file(filename))
    for i,j in freq.items():
	print i,j

print print_word('she.txt')
