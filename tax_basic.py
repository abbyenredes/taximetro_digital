import time

class Taximeter:
    RATE_IDLE = 0.02  
    RATE_MOVING = 0.05  
    
    def __init__(self):
        self.total = 0.0
        self.in_trip = False
        self.start_time = None
        self.state = "idle"

    def start_trip(self):
        print("\nStarting a new trip...")
        self.total = 0.0
        self.in_trip = True
        self.start_time = time.time()
        self.state = "idle"
        self.trip_menu()

    def change_state(self, new_state):
        if not self.in_trip:
            print("There is no ongoing trip.")
            return
        
        elapsed_time = time.time() - self.start_time
        if self.state == "idle":
            self.total += elapsed_time * self.RATE_IDLE
        else:
            self.total += elapsed_time * self.RATE_MOVING
        
        self.state = new_state
        self.start_time = time.time()
        print(f"\033[92mThe taxi is now {self.state}. \033[0;m")
    
    def end_trip(self):
        if not self.in_trip:
            print("There is no ongoing trip.")
            return
        
        elapsed_time = time.time() - self.start_time
        if self.state == "idle":
            self.total += elapsed_time * self.RATE_IDLE
        else:
            self.total += elapsed_time * self.RATE_MOVING
        
        self.in_trip = False
        print(f"\033[95m\nTrip ended. Total fare: €{self.total:.2f}\n \033[0;m")
    
    def trip_menu(self):
        while self.in_trip:
            print("\033[93m\nOptions: ")
            print("1 - Change to MOVING")
            print("2 - Change to IDLE")
            print("3 - End trip \033[0;m")
            option = input("Select an option: ")
            
            if option == "1":
                self.change_state("moving")
            elif option == "2":
                self.change_state("idle")
            elif option == "3":
                self.end_trip()
            else:
                print("Invalid option. Try again.")


def main():
    print ("\033[96m")
    print('*' * 50)
    print('*' *10 + " Welcome to digital taximeter " + '*' * 10)
    print('*' * 50)
    print("\033[0;m")
    taximeter = Taximeter()
    
    while True:
        option = input("\nDo you want to start a new trip? (y/n): ")
        if option.lower() == "y":
            taximeter.start_trip()
        elif option.lower() == "n":
            print("\033[91m Exiting the program... \033[0;m")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()