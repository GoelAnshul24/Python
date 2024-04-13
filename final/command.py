command=input("Enter Command : ")
command=command.upper()
if(command=="START"):
    print("Starting the car")
elif(command=="STOP"):
    print("Stopping the car")
elif(command=="QUIT"):
    print("Exiting")
elif(command=="HELP"):
    print("Help")
else:
    print("Wrong Command")