name = 'rahi'
print('enter your name')
enter = input()


if enter == name:

    print("hello "+ str(name) + "what is your password?")
    
    if input() == "kalababa":       #for some reason it won't work if i don't put input directly on to the thing#
        print("access granted")
    else:
        print('wrong password')
