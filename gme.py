#баг с счетом победителя
#баг с мультиплеером -- выбором машинки
#баг с цветом карты в фан-режиме

import pygame as pg, time, random

pg.init()

clock = pg.time.Clock()
pg.mixer.music.load('rasa_-_pchelovod_(zaycev.net).mp3')
pg.mixer.music.play(-1)
pg.mixer.music.pause()

score = 0
flag = True

def ask(language, coins):
    screen = pg.display.set_mode((1200, 700))

    font = pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 30)

    if language == "e":
        choice = font.render("Please choose the game mode", 1, (0, 0, 0))
        double = font.render("Multiplayer", 1, (0, 0, 0))
        manual = font.render("Career", 1, (0, 0, 0))
    elif language == "r":
        choice = font.render("Пожалуйста, выберите режим игры", 1, (0, 0, 0))
        double = font.render("С другом", 1, (0, 0, 0))
        manual = font.render("Карьера", 1, (0, 0, 0))

    place_choice = choice.get_rect(center=(600, 100))
    place_double = double.get_rect(topleft=(100, 400))
    place_manual = manual.get_rect(topleft=(100, 300))

    while 1:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                pg.quit()
                exit()
            elif i.type == pg.KEYUP:
                if i.key == pg.K_ESCAPE:
                    start(language)
                elif i.key == pg.K_f or i.key == pg.K_t:
                    fun()
        
        pressed = pg.mouse.get_pressed()
        pos = pg.mouse.get_pos()
        if pressed[0]:
            if pos[0] >= 90 and pos[0] <= 290 and pos[1] >= 290 and pos[1] <= 350:
                single(language, coins)
            elif pos[0] >= 90 and pos[0] <= 290 and pos[1] >= 390 and pos[1] <= 450:
                multi(language)
        screen.fill((255, 255, 255))
        screen.blit(choice, place_choice)
        screen.blit(double, place_double)
        screen.blit(manual, place_manual)
        pg.draw.rect(screen, (0, 0, 0), (90, 290, 200, 60), 3)
        pg.draw.rect(screen, (0, 0, 0), (90, 390, 200, 60), 3)
        pg.display.update()

