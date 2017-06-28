"""
Written by :    Aditya Gaur
"""

print "Hello!"
# backslash for scaping characters
print ('what\'s up')

print "Let's get started"

# WE ARE GOING TO IMPORT THE spy_details FILE HERE
from spy_details import spy,Spy,friends,ChatMessage
from steganography.steganography import Steganography
from datetime import datetime


STATUS_MESSAGE = ['Status 1' , 'Class is ongoing' , 'Building a chat application']
#FUNCTION TO VALIDATE THE NAME FIELD
def name_valid(nme):
    # return True if valid name else False
    if nme.strip():     # strip() checks if the string is empty or not and then proceeds
        return True
    else:
        return False
#FUNCTION TO VALIDATE THE AGE FIELD
def age_valid(no):
    # return True if valid age else False
    if no > 12 and no <= 50:
        return True
    else:
        return False


# FUNCTION TO ADD A FRIEND
def add_friend():
    new_friend = Spy('','',0.00,0)
    print("\n Enter details of your new friend : ")
    new_friend.name = raw_input("\nEnter the name of your friend : ")
    new_friend.salutation = raw_input("\nAre they Mr. or Ms.? : ")
    new_friend.age = int(raw_input("\nEnter their age : "))
    new_friend.rating = float(raw_input("\nEnter their rating : "))

    pass_name = new_friend.name
    pass_age = new_friend.age

    #checking for valid age and name
    if name_valid(pass_name) is True and age_valid(pass_age) is True :
        friends.append(new_friend)
        print("\nYour friend has been added.")
    else:
        print("\nWrong Entry!\tWe can't add the spy with the details you provided.")

    return len(friends)

# FUNCTION TO SELECT A FRIEND
def select_friend():
    try:
        print("\nChose one friend from the list below : ")
        a=0
        for friend in friends:
            print("\n%d. %s %s of age : %d and rating : %.2f.") %(a+1 , friend.salutation ,
                                                                   friend.name,friend.age,friend.rating)
            a += 1

        friend_selection = int(raw_input("\nEnter your choice : "))
        friend_selection -= 1
        if(len(friends) >= friend_selection):
            print("\nYou selected %s %s ") %(friends[friend_selection].salutation , friends[friend_selection].name)
        else:
            print("WRONG SELECTION! SELECT A VALID OPTION!")

        return (friend_selection)
    except ValueError:
        print("Please enter a correct value for the input!!")
        return (False)

# FUCNCTION TO SEND A MESSAGE
def send_message():
    try:
        friend_select = select_friend()
        if friend_select is not False:
            input_path = raw_input("Enter the full path of the image : ")
            output_path = raw_input("Enter path where you want to store the output image : ")
            text = raw_input("Enter secret text that you want to encode : ")
            if name_valid(text) is True:
                if len(text.split()) > 100 :
                    print ("You're speaking a lot, this is Intolerable!!\nYou're banished from the chat!!")
                    del friends[friend_select]
                else:
                    Steganography.encode(input_path , output_path , text)
                    # VARIABLE TO STORE THE DETAILS OF THE NEW CHAT DATA
                    new_chat = ChatMessage(text,True,0)
                    friends[friend_select].chats.append(new_chat)

                    print("Your secret image is ready !")
            else:
                print ("You haven't entered any secret message. Please try again!")

    except IOError:
        print("No such file or directory found!!\nEnter a valid path and try again!!")

#FUNCTION TO DECODE A MESSAGE
def read_message():
    try:
        sender = select_friend()
        if sender is not False:
            words_spoken = None
            orig_image = raw_input("Enter the full path of the image to be decoded: ")
            secret_text = Steganography.decode(orig_image)
            # TO STORE THE NO. OF WORDS SPOKEN BY A USER
            for word in friends[sender].chats:
                words_spoken = word.avg_words + len(secret_text.split())
            # VARIABLE TO STORE THE DETAILS OF THE NEW CHAT DATA
            new_chat = ChatMessage(secret_text,False,words_spoken)
            friends[sender].chats.append(new_chat)
            print("Your secret message has been decoded and saved!")


    except IOError:
        print("No such file or directory found!!\nEnter a valid path and try again!!")

# FUNCTION TO READ CHAT HISTORY FROM A FRIEND
def read_chat_history():
    read_from = select_friend()
    for i in friends[read_from].chats:
        if i.sent_by_me is True:
            print("\033[1;34m    [%s]   \033[1m    \033[1;31m   You said : \033[1m    \033[0;37;45m   %s  \033[0m")  %(i.time.strftime("%d %B %Y"),i.message)
        else:
            print("\033[1;34m   [%s]    \033[1m \033[1;31m  %s  said :    \033[1m  \033[0;37;45m   %s   \033[0m")  %(i.time.strftime("%d %B %Y"),friends[read_from].name,i.message)


