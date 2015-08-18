"""function make_slug that takes a name converts it into a slug
     A slug is A slug is a string where spaces and special characters are replaced by a hyphen, typically used to create blog post URL from post title """


import re
def make_slug(word):
    word1=re.findall('\w+',word)
    print word1
    word1="-".join(word1)
    print word1

make_slug('hello world')
make_slug('hello---world!!')
