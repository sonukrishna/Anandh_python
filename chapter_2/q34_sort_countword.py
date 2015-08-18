
"""print the words in the descending order of the number of occurrences. """

def word_freq(word):
    freq={}
    for i in word:
        freq[i]=freq.get(i,0)+1
    return freq

def read_file(filename):
    ss=open(filename).read().split()
    print ss
    return ss
def words_in_file(filename):
    a=[]
    freq= word_freq(read_file(filename))
   # for i,j in freq.items():
   # return freq
    sort_val= sorted(freq.items(),key=lambda x:x[1],reverse=True)
    for i,j in sort_val:
        print i,j
words_in_file('she.txt')

