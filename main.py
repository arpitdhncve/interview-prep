from notification_factory import NotificationFactory
from notification import NotificationType

class NotificationSystem:

    # implemented factory method in this
    # less changes required on client side
    @staticmethod
    def run():
        notification1 = NotificationFactory.create_notification(NotificationType.EMAIL)
        notification1.send("arpit", "padhai kar")

        notification2 = NotificationFactory.create_notification(NotificationType.SMS)
        notification2.send("july", "qwerty")

        notification3 = NotificationFactory.create_notification(NotificationType.WHA)
        notification3.send("agrawal", "let it be")


if __name__ == "__main__":
    NotificationSystem.run()