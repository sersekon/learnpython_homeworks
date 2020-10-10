#with open('text.txt', 'a', encoding='utf-8') as myfile:
 #   myfile.write('\twithout snowing')


#with open('text.txt', 'r', encoding='utf-8') as myfile:
#    content = myfile.read()
#    print(content)

    #for ln in myfile:
        #ln = ln.upper()
        #ln = ln.replace("\n", "")
        #print(ln)


with open('referat.txt', 'r', encoding='utf-8') as hmfile:
    text = hmfile.read()
    text = len(text)
    for words in hmfile:
        words = str(hmfile)
        print(len(words.split()))
    for points in hmfile:
        points = points.replace(".", "!")
        print(points)
       
    #content = str(hmfile.readlines())
   # print(len(content.split())

