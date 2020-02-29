f = open('pic.jpeg','rb')
f1= open('pic2.jpeg','wb')
for i in f:
    f1.write(i)