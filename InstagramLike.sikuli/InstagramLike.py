from datetime import datetime
import random
Settings.MoveMouseDelay = 0.01
LogFilePath = "E:\\"
LogFileName = "Sikuli_InstaBot_Log_" + datetime.strftime(datetime.now(), "%Y.%m.%d %H_%M_%S") + ".txt"
log = file(LogFilePath + LogFileName, "w")
base_x = -19
base_y = -1
max_dx = 4
max_dy = 5
iter = 200

def randomClick(image, max_dx, max_dy):
    dx = random.randrange(-max_dx, max_dx)
    dy = random.randrange(-max_dy, max_dy)
    baseOffset_x = base_x 
    baseOffset_y = base_y 
    click(image.targetOffset(baseOffset_x + dx, baseOffset_y + dy))

def latinizator(letter):
    legend = {
    #' ':'_',
    #',':'',
    'а':'a',
    'б':'b',
    'в':'v',
    'г':'g',
    'д':'d',
    'е':'e',
    'ё':'yo',
    'ж':'zh',
    'з':'z',
    'и':'i',
    'й':'y',
    'к':'k',
    'л':'l',
    'м':'m',
    'н':'n',
    'о':'o',
    'п':'p',
    'р':'r',
    'с':'s',
    'т':'t',
    'у':'u',
    'ф':'f',
    'х':'h',
    'ц':'c',
    'ч':'ch',
    'ш':'sh',
    'щ':'shch',
    'ъ':'y',
    'ы':'y',
    'ь':"'",
    'э':'e',
    'ю':'yu',
    'я':'ya',
    
    'А':'A',
    'Б':'B',
    'В':'V',
    'Г':'G',
    'Д':'D',
    'Е':'E',
    'Ё':'Yo',
    'Ж':'Zh',
    'З':'Z',
    'И':'I',
    'Й':'Y',
    'К':'K',
    'Л':'L',
    'М':'M',
    'Н':'N',
    'О':'O',
    'П':'P',
    'Р':'R',
    'С':'S',
    'Т':'T',
    'У':'U',
    'Ф':'F',
    'Х':'H',
    'Ц':'Ts',
    'Ч':'Ch',
    'Ш':'Sh',
    'Щ':'Shch',
    'Ъ':'Y',
    'Ы':'Y',
    'Ь':"'",
    'Э':'E',
    'Ю':'Yu',
    'Я':'Ya',
    }
    for i, j in legend.items():
        letter = letter.replace(i, j)
    return letter

def WriteLog(t):
    nl = "\n" # new line character
    log = open(LogFilePath + LogFileName, "a")
    TD = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") + "\t"
    log.write(TD + t + nl)
    log.close()
    print(TD + latinizator(t))
    
count = random.randrange(iter, iter * 2)
clickCount = 0;
i = 1
while i <= count:
    try:
        if exists(Pattern("OO.png").similar(0.80).targetOffset(-19,-1)):
            randomClick(Pattern("OO.png").similar(0.80).targetOffset(-19,-1), max_dx, max_dy)
            clickCount += 1
            WriteLog("\tЦикл\t" + str(i) + "\tКлик\t" + str(clickCount))
            if exists(Pattern("1639060530200.png").similar(0.80)):
                hover(Pattern("1639060530200.png").similar(0.80).targetOffset(-69,0)) #Чтобы не всплывали окна по ссылке профиля
        type(Key.PAGE_DOWN)
    except:
        type(Key.PAGE_DOWN)
    print(count-i)
    i += 1
    

