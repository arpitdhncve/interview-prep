from enum import Enum
import threading

class RoomType(Enum):
    SINGLE = 1
    DOUBLE = 2
    DELUXE = 3
    SUITE = 4


class Room:

    def __init__(self, hotel_id, room_no, room_inventory):
        self.hotelId = hotel_id
        self.roomNo = room_no
        self.inventory = room_inventory
        self.reservations = []
        self.lock = threading.Lock()
    
    def get_price(self):
        return self.inventory.room_price

    def room_type(self):
        return self.inventory.room_type


