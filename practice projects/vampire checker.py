
vamp_meter = 0


print("welcome to vampire checker v0.01")
print("please answer the questions with 'yes' or 'no' ")

print("1. does the person like garlic?")
if input() == "yes":
    print("the person is human. yay!!")
    
else:
    print("sus")
    x = int(vamp_meter) + int(30)
    vamp_meter = x

print("2. is he/she often seen out during the day?")
if input() == "yes":
    print("hmm, convincing.... could also be a daywalker though")
    x = int(vamp_meter) - int(20)
else:
    print("sus")
    x = int(vamp_meter) + int(30)
    vamp_meter = x

print("3. what is the person's age?")
age = input()
if int(age) < int(130):
    print("hmm, nothing suspicious with the age.")
else:
    print("sus, time to buy some neck guards")
    x = int(vamp_meter) + int(100)
    vamp_meter = x


if int(x) > int(60):
    print("this person is a vampire for sure!!, call the hujurs noww!!")
elif int(x) <= 0:
    print("this nigga aint no vampire, he a real nigga")
else:
    print("he's most likely just a jeffrey, but watch out, he could be a young vampire")

    


