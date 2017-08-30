# This program says hello and greets a person by name.
#
# Chase Dunlap
# August 25, 2017

print("Hello.")
print("What's your name?")
name = input ()
print("It is good to see you, " + name + ".")
print("Where were you born, " + name + "?")
city = input ()
print("That's interesting. I'd like to visit " + city + " one day.")
print("What's your favourite food, " + name + "?")
food = input ()
print("Hmmm. " + food + " sounds tasty, " + name + ".")
print("Hey do you watch the NFL?")
Answer1 = input ()
if Answer1 == "yes":
    print("Cool what's your favorite team?")
    football_team = input ()
    if "Dolphins" in football_team:
        print("Oh that's cool! That's my favorite team! Go Phins!")
    elif "Patriots" in football_team:
        print("Ugh... That team is horrible.")
    else:
        print("That's cool.")
else:
    print("Oh. Ok.")
    
        
