import pywhatkit as kit

class Text:
    """A model to send messages to my crush"""
    def __init__(self,  phone_number, paragraph):
        """initialize the paragraph where the message to be sent is held"""
        self.phone_number = phone_number
        self.paragraph = paragraph

    def first_line(self, message):
        """"Sends the first message of the convesation"""
        self.message = message
        kit.sendwhatmsg(self.phone_number,self.message, 23, 10)

    def line(self, line):
         """Gets the lines from the paragraph"""
         self.line = line
         kit.sendwhatmsg(self.phone_number,self.line, 23, 25)


# Using 'with' to open the file
with open('paragraph.txt', 'r') as file:
    paragraph = file.read()

# No need to call file.close() 

#split the paragraph into different lines using a for loop
lines =paragraph.split('\n')
#save each line skipping empty lines
for line in lines:
    if line.strip():
        line = line
        
paragraph = Text("+254734615998", paragraph )

paragraph.line(line)












