'''	mutation is defined as inserting a character, deleting a character, replacing a character, or swapping 2 consecutive characters in a string	'''


def  insert(word):
    "inserting alphabets to the given word"
    res=[]
    res1=[]
    word1=[word[i] for i in range(len(word))]
    alpha='abcdefghijklmnopqrstuvwxyz'
    alpha1=[alpha[i] for i in range(len(alpha))]
   # print alpha1
    for i in alpha1:
	for j in range(len(word1)+1):
	    res.extend(word1)
	    res.insert(j,i)
    	    word2="".join(res)
	    res1.append(word2)
	    res=[]
    return res1
def delete(word):
    "inserting characters from the given word,and print new words"
    res=[]
    res1=[]
    word1=[word[i] for i in range(len(word))]
    #print word1
    for i in range(len(word1)):
        res.extend(word1)
        del word1[i]
	word3="".join(word1)
	res1.append(word3)
	word1=res
	res=[]
    return res1
def remove(word):
    "remove a character from a word and insert an alphabet"
    res=[]
    res1=[]
    word1=[word[i] for i in range(len(word))]
    alpha='abcdefghijklmnopqrstuvwxyz'
    alpha1=[alpha[i] for i in range(len(alpha))]
    for i in alpha1:
	for j in range(len(word1)):
	    res.extend(word1)
	    del res[j]
	    res.insert(j,i)
	    word2="".join(res)
	    res1.append(word2)
	    res=[] 
    return res1
def swap(word):
    "swap two adjacent characters"
    res=[]
    res1=[]
    word1=[word[i] for i in range(len(word))]
    for i in range(len(word1)):
	if i!=len(word1)-1:
	    res.extend(word1)
	    res[i],res[i+1]=res[i+1],res[i]
	    word2="".join(res)
	    res1.append(word2)
	    res=[]
    return res1
def mutate(word):
    return  (insert(word)+delete(word)+remove(word)+swap(word))
   # return aa 
   # return aa
  #  print delete(word)+
  #  print remove(word)+ 
   # print swap(word)

print mutate('anu')
def check_mutate(f,words,word):
    aa=f(words)
    if word in aa:
	return True
    else:
	return False
	   
#print insert('sonu')
print check_mutate(mutate,'sonu','nnn')	    
#print swapping('hello')
