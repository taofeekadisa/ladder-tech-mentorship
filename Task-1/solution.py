from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


"Email Notification"
class EmailNotification(NotificationChannel):
    def __init__(self, email: str):
        self.email = email
    
    def send(self, message: str):
        print(f"Sending EMAIL to {self.email}: {message}")

"SMS Notification"
class SMSNotification(NotificationChannel):
    def __init__(self, phone_number: str):
        self.phone_number = phone_number

    def send(self, message: str):
        print(f"Sending SMS to {self.phone_number}: {message}")


"WhatsApp Notification"
class WhatsAppNotification(NotificationChannel):
    def __init__(self, whatsapp_number: str):
        self.whatsapp_number = whatsapp_number

    def send(self, message: str):
        print(f"Sending WhatsApp message to {self.whatsapp_number}: {message}")


"In-App Notification"
class InAppNotification(NotificationChannel):
    def __init__(self, user_id: str):
        self.user_id = user_id

    def send(self, message: str):
        print(f"Sending IN-APP notification to user ID {self.user_id}: {message}")



if __name__ == "__main__":
    email = EmailNotification(email="john@example.com")
    sms = SMSNotification(phone_number="08012345678")
    whatsapp = WhatsAppNotification(whatsapp_number="2348012345678")
    in_app = InAppNotification(user_id="user_123")
    
    message = "Testing the notification channels"

    email.send(message)
    sms.send(message)
    whatsapp.send(message)
    in_app.send(message)