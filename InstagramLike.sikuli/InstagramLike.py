import random
Settings.MoveMouseDelay = 0.01
iter = 200
count = random.randrange(iter, iter * 2)
i = 1
while i <= count:
    try:
        if exists(Pattern("OO.png").similar(0.80).targetOffset(-19,-1)):
            click(Pattern("OO.png").similar(0.80).targetOffset(-19,-1))
            if exists(Pattern("1639060530200.png").similar(0.80)):
                hover(Pattern("1639060530200.png").similar(0.80).targetOffset(-69,0)) #Чтобы не всплывали окна по ссылке профиля
        type(Key.PAGE_DOWN)
    except:
        type(Key.PAGE_DOWN)
    print(count-i)
    i += 1
    

