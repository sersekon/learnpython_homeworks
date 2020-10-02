while True:
    try:
        hello_user = input('Как дела? ')
        if hello_user == 'хорошо':
            print('Супер!')
            break
        else:
            print('Почему не хорошо?')
    except KeyboardInterrupt:
        print('Пока')
        break

   
    
    

