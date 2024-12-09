f1= open('the.txt', 'a+ ')
f2= open('the.txt','r')

f1.write(f2.read())

f1.seek(0)
f2.seek(0)

f1.close()
f2.close()