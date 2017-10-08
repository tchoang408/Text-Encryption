#Tam Hoang
# this program encrypting a sentence or words using vigenerr
# cypher. 

from string import*

def createVigenereTable(keyword):
    vigenereTable = []
    alphabetList = []
    keywordList = []
    alphabet = ascii_lowercase   
    for i in range(len(alphabet)):
        alphabetList.append(alphabet[i]) 
             
    index = 0
    for i in range(len(keyword)):
        tempList = list(alphabetList)
        while(alphabetList[index] != keyword[i]):
            tempList.append(tempList[0])
            tempList.pop(0)
            index += 1    
        index = 0       
        keywordList.append(tempList)
                 
    vigenereTable.append(alphabetList)
    for i in range (len(keyword)):
        vigenereTable.append(keywordList[i])
       

    return vigenereTable
 
def encryption():
    keyword = input("Please enter your keyword to encrypt a message: ") 
    table = createVigenereTable(keyword)
    text =  input("Please enter a message for encryption: ") 
    counter = 1
    encryptedCode =''
    for i in range(len(text)):
        if(counter >= len(table)):
            counter = 1
        index = table[0].index(text[i])
        letter = table[counter][index]
        counter += 1
        encryptedCode += letter
    return encryptedCode

def decryption():
    encryptedText = input("Please enter the encrypted message for decryption: ")  
    keyword = input("Please enter your keyword to decrypt a message: ")
    message = ''
    vigTable = createVigenereTable(keyword)
    ele = 1 

    for i in range(len(encryptedText)):
        if ele == len(vigTable):
            ele = 1
        index = vigTable[ele].index(encryptedText[i])
        ele += 1
        message += vigTable[0][index]
      
    return message
    
    
cont =1    
while(cont):
    print("     Please enter a choice\n\n")
    print("Press 1:            Encrypt a message\n"
          "Press 2:            Decrypt a message\n"
          "Press 3:            Quit")
    
    choice = int(input("Enter your choice: "))
    if (choice == 1):
        encryptedText = encryption()  
        print("The encrypted messages: %s\n\n" % (encryptedText))
    elif choice == 2:
        decryptedMess = decryption()    
        print("The decrypted messages: %s\n\n" % (decryptedMess)) 
    else:
        cont = 0

