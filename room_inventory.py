class RoomInventory:

    def __init__(self, hotel_id, room_type, no_of_rooms, room_price):
        self.hotel_id = hotel_id
        self.room_type = room_type
        self.no_of_rooms = no_of_rooms
        self.room_price = room_price
        self.rooms = {}

    def add_room(self,room):
        self.rooms[room.roomNo] = room

    def update_price(self, price):
        self.room_price = price



