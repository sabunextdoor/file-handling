file=open('the.txt','r')
print(file.read())
file.close()

file=open('the.txt','w')
file.write("On the Sabbath day, we keep it holy")
file.close()

file=open('the.txt','a')
file.write("\n this is the next line")
file.close()