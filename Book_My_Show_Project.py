class BookMyShow:
    def __init__(self):
        # Initialize with some default data
        self.movies = {
            "Avatar": {"timing": "12:30 PM", "duration": "2h 45m", "languages": ["English", "Hindi", "Telugu"], "price": 200},
            "Inception": {"timing": "3:30 PM", "duration": "2h 30m", "languages": ["English", "Hindi"], "price": 250},
            "Bahubali": {"timing": "6:00 PM", "duration": "3h 10m", "languages": ["Telugu", "Hindi"], "price": 180}
        }
        self.snacks_menu = {"Popcorn": 50, "Soda": 30, "Nachos": 40}
        self.seats = {f"{row}{num}": None for row in "ABCDEFGH" for num in range(1, 37)}
        self.bookings = []

    def show_movies(self):
        print("\nAvailable Movies:")
        for movie in self.movies:
            print(f"{movie} - Timings: {self.movies[movie]['timing']} | Duration: {self.movies[movie]['duration']} | Price: Rs {self.movies[movie]['price']}")

    def choose_movie(self):
        movie = input("\nEnter the movie name you want to watch: ")
        if movie in self.movies:
            print(f"You selected {movie}. Timings: {self.movies[movie]['timing']}, Duration: {self.movies[movie]['duration']}, Price per ticket: Rs {self.movies[movie]['price']}")
            return movie
        else:
            print("Movie not found! Please choose a valid movie.")
            return None

    def select_seat(self):
        selected_seats = []
        while True:
            print("\nAvailable seats (rows A1-A36):")
            for seat, booked in self.seats.items():
                status = "Booked" if booked else "Available"
                print(f"{seat}: {status}", end=" | ")

            seat_choice = input("\nEnter your seat number (e.g., A1) or type 'done' to finish: ").strip().upper()

            if seat_choice == "DONE":
                break

            if seat_choice not in self.seats:
                print("Invalid seat selection. Please enter a seat in the format A1-A36.")
            elif self.seats[seat_choice] is not None:
                print(f"Seat {seat_choice} is already booked. Please choose another.")
            else:
                self.seats[seat_choice] = "Booked"
                selected_seats.append(seat_choice)
                print(f"Seat {seat_choice} successfully booked.")

        return selected_seats

    def select_snacks(self):
        print("\nSnacks Menu:")
        for snack, price in self.snacks_menu.items():
            print(f"{snack}: Rs {price}")
        snack_choice = input("Enter the snack you want: ")
        if snack_choice in self.snacks_menu:
            return snack_choice, self.snacks_menu[snack_choice]
        else:
            print("Snack not available.")
            return None, 0

    def make_payment(self, total_amount):
        print("\nPayment Options:\n1. UPI\n2. Debit Card\n3. Credit Card")
        option = input("Choose your payment option (1, 2, or 3): ")
        if option in ["1", "2", "3"]:
            print(f"Payment of Rs {total_amount} successful!")
            return True
        else:
            print("Invalid payment option.")
            return False

    def book_ticket(self):
        self.show_movies()
        movie = self.choose_movie()
        if movie is None:
            return

        seats = self.select_seat()
        if not seats:
            return

        snack, snack_price = self.select_snacks()
        total_price = (self.movies[movie]['price'] * len(seats)) + snack_price
        print(f"\nTotal amount to pay: Rs {total_price}")

        if self.make_payment(total_price):
            self.bookings.append({
                "movie": movie,
                "seats": seats,
                "snack": snack,
                "price": total_price
            })
            print("Booking successful!\n")
        else:
            print("Booking failed due to payment error.")

    def view_bookings(self):
        print("\nYour Bookings:")
        if not self.bookings:
            print("No bookings found.")
        for idx, booking in enumerate(self.bookings, 1):
            seats = ", ".join(booking["seats"])
            print(f"Booking {idx}: Movie - {booking['movie']}, Seats - {seats}, Snack - {booking['snack']}, Total Paid - Rs {booking['price']}")


def main():
    app = BookMyShow()
    
    while True:
        print("\n--- Book My Show ---")
        print("1. View Bookings")
        print("2. Book a Ticket")
        print("3. Exit")
        print("4. Snacks")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            app.view_bookings()
        elif choice == "2":
            app.book_ticket()
        elif choice == "3":
            print("Exiting the application.")
        elif choice == "4":
            app.select_snacks()
            break
        else:
            print("Invalid option. Please choose a valid option.")

# Run the main function to start the program
main()
