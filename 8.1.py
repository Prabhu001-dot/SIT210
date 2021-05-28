
from smbus import SMBus

address = 0x9 # bus addressess
bus = SMBus(1) # indicates /dev/ic2-1

ic = 1

print ("Lights will ON on 1,2,3 or 0 will turn OFF ")
while ic == 1:
    
	LightStatus = input(":: ")

	if LightStatus == "1":
		bus.write_byte(address, 0x1)
		
	elif LightStatus == "0":
		bus.write_byte(address, 0x0)
		print("THank you for testing")
		break
		
	elif LightStatus == "2":
		bus.write_byte(address, 0x2) 
	elif LightStatus == "3":
		bus.write_byte(address, 0x3) 
	else:
		ic = 0
		
        
	print ("Lights will ON on 1,2,3 or 0 will turn OFF ")
	
