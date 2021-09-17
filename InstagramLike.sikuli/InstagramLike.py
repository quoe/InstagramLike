import random
Settings.MoveMouseDelay = 0.02
iter = 200
count = random.randrange(iter, iter * 2)
i = 1
while i <= count:
    try:
        if exists(Pattern("1609497574296.png").similar(0.95)):
            click(Pattern("1609497574296.png").similar(0.95))
        type(Key.PAGE_DOWN)
    except:
        type(Key.PAGE_DOWN)
    i += 1


