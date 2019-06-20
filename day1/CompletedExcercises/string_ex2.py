ip_addr = input("Whats you the IP Address? ")

new_num_list = ip_addr.split(".")

print("{:<12}{:<12}{:<12}{:<12}".format(new_num_list[0], new_num_list[1], new_num_list[2], new_num_list[3]))