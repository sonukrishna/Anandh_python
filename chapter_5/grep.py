"""the grep command with use of generators """


def readfiles(filenames):
    for file in filenames:
	for line in open(file):
	    yield line
def greps(pattern,lines):
    return (line for line in lines if pattern in line)
def printlines(lines):
    for line in lines:
	print line
def len_lines(lines):
    a=[]
    for line in lines:
	a.append(line)
    return len(a)
def main(pattern,filenames):
    lines=readfiles(filenames)
    lines=greps(pattern,lines)
    printlines(lines)



