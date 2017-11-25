

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
    
    

    while True:

        try:
            print ("ask something simple ")
            statement = input().lower()
        except KeyboardInterrupt:
            print ("uh-uh, that isn't working")
            statement = None

        if statement == "bye":
            print("see you!")
            break
            
        try:
            if statement is not None:
                print(dialogue [statement.lower()])
                """print ("ask something simple ")"""
        except KeyError:
            print ("that's complicated")
        
        
    


get_answer()

def dialogue():
   
    try:
        ask_user()
    except KeyboardInterrupt:
        print ("uh-uh, that isn't working")
        ask_user()
    """try:
        get_answer()
    except KeyboardInterrupt:
        print ("uh-uh, that isn't working")"""
    get_answer()
dialogue()
