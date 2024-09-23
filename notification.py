from enum import Enum
from abc import ABC, abstractmethod

class NotificationType(Enum):
    EMAIL = 1
    SMS = 2
    WHA = 3



class Notification(ABC):

    @abstractmethod
    def send(self, recipient, message):
        pass
        


class EmailNotification(Notification):

    def send(self, recipient, message):
        print(f"Send Email to {recipient} and message is {message}")


class SmsNotification(Notification):

    def send(self, recipient, message):
        print(f"send sms to {recipient} and {message}")


class WhatsAppSMS(Notification):

    def send(self, recipient, whatsapp_message):
        print(f"send sms to {recipient} and {whatsapp_message}")

