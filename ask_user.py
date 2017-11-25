

def ask_user():
    print ("how r u? ")
    answer = input().lower()
    a = "fine"
    while a not in answer:
        ask_user()
        break
   
ask_user()

dialogue = {"how are you?" : "fine, tnks", "what's your name?" : "jenechka", "where are you from?" : "Russia"}

def get_answer():

    dialogue = {"how are you?" : "fine, tnks", "what's your name?" : "jenechka", "where are you from?" : "Russia"}
    print ("ask something simple ")
    statement = input().lower()
    while statement != "bye":
        
        try:
            print(dialogue [statement.lower()])
            print ("ask something simple ")
        except KeyError:
            print ("that's complicated, ask something simple ")
        
        
        statement = input().lower()
        
        if statement == "bye":
            print("see you!")
            break
    


get_answer()

def dialogue():
   
    try:
        ask_user()
    except KeyboardInterrupt:
        print ("uh-uh, that isn't working")
        ask_user()
    try:
        get_answer()
    except KeyboardInterrupt:
        print ("uh-uh, that isn't working")
        get_answer()
dialogue()
