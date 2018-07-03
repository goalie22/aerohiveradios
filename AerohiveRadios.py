############################################################
#
#Aerohive AP - Converts Ethernet Mac to Radio Mac Addresses
#
# Written By Larry Chisholm  - goalie22@gmail.com
# 3/July/2018
# Version 1.5
############################################################

##  Input and Conversion
mac_hex = input("Enter AP Ethernet Mac Address:")
mac_dec = int(mac_hex, 16)

#   Print the results
print (" ")
print ("The Ethernet MAC address is " + (mac_hex))

print (" ")
print ("2.4 Ghz Radio MAC Addresses are as follows")
print (" ")

print ("Radio #1 = " + (hex(mac_dec+14)[2:]))
print ("Radio #2 = " + (hex(mac_dec+15)[2:]))
print ("Radio #3 = " + (hex(mac_dec+16)[2:]))

print (" ")
print ("5 Ghz Radio MAC Addresses are as follows")
print (" ")

print ("Radio #1 = " + (hex(mac_dec+24)[2:]))
print ("Radio #2 = " + (hex(mac_dec+25)[2:]))
print ("Radio #3 = " + (hex(mac_dec+26)[2:]))


