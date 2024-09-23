

class RoomReservationManager:

    def __init__(self, room_no):
        self.room = room_no
        self.reservations = []
    
    def add_reservation(self, reservation):
        self.reservations.append(reservation)

    def check_availablity(self, checkin_date, checkout_date):
        for reservation in self.reservations:
            if reservation.checkin_date < checkout_date or reservation.checkout_date > checkin_date:
                return False
            else:
                return True
        
        return True