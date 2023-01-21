
class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password


class Bus:
    def __init__(self, coach, driver, arrival, departure, from_dest, to) -> None:
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_dest = from_dest
        self.to = to
        self.seat = ["Empty" for i in range(20)]


class PhitronCompany:
    total_bus = 5
    total_bus_list = []  # dummy database

    def install(self):
        bus_number = int(input("Enter bus number: "))
        flag = 1
        for bus in self.total_bus_list:  # checking kono bus already installed kina
            if bus_number == bus['coach']:
                print("Bus already installed")
                flag = 0
                break
        if flag:
            bus_driver = input("Enter bus driver name: ")
            bus_arrival = input("Enter arrival time: ")
            bus_departure = input("Bus departure time: ")
            bus_from = input("Enter bus start from: ")
            bus_to = input("Enter bus destination to: ")
            self.new_bus = Bus(bus_number, bus_driver,
                               bus_arrival, bus_departure, bus_from, bus_to)
            self.total_bus_list.append(vars(self.new_bus))
            print("\nBus installed successfully\n")


class BusCounter(PhitronCompany):
    user_lst = []  # user database
    bus_seat = 20

    def reservation(self):
        bus_no = int(input("Enter bus number: "))
        for bus in self.total_bus_list:
            if bus_no == bus['coach']:
                passenger = input("Enter your name: ")
                seat_no = int(input("Enter your seat number: "))
                if seat_no > self.bus_seat:  # maximum seat checking
                    print("Seat number crossed the limit")
                elif bus['seat'][seat_no - 1] != "Empty":  # checking not empty
                    print("Seat already booked")
                else:  # reserve the seat for the user
                    bus['seat'][seat_no - 1] = passenger
                    print("Seat booked successfully")
            else:
                print("No bus available in this number")
                break

    def showBusInfo(self):
        bus_number = int(input("Enter bus number: "))
        for bus in self.total_bus_list:
            if bus['coach'] == bus_number:
                print("*" * 50)
                print()
                print(f"{' '*10}{'#'*10} BUS INFO {'#'*10}")
                print(f"Bus No: {bus_number}\t\t Driver: {bus['driver']}")
                print(
                    f"Arrival: {bus['arrival']}\t\t Departure: {bus['departure']}")
                print(f"From: {bus['from_dest']}\t\t To: {bus['to']}")

                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                    print()

    def get_user(self):
        return self.user_lst

    def create_account(self):
        name = input("Enter your username: ")
        password = input("Enter your password: ")
        self.new_user = User(name, password)
        if self.new_user in self.get_user():
            print("User already exists")
            return
        self.user_lst.append(vars(self.new_user))
        print("Account created successfully")

    def available_buses(self):
        if (len(self.total_bus_list)) == 0:
            print("No bus available")
        else:
            for bus in self.total_bus_list:
                print("*" * 50)
                print()
                print(f"{' '*10}{'#'*10} BUS INFO {'#'*10}")
                print(f"Bus No: {bus['coach']}\t\t Driver: {bus['driver']}")
                print(
                    f"Arrival: {bus['arrival']}\t\t Departure: {bus['departure']}")
                print(f"From: {bus['from_dest']}\t\t To: {bus['to']}")

                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                    print()


while True:
    counter = BusCounter()
    print("1. Create an account\n2. Login to your account\n3.Exit")
    user_input = int(input("Enter your choice: "))
    if user_input == 3:
        break
    elif user_input == 1:
        counter.create_account()
    elif user_input == 2:
        name = input("Enter your name: ")
        password = input("Enter your password")
        isAdmin = False
        flag = 0
        if name == 'admin' and password == '1234':
            isAdmin = True
        if isAdmin == False:
            for user in counter.get_user():
                if user['username'] == name and user['password'] == password:
                    flag = 1
                    break
            if flag:
                while True:
                    print(
                        "1. Available buses\n2. Show bus info\n3. Reservation\n4. Exit")
                    a = int(input("Enter your choice: "))
                    if a == 1:
                        counter.available_buses()
                    elif a == 2:
                        counter.showBusInfo()
                    elif a == 3:
                        counter.reservation()
                    elif a == 4:
                        break
            else:
                print("Invalid username or password")

        else:
            while True:
                print("Hello Admin welcome back")
                print(
                    "1. Install Bus\n2. Check available buses\n3. Show Bus info\4. Show user List\n5. Exit")
                a = int(input("Enter choice: "))
                if a == 1:
                    counter.install()
                elif a == 2:
                    counter.available_buses()
                elif a == 3:
                    counter.showBusInfo()
                elif a == 4:
                    counter.get_user()
                elif a == 5:
                    break
