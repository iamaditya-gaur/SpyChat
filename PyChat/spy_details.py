from datetime import datetime

# CLASS SPY WHICH CONTATINS ALL THE DETIALS OF THE SPY
class Spy:
    def __init__(self,name,salutation,rating,age):
        self.name = name
        self.salutation = salutation
        self.rating = rating
        self.age = age
        self.chats = []
        self.is_online = True
        self.current_status_message = None

# CLASS TO STORE THE CHATS
class ChatMessage:
    def __init__(self,message,sent_by_me,avg_words):
        self.message = message
        self.sent_by_me = sent_by_me
        self.time = datetime.now()
        if avg_words is not 0:
            self.avg_words = avg_words
        else:
            self.avg_words = 0
spy = Spy('Bond' , 'Mr.' , 4.7,39)

friend_one = Spy('Raja', 'Mr.', 4.9, 27)
friend_two = Spy('Mata Hari', 'Ms.', 4.39, 21)
friend_three = Spy('No', 'Dr.', 4.95, 37)
friends = [friend_one, friend_two, friend_three]
