## ✨ Coding Challenge
### Secenerio:

<p>
You’ve been asked to clean up a code base and improve how notifications are sent. Currently, the system only supports sending emails, but your team is about to add support for SMS, in-app messages, and even WhatsApp notifications! Your job? Make the notification system ready for the future... without breaking what already works.
</p>

### 🧩 Your Task
<p>Start with this simple setup:</p>

```python
class Notifier:
    def send_notification(self, message: str, recipient: str):
        # only sends email for now
        print(f"Sending EMAIL to {recipient}: {message}")

```
<p>Your job is to rethink and redesign the notification system so that:</p>

<ol>
<li>
It supports more than one type of notification (Email, SMS, In-App, WhatsApp, etc.).
</li>

<li>
It can be easily extended in the future without modifying existing code.
</li>

<li>
If business logic changes (e.g., logging, message formatting), the code is not hard to update.
</li>

<li>
You can write a small test to show your design work.
</li>
</ol>

### 🔍 Hints

<ul>
<li>
Think about each class having a single responsibility.
</li>

<li>
Try to design it so you don’t need to touch existing classes just to add new ones.
</li>

<li>
Your system should be open to extension, but closed for modification.
</li>

<li>
Different types of notifications might share a contract.
</li>

<li>
Make your design testable and loosely coupled.
</li>
</ul>