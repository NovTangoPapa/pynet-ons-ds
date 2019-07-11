#!/bin/env python
class NetworkDevice:
    def __init__(self, ip_addr, username, password, serial_number, model, vendor, uptime, os_version):
        ip_addr = ip_addr
        username = username
        password = password
        serial_number = serial_number
        vendor = vendor
        uptime = uptime
        os_version = os_version
    def ip_print(self):
        print(f"The IP Address is {ip_addr}")

    def user_pw(self):
        print(f"Username: {username}")
    def vendor_print(self, vendor):
        vendor = vendor

router1 = NetworkDevice("1.1.1.1", "dude1", "password1", "abc123", "MicroLopht", "2 Years", "2")
router1 = NetworkDevice("1.1.1.2", "dude2", "password1", "abc124", "MicroLopht", "2 Years", "2")
router1 = NetworkDevice("1.1.1.3", "dude3", "password1", "abc125", "MicroLopht", "2 Years", "2")
router1 = NetworkDevice("1.1.1.4", "dude4", "password1", "abc126", "MicroLopht", "2 Years", "2")


router1.NetworkDevice(ip_addr)
