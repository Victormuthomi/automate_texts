import pywhatkit as kit
import datetime
import time

class Text:
    """A model to send messages to my crush"""
    def __init__(self, phone_number, filename):
        """initialize the paragraph where the message to be sent is held"""
        self.phone_number = phone_number
        with open('paragraph.txt' 'r') as file:
            self.paragraph = file.read().split('\n')

    def send_messages(self):
        """"Sends the messages of the conversation"""
        # Send the first message
        now = datetime.datetime.now()
        hour, min = now.hour, now.minute
        kit.sendwhatmsg(self.phone_number, "The messages are auto-sent. Please reply after they are over.", hour, min+1)
        time.sleep(60)  # wait for 60 seconds

        # Send each line of the paragraph every 2 minutes
        for line in self.paragraph:
            min += 2  # increment the minute by 2
            if min > 59:
                min -= 60
                hour = (hour + 1) % 24
            kit.sendwhatmsg(self.phone_number, line, hour, min)
            time.sleep(120)  # wait for 120 seconds

        # Send the last message
        min += 2  # increment the minute by 2
        if min > 59:
            min -= 60
            hour = (hour + 1) % 24
        kit.sendwhatmsg(self.phone_number, "The messages are over. You can reply now.", hour, min)

# Replace 'text.txt' with the name of your file
paragraph = Text("+254734615998", 'paragraph.txt')
paragraph.send_messages()