def fun():
    file = open("fun_game.txt", "r")
    num = None
    try:
        num = int(file.read())
        file.close()
        pg.mixer.music.unpause()
    except:
        file.close()
        file = open("fun_game.txt", "w")
        file.write("1")
        file.close()
        pg.mixer.music.load('rasa_-_pchelovod_(zaycev.net).mp3')
        pg.mixer.music.play(-1)

    if 1:
        global score, flag
        
        FPS = 60
        x = 600
        y = 650
        font = pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 30)
        nfont = pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 20)
        y1 = 50
        y2 = 225
        y3 = 400
        y4 = 575
        flag = False
        sencibility = 3
        crash = None
        PAUSE = False
        FINISH = False

        file = open("colour.txt", "r")
        colour = int(file.read())
        file.close()

        SPAWN = pg.USEREVENT + 1

        event = pg.time.set_timer(SPAWN, 3000)
        
        if colour == 1:
            color1 = (0, 255, 0)
            color2 = (127, 127, 127)
            color3 = (255, 255, 255)
        else:
            color1 = (0, 125, 5)
            color2 = (95, 95, 95)
            color3 = (25, 25, 25)
        
        screen = pg.display.set_mode((1200, 700))

        enemies = ['car1.png', 'car2.png', 'car3.png', 'car4.png', 'car5.png', 'car6.png', 'car7.png', 'car8.png']
        for i in range(len(enemies)):
            enemies[i] = pg.image.load(enemies[i]).convert_alpha()
            enemies[i] = pg.transform.scale(enemies[i], (enemies[i].get_width() * 2, enemies[i].get_height() * 2))
        group = pg.sprite.Group()

        grass = pg.Surface((1200, 700))
        grass.fill(color1)
        grass_place = grass.get_rect(topleft=(0, 0))
        road = pg.Surface((400, 700))       
        road.fill(color2)
        road_place = road.get_rect(center=(600, 350))
        line1 = pg.Surface((20, 70))
        line1.fill(color3)
        line2 = pg.Surface((20, 70))
        line2.fill(color3)
        line3 = pg.Surface((20, 70))
        line3.fill(color3)
        line4 = pg.Surface((20, 70))
        line4.fill(color3)

        howtocontinue = nfont.render("Играет: RASA - 'Пчеловод'", 1, (0, 0, 0))
            
        place_continue = howtocontinue.get_rect(topleft=(800, 140))


        class Enemy(pg.sprite.Sprite):
            def __init__(self, x, file, group, speed, mode):
                pg.sprite.Sprite.__init__(self)
                self.image = file
                if mode == 1:
                    if x == 1:
                        self.rect = file.get_rect(center=(550, 0))
                    else:
                        self.rect = file.get_rect(center=(650, 0))
                elif mode == 2:
                    if x == 1:
                        self.rect = file.get_rect(center=(470, 0))
                    elif x == 2:
                        self.rect = file.get_rect(center=(595, 0))
                    else:
                        self.rect = file.get_rect(center=(735, 0))
                elif mode == 3:
                    if x == 1:
                        self.rect = file.get_rect(center=(405, 0))
                    elif x == 2:
                        self.rect = file.get_rect(center=(515, 0))
                    elif x == 3:
                        self.rect = file.get_rect(center=(610, 0))
                    else:
                        self.rect = file.get_rect(center=(725, 0))
                elif mode == 4:
                    if x == 1:
                        self.rect = file.get_rect(center=(340, 0))
                    elif x == 2:
                        self.rect = file.get_rect(center=(440, 0))
                    elif x == 3:
                        self.rect = file.get_rect(center=(540, 0))
                    elif x == 4:
                        self.rect = file.get_rect(center=(640, 0))
                    elif x == 5:
                        self.rect = file.get_rect(center=(740, 0))
                    else:
                        self.rect = file.get_rect(center=(855, 0))
                self.add(group)
                self.speed = 4 + speed
            def update(self):
                global score
                if self.rect.y < 700:
                    #self.image = pg.transform.scale(self.image, (self.rect.width + self.speed, self.rect.height))
                    #self.rect = self.image.get_rect(center=(self.x - self.speed, 0))
                    self.rect.y += self.speed
                    #self.rect.x -= 0.5 * self.speed
                else:
                    score += 1
                    self.kill()

        class Player(pg.sprite.Sprite):
            def __init__(self, x, y, file):
                pg.sprite.Sprite.__init__(self)
                self.image = file
                self.rect = file.get_rect(center=(x, y))

        while 1:

            player = Player(x, y, pg.transform.scale(pg.image.load('car_bee.png').convert_alpha(), (pg.image.load('car3.png').convert_alpha().get_width() * 2, pg.image.load('car3.png').convert_alpha().get_height() * 2)))

            whatline = random.randint(1, 3)
                
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    pg.quit()
                    exit()
                elif i.type == pg.KEYUP:
                    if i.key == pg.K_SPACE:
                        pg.mixer.music.pause()
                        PAUSE = True
                        
                    elif i.key == pg.K_ESCAPE:
                        pg.mixer.music.pause()
                        file = open("fun_game.txt", "w")
                        file.write("0.5")
                        file.close()
                        start(language)
                elif i.type == SPAWN:
                    Enemy(whatline, enemies[random.randint(0, len(enemies) - 1)], group, score // 2, 2)
            pressed = pg.key.get_pressed()
            if pressed[pg.K_LEFT] or pressed[pg.K_a]:
                x -= sencibility
            if pressed[pg.K_RIGHT] or pressed[pg.K_d]:
                x += sencibility
            if pressed[pg.K_UP] or pressed[pg.K_w]:
                y -= sencibility
            if pressed[pg.K_DOWN] or pressed[pg.K_s]:
                y += sencibility

            if x >= 770: 
                x = 770
            elif x <= 430: 
                x = 430
            
            if y <= 550:
                y = 550
            elif y >= 650:
                y = 650
            if pg.sprite.spritecollideany(player, group):
                time.sleep(1)
                score = 0
                fun()
            y1 += (4 + score // 4) * 2
            y2 += (4 + score // 4) * 2
            y3 += (4 + score // 4) * 2
            y4 += (4 + score // 4) * 2
            if y1 >= 700:
                y1 = 0
            elif y2 >= 700:
                y2 = 0
            elif y3 >= 700:
                y3 = 0
            elif y4 >= 700:
                y4 = 0
                
            if (score + 2) // 3 > 0:
                color = (0, 0, 255)
            else:
                color = (255, 0, 0)
            
            if PAUSE:
                while PAUSE:
                    time.sleep(0.1)
                    for i in pg.event.get():
                        if i.type == pg.QUIT:
                            pg.quit()
                            exit()
                        elif i.type == pg.KEYUP:
                            if i.key == pg.K_SPACE:
                                pg.mixer.music.unpause()
                                PAUSE = False
                            elif i.key == pg.K_ESCAPE:
                                pg.mixer.music.pause()
                                file = open("fun_game.txt", "w")
                                file.write("0.5")
                                file.close()
                                score = 0
                                start(language)

            text = font.render("Ваш счёт:"+str(score), 1, (0, 0, 0))
            place = text.get_rect(center=(600, 100))
            
            screen.fill((255, 255, 255))
            screen.blit(grass, grass_place)
            screen.blit(road, road_place)
            screen.blit(line1, (520, y1))
            screen.blit(line2, (520, y2))
            screen.blit(line3, (520, y3))
            screen.blit(line4, (520, y4))
            screen.blit(line1, (660, y1))
            screen.blit(line2, (660, y2))
            screen.blit(line3, (660, y3))
            screen.blit(line4, (660, y4))
            screen.blit(text, place)
            screen.blit(howtocontinue, place_continue)
            screen.blit(player.image, player.rect)
            group.draw(screen)
            pg.display.update()
            clock.tick(FPS)
            group.update()

def choose_language():
    screen = pg.display.set_mode((1200, 700))

    lang = "e"
    string = ""
    flag = False
    font = pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 30)
    
    language = font.render("Please, choose your language", 1, (0, 0, 0))
    place_language = language.get_rect(center=(600, 150))
    text1 = "Please, choose your language"
    text2 = "To continue, press any button"
    
    russian = font.render("Русский", 1, (0, 0, 0))
    place_russian = russian.get_rect(topleft=(650, 300))
    english = font.render("English", 1, (0, 0, 0))
    place_english = english.get_rect(topleft=(650, 400))
    russianflag = pg.image.load("Russia.png").convert_alpha()
    russianflag = pg.transform.scale(russianflag, (70, 70))
    place_rflag = russianflag.get_rect(center=(600, 300))
    englishflag = pg.image.load("England.png").convert_alpha()
    englishflag = pg.transform.scale(englishflag, (70, 70))
    place_eflag = englishflag.get_rect(center=(600, 400))

    howtocontinue = font.render("To continue, press any button", 1, (0, 0,0))
    place_continue = howtocontinue.get_rect(center=(600, 600))
    
    while 1:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                pg.quit()
                exit()
            elif i.type == pg.KEYUP:
                hello(lang)

        pressed = pg.mouse.get_pressed()
        pos = pg.mouse.get_pos()

        if pressed[0] and pos[0] >= 565 and pos[0] <= 770 and pos[1] >= 265 and pos[1] <= 335:
            lang = "r"
            text1 = "Пожалуйста, выберите язык"
            text2 = "Чтобы продолжить, нажмите на любую кнопку"
        elif pressed[0] and pos[0] >= 565 and pos[0] <= 770 and pos[1] >= 365 and pos[1] <= 435:
            lang = "e"
            text1 = "Please, choose your language"
            text2 = "To continue, press any button"

        file = open("language.txt", "w")
        file.write(lang)
        file.close()
        
        language = font.render(text1, 1, (0, 0, 0))
        place_language = language.get_rect(center=(600, 150))
        howtocontinue = font.render(text2, 1, (0, 0,0))
        place_continue = howtocontinue.get_rect(center=(600, 600))
        
        screen.fill((255, 255, 255))
        screen.blit(language, place_language)
        screen.blit(russian, place_russian)
        screen.blit(russianflag, place_rflag)
        screen.blit(english, place_english)
        screen.blit(englishflag, place_eflag)
        screen.blit(howtocontinue, place_continue)
        pg.display.update()    

def hello(language):
    screen = pg.display.set_mode((1200, 700))

    string = ""
    flag = False
    font = pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 30)
    nfont = pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 25)
    
    if language == "r":
        s = font.render("Пожалуйста, придумайте свое игровое имя", 1, (0, 0, 0))
        s2 = nfont.render("Вы можете использовать свое настоящее имя или придумать никнейм", 1, (0, 0, 0))
        s3 = nfont.render("Ваше имя может содержать только латинские буквы и цифры", 1, (0, 0, 0))
        s4 = font.render("Чтобы продолжить, нажмите на Enter", 1, (0, 0, 0))
    elif language == "e":
        s = font.render("Please, invent a name", 1, (0, 0, 0))
        s2 = nfont.render("You can use your real name or a nickname", 1, (0, 0, 0))
        s3 = nfont.render("Your name can only content english letters and numbers", 1, (0, 0, 0))
        s4 = font.render("To contiue, please press ENTER-button", 1, (0, 0, 0))
    
    ps = s.get_rect(center=(600, 100))
    ps2 = s2.get_rect(center=(600, 150))
    ps3 = s3.get_rect(center=(600, 250))
    ps4 = s4.get_rect(center=(600, 550))

    while 1:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                pg.quit()
                exit()
            elif i.type == pg.KEYDOWN:
                if i.key == 304:
                    flag = True
                elif i.key == 301:
                    flag = not flag
            elif i.type == pg.KEYUP:
                if i.key == 304:
                    flag = False
                elif i.key == 8:
                    string = string[:-1]
                elif i.key == pg.K_RETURN:
                    start(language)
                elif i.key != 301:
                    if flag:
                        string += chr(i.key - 32)
                    else:
                        string += chr(i.key)
        try:
            file = open("name.txt", "w")
            file.write(string)
            file.close()
        except UnicodeEncodeError:
            string = string[:-1]
                
        name = font.render(string, 1, (0, 0, 0))
        name_place = name.get_rect(center=(600, 350))

        screen.fill((255, 255, 255))
        pg.draw.rect(screen, (0, 0, 0), (300, 300, 600, 100), 3)
        screen.blit(s, ps)
        screen.blit(s2, ps2)
        screen.blit(s3, ps3)
        screen.blit(s4, ps4)
        screen.blit(name, name_place)
        pg.display.update()

def settings(language):
    screen = pg.display.set_mode((1200, 700))

    font = pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 30)
    nfont = pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 25)

    flag1, flag2 = False, False
    
    russian = font.render("Русский", 1, (0, 0, 0))
    place_russian = russian.get_rect(topleft=(650, 50))
    english = font.render("English", 1, (0, 0, 0))
    place_english = english.get_rect(topleft=(650, 90))
    russianflag = pg.image.load("Russia.png").convert_alpha()
    russianflag = pg.transform.scale(russianflag, (40, 40))
    place_rflag = russianflag.get_rect(center=(600, 70))
    englishflag = pg.image.load("England.png").convert_alpha()
    englishflag = pg.transform.scale(englishflag, (40, 40))
    place_eflag = englishflag.get_rect(center=(600, 110))

    ehit = pg.image.load("quit.png").convert_alpha()
    ehit = pg.transform.scale(ehit, (50, 50))
    place_ehit = ehit.get_rect(topright=(1180, 20))
    
    if language == "r":
        main_language = font.render("Выберите главный язык", 1, (0, 0, 0))
        show = font.render("Никогда не показывать виджет с информацией об управлении", 1, (0, 0, 0))
        yes = font.render("ДА", 1, (0, 0, 0))
        no = font.render("НЕТ", 1, (0, 0, 0))
        yourname = font.render("Ваше имя:", 1, (0, 0, 0))
        mode = font.render("Цветовая гамма игры:", 1, (0, 0, 0))
        d = nfont.render("Тёмный", 1, (0, 0, 0))
        b = nfont.render("Светлый", 1, (0, 0, 0))
        change = nfont.render("Изменить", 1, (0, 0, 0))
    elif language == "e":
        main_language = font.render("Choose your main language", 1, (0, 0, 0))
        show = font.render("Never show widget before choosing a car", 1, (0, 0, 0))
        yes = nfont.render("YES", 1, (0, 0, 0))
        no = nfont.render("NO", 1, (0, 0, 0))
        yourname = font.render("Your name:", 1, (0, 0, 0))
        mode = font.render("Colour mode:", 1, (0, 0, 0))
        d = font.render("Dark", 1, (0, 0, 0))
        b = font.render("Bright", 1, (0, 0, 0))
        change = nfont.render("Change", 1, (0, 0, 0))
        
    place_lang = main_language.get_rect(topleft=(50, 80))
    place_show = show.get_rect(topleft=(50, 150))
    place_yes = yes.get_rect(topleft=(100, 200))
    place_no = no.get_rect(topleft=(100, 250))
    place_mode = mode.get_rect(topleft=(50, 300))
    pd = d.get_rect(topleft=(120, 500))
    pb = b.get_rect(topleft=(370, 500))
    place_yourname = yourname.get_rect(topleft=(50, 550))
    place_change = change.get_rect(center=(300, 650))

    dark = pg.image.load("dark_mode.png").convert_alpha()
    dark = pg.transform.scale(dark, (150, 150))
    bright = pg.image.load("bright_mode.png").convert_alpha()
    bright = pg.transform.scale(bright, (150, 150))
    place_dark = dark.get_rect(topleft=(70, 350))
    place_bright = bright.get_rect(topleft=(320, 350))

    flag3 = False
    flag4 = False

    file = open("name.txt", "r")
    name = file.read()
    file.close()
    name = font.render(name, 1, (0, 0, 0))
    place_name = name.get_rect(topleft=(50, 590))
    
    while 1:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                pg.quit()
                exit()
            elif i.type == pg.KEYDOWN and i.key == pg.K_ESCAPE:
                start(language)

        if language == "r":
            main_language = font.render("Выберите главный язык", 1, (0, 0, 0))
            show = font.render("Никогда не показывать виджет с информацией об управлении", 1, (0, 0, 0))
            yes = font.render("ДА", 1, (0, 0, 0))
            no = font.render("НЕТ", 1, (0, 0, 0))
            yourname = font.render("Ваше имя:", 1, (0, 0, 0))
            mode = font.render("Цветовая гамма игры:", 1, (0, 0, 0))
            d = nfont.render("Тёмный", 1, (0, 0, 0))
            b = nfont.render("Светлый", 1, (0, 0, 0))
            change = nfont.render("Изменить", 1, (0, 0, 0))
        elif language == "e":
            main_language = font.render("Choose your main language", 1, (0, 0, 0))
            show = font.render("Never show widget before choosing a car", 1, (0, 0, 0))
            yes = nfont.render("YES", 1, (0, 0, 0))
            no = nfont.render("NO", 1, (0, 0, 0))
            yourname = font.render("Your name:", 1, (0, 0, 0))
            mode = font.render("Colour mode:", 1, (0, 0, 0))
            d = font.render("Dark", 1, (0, 0, 0))
            b = font.render("Bright", 1, (0, 0, 0))
            change = nfont.render("Change", 1, (0, 0, 0))

        pressed = pg.mouse.get_pressed()
        pos = pg.mouse.get_pos()
        
        if pressed[0] and pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 200 and pos[1] <= 240:
            flag1 = True
            flag2 = False
        elif pressed[0] and pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 250 and pos[1] <= 290:
            flag2 = True
            flag1 = False
        elif pressed[0] and pos[0] >= 90 and pos[0] <= 120 and pos[1] >= 500 and pos[1] <= 530:
            flag3 = True
            flag4 = False
        elif pressed[0] and pos[0] >= 340 and pos[0] <= 370 and pos[1] >= 500 and pos[1] <= 530:
            flag4 = True
            flag3 = False
        elif pressed[0] and pos[0] >= 580 and pos[0] <= 690 and pos[1] >= 50 and pos[1] <= 90:
            file = open("language.txt", "w")
            file.write("r")
            file.close()
            language = "r"
        elif pressed[0] and pos[0] >= 580 and pos[0] <= 690 and pos[1] >= 90 and pos[1] <= 130:
            file = open("language.txt", "w")
            file.write("e")
            file.close()
            language = "e"
        elif pressed[0] and place_ehit.collidepoint(pos):
            start(language)
        elif pressed[0] and place_change.collidepoint(pos):
            file = open("first_time.txt", "w")
            file.write("False1")
            file.close()
            hello(language)
        
        screen.fill((255, 255, 255))
        screen.blit(main_language, place_lang)
        screen.blit(show, place_show)
        screen.blit(russian, place_russian)
        screen.blit(english, place_english)
        screen.blit(russianflag, place_rflag)
        screen.blit(englishflag, place_eflag)
        screen.blit(yes, place_yes)
        screen.blit(no, place_no)
        screen.blit(mode, place_mode)
        screen.blit(dark, place_dark)
        screen.blit(bright, place_bright)
        screen.blit(d, pd); screen.blit(b, pb)
        screen.blit(yourname, place_yourname)
        screen.blit(name, place_name)
        screen.blit(change, place_change)
        screen.blit(ehit, place_ehit)

        pg.draw.circle(screen, (0, 0, 0), (65, 220), 20, 1)
        pg.draw.circle(screen, (0, 0, 0), (65, 270), 20, 1)
        
        file = open("how_to_play.txt", "w")

        if flag1:
            pg.draw.circle(screen, (0, 0, 0), (65, 220), 15)
            pg.draw.circle(screen, (255, 255, 255), (70, 270), 15)
            file.write("False")
        elif flag2:
            pg.draw.circle(screen, (255, 255, 255), (65, 220), 15)
            pg.draw.circle(screen, (0, 0, 0), (65, 270), 15)
            file.write("True")
        file.close()
        
        file = open("colour.txt", "w")
        if flag3:
            pg.draw.circle(screen, (0, 0, 0), (105, 515), 10)
            pg.draw.circle(screen, (255, 255, 255), (355, 515), 10)
            file.write("2")
        elif flag4:
            pg.draw.circle(screen, (255, 255, 255), (105, 515), 10)
            pg.draw.circle(screen, (0, 0, 0), (355, 515), 10)
            file.write("1")
        file.close()

        pg.draw.circle(screen, (0, 0, 0), (105, 515), 15, 2)
        pg.draw.circle(screen, (0, 0, 0), (355, 515), 15, 2)
        
        pg.display.update()
    
