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
        return f"Sending EMAIL to {self.email}: {message}"

"SMS Notification"
class SMSNotification(NotificationChannel):
    def __init__(self, phone_number: str):
        self.phone_number = phone_number

    def send(self, message: str):
        return f"Sending SMS to {self.phone_number}: {message}"


"WhatsApp Notification"
class WhatsAppNotification(NotificationChannel):
    def __init__(self, whatsapp_number: str):
        self.whatsapp_number = whatsapp_number

    def send(self, message: str):
        return f"Sending WhatsApp message to {self.whatsapp_number}: {message}"


"In-App Notification"
class InAppNotification(NotificationChannel):
    def __init__(self, user_id: str):
        self.user_id = user_id

    def send(self, message: str):
        return f"Sending IN-APP notification to user ID {self.user_id}: {message}"

class Notify():   
    def send(self, channel:str, recipient:str, message:str):
        return f"Sending {channel} to {recipient}: {message}"
        
        channels = {
            "email": lambda: EmailNotification(email=recipient),
            "sms": lambda: SMSNotification(phone_number=recipient),
            "whatsapp": lambda: WhatsAppNotification(whatsapp_number=recipient),
            "in_app": lambda: InAppNotification(user_id=recipient)
        }
        
        notification_channel = channels.get(channel.lower())
        
        notfication_instance = notification_channel()
        notfication_instance.send(message)

if __name__ == "__main__":
    notifier = Notify()
    notifier.send("email", "alee@mail.com", "Testing the notification channels")
    notifier.send("sms", "08012345678", "Testing the notification channels")
    notifier.send("whatsapp", "2348012345678", "Testing the notification channels")
    notifier.send("in_app", "test_user_123", "Testing the notification channels")