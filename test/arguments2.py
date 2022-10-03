import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--foo", default=argparse.SUPPRESS)
parser.add_argument("--test", default=argparse.SUPPRESS)
ns = parser.parse_args()

#print("Parsed arguments: {}".format(ns))
#print("foo in namespace?: {}".format("foo" in ns))
test = format("test" in ns)
print (test)

if test == "False":
    print ("Niks ingevuld")

if test == "True":
    print ("Wel ingevuld")