def widget(language, coins):
    screen = pg.display.set_mode((1200, 700))

    flag = False
    text = []
    place = []
    font = pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 30)
    nfont = pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 25)
    
    enter = pg.image.load("enter.png").convert_alpha()
    enter = pg.transform.scale(enter, (150, 75))
    place_enter = enter.get_rect(topleft=(890, 160))
    wasd = pg.image.load("arrows.png").convert_alpha()
    wasd = pg.transform.scale(wasd, (300, 150))
    place_wasd = wasd.get_rect(topleft=(790, 400))
    arrows = pg.image.load("arrows.jpg").convert()
    arrows = pg.transform.scale(arrows, (200, 100))
    place_arrows = arrows.get_rect(topleft=(850, 70))

    ehit = pg.image.load("quit.png").convert_alpha()
    ehit = pg.transform.scale(ehit, (50, 50))
    place_ehit = ehit.get_rect(topright=(1180, 20))
    
    if language == "r":
        text.append(font.render("Чтобы выбрать машинку, используйте стрелочки", 1, (0, 0, 0)))
        text.append(font.render("Чтобы купить машинку, используйте клавишу Enter", 1, (0, 0, 0)))
        text.append(font.render("Чтобы начать игру, нажмите на любую кнопку, находясь в окне выбора", 1, (0, 0, 0)))
        text.append(font.render("Чтобы управлять машинкой, нажимайте на стрелочки или кнопки wasd", 1, (0, 0, 0)))
        goback = font.render("Чтобы вернуться на стартовый экран, нажмите на кнопку esc", 1, (0, 0, 0))
        languages = font.render("Чтобы изменить язык, нажмите на его иконку на главном окне", 1, (0, 0, 0))
        donotshow = nfont.render("Больше не показывать это", 1, (0, 0, 0))
        
    elif language == "e":
        text.append(font.render("To choose a car, you can use arrows", 1, (0, 0, 0)))
        text.append(font.render("To buy a car, please use Enter button", 1, (0, 0, 0)))
        text.append(font.render("To start the game, please press any button when are choosing a car", 1, (0, 0, 0)))
        text.append(font.render("To manage a car, just press arrows or WASD-buttons", 1, (0, 0, 0)))
        languages = font.render("To change language, press on its icon on the main window", 1, (0, 0, 0))
        goback = font.render("To get back on the start window, please press esc-button", 1, (0, 0, 0))
        donotshow = nfont.render("Do not show it anymore", 1, (0, 0, 0))

    place_languages = languages.get_rect(topleft=(30, 530))
    place_goback = goback.get_rect(topleft=(30, 570))
    place_donot = donotshow.get_rect(center=(600, 645))

    for i in range(len(text)):
        place.append(text[i].get_rect(topleft=(30, 100 + 80 * i)))

    while 1:
        for i in pg.event.get():
            if i.type  == pg.QUIT:
                pg.quit()
                exit()
            elif i.type == pg.KEYDOWN and i.key == pg.K_ESCAPE:
                start(language)
            elif i.type == pg.MOUSEBUTTONDOWN and i.button == 1:
                if i.pos[0] >= 400 and i.pos[0] <= 420 and i.pos[1] >= 635 and i.pos[1] <= 645:
                    flag = not flag
                elif place_ehit.collidepoint(i.pos):
                    if flag:
                        file = open("how_to_play.txt", "w")
                        file.write("False")
                        file.close()
                    ask(language, coins)
        
        screen.fill((255, 255, 255))
        for i in range(len(text)):
            screen.blit(text[i], place[i])
        screen.blit(wasd, place_wasd)
        screen.blit(arrows, place_arrows)
        screen.blit(enter, place_enter)
        screen.blit(languages, place_languages)
        screen.blit(goback, place_goback)
        screen.blit(donotshow, place_donot)
        screen.blit(ehit, place_ehit)
        if flag:
            pg.draw.rect(screen, (0, 0, 0), (405, 640, 11, 11))
        pg.draw.rect(screen, (0, 0, 0), (400, 635, 20, 20), 2)
        pg.display.update()

def rool(language, coins):
    screen = pg.display.set_mode((1200, 700))
    string = []
    
    file = open("how_to_play.txt", "r")
    truefalse = file.read()
    file.close()
    
    if language == "r":
        font = pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 40)
        txt = font.render("Правила", 1, (0, 0, 0))
        font = pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 30)
        string.append(font.render("Правила игры предельно просты.", 1, (0, 0, 0)))
        string.append(font.render("Предыстория: Вы очень спешите на встречу, но как всегда Вам ", 1, (0, 0, 0)))
        string.append(font.render("преграждает дорогу огромное множество автомобилей.Ваша задача --", 1, (0, 0, 0)))
        string.append(font.render("не врезаться ни в один из автомобилей. Удачи!", 1, (0, 0, 0)))
        string.append(font.render("Вы заработаете ((Ваш счёт + 2) / 3) монет на Лёгком режиме", 1, (0, 0, 0)))
        string.append(font.render("Вы заработаете (Ваш счёт / 3) монет на Среднем режиме", 1, (0, 0, 0)))
        string.append(font.render("Вы заработаете ((Ваш счёт + 4) / 5) монет на Сложном режиме", 1, (0, 0, 0)))
        string.append(font.render("Вы заработаете (Ваш счёт / 6) монет на Мегасложном режиме", 1, (0, 0, 0)))
        string.append(font.render("Чтобы поставить игру на паузу, нажмите на пробел. Когда игра закон-", 1, (255, 0, 0)))
        string.append(font.render("чится, нажмите на любую клавишу, чтобы продолжить", 1, (255, 0, 0)))
        nfont =  pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 25)
        text = nfont.render("Чтобы начать игру, нажмите на любую клавишу", 1, (0, 0, 0))
    elif language == "e":
        font = pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 40)
        txt = font.render("Rools", 1, (0, 0, 0))
        font = pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 30)
        string.append(font.render("The rools of the game are really easy.", 1, (0, 0, 0)))
        string.append(font.render("You're very hurry cause you're late for a meeting. But", 1, (0, 0, 0)))
        string.append(font.render("there're a lot of cars so it's hard for you to . ", 1, (0, 0, 0)))
        string.append(font.render("Your task is not to crash. Have a good luck!", 1, (0, 0, 0)))
        string.append(font.render("You will earn ((your score + 2) / 3) coins in the Easy mode", 1, (0, 0, 0)))
        string.append(font.render("You will earn (your score / 3) coins in the Medium mode", 1, (0, 0, 0)))
        string.append(font.render("You will earn ((your score + 4) / 5) coins in the Hard mode", 1, (0, 0, 0)))
        string.append(font.render("You will earn (your score / 3) coins in the Megahard mode", 1, (0, 0, 0)))
        string.append(font.render("To pause the game, just press the SPACE button. When the game", 1, (255, 0, 0)))
        string.append(font.render("will over, press any button to continue.", 1, (255, 0, 0)))
        nfont =  pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 25)
        text = nfont.render("To start playing, press any button", 1, (0, 0, 0))
    place_txt = txt.get_rect(center=(600, 100))
    text_place = text.get_rect(center=(600, 670))        

    
    while 1:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                pg.quit()
                file = open("credits.txt", "w")
                file.write(str(coins))
                file.close()
                exit()
            elif i.type == pg.KEYDOWN and i.key == pg.K_ESCAPE:
                start(language)
            elif i.type == pg.KEYUP:
                if truefalse == "True":
                    widget(language, coins)
                else:
                    ask(language, coins)
                
        screen.fill((255, 255, 255))
        screen.blit(txt, place_txt)
        for i in range(len(string)):
            screen.blit(string[i], (50, 150 + 50 * i))
        screen.blit(text, text_place)
        pg.display.update()    

