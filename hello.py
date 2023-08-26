class AirplaneReservationSystem:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.seats = [[False] * cols for _ in range(rows)]

    def display_seats(self):
        print("Available seats:")
        for row in range(self.rows):
            for col in range(self.cols):
                if self.seats[row][col]:
                    print("X", end=" ")
                else:
                    print("O", end=" ")
            print()

    def reserve_seat(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            if not self.seats[row][col]:
                self.seats[row][col] = True
                print(f"Seat [{row + 1}][{col + 1}] reserved successfully.")
            else:
                print("Seat already reserved.")
        else:
            print("Invalid row or column.")

def main():
    rows = 5
    cols = 4
    airplane_system = AirplaneReservationSystem(rows, cols)

    while True:
        print("\n1. Display Available Seats")
        print("2. Reserve a Seat")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            airplane_system.display_seats()
        elif choice == "2":
            row = int(input("Enter row number: ")) - 1
            col = int(input("Enter column number: ")) - 1
            airplane_system.reserve_seat(row, col)
        elif choice == "3":
            print("Exiting the reservation system.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
      
