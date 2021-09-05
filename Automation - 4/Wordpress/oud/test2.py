cleandomain = "rouwensnl"
password = "daan0409"

yml_database = "        name: " + cleandomain + "\n"
yml_username = "        name: " + cleandomain + "\n"
yml_password = "        password: " + password + "\n"
yml_priv     = "        priv: '" + cleandomain + ".*:ALL,GRANT'" + "\n"

a_file = open("test2.yml", "r")
list_of_lines = a_file.readlines()
list_of_lines[7] = yml_database
list_of_lines[12] = yml_username
list_of_lines[13] = yml_password
list_of_lines[14] = yml_priv

a_file = open("test2.yml", "w")
a_file.writelines(list_of_lines)
a_file.close()
