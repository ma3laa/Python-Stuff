#Mail Merging

#Sending emails but only the name changes

#Using "with" you get better syntax and exceptions handling
#In addition, it will automatically close the file

#x = open("Hello.txt", "w")
#y = x.read()
#print(y)
#x.close()


#with open("Hello.txt", "w") as file:
#    file.write("Hey there!")


#with open("Hello.txt", "w") as file:
#    file.write("Hey there!")

#x = open("Hello.txt", "r")
#print(x.read())



with open("Names.txt", "r") as n_file:
    with open("Messages.txt", "r") as m_file:

        body = m_file.read()
        for name in n_file:

            mail = "Hello " + name + "\n" +  body
            with open(name.strip()+".txt","w") as m_file:
                m_file.write(mail)




