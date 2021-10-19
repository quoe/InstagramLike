import random
Settings.MoveMouseDelay = 0.01
iter = 2
count = random.randrange(iter, iter * 2)
i = 1
while i <= count:
    try:
        if exists(Pattern("1609497574296.png").similar(0.95)):
            click(Pattern("1609497574296.png").similar(0.95))
            if exists(Pattern("1634675207891.png").similar(0.95)):
                hover(Pattern("1634675207891.png").similar(0.95).targetOffset(-50,0)) #Чтобы не всплывали окна по ссылке профиля
        type(Key.PAGE_DOWN)
    except:
        type(Key.PAGE_DOWN)
    print(count-i)
    i += 1
    

