# -----------------------------
# Simple Car Simulator
# -----------------------------

command = ""
car_started = False

print("Welcome to the Car Simulator!")
print("Type 'help' to see available commands.\n")

while True:
    command = input("> ").lower()  # Read user input and convert to lowercase
    
    if command == "start":
        if car_started:
            print("The car is already started!")
        else:
            car_started = True
            print("Car started... Ready to go!")
            
    elif command == "stop":
        if not car_started:
            print("The car is already stopped! Start it first.")
        else:
            car_started = False
            print("Car stopped.")
            
    elif command == "help":
        print("""
Available commands:
  start - to start the car
  stop  - to stop the car
  quit  - to exit the program
        """)
        
    elif command == "quit":
        print("Exiting the Car Simulator. Goodbye!")
        break
        
    else:
        print("Invalid command. Type 'help' to see available commands.")
