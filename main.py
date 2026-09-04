from mfrc522 import MFRC522
import signal

continue_reading = True

#Function to read uid and conver it to a string

def uidToString(uid):
	mystring = ""
	for i in uid:
		mystring = format(i,'02X') + mystring
	return mystring

def end_read(signal, frame):
	global continue_reading
	print("Ending Read")
	continue_reading = False

signal.signal(signal.SIGINT, end_read)

MIFAREReader = MFRC522.MFRC522()

while continue_reading:

	(status, TagType) = MIFAREReader.MFRC522_request(MIFAREReader.PICC_REQIDL)

	if status == MIFAREReader.MI_OK:
		(status, uid) = MIFAREReader.MFRC522_SelectTagSN()
	if status == MIFAREReader.MI_OK:
		print("UID: %s" % uidToString(uid))
	else:
		print("Error")
 
