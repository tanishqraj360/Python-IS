import random
response=["It is certain",
        "Outlook good",
        "You may rely on it",
        "Ask again later",
        "Concentrate and ask again",
        "Reply hazy, try again",
        "My reply is no",
        "My sources say no"]
choice=input("Press 'any key' for answer or 'quit' to exit.\n Enter your question.\n")
while choice!='quit':
    print(response[random.randint(0,8)])
    choice=input("Press 'any key' for answer or 'quit' to exit.\n Enter your question.\n")
print('Closing Program.')
quit()
