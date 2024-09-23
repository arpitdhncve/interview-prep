from room import RoomType, Room
from room_inventory import RoomInventory
from resservation import Reservation
from room_reservation_manager import RoomReservationManager


class Hotel:

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.room_inventory = {}
        self.rooms = {}
        self.room_reservation_managers = {}

    def add_room(self, room):
        self.rooms[room.roomNo] = room
        self.room_reservation_managers[room.roomNo] = RoomReservationManager(room.roomNo)


    def create_room_inventory(self, room_type, no_of_rooms, room_price):
        room_inventory = RoomInventory(self.id, room_type, no_of_rooms, room_price)
        self.room_inventory[room_type] = room_inventory

        for i in range(no_of_rooms):
            new_room_no = f"{room_type.value}_{i}"
            new_room = Room(self.id, new_room_no, room_inventory)
            room_inventory.add_room(new_room)
            self.add_room(new_room)                   

    
    def view_rooms(self):
        for room in self.rooms.values():
           print(f"room is {room.room_type()} and room number is {room.roomNo} and price is {room.get_price()}")

    
    def update_price(self, room_type, room_price):
        room_inventory = self.room_inventory[room_type]
        room_inventory.update_price(room_price)

    
    def create_reservation(self, room_no, amount_paid, checkin_date, checkout_date):
        room = self.rooms[room_no]

        with room.lock:
            if self.room_reservation_managers[room_no].check_availablity(checkin_date, checkout_date):
                total_days = (checkout_date - checkin_date).days
                total_amount = self.rooms[room_no].get_price()*total_days
                new_reservation = Reservation(self.id, room_no, total_amount, self.rooms[room_no].get_price(), amount_paid, checkin_date, checkout_date)
                room_reservation_manager = self.room_reservation_managers[room_no]
                room_reservation_manager.add_reservation(new_reservation)
                return new_reservation
            else:
                raise Exception("room not available")

            


    

    