def start(language):    
    screen = pg.display.set_mode((1200, 700))
    font = pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 40)
    txt = font.render("Большое Путешествие", 1, (0, 0, 0))
    place_txt = txt.get_rect(center=(600, 100))
    play = pg.Surface((400, 100))
    rools = pg.Surface((400, 100))
    play.fill((125, 125, 125))
    rools.fill((125, 125, 125))
    play_rect = play.get_rect(center=(600, 250))
    rools_rect = rools.get_rect(center=(600, 450))
    nfont = pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 30)

    #languages
    english = pg.image.load('England.png').convert()
    english = pg.transform.scale(english, (50, 50))
    english_place = english.get_rect(topleft=(1100, 150))
    russian = pg.image.load('Russia.png').convert()
    russian = pg.transform.scale(russian, (50, 50))
    russian_place = russian.get_rect(topleft=(1100, 200))

    file = open("name.txt", "r")
    name = file.read()
    file.close()

    file = open("first_time.txt", "r")
    t = file.read()
    file.close()

    if t == "False1":
        file = open("first_time.txt", "w")
        file.write("False")
        file.close()
    
    if language == "r":
        langPlay = "Играть"
        langRools = "Правила"
        if t != "False1":
            welcome = "С возвращением, "+name+"!"
        else:
            welcome = "Добро пожаловать, "+name+"!"
    elif language == "e":
        langPlay = "Play"
        langRools = "Rools"
        if t != "False1":
            welcome = "Welcome back, "+name+"!"
        else:
            welcome = "Welcome, "+name+"!"

    file = open("credits.txt", "r")
    coins = int(file.read())
    file.close()

    file = open("how_to_play.txt", "r")
    truefalse = file.read()
    file.close()
    
    setting = pg.image.load("settings.png").convert_alpha()
    setting = pg.transform.scale(setting, (70, 70))
    place_settings = setting.get_rect(topright=(1180, 20))
    
    while 1:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                pg.quit()
                file = open("credits.txt", "w")
                file.write(str(coins))
                file.close()
                exit()
        play_text = nfont.render(langPlay, 1, (255, 255, 255))
        rools_text = nfont.render(langRools, 1, (255, 255, 255))
        ptxt_place = play_text.get_rect(center=(600, 250))
        rtxt_place = rools_text.get_rect(center=(600, 450))
        place_txt = txt.get_rect(center=(600, 100))
        welcome_text = nfont.render(welcome, 1, (0, 0, 0))
        place_wtxt = welcome_text.get_rect(center=(600, 40))
    
        pressed = pg.mouse.get_pressed()
        pos = pg.mouse.get_pos()

        if pressed[0] and play_rect.collidepoint(pos):
            if truefalse == "True":
                widget(language, coins)
            else:
                ask(language, coins)
        elif pressed[0] and rools_rect.collidepoint(pos):
            rool(language, coins)
        try:
            if pressed[0] and english_place.collidepoint(pos):
                langPlay = "Play"
                langRools = "Rools"
                if t != "False1":
                    welcome = "Welcome back, "+name+"!"
                else:
                    welcome = "Welcome, "+name+"!"
                language = "e"
            elif pressed[0] and russian_place.collidepoint(pos):
                langPlay = "Играть"
                langRools = "Правила"
                if t != "False1":
                    welcome = "С возвращением, "+name+"!"
                else:
                    welcome = "Добро пожаловать, "+name+"!"
                language = "r"
                
            if language == "r":
                txt = font.render("Большое Путешествие", 1, (0, 0, 0))
            elif language == "e":
                txt = font.render("Big Trip", 1, (0, 0, 0))        
        except AttributeError:
            language = language

        if pressed[0] and place_settings.collidepoint(pos):
            settings(language)
                
        screen.fill((255, 255, 255))
        screen.blit(txt, place_txt)
        screen.blit(play, play_rect)
        screen.blit(rools, rools_rect)
        screen.blit(english, english_place)
        screen.blit(russian, russian_place)
        screen.blit(play_text, ptxt_place)
        screen.blit(rools_text, rtxt_place)
        screen.blit(setting, place_settings)
        screen.blit(welcome_text, place_wtxt)
        pg.display.update()
        
