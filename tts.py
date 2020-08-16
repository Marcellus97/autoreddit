import pyttsx3

def save_to_file(self, text, filename, name=None):
	'''
	Adds an utterance to speak to the event queue.
	@param text: Text to sepak
	@type text: unicode
	@param filename: the name of file to save.
	@param name: Name to associate with this utterance. Included in
	notifications about this utterance.
	@type name: str
	'''
	self.proxy.save_to_file(text, filename, name)


engine = pyttsx3.init()
engine.save_to_file("this is just a test", "./test.mp3")
engine.runAndWait()
