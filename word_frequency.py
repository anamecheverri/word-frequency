
def word_frequency(texto):
    bad_chars=".,;:/?><!@#$%^&*()_-+\"\'"
    for bad in bad_chars:
        texto=texto.replace(bad," ").lower()
        result={}
    mylist=texto.split()
    for word in mylist:
        if word in result:
          result[word] +=1
        else:
          result[word]=1
    return result



def top_20(mydict):
    top20=sorted(mydict.items(),
          key=lambda frequency: frequency[1],reverse=True)[0:20]
    print("The 20 most frequently used words are:")
    for mytuple in top20:
        print(mytuple[0],mytuple[1])
    


myfile = open("sample.txt")
myfile_content = myfile.read()
final_dict = word_frequency(myfile_content)
top_20(final_dict)
