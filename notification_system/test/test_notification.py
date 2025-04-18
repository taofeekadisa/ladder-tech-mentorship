import pytest # type: ignore
import notification_system.notification as notification

class TestNoficationChannel:
    def test_send(self):
        pass
    
@pytest.fixture
def message():
    return "Testing the notification channels"

"Email Notification Test"
class TestEmailNotification:
    def setup_method(self):
        self.email = notification.EmailNotification("alee@mail.com")
        
        
    def test_send(self, message):
        assert self.email.send(message) == f"Sending EMAIL to alee@mail.com: {message}"
        

"WhatsApp Notification Test"        
class TestWhatsAppNotification:
    def setup_method(self):
        self.whatsapp = notification.WhatsAppNotification("2348012345678")
        
        
    def test_send(self, message):
        assert self.whatsapp.send(message) == f"Sending WhatsApp message to 2348012345678: {message}"
        

"SMS Notification Test"  
class TestSMSNotification:
    def setup_method(self):
        self.sms = notification.SMSNotification("080123456788")
        
        
    def test_send(self, message):
        assert self.sms.send(message) == f"Sending SMS to 080123456788: {message}" 
        

"In-App Notification Test"
class TestInAppNotification:
    def setup_method(self):
        self.inapp = notification.InAppNotification("test_user_123")
        
        
    def test_send(self, message):
        assert self.inapp.send(message) == f"Sending IN-APP notification to user ID test_user_123: {message}"   
        
       
"Notify Test"
class TestInAppNotification:
    def setup_method(self):
        self.notifier = notification.Notify()
        
        
    def test_send(self, message):
        assert self.notifier.send("email", "alee@mail.com", message) == f"Sending email to alee@mail.com: {message}"       
          