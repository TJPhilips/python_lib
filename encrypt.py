result = ''
message = ''
choice = ''

while choice != 0:
 choice = raw_input("\nDo you wish to encrypt or decrypt?\nPlease enter '1' to encrypt and '2' to decrypt. ")
#Had to change to raw_input due to python verison 2
 if choice == '1':
      message = raw_input("\nEnter the message for encryption: ")
      for i in range(0, len(message)):
        result = result + chr(ord(message[i]) - 2)

        print(result + '\n\n')
        result = ''


 elif choice == '2':
        message = raw_input("\nEnter the message to decrypt: ")
        for i in range(0, len(message)):
           result = result + chr(ord(message[i]) + 2)

           print(result + '\n\n')
           result = ''

 elif choice != '0':
            print("This is an incorrect number, please try again using either '1' or '2'. \n\n")
