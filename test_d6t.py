# i2ctest.py

import smbus
import pigpio
import time

# I2C channel 1 is connected to the GPIO pins
channel = 1

#  D6T defaults to address 0x0a (only 7 bit)
address = 0x0a

# Register addresses (with "normal mode" power-down bits)
reg_write_addr = 0x14  #(0x0a + 0b for write )
reg_read_addr = 0x15   #(0x0a + 1b for write )



####### using pigpio #######
# i2c_bus = smbus.SMBus(1)
#
# pi = pigpio.pi()              # use defaults
#
# def d6T():
#
#     OMRON_BUFFER_LENGTH=5				# Omron data buffer size PTAT(Lo) PTAT(Hi) P0(Lo) P0(Hi) PEC(error check)
#     temperature_data=[0]*OMRON_BUFFER_LENGTH 	# initialize the temperature data list
#
#     global handle
#
#     version = pi.get_pigpio_version()
#     print('PiGPIO version = '+str(version))
#     handle = pi.i2c_open(1, address) # open Omron D6T device at address 0x0a on bus 1
#
#     result=i2c_bus.write_byte(address,0x4c);
#     (bytes_read, temperature_data) = pi.i2c_read_device(handle, len(temperature_data))
#
#     print ('Bytes read from Omron D6T: '+str(bytes_read))
#     print ('Data read from Omron D6T : ')
#
#     print('PTAT temperature: ')
#     PTAT = (temperature_data[0]+temperature_data[1]*256)*0.1
#     print(PTAT)
#
#     print( 'temperature: ')
#     TEMP = (temperature_data[2]+temperature_data[3]*256)*0.1
#     print(TEMP)
#
#     print('PEC check code: ')
#     print(temperature_data[4])
#
#     pi.i2c_close(handle)
#
#
# try:
#     while True:
#         time.sleep(1)
#         d6T()
#
#
# except KeyboardInterrupt:
#
#     pi.i2c_close(handle)
#     pi.stop()



###### using smbus only ######
# Initialize I2C (SMBus)
bus = smbus.SMBus(channel)

write_result = bus.write_byte(reg_write_addr,0x4c) #4c is the command for getting sensor reading
print('write result = '+str(write_result))

read_result = bus.read_block_data(reg_read_addr)
print('read result = '+str(read_result))

exit(0)
