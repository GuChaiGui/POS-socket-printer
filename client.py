import socket         

from barcode import EAN13
  
# ImageWriter to generate an image file
from barcode.writer import ImageWriter
  

# Make sure to pass the number as string
number = '111111111110'
barcode = "barcode100"
# Now, let's create an object of EAN13 class and 
# pass the number with the ImageWriter() as the 
# writer
my_code = EAN13(number, writer=ImageWriter())
  
# Our barcode is ready. Let's save it.
my_code.save(barcode)

file_name = barcode + ".png"

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.

s.connect((host, port))
f = open(file_name,'rb')
print ('Sending...')
l = f.read(1024)
while (l):
    print ('Sending...')
    s.send(l)
    l = f.read(1024)
f.close()
print ("Done Sending")
s.shutdown(socket.SHUT_WR)
print (s.recv(1024))
s.close()          