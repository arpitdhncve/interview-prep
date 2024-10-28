import hashlib
import bisect
from lib2to3.pgen2.token import NUMBER
from dotenv import load_dotenv
import os

load_dotenv()

NUMBERS = [
    "6001234567",
    "6012345678",
    "6023456789",
    "6034567890",
    "6045678901",
    "6056789012",
    "6067890123",
    "6078901234",
    "6089012345",
    "6090123456",
    "7001234567",
    "7012345678",
    "7023456789",
    "7034567890",
    "7045678901",
    "7056789012",
    "7067890123",
    "7078901234",
    "7089012345",
    "7090123456",
    "8001234567",
    "8012345678",
    "8023456789",
    "8034567890",
    "8045678901",
    "8056789012",
    "8067890123",
    "8078901234",
    "8089012345",
    "8090123456",
    "9001234567",
    "9012345678",
    "9023456789",
    "9034567890",
    "9045678901",
    "9056789012",
    "9067890123",
    "9078901234",
    "9089012345",
    "9090123456",
    "6101234567",
    "6112345678",
    "6123456789",
    "6134567890",
    "6145678901",
    "6156789012",
    "6167890123",
    "6178901234",
    "6189012345",
    "6190123456",
    "7101234567",
    "7112345678",
    "7123456789",
    "7134567890",
    "7145678901",
    "7156789012",
    "7167890123",
    "7178901234",
    "7189012345",
    "7190123456",
    "8101234567",
    "8112345678",
    "8123456789",
    "8134567890",
    "8145678901",
    "8156789012",
    "8167890123",
    "8178901234",
    "8189012345",
    "8190123456",
    "9101234567",
    "9112345678",
    "9123456789",
    "9134567890",
    "9145678901",
    "9156789012",
    "9167890123",
    "9178901234",
    "9189012345",
    "9190123456",
    "6201234567",
    "6212345678",
    "6223456789",
    "6234567890",
    "6245678901",
    "6256789012",
    "6267890123",
    "6278901234",
    "6289012345",
    "6290123456",
    "7201234567",
    "7212345678",
    "7223456789",
    "7234567890",
    "7245678901",
    "7256789012",
    "7267890123",
    "7278901234",
    "7289012345",
    "7290123456"
]





all_users = []





class ConsistentHashing:

    _instance = None


    def __new__(cls, whatsapp_number, virtual_nodes=10):
        if cls._instance is None:
            cls._instance = super(ConsistentHashing, cls).__new__(cls)
            cls._instance._initialize(whatsapp_number, virtual_nodes)
            print("class created")
        
        return cls._instance

    def _initialize(self, whatsapp_number, virtual_nodes):
        if hasattr(self, 'ring'):
            return

        self.whatsapp_number = whatsapp_number
        self.virtual_nodes = virtual_nodes
        self.ring = []
        self.hash_to_number = {}

        # Add each WhatsApp number with virtual nodes
        for number in whatsapp_number:
            for i in range(virtual_nodes):
                virtual_node_key = f"{number}#{i}"
                hash_value = self.hash_function(virtual_node_key)
                self.hash_to_number[hash_value] = number
                self.ring.append(hash_value)

        self.ring.sort()


    
    def hash_function(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), 16)

    
    def get_whatsapp_number(self, user_mobile):

        user_hash = self.hash_function(user_mobile)

        idx = bisect.bisect(self.ring, user_hash)

        if idx == len(self.ring):
            idx = 0

        return self.hash_to_number[self.ring[idx]]

    
    def add_new_number(self, new_number):
        for i in range(self.virtual_nodes):
            virtual_node_key = f"{new_number}#{i}"
            hash_value = self.hash_function(virtual_node_key)
            self.hash_to_number[hash_value] = new_number
            self.ring.append(hash_value)
        self.ring.sort()

    
    def remove_number(self, remove_number):
        self.ring = [hash for hash in self.ring if self.hash_to_number[hash]!= remove_number]
        self.hash_to_number = {hash_value:number for hash_value, number in self.hash_to_number.items() if number!= remove_number}

    







class User:

    def __init__(self, mobile, whatsapp_notification_number):
        self.mobile = mobile
        self.whatsapp_notification_number = whatsapp_notification_number
        self.numberChanged = False


def main():

    # Create a list of WhatsApp numbers
    whatsapp_numbers = [
    "8860107780",
    "9950247727",
    "9929995921",
    "9079650236",
    "7929995821"
]

    # Initialize Consistent Hashing with WhatsApp numbers
    hashing_object = ConsistentHashing(whatsapp_numbers)

    dict_count = {}
    # Register users and assign WhatsApp numbers
    for number in NUMBERS:
       whatsapp_number = hashing_object.get_whatsapp_number(number)
       user = User(number, whatsapp_number)
       all_users.append(user)
       if whatsapp_number not in dict_count:
           dict_count[whatsapp_number] = 0
       dict_count[whatsapp_number] += 1

    
    print(dict_count)
    
    for user in all_users:
        print(f"{user.mobile} and whatsapp number is {user.whatsapp_notification_number}")
        print("------")


    hashing_object.remove_number("8860107780")
    dict_count = {}
    total_number_changed = 0
    for user in all_users:
        new_whatsapp_number = hashing_object.get_whatsapp_number(user.mobile)
        if new_whatsapp_number != user.whatsapp_notification_number:
            user.whatsapp_notification_number = new_whatsapp_number
            user.numberChanged = True
            total_number_changed += 1

        if new_whatsapp_number not in dict_count:
            dict_count[new_whatsapp_number] = 1
        else:
            dict_count[new_whatsapp_number] += 1

    
    print(dict_count)
    print(total_number_changed)





       
  







if __name__ == "__main__":
    main()