def single(language, coins):    
    def choose(language, coins):
        car = 0
        no_money = False
        success = False
        unsuccess = [False, False]
        already_bought = []
        specifications = {"sencibility" : [1, 2, 2, 2, 3, 3, 4, 5], "lives" : [1, 1, 1, 1, 2, 2, 3, 4], "price" : [0, 10, 15, 20, 30, 40, 45, 65]}


        file = open("cars.txt", "r")
        for line in file:
            if  "True" in line:
                already_bought.append(True)
            else:
                already_bought.append(False)

        file.close()
      
        screen = pg.display.set_mode((1200, 700))
        font = pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 40)
        names = []
        places_names = []
        images = ['car5.png', 'car6.png', 'car7.png', 'car2.png', 'car4.png', 'car3.png', 'car1.png', 'car8.png']
        places_images = []
        sencibility = []
        places_sencibility = []
        lives = []
        places_lives = []
        price = []
        places_price = []

        if language == "r":
            txt = font.render("Выберите автомобиль", 1, (0, 0, 0))
            font = pg.font.Font('C:\\WINDOWS\\Fonts\\segoesc.ttf', 35)
            names.append(font.render("недоМосквич", 1, (0, 0, 0)))
            names.append(font.render("недоЖигуль", 1, (0, 0, 0)))
            names.append(font.render("недоМерседес", 1, (0, 0, 0)))
            names.append(font.render("недоТесла", 1, (0, 0, 0)))
            names.append(font.render("недоАстонМартин", 1, (0, 0, 0)))
            names.append(font.render("недоЛамборджини", 1, (0, 0, 0)))
            names.append(font.render("недоФеррари", 1, (0, 0, 0)))
            names.append(font.render("недоБугатти", 1, (0, 0, 0)))
            font =  pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 25)
            text = font.render("Чтобы начать игру, 2 раза нажмите на любую клавишу", 1, (0, 0, 0))
            money = font.render("Данный автомобиль не куплен", 1, (255, 0, 0))
            notenough = font.render("Недостаточно средств на счету", 1, (255, 0, 0))
            already = font.render("Вы уже купили данный автомобиль", 1, (255, 0, 0))
            ifsuccess = font.render("Поздравляем! Вы приобрели данный автомобиль!", 1, (0, 255, 0))
            
        elif language == "e":
            txt = font.render("Choose your car", 1, (0, 0, 0))
            font = pg.font.Font('C:\\WINDOWS\\Fonts\\segoesc.ttf', 35)
            names.append(font.render("almostFord", 1, (0, 0, 0)))
            names.append(font.render("almostJeep", 1, (0, 0, 0)))
            names.append(font.render("almostMercedes", 1, (0, 0, 0)))
            names.append(font.render("almostTesla", 1, (0, 0, 0)))
            names.append(font.render("almostAstonMartin", 1, (0, 0, 0)))
            names.append(font.render("almostLamborghini", 1, (0, 0, 0)))
            names.append(font.render("almostFerrari", 1, (0, 0, 0)))
            names.append(font.render("almostBugatti", 1, (0, 0, 0)))
            font =  pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 25)
            text = font.render("To start the game, press any button twice", 1, (0, 0, 0))
            money = font.render("You hasn't bought this car yet", 1, (255, 0, 0))
            notenough = font.render("Not enough money to buy this car", 1, (255, 0, 0))
            already = font.render("You has already bought this car", 1, (255, 0, 0))
            ifsuccess = font.render("Hooray!!! You bought this car!", 1, (0, 255, 0))

        place_txt = txt.get_rect(center=(600, 100))
        text_place = text.get_rect(center=(600, 610))
        place_money = money.get_rect(center=(600, 570))
        place_notenough = notenough.get_rect(center=(600, 570))
        place_already = already.get_rect(center=(600, 570))
        place_ifsuccess = ifsuccess.get_rect(center=(600, 570))
            
        for i in range(8):
            images[i] = pg.image.load(images[i]).convert_alpha()
            images[i] = pg.transform.scale(images[i], (images[i].get_width() * 4, images[i].get_height() * 4))
            places_names.append(names[i].get_rect(center=(600, 190)))
            places_images.append(images[i].get_rect(center=(600, 330)))
            if language == "r":
                if str(specifications["price"][i])[-1] >= "5" and str(specifications["price"][i])[-1] <= "9" or str(specifications["price"][i])[-1] == "0" or specifications["price"][i] >= 11 and specifications["price"][i] <= 14:
                    grammar = " монет"
                elif str(specifications["price"][i])[-1] >= "2" and str(specifications["price"][i])[-1] <= "4":
                    grammar = " монеты"
                else:
                    grammar = " монета"
                    
                sencibility.append(font.render("Управляемость:"+str(specifications["sencibility"][i])+"/5", 1, (0, 0, 0)))
                lives.append(font.render("Жизни:"+str(specifications["lives"][i]), 1, (0, 0, 0)))
                if not already_bought[i]:
                    price.append(font.render("Цена:"+str(specifications["price"][i])+grammar, 1, (0, 0, 0)))
                else:
                    price.append(font.render("Цена:"+str(specifications["price"][i])+grammar, 1, (0, 255, 0)))
            elif language == "e":
                sencibility.append(font.render("Manageability:"+str(specifications["sencibility"][i])+"/5", 1, (0, 0, 0)))
                lives.append(font.render("Lives:"+str(specifications["lives"][i]), 1, (0, 0, 0)))
                if not already_bought[i]:
                    price.append(font.render("Price:"+str(specifications["price"][i])+" coins", 1, (0, 0, 0)))
                else:
                    price.append(font.render("Price:"+str(specifications["price"][i])+" coins", 1, (0, 255, 0)))
           
            places_sencibility.append(sencibility[i].get_rect(center=(600, 450)))
            places_lives.append(lives[i].get_rect(center=(600, 490)))
            places_price.append(price[i].get_rect(center=(600, 530)))
        while 1:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    pg.quit()
                    file = open("credits.txt", "w")
                    file.write(str(coins))
                    file.close()
                    exit()
                elif i.type == pg.KEYDOWN:
                    if i.key == pg.K_LEFT:
                        car -= 1
                        no_money = False
                        success = False
                        unsuccess = [False, False]
                    elif i.key == pg.K_RIGHT:
                        no_money = False
                        success = False
                        unsuccess = [False, False]
                        car += 1

                    elif i.key == pg.K_RETURN:
                        if not already_bought[car % 8]:
                            if coins >= specifications["price"][car % 8]:
                                already_bought[car % 8] = True
                                no_money = False
                                unsuccess = [False, False]
                                coins -= specifications["price"][car % 8]
                                success = True
                                g = open("cars.txt", "w")
                                for i in already_bought:
                                    g.write(str(i)+"\n")
                                g.close()
                            else:
                                unsuccess[1] = True
                                no_money = False
                                success = False
                                unsuccess[0] = False
                        else:
                            unsuccess[0] = True
                            no_money = False
                            success = False
                            unsuccess[1] = False
                    elif i.key == pg.K_ESCAPE:
                        start(language)
                    else:
                        if already_bought[car % 8]:
                            cmode(car % 8, specifications["sencibility"][car % 8], specifications["lives"][car % 8], language, coins)
                        else:
                            no_money = True

            if language == "r":
                if str(coins)[-1] >= "5" and str(coins)[-1] <= "9" or str(coins)[-1] == "0" or coins >= 11 and coins <=14:
                    grammar = " монет"
                elif str(coins)[-1] >= "2" and str(coins)[-1] <= "4":
                    grammar = " монеты"
                else:
                    grammar = " монета"
                yourmoney = font.render("У вас на счету "+str(coins)+grammar, 1, (0, 0, 0))
            elif language == "e":
                if coins != 1:
                    grammar = " coins"
                else:
                    grammar = " coin"
                yourmoney = font.render("You have "+str(coins)+grammar, 1, (0, 0, 0))
            place_yourmoney = yourmoney.get_rect(center=(1000, 50))
            
            screen.fill((255, 255, 255))
            screen.blit(names[car % 8], places_names[car % 8])
            screen.blit(images[car % 8], places_images[car % 8])
            screen.blit(sencibility[car % 8], places_sencibility[car % 8])
            screen.blit(lives[car % 8], places_lives[car % 8])
            screen.blit(price[car % 8], places_price[car % 8])
            screen.blit(txt, place_txt)
            screen.blit(yourmoney, place_yourmoney)
            screen.blit(text, text_place)

            #print(no_money, success, unsuccess)

            if no_money:
                screen.blit(money, place_money)
            if success:
                screen.blit(ifsuccess, place_ifsuccess)
            if unsuccess[0]:
                screen.blit(already, place_already)
            if unsuccess[1]:
                screen.blit(notenough, place_notenough)
                
            pg.display.update()    

    def cmode(car, sencibility, lives, language, coins):
        screen = pg.display.set_mode((1200, 700))

        nfont = pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 40)
        font = pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 30)

        flag = False
        
        if language == "r":
            mode = nfont.render("Выберите режим игры", 1, (0, 0, 0))
            easy = font.render("Лёгкий", 1, (0, 0, 0))
            medium = font.render("Средний", 1, (0, 0, 0))
            hard = font.render("Сложный", 1, (0, 0, 0))
            megahard = font.render("Мегасложный", 1, (0, 0, 0))
            cont = font.render("Чтобы начать игру, нажмите на любую клавишу", 1, (0, 0, 0))
            prices = [font.render("(нажмите 1)", 1, (0, 0, 0)), font.render("(нажмите 2)", 1, (0, 0, 0)), font.render("(нажмите 3)", 1, (0, 0, 0)), font.render("(нажмите 4)", 1, (0, 0, 0))]
        elif language == "e":
            mode = nfont.render("Please choose game mode", 1, (0, 0, 0))
            easy = font.render("Easy", 1, (0, 0, 0))
            medium = font.render("Medium", 1, (0, 0, 0))
            hard = font.render("Hard", 1, (0, 0, 0))
            megahard = font.render("Megahard", 1, (0, 0, 0))
            prices = [font.render("(press 1)", 1, (0, 0, 0)), font.render("(press 2)", 1, (0, 0, 0)), font.render("(press 3)", 1, (0, 0, 0)), font.render("(press 4)", 1, (0, 0, 0))]

        place = []
        for i in range(len(prices)):
            place.append(prices[i].get_rect(topleft=(100 + 250 * i, 250)))
        place_mode = mode.get_rect(center=(600, 100))
        place_easy = easy.get_rect(topleft=(100, 200))
        place_medium = medium.get_rect(topleft=(350, 200))
        place_hard = hard.get_rect(topleft=(600, 200))
        place_megahard = megahard.get_rect(topleft=(850, 200))

        while 1:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    pg.quit()
                    exit()
                elif i.type == pg.KEYDOWN:
                    if i.key == pg.K_ESCAPE:
                        start(language)
                    elif i.key == pg.K_1:
                        main(car, sencibility, lives, 1, language, coins)
                    elif i.key == pg.K_2:
                        main(car, sencibility, lives, 2, language, coins)
                    elif i.key == pg.K_3:
                        main(car, sencibility, lives, 3, language, coins)
                    elif i.key == pg.K_4:
                        main(car, sencibility, lives, 4, language, coins)
                
            screen.fill((255, 255, 255))
            for i in range(len(prices)):
                screen.blit(prices[i], place[i])
            screen.blit(mode, place_mode)
            screen.blit(easy, place_easy)
            screen.blit(medium, place_medium)
            screen.blit(hard, place_hard)
            screen.blit(megahard, place_megahard)

            pg.display.update()
            
    def main(car, sencibility, lives, mode, language, coins):
        global score
        
        FPS = 60
        x = 600
        y = 650
        font = pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 30)
        if mode != 4:
            y1 = 50
            y2 = 225
            y3 = 400
            y4 = 575
        else:
            y1 = 0
            y2 = 175
            y3 = 350
            y4 = 525
        flag = False
        crashx = 0
        crashy = 0
        crash = None
        PAUSE = False
        FINISH = False

        file = open("colour.txt", "r")
        colour = int(file.read())
        file.close()

        SPAWN = pg.USEREVENT + 1

        if mode == 1:
            event = pg.time.set_timer(SPAWN, 4000)
        elif mode == 2:
            event = pg.time.set_timer(SPAWN, 3000)
        elif mode == 3:
            event = pg.time.set_timer(SPAWN, 1000)
        elif mode == 4:
            event = pg.time.set_timer(SPAWN, 500)
        
        if colour == 1:
            color1 = (0, 255, 0)
            color2 = (127, 127, 127)
            color3 = (255, 255, 255)
        else:
            color1 = (0, 125, 5)
            color2 = (95, 95, 95)
            color3 = (25, 25, 25)
        
        screen = pg.display.set_mode((1200, 700))

        enemies = ['car1.png', 'car2.png', 'car3.png', 'car4.png', 'car5.png', 'car6.png', 'car7.png', 'car8.png']
        for i in range(len(enemies)):
            enemies[i] = pg.image.load(enemies[i]).convert_alpha()
            enemies[i] = pg.transform.scale(enemies[i], (enemies[i].get_width() * 2, enemies[i].get_height() * 2))
        group = pg.sprite.Group()

        grass = pg.Surface((1200, 700))
        grass.fill(color1)
        grass_place = grass.get_rect(topleft=(0, 0))
        if mode == 1:
            road = pg.Surface((260, 700))
        elif mode == 2:
            road = pg.Surface((400, 700))
        elif mode == 3:
            road = pg.Surface((440, 700))
        elif mode == 4:
            road = pg.Surface((660, 700))
            
        road.fill(color2)
        if mode != 3:
            road_place = road.get_rect(center=(600, 350))
        else:
            road_place = road.get_rect(topleft=(350, 0))
        if mode != 4:
            line1 = pg.Surface((20, 70))
            line1.fill(color3)
            line2 = pg.Surface((20, 70))
            line2.fill(color3)
            line3 = pg.Surface((20, 70))
            line3.fill(color3)
            line4 = pg.Surface((20, 70))
            line4.fill(color3)
        else:
            line1 = pg.Surface((5, 175))
            line1.fill((255, 255, 255))
            line2 = pg.Surface((5, 175))
            line2.fill((255, 0, 0))
            line3 = pg.Surface((5, 175))
            line3.fill((255, 255, 255))
            line4 = pg.Surface((5, 175))
            line4.fill((255, 0, 0))
            
        if language == "r":
            howtocontinue = font.render("Чтобы продолжить, нажмите на любую клавишу", 1, (0, 0, 255))
        elif language == "e":
            howtocontinue = font.render("To continue, press any button", 1, (0, 0, 255))
            
        place_continue = howtocontinue.get_rect(center=(600, 240))

        if colour == 1:    
            live = pg.image.load('bright_live.png').convert_alpha()
        else:
            live = pg.image.load('dark_live.png').convert_alpha()
        live = pg.transform.scale(live, (80, 80))

        high_score = []

        if mode == 1:
            f = open("easy_hs.txt", "r")
        elif mode == 2:
            f = open("medium_hs.txt", "r")
        elif mode == 3:
            f = open("hard_hs.txt", "r")
        elif mode == 4:
            f = open("megahard_hs.txt", "r")
        
        for line in f:
            h = line
            high_score.append(int(h[:-1]))
        f.close()

        class Enemy(pg.sprite.Sprite):
            def __init__(self, x, file, group, speed, mode):
                pg.sprite.Sprite.__init__(self)
                self.image = file
                if mode == 1:
                    if x == 1:
                        self.rect = file.get_rect(center=(550, 0))
                    else:
                        self.rect = file.get_rect(center=(650, 0))
                elif mode == 2:
                    if x == 1:
                        self.rect = file.get_rect(center=(470, 0))
                    elif x == 2:
                        self.rect = file.get_rect(center=(595, 0))
                    else:
                        self.rect = file.get_rect(center=(735, 0))
                elif mode == 3:
                    if x == 1:
                        self.rect = file.get_rect(center=(405, 0))
                    elif x == 2:
                        self.rect = file.get_rect(center=(515, 0))
                    elif x == 3:
                        self.rect = file.get_rect(center=(610, 0))
                    else:
                        self.rect = file.get_rect(center=(725, 0))
                elif mode == 4:
                    if x == 1:
                        self.rect = file.get_rect(center=(340, 0))
                    elif x == 2:
                        self.rect = file.get_rect(center=(440, 0))
                    elif x == 3:
                        self.rect = file.get_rect(center=(540, 0))
                    elif x == 4:
                        self.rect = file.get_rect(center=(640, 0))
                    elif x == 5:
                        self.rect = file.get_rect(center=(740, 0))
                    else:
                        self.rect = file.get_rect(center=(855, 0))
                self.add(group)
                self.speed = 4 + speed
            def update(self):
                global score
                if self.rect.y < 700:
                    #self.image = pg.transform.scale(self.image, (self.rect.width + self.speed, self.rect.height))
                    #self.rect = self.image.get_rect(center=(self.x - self.speed, 0))
                    self.rect.y += self.speed
                    #self.rect.x -= 0.5 * self.speed
                else:
                    score += 1
                    self.kill()

        class Player(pg.sprite.Sprite):
            def __init__(self, x, y, file):
                pg.sprite.Sprite.__init__(self)
                self.image = file
                self.rect = file.get_rect(center=(x, y))

        while 1:
            if mode == 1:
                earn = (score + 2) // 3
            elif mode == 2:
                earn = score // 3
            elif mode == 3:
                earn = (score + 4) // 5
            elif mode == 4:
                earn = score // 6
            if score > high_score[car]:
                high_score[car] = score
                if mode == 1:
                    g = open("easy_hs.txt", "w")
                elif mode == 2:
                    g = open("medium_hs.txt", "w")
                elif mode == 3:
                    g = open("hard_hs.txt", "w")
                elif mode == 4:
                    g = open("megahard_hs.txt", "w")
                for i in range(len(high_score)):
                    g.write(str(high_score[i])+"\n")
                g.close()
            if car == 0:
                player = Player(x, y, pg.transform.scale(pg.image.load('car5.png').convert_alpha(), (pg.image.load('car3.png').convert_alpha().get_width() * 2, pg.image.load('car3.png').convert_alpha().get_height() * 2)))
            elif car == 1:
                player = Player(x, y, pg.transform.scale(pg.image.load('car6.png').convert_alpha(), (pg.image.load('car3.png').convert_alpha().get_width() * 2, pg.image.load('car3.png').convert_alpha().get_height() * 2)))
            elif car == 2:
                player = Player(x, y, pg.transform.scale(pg.image.load('car7.png').convert_alpha(), (pg.image.load('car3.png').convert_alpha().get_width() * 2, pg.image.load('car3.png').convert_alpha().get_height() * 2)))
            elif car == 3:
                player = Player(x, y, pg.transform.scale(pg.image.load('car2.png').convert_alpha(), (pg.image.load('car3.png').convert_alpha().get_width() * 2, pg.image.load('car3.png').convert_alpha().get_height() * 2)))
            elif car == 4:
                player = Player(x, y, pg.transform.scale(pg.image.load('car4.png').convert_alpha(), (pg.image.load('car3.png').convert_alpha().get_width() * 2, pg.image.load('car3.png').convert_alpha().get_height() * 2)))
            elif car == 5:
                player = Player(x, y, pg.transform.scale(pg.image.load('car3.png').convert_alpha(), (pg.image.load('car3.png').convert_alpha().get_width() * 2, pg.image.load('car3.png').convert_alpha().get_height() * 2)))
            elif car == 6:
                player = Player(x, y, pg.transform.scale(pg.image.load('car1.png').convert_alpha(), (pg.image.load('car3.png').convert_alpha().get_width() * 2, pg.image.load('car3.png').convert_alpha().get_height() * 2)))
            elif car == 7:
                player = Player(x, y, pg.transform.scale(pg.image.load('car8.png').convert_alpha(), (pg.image.load('car3.png').convert_alpha().get_width() * 2, pg.image.load('car3.png').convert_alpha().get_height() * 2)))

            if mode != 4:
                whatline = random.randint(1, mode + 1)
            else:
                whatline = random.randint(1, 6)
                
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    pg.quit()
                    file = open("credits.txt", "w")
                    file.write(str(coins))
                    file.close()
                    exit()
                elif i.type == pg.KEYUP:
                    if i.key == pg.K_SPACE:
                        PAUSE = True
                    elif i.key == pg.K_ESCAPE:
                        score = 0
                        start(language)
                elif i.type == SPAWN:
                    Enemy(whatline, enemies[random.randint(0, len(enemies) - 1)], group, score // 2, mode)
            pressed = pg.key.get_pressed()
            if pressed[pg.K_LEFT] or pressed[pg.K_a]:
                x -= sencibility
            if pressed[pg.K_RIGHT] or pressed[pg.K_d]:
                x += sencibility
            if pressed[pg.K_UP] or pressed[pg.K_w]:
                y -= sencibility
            if pressed[pg.K_DOWN] or pressed[pg.K_s]:
                y += sencibility
            if mode == 4:
                if x >= 900: 
                    x = 900
                elif x <= 310: 
                    x = 310
            elif mode == 1:
                if x >= 700: 
                    x = 700
                elif x <= 500: 
                    x = 500
            elif mode == 2:
                if x >= 770: 
                    x = 770
                elif x <= 430: 
                    x = 430
            elif mode == 3:
                if x >= 760:
                    x = 760
                elif x <= 380: 
                    x = 380
            
            if y <= 550:
                y = 550
            elif y >= 650:
                y = 650
            if pg.sprite.spritecollideany(player, group):
                lives -= 1
                if lives < 1:
                    flag = True
                else:
                    time.sleep(1)
                    main(car, sencibility, lives, mode, language, coins)
            y1 += (4 + score // 4) * 2
            y2 += (4 + score // 4) * 2
            y3 += (4 + score // 4) * 2
            y4 += (4 + score // 4) * 2
            if y1 >= 700:
                y1 = 0
            elif y2 >= 700:
                y2 = 0
            elif y3 >= 700:
                y3 = 0
            elif y4 >= 700:
                y4 = 0
                
            if (score + 2) // 3 > 0:
                color = (0, 0, 255)
            else:
                color = (255, 0, 0)
            
            if PAUSE:
                while PAUSE:
                    time.sleep(0.1)
                    for i in pg.event.get():
                        if i.type == pg.QUIT:
                            pg.quit()
                            exit()
                        elif i.type == pg.KEYUP:
                            if i.key == pg.K_SPACE:
                                PAUSE = False
                            elif i.key == pg.K_ESCAPE:
                                score = 0
                                start(language)
            if FINISH:
                coins += earn
                file = open("credits.txt", "w")
                file.write(str(coins))
                file.close()
                while FINISH:
                    time.sleep(0.1)
                    for i in pg.event.get():
                        if i.type == pg.QUIT:
                            pg.quit()
                            exit()
                        elif i.type == pg.KEYDOWN:
                            FINISH = False
                            score = 0
                            start(language)

            if language == "r":
                if str((score + 2) // 3)[-1] >= "5" and str((score + 2) // 3)[-1] <= "9" or str((score + 2) // 3)[-1] == "0" or (score + 2) // 3 >= 11 and (score + 2) // 3 <=14:
                    grammar = " монет"
                elif str((score + 2) // 3)[-1] >= "2" and str((score + 2) // 3)[-1] <= "4":
                    grammar = " монеты"
                else:
                    grammar = " монету"
                    
                uearn = font.render("Вы заработали "+str(earn)+grammar, 1, color)
                text = font.render("Ваш счёт:"+str(score), 1, (0, 0, 0))
                hs = font.render("Ваш рекорд:"+str(high_score[car]), 1, (0, 0, 0))
            elif language == "e":
                if (score + 2) // 3 != 1:
                    grammar = " coins"
                else:
                    grammar = " coin"
                uearn = font.render("You earned "+str(earn)+grammar, 1, color)
                text = font.render("Your score:"+str(score), 1, (0, 0, 0))
                hs = font.render("Your best score:"+str(high_score[car]), 1, (0, 0, 0))
            place_earnings = uearn.get_rect(center=(600, 200))
            text_place = text.get_rect(center=(600, 120))
            hs_place = hs.get_rect(center=(600, 150))
            screen.fill((255, 255, 255))
            screen.blit(grass, grass_place)
            screen.blit(road, road_place)
            if mode == 1:
                screen.blit(line1, (590, y1))
                screen.blit(line2, (590, y2))
                screen.blit(line3, (590, y3))
                screen.blit(line4, (590, y4))
            elif mode == 2:
                screen.blit(line1, (520, y1))
                screen.blit(line2, (520, y2))
                screen.blit(line3, (520, y3))
                screen.blit(line4, (520, y4))
                screen.blit(line1, (660, y1))
                screen.blit(line2, (660, y2))
                screen.blit(line3, (660, y3))
                screen.blit(line4, (660, y4))
            elif mode == 3:
                screen.blit(line1, (440, y1))
                screen.blit(line2, (440, y2))
                screen.blit(line3, (440, y3))
                screen.blit(line4, (440, y4))
                screen.blit(line1, (555, y1))
                screen.blit(line2, (555, y2))
                screen.blit(line3, (555, y3))
                screen.blit(line4, (555, y4))
                screen.blit(line1, (665, y1))
                screen.blit(line2, (665, y2))
                screen.blit(line3, (665, y3))
                screen.blit(line4, (665, y4))
            elif mode == 4:
                screen.blit(line1, (270, y1))
                screen.blit(line2, (270, y2))
                screen.blit(line3, (270, y3))
                screen.blit(line4, (270, y4))
                screen.blit(line1, (930, y1))
                screen.blit(line2, (930, y2))
                screen.blit(line3, (930, y3))
                screen.blit(line4, (930, y4))
                    
            screen.blit(text, text_place)
            screen.blit(hs, hs_place)
            screen.blit(player.image, player.rect)
            group.draw(screen)
            if flag:
                screen.blit(howtocontinue, place_continue)
                screen.blit(uearn, place_earnings)
                FINISH = True
            if lives < 4 or mode != 4:
                for i in range(lives):
                    screen.blit(live, (1100 - 80 * i, 80))
            else:
                for i in range(3):
                    screen.blit(live, (1100 - 80 * i, 80))
                screen.blit(live, (1100, 160))
            pg.display.update()
            clock.tick(FPS)
            group.update()

    choose(language, coins)

def multi(language):
    def choose1(language):
        car = 0
      
        screen = pg.display.set_mode((1200, 700))
        font = pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 40)
        names = []
        places_names = []
        images = ['car5.png', 'car6.png', 'car7.png', 'car2.png', 'car4.png', 'car3.png', 'car1.png']
        places_images = []

        if language == "r":
            txt = font.render("Выберите автомобиль", 1, (0, 0, 0))
            font = pg.font.Font('C:\\WINDOWS\\Fonts\\segoesc.ttf', 35)
            names.append(font.render("Машинка1", 1, (0, 0, 0)))
            names.append(font.render("Машинка2", 1, (0, 0, 0)))
            names.append(font.render("Машинка3", 1, (0, 0, 0)))
            names.append(font.render("Машинка4", 1, (0, 0, 0)))
            names.append(font.render("Машинка5", 1, (0, 0, 0)))
            names.append(font.render("Машинка6", 1, (0, 0, 0)))
            names.append(font.render("Машинка7", 1, (0, 0, 0)))
            font =  pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 25)
            text = font.render("Чтобы продолжить, нажмите на любую клавишу", 1, (0, 0, 0))
            
        elif language == "e":
            txt = font.render("Choose your car", 1, (0, 0, 0))
            font = pg.font.Font('C:\\WINDOWS\\Fonts\\segoesc.ttf', 35)
            names.append(font.render("Car1", 1, (0, 0, 0)))
            names.append(font.render("Car2", 1, (0, 0, 0)))
            names.append(font.render("Car3", 1, (0, 0, 0)))
            names.append(font.render("Car4", 1, (0, 0, 0)))
            names.append(font.render("Car5", 1, (0, 0, 0)))
            names.append(font.render("Car6", 1, (0, 0, 0)))
            names.append(font.render("Car7", 1, (0, 0, 0)))
            font =  pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 25)
            text = font.render("To continue, press any button", 1, (0, 0, 0))

        place_txt = txt.get_rect(center=(600, 100))
        text_place = text.get_rect(center=(600, 500))
            
        for i in range(7):
            images[i] = pg.image.load(images[i]).convert_alpha()
            images[i] = pg.transform.scale(images[i], (images[i].get_width() * 4, images[i].get_height() * 4))
            places_names.append(names[i].get_rect(center=(600, 190)))
            places_images.append(images[i].get_rect(center=(600, 330)))
                    
        while 1:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    pg.quit()
                    exit()
                elif i.type == pg.KEYDOWN:
                    if i.key == pg.K_LEFT:
                        car -= 1
                    elif i.key == pg.K_RIGHT:
                        car += 1
                    elif i.key == pg.K_ESCAPE:
                        start(language)
                    else:
                        choose2(car % 8, language)
            
            screen.fill((255, 255, 255))
            screen.blit(names[car % 8], places_names[car % 8])
            screen.blit(images[car % 8], places_images[car % 8])
            screen.blit(txt, place_txt)
            screen.blit(text, text_place)
                
            pg.display.update()    

    def choose2(fcar, language):
        car = 0
      
        screen = pg.display.set_mode((1200, 700))
        font = pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 40)
        names = []
        places_names = []
        images = ['car5.png', 'car6.png', 'car7.png', 'car2.png', 'car4.png', 'car3.png', 'car1.png']
        places_images = []

        if language == "r":
            txt = font.render("Выберите автомобиль", 1, (0, 0, 0))
            font = pg.font.Font('C:\\WINDOWS\\Fonts\\segoesc.ttf', 35)
            names.append(font.render("Машинка1", 1, (0, 0, 0)))
            names.append(font.render("Машинка2", 1, (0, 0, 0)))
            names.append(font.render("Машинка3", 1, (0, 0, 0)))
            names.append(font.render("Машинка4", 1, (0, 0, 0)))
            names.append(font.render("Машинка5", 1, (0, 0, 0)))
            names.append(font.render("Машинка6", 1, (0, 0, 0)))
            names.append(font.render("Машинка7", 1, (0, 0, 0)))
            font =  pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 25)
            text = font.render("Чтобы продолжить, нажмите на любую клавишу", 1, (0, 0, 0))
            
        elif language == "e":
            txt = font.render("Choose your car", 1, (0, 0, 0))
            font = pg.font.Font('C:\\WINDOWS\\Fonts\\segoesc.ttf', 35)
            names.append(font.render("Car1", 1, (0, 0, 0)))
            names.append(font.render("Car2", 1, (0, 0, 0)))
            names.append(font.render("Car3", 1, (0, 0, 0)))
            names.append(font.render("Car4", 1, (0, 0, 0)))
            names.append(font.render("Car5", 1, (0, 0, 0)))
            names.append(font.render("Car6", 1, (0, 0, 0)))
            names.append(font.render("Car7", 1, (0, 0, 0)))
            font =  pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 25)
            text = font.render("To continue, press any button", 1, (0, 0, 0))

        place_txt = txt.get_rect(center=(600, 100))
        text_place = text.get_rect(center=(600, 500))
            
        for i in range(7):
            images[i] = pg.image.load(images[i]).convert_alpha()
            images[i] = pg.transform.scale(images[i], (images[i].get_width() * 4, images[i].get_height() * 4))
            places_names.append(names[i].get_rect(center=(600, 190)))
            places_images.append(images[i].get_rect(center=(600, 330)))
                    
        while 1:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    pg.quit()
                    exit()
                elif i.type == pg.KEYDOWN:
                    if i.key == pg.K_LEFT:
                        car -= 1
                    elif i.key == pg.K_RIGHT:
                        car += 1
                    elif i.key == pg.K_ESCAPE:
                        start(language)
                    else:
                        main(fcar, car % 8, language)
            
            screen.fill((255, 255, 255))
            screen.blit(names[car % 8], places_names[car % 8])
            screen.blit(images[car % 8], places_images[car % 8])
            screen.blit(txt, place_txt)
            screen.blit(text, text_place)
                
            pg.display.update()  
    
    def main(car1, car2, language):
        global score1, score2
        
        FPS = 60
        x1 = 300
        y11 = 650
        x2 = 900
        y22 = 650
        font = pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 30)
        y1 = 50
        y2 = 225
        y3 = 400
        y4 = 575
        y5 = 50
        y6 = 225
        y7 = 400
        y8 = 575
        flag1, flag2 = False, False
        lives1, lives2 = 1, 1
        score1, score2 = 0, 0
        f1, f2 = 0, 0
        crashx = 0
        crashy = 0
        crash = None
        PAUSE = False
        FINISH = False
        flag = True
        t = time.time()
        
        file = open("colour.txt", "r")
        colour = int(file.read())
        file.close()

        if colour == 1:
            color1 = (0, 255, 0)
            color2 = (127, 127, 127)
            color3 = (255, 255, 255)
        else:
            color1 = (0, 125, 5)
            color2 = (95, 95, 95)
            color3 = (25, 25, 25)
        
        screen = pg.display.set_mode((1200, 700))
        pg.time.set_timer(pg.USEREVENT, 4000)

        surf = pg.Surface((5, 700))
        surf_place = surf.get_rect(center=(600, 350))
        
        enemies = ['car1.png', 'car2.png', 'car3.png', 'car4.png', 'car5.png', 'car6.png', 'car7.png', 'car8.png']
        cars = ['car5.png', 'car6.png', 'car7.png', 'car2.png', 'car4.png', 'car3.png', 'car1.png', 'car8.png']
        for i in range(len(enemies)):
            enemies[i] = pg.image.load(enemies[i]).convert_alpha()
            enemies[i] = pg.transform.scale(enemies[i], (enemies[i].get_width() * 2, enemies[i].get_height() * 2))

        group1 = pg.sprite.Group()
        group2 = pg.sprite.Group()
        
        grass = pg.Surface((1200, 700))
        grass.fill(color1)
        grass_place = grass.get_rect(topleft=(0, 0))
        road = pg.Surface((260, 700))
        road.fill(color2)
        road1_place = road.get_rect(center=(300, 350))
        road2_place = road.get_rect(center=(900, 350))
        line1 = pg.Surface((20, 70))
        line1.fill(color3)
        line2 = pg.Surface((20, 70))
        line2.fill(color3)
        line3 = pg.Surface((20, 70))
        line3.fill(color3)
        line4 = pg.Surface((20, 70))
        line4.fill(color3)
        if language == "r":
            howtocontinue = font.render("Чтобы продолжить, нажмите на любую клавишу", 1, (0, 0, 255))
            wait = font.render("Подождите другого игрока", 1, (0, 0, 255))
            manage = font.render("Чтобы управлять машинкой, используйте:", 1, (0, 0, 255))
            wasd = font.render("Кнопки WASD", 1, (0, 0, 255))
            arrows = font.render("Стрелочки", 1, (0, 0, 255))
        elif language == "e":
            howtocontinue = font.render("To continue, press any button", 1, (0, 0, 255))
            wait = font.render("Please wait for your partner", 1, (0, 0, 255))
            manage = font.render("To manage a car please use:", 1, (0, 0, 255))
            wasd = font.render("WASD-buttons", 1, (0, 0, 255))
            arrows = font.render("Arrows", 1, (0, 0, 255))
            
        place_continue = howtocontinue.get_rect(center=(600, 240))
        place1_wait = wait.get_rect(topleft=(50, 240))
        place2_wait = wait.get_rect(topleft=(650, 240))
        place_manage = manage.get_rect(center=(600, 100))
        place_wasd = wasd.get_rect(center=(300, 150))
        place_arrows = arrows.get_rect(center=(900, 150))

        if colour == 1:    
            live = pg.image.load('bright_live.png').convert_alpha()
        else:
            live = pg.image.load('dark_live.png').convert_alpha()
        live = pg.transform.scale(live, (80, 80))

        class Enemy1(pg.sprite.Sprite):
            def __init__(self, x, file, group, speed):
                pg.sprite.Sprite.__init__(self)
                self.image = file
                if x == 1:
                    self.rect = file.get_rect(center=(250, 0))
                else:
                    self.rect = file.get_rect(center=(350, 0))
                    
                self.add(group)
                self.speed = 4 + speed
            def update(self):
                global score1
                if self.rect.y < 700:
                    #self.image = pg.transform.scale(self.image, (self.rect.width + self.speed, self.rect.height))
                    #self.rect = self.image.get_rect(center=(self.x - self.speed, 0))
                    self.rect.y += self.speed
                    #self.rect.x -= 0.5 * self.speed
                else:
                    score1 += 1
                    self.kill()
                    
        class Enemy2(pg.sprite.Sprite):
            def __init__(self, x, file, group, speed):
                pg.sprite.Sprite.__init__(self)
                self.image = file
                if x == 1:
                    self.rect = file.get_rect(center=(850, 0))
                else:
                    self.rect = file.get_rect(center=(950, 0))
                
                self.add(group)
                self.speed = 4 + speed
            def update(self):
                global score2
                if self.rect.y < 700:
                    #self.image = pg.transform.scale(self.image, (self.rect.width + self.speed, self.rect.height))
                    #self.rect = self.image.get_rect(center=(self.x - self.speed, 0))
                    self.rect.y += self.speed
                    #self.rect.x -= 0.5 * self.speed
                else:
                    score2 += 1
                    self.kill()
                    
        class Player(pg.sprite.Sprite):
            def __init__(self, x, y, file):
                pg.sprite.Sprite.__init__(self)
                self.image = file
                self.x = x
                self.y = y
                self.rect = file.get_rect(center=(self.x, self.y))
                
        while 1:
            player1 = Player(x1, y11, pg.transform.scale(pg.image.load(cars[car1]).convert_alpha(), (pg.image.load('car3.png').convert_alpha().get_width() * 2, pg.image.load('car3.png').convert_alpha().get_height() * 2)))
            player2 = Player(x2, y22, pg.transform.scale(pg.image.load(cars[car2]).convert_alpha(), (pg.image.load('car3.png').convert_alpha().get_width() * 2, pg.image.load('car3.png').convert_alpha().get_height() * 2)))
            whatline1 = random.randint(1, 2)
            whatline2 = random.randint(1, 2)
            
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    pg.quit()
                    exit()
                elif i.type == pg.KEYUP:
                    if i.key == pg.K_SPACE:
                        PAUSE = True
                    elif i.key == pg.K_ESCAPE:
                        start(language)
                elif i.type == pg.USEREVENT:
                    if not flag1:
                        Enemy1(whatline1, enemies[random.randint(0, len(enemies) - 1)], group1, score1 // 2)
                    if not flag2:
                        Enemy2(whatline2, enemies[random.randint(0, len(enemies) - 1)], group2, score2 // 2)
                    
            pressed = pg.key.get_pressed()
            if not flag2:
                if pressed[pg.K_LEFT]:
                    x2 -= 3
                if pressed[pg.K_RIGHT]:
                    x2 += 3
                if pressed[pg.K_UP]:
                    y22 -= 3
                if pressed[pg.K_DOWN]:
                    y22 += 3
            if not flag1:
                if pressed[pg.K_a]:
                    x1 -= 3
                if pressed[pg.K_d]:
                    x1 += 3
                if pressed[pg.K_w]:
                    y11 -= 3
                if pressed[pg.K_s]:
                    y11 += 3

            if flag:
                t2 = time.time()

                if t2 - t >= 3:
                    flag = False
            
            if x1 >= 400:
                x1 = 400
            elif x1 <= 200:
                x1 = 200
            if y11 <= 550:
                y11 = 550
            elif y11 >= 650:
                y11 = 650
            if x2 >= 1000:
                x2 = 1000
            elif x2 <= 800:
                x2 = 800
            if y22 <= 550:
                y22 = 550
            elif y22 >= 650:
                y22 = 650
            if pg.sprite.spritecollideany(player1, group1):
                flag1 = True
            if pg.sprite.spritecollideany(player2, group2):
                flag2 = True
            if not flag1:
                y1 += (4 + score1 // 4) * 2
                y2 += (4 + score1 // 4) * 2
                y3 += (4 + score1 // 4) * 2
                y4 += (4 + score1 // 4) * 2
            if not flag2:
                y5 += (4 + score2 // 4) * 2
                y6 += (4 + score2 // 4) * 2
                y7 += (4 + score2 // 4) * 2
                y8 += (4 + score2 // 4) * 2
            if y1 >= 700:
                y1 = 0
            elif y2 >= 700:
                y2 = 0
            elif y3 >= 700:
                y3 = 0
            elif y4 >= 700:
                y4 = 0
            if y5 >= 700:
                y5 = 0
            elif y6 >= 700:
                y6 = 0
            elif y7 >= 700:
                y7 = 0
            elif y8 >= 700:
                y8 = 0
            
            if PAUSE:
                while PAUSE:
                    time.sleep(0.1)
                    for i in pg.event.get():
                        if i.type == pg.QUIT:
                            pg.quit()
                            exit()
                        elif i.type == pg.KEYUP:
                            if i.key == pg.K_SPACE:
                                PAUSE = False
                            elif i.key == pg.K_ESCAPE:
                                start(language)
            if FINISH:
                while FINISH:
                    time.sleep(0.1)
                    for i in pg.event.get():
                        if i.type == pg.QUIT:
                            pg.quit()
                            exit()
                        elif i.type == pg.KEYDOWN:
                            FINISH = False
                            result(language, score1, score2)

            if language == "r":
                text = font.render("Ваш счёт:"+str(score1), 1, (0, 0, 0))
                text2= font.render("Ваш счёт:"+str(score2), 1, (0, 0, 0))
            elif language == "e":
                text = font.render("Your score:"+str(score1), 1, (0, 0, 0))
                text2 = font.render("Your score:"+str(score2), 1, (0, 0, 0))
                
            text_place = text.get_rect(center=(300, 120))
            text2_place = text2.get_rect(center=(900, 120))
            
            screen.fill((255, 255, 255))
            screen.blit(grass, grass_place)
            screen.blit(road, road1_place)
            screen.blit(road, road2_place)
            screen.blit(line1, (290, y1))
            screen.blit(line2, (290, y2))
            screen.blit(line3, (290, y3))
            screen.blit(line4, (290, y4))
            screen.blit(line1, (890, y5))
            screen.blit(line2, (890, y6))
            screen.blit(line3, (890, y7))
            screen.blit(line4, (890, y8))
            screen.blit(text, text_place)
            screen.blit(text2, text2_place)
            screen.blit(surf, surf_place)
            screen.blit(player1.image, player1.rect)
            screen.blit(player2.image, player2.rect)
            group1.draw(screen)
            group2.draw(screen)
            if flag1:
                if f1 < 3:
                    f1 += 1
                if f1 == 1:
                    score1 -= 1
                if flag2:
                    screen.blit(howtocontinue, place_continue)
                    FINISH = True
                else:
                    screen.blit(wait, place1_wait)
            if flag2:
                if f2 < 3:
                    f2 += 1
                if f2 == 1:
                    score2 -= 1
                if flag1:
                    screen.blit(howtocontinue, place_continue)
                    FINISH = True
                else:
                    screen.blit(wait, place2_wait)

            for i in range(lives2):
                screen.blit(live, (1100 - 80 * i, 80))
            for i in range(lives1):
                screen.blit(live, (50 + 80 * i, 80))

            if flag:
                screen.blit(manage, place_manage)
                screen.blit(wasd, place_wasd)
                screen.blit(arrows, place_arrows)
                time.sleep(0.1)
                
            pg.display.update()
            clock.tick(FPS)
            group1.update()
            group2.update()

    def result(language, score1, score2):
        #score12 = 0
        
        font = pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 50)
        nfont = pg.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 30)
        
        flag1 = True
        flag2 = False
        t1 = time.time()
        
        screen = pg.display.set_mode((1200, 700))

        if language == "r":
            congratulations = pg.image.load('congratulations.png').convert_alpha()
            text1 = font.render("Счёт WASD-Игрока:"+str(score1), 1, (0, 0, 0))
            text2 = font.render("Счёт Игрока стрелочками:"+str(score2), 1, (0, 0, 0))
            txt = nfont.render("Чтобы продолжить, нажмите на любую клавишу", 1, (0, 0, 0))
            draw = pg.image.load('nb.png').convert_alpha()
        elif language == "e":
            congratulations = pg.image.load('congratulations.jpg').convert_alpha()
            text1 = font.render("Score of WASD-Player:"+str(score1), 1, (0, 0, 0))
            text2 = font.render("Score of Arrows-Player:"+str(score2), 1, (0, 0, 0))
            txt = nfont.render("To continue please press any button", 1, (0, 0, 0))
            draw = pg.image.load('draw.png').convert_alpha()
            
        congratulations = pg.transform.scale(congratulations, (600, 100))
        place_cong = congratulations.get_rect(center=(600, 100))
        draw = pg.transform.scale(draw, (400, 100))
        place_draw = draw.get_rect(center=(600, 550))
        place1 = text1.get_rect(center=(600, 300))
        place2 = text2.get_rect(center=(600, 400))
        place = txt.get_rect(center=(600, 650))

        winner = pg.image.load('winner.png').convert_alpha()
        winner = pg.transform.scale(winner, (200, 400))
        place_winner = winner.get_rect(center=(600, 350))
        
        while 1:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    pg.quit()
                    exit()
                elif i.type == pg.KEYDOWN:
                    if score1 == score2:
                        start(language)
                    else:
                        if flag2:
                            start(language)

            t2  = time.time()

            if t2 - t1 >= 4:
                flag1 = False
                
            if flag1:
                if score1 < score2:
                    if language == "e":
                        text = font.render("Score of WASD-Player:"+str(score1), 1, (0, 0, 0))
                    elif language == "r":
                        text = font.render("Счёт WASD-Игрока:"+str(score1), 1, (0, 0, 0))
                    place_text = text.get_rect(center=(600, 350))
                elif score2 < score1:
                    if language == "e":
                        text = font.render("Score of Arrows-Player:"+str(score2), 1, (0, 0, 0))
                    elif language == "r":
                        text = font.render("Счёт Игрока стрелочками:"+str(score2), 1, (0, 0, 0))
                    place_text = text.get_rect(center=(600, 350))
            else:
                if score1 > score2:
                    if language == "e":
                        text = font.render("Score of WASD-Player:"+str(score1), 1, (0, 0, 0))
                    elif language == "r":
                        text = font.render("Счёт WASD-Игрока:"+str(score1), 1, (0, 0, 0))
                    place_text = text.get_rect(center=(600, 350))
                elif score2 > score1:
                    if language == "e":
                        text = font.render("Score of Arrows-Player:"+str(score2), 1, (0, 0, 0))
                    elif language == "r":
                        text = font.render("Счёт Игрока стрелочками:"+str(score2), 1, (0, 0, 0))
                    place_text = text.get_rect(center=(600, 350))
                if score1 != score2:
                    flag2 = True                 
            
            screen.fill((255, 255, 255))
            screen.blit(congratulations, place_cong)
            if score1 != score2:
                screen.blit(text, place_text)
            else:
                screen.blit(txt, place)
                screen.blit(text1, place1)
                screen.blit(text2, place2)
                screen.blit(draw, place_draw)
            if flag2:
                screen.blit(winner, place_winner)
                screen.blit(txt, place)
            pg.display.update()
    
    choose1(language)

if __name__ == "__main__":
    file = open("first_time.txt", "r")
    r = file.read()
    file.close()
    file = open("language.txt", "r")
    language = file.read()
    file.close()
    if r == "True":
        file = open("first_time.txt", "w")
        file.write("False1")
        file.close()
        choose_language()
    else:
        start(language)
