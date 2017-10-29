#a program to allow someone to personalize a story
name = raw_input("tell me your name: ")
country_of_origin = raw_input("tell me where are you from: ")
live_now = raw_input("where do you live now: ")
age = raw_input("how old are you: ")
what_transport = raw_input("how did you come here: ")

print ("\nHi " + name.capitalize() + ". " + "\nSo you are from " + country_of_origin.capitalize() + " and are " + age + " years old." + "\nIt's nice that you chose to come to " + live_now.capitalize() + " " + what_transport + "." + "\nNow we now more about you.\n")