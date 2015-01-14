import sys

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

def print_histogram(tuple_list):
    maxvalue=tuple_list[0][1]
    for mytuple in tuple_list:
        word20=mytuple[0]
        freq=((mytuple[1]*50)//maxvalue)*"#"
        print("{:15}  {}".format(word20,freq))


def top_20(mydict):
    top20=sorted(mydict.items(),
          key=lambda frequency: frequency[1],reverse=True)[0:20]
    print("The 20 most frequently used words are:")
    for mytuple in top20:
        print(mytuple[0],mytuple[1])
    print("Histogram for the top 20 words")
    print_histogram(top20)


file_name = sys.argv[1]
myfile = open(file_name)
myfile_content = myfile.read()
final_dict = word_frequency(myfile_content)
top_20(final_dict)
