import aiml

k = aiml.Kernel()
k.learn("learning_file_list.aiml")
k.respond("LEARN AIML")

while True:
    reply = k.respond(input("User > "))
    if reply:
        print("bot > ", reply)
    else:
        print("bot > :) ", )