# FUNCTION TO SET A STATUS MESSAGE
def add_status():
    updated_status_message = None
    if spy.current_status_message!=None:
        print("\nYour current status message is :%s") %(spy.current_status_message)
    else:
        print("\nYou don't have any status message set.")

    choice = raw_input("Do you want to proceed with the current status message or you want to change it? (Y/N) : ")
    if choice.upper() == 'Y':
        STATUS_MESSAGE.append(spy.current_status_message)
        updated_status_message = spy.current_status_message
    elif choice.upper() == 'N':
        default = raw_input("\nDo you want to select a status message from older status messages? (Y/N): ")
        if default.upper() == 'Y':

            print("\nChoose one of the status from the list below : ")
            for i in range(len(STATUS_MESSAGE)):
                print(str(i + 1) + ". " + STATUS_MESSAGE[i] + "\n")
            select_message = int(raw_input("Enter your choice : "))

            if len(STATUS_MESSAGE) >= select_message:
                select_message -= 1
                updated_status_message = STATUS_MESSAGE[select_message]
            else:
                print("\nKindly select a valid input!")


        elif default.upper() == 'N':
            get_message = raw_input("\nEnter your status message : ")
            STATUS_MESSAGE.append(get_message)
            updated_status_message = get_message


        else:
            print('\n WRONG CHOICE INPUT! \n KINDLY SELECT Y/N')



    else:
        print("\nWRONG CHOICE INPUT! \n KINDLY SELECT Y/N")

    if updated_status_message != None:

        print("\nYour current status message is : %s") % (updated_status_message)
    else:
        print("\nYou currently don't have any status message set.")

# CREATING A FUNCTION TO USE IT AGAIN AND AGAIN THAT PERFORMS OUR MAIN OPERATN

# MAIN FUNCTION TO START THE CHAT
def start_chat(spy):
    spy.current_status_message = None

    spy.name = spy.salutation+" "+spy.name
    if spy.age > 12 and spy.age < 50:
        print "Authentication complete. Welcome " + spy.name + " age: " + str(spy.name) + " and rating of: " + str(
            spy.rating) + " Proud to have you onboard"

        show_menu = True
        try:
            while show_menu:
                menu_choice = raw_input("\nWhat do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n")
                if name_valid(menu_choice) is True:
                    menu_choice = int(menu_choice)
                    if menu_choice == 1:
                        print("You chose to update the status.")
                        add_status()
                    elif menu_choice == 2:
                        no_of_friends = add_friend()
                        print("\nYou've %d number of friends in total.") %(no_of_friends)
                    elif menu_choice == 3:
                        send_message()
                    elif menu_choice == 4:
                        read_message()
                    elif menu_choice == 5:
                        read_chat_history()

                    elif menu_choice == 6:
                        show_menu = False
                    else:
                        print("Invalid choice input!")
                        show_menu = False
        except ValueError:
            print("Please enter a correct value for the input!!")

    else:
        print("Sorry! You are not of corect age to be a spy, come back later!! ")




# CONDITION TO CHECK IF THE USER WANTS TO CONTINUE WITH DEFAULT SPY OR WANT TO CREATE NEW

question = raw_input(('Do you want to continue as ') + spy.salutation+" "+spy.name + ('( Y/N: ?)'))

if question.upper() == 'Y':
    start_chat(spy)

elif question.upper() == 'N':
    spy = Spy('','',0.00,0)

    # taking input from user and storing into variable
    spy.name=raw_input("Welcome to spy chat, you must tell me your spy name first:")

    if name_valid(spy.name) is True:
        spy.salutation = raw_input("What should we call you (Mr. or Mrs.)")
        # string updation
        spy.name = spy.salutation + " " + spy.name
        # string concatenation
        print("Welcome "+spy.name+" to SpyChat")
        # HERE WE CONVERTED THE INPUT INTO int SINCE BY DEFAULT raw_input GIVES STRING

        spy.age = int(raw_input("Enter the age of your spy :"))
        if age_valid(spy.age) is True:
            spy.rating = float(raw_input("Enter Spy Rating :"))
            if spy.rating > 4.7:
                print("You are an elite, Welcome Master!")
            elif spy.rating > 3.5 and spy.rating <= 4.5:
                print("You are good, Welcome !")
            elif spy.rating > 2.5 and spy.rating <= 3.5:
                print("You can always do better, Welcome!")
            else:
                print("You can help others in the office, Welcome!")

            spy.is_online = True
            print 'Authentication completed! Welcome ' +spy.name + " age:" + str(spy.age) + " with Rating :" + str(spy.rating)
            start_chat(spy)
        else:
            print("Sorry!! You are not eligible to be a spy kiddo!")
    else:
        print('Invalid Input!!')

else:
    print("Please provide a valid input (Y/N)")

