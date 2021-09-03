a_file = open("sample.txt", "r")
list_of_lines = a_file.readlines()
list_of_lines[29] = "$cfg['Servers'][$i]['host'] = '192.168.123.13';\n"

a_file = open("sample.txt", "w")
a_file.writelines(list_of_lines)
a_file.close()