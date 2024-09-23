from notification import EmailNotification, NotificationType, SmsNotification, WhatsAppSMS

class NotificationFactory:

    @staticmethod
    def create_notification(notification_type: NotificationType):
        if notification_type ==  NotificationType.EMAIL:
            return EmailNotification()
        if notification_type == NotificationType.SMS:
            return SmsNotification()
        if notification_type ==  NotificationType.WHA:
            return WhatsAppSMS()
        else:
            raise Exception("Not a valid type")