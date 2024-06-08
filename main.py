class Text:
	"""A model to send messages to my crush"""
	def __init__(self, paragraph):
	    """initialize the paragraph where the message to be sent is held"""
	    self.paragraph = paragraph

	def fist_line(self, message):
        """"Sends the first message of the convesation"""
        self.message = message
        message = "Hello this are automated messages don't reply untill you get the messgae that
        the messages are over"

	def line(self):
	    """Gets the lines from the paragraph"""
        #Split the paragrap into different lines using a for loop

        lines = paragraph.split('\n')

        #save each line skipping empty lines

	    for line in lines:
            if line.strip():
                print(line)

