from hotel import Hotel
from room import RoomType
from datetime import date
import threading

class HotelManagementDemo:

    @staticmethod
    def reserve_room_concurrently(hotel, room_no, amount_paid, checkin_date, checkout_date):
        """
        This method will attempt to reserve a room in the hotel concurrently in multiple threads.
        """
        try:
            reservation = hotel.create_reservation(room_no, amount_paid, checkin_date, checkout_date)
            print(f"Reservation successful for room {room_no}: Total Amount: {reservation.total_amount}, Paid: {reservation.amount_paid}")
        except Exception as e:
            print(f"Failed to reserve room {room_no}: {str(e)}")



    @staticmethod
    def run():


        hotel1 = Hotel("le mor", "1") 
        hotel1.create_room_inventory(RoomType.SINGLE, 5, 800)
        hotel1.create_room_inventory(RoomType.DOUBLE, 3, 1000)

        hotel1.view_rooms()

        checkin_date = date(24, 5, 1)
        checkout_date = date(24, 5, 3)

        checkin_date2 = date(24, 5, 2)

         # Creating two threads that will try to reserve the same room at the same time
        thread1 = threading.Thread(target=HotelManagementDemo.reserve_room_concurrently, args=(hotel1, "1_0", 0, checkin_date, checkout_date))
        thread2 = threading.Thread(target=HotelManagementDemo.reserve_room_concurrently, args=(hotel1, "1_0", 0, checkin_date2, checkout_date))


        # Creating another thread to reserve a different room at the same time
        thread3 = threading.Thread(target=HotelManagementDemo.reserve_room_concurrently, args=(hotel1, "1_1", 0, checkin_date, checkout_date))

        # Start all threads
        thread1.start()
        thread2.start()
        thread3.start()

        # Wait for all threads to finish
        thread1.join()
        thread2.join()
        thread3.join()

       
     



if __name__ == "__main__":
    HotelManagementDemo.run()
    