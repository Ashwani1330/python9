fh = open(r"/root/Documents/poem.txt", 'r')
a = fh.read()
count = 0
lsplit_to = a.split('to')
print("No of 'to' present in the file: ", len(lsplit_to)-1)

lsplit_the = a.split('the')
print("No of 'the' present in the file: ", len(lsplit_the) - 1)
print(lsplit_the)
