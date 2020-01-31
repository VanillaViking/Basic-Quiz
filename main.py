import pygame
from text_screens import *
from button import *
from text_input import *
from dots import *
import time
from truefalse import *
from hp_bar import *
import tictac

pygame.font.init()
arial = pygame.font.SysFont('Arial', 40)
marks = 0

pygame.init()
DISPLAY = pygame.display.set_mode((1920, 1080))          #change to preffered resolution (should not break the program)

#SCREENS
msg_screen = text_screens((255,255,255), (50,50,50))

def say(DISPLAY, sentence, pos, colour=(0,0,0)):
    DISPLAY.blit(arial.render(sentence, True, colour), pos)
def q1_draw(DISPLAY):
    for n in range(2):
        text = arial.render('What\'s "1" + "1"?', True, (0,0,0))
        answer = text_input(DISPLAY, (DISPLAY.get_width() /2) - 100, ((DISPLAY.get_height())/2) - 32, 200, 75)
        submit = button([200,200,200], (190,0, 230), (DISPLAY.get_width() /2) - 100, ((3 * DISPLAY.get_height())/4), 200, 75, "Submit")
        while not submit.pressed:     #main loop
            pygame.display.update()
            DISPLAY.fill((255,255,255))
            DISPLAY.blit(text, ((DISPLAY.get_width() / 2) - (text.get_width() / 2),(DISPLAY.get_height()/4) - (text.get_height() / 2)))
            answer.draw()
            submit.draw(DISPLAY)



            for event in pygame.event.get():
                answer.activate(event)
                submit.update(event, DISPLAY)
                if event.type == pygame.QUIT:
                    pygame.QUIT
                    quit()
            
        if answer.text == "11" or answer.text == '"11"' or answer.text == "'11'":
            msg_screen.draw(DISPLAY, "Correct! Good Job!")
            break
        else:
            msg_screen.draw(DISPLAY, "Wrooong, pay attention to the quotation marks :)")


def q2_draw(DISPLAY):
    text = arial.render("click the moving dot before it escapes", True, (0,0,0))
    bob = dot(DISPLAY.get_width()/2,DISPLAY.get_height()/2)

    while not bob.dead and not bob.goal_reached:
        pygame.display.update()
        DISPLAY.fill((255,255,255))
        DISPLAY.blit(text, ((DISPLAY.get_width() / 2) - (text.get_width() / 2),(DISPLAY.get_height()/4) - (text.get_height() / 2)))
        bob.draw(DISPLAY)
        bob.move(DISPLAY)
        time.sleep(0.04)
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                bob.check(event)
            if event.type == pygame.QUIT:
                pygame.QUIT
                quit()
    if bob.dead:
        msg_screen.draw(DISPLAY, "Nice Job!")
    elif bob.goal_reached:
        msg_screen.draw(DISPLAY, "Too Slow!")

def q3_draw(DISPLAY):
    text = arial.render("Huawei is banned from doing business in America", True, (0,0,0))
    true = tf(DISPLAY,DISPLAY.get_width()/4,DISPLAY.get_height()/2, 10, "True")
    false = tf(DISPLAY, (3*DISPLAY.get_width())/4,DISPLAY.get_height()/2, 10, "False")
    cont_button = button([200,200,200], (190,0, 230), (DISPLAY.get_width() /2) - 100, ((3 * DISPLAY.get_height())/4), 200, 75, "continue")
    huawei_logo = pygame.image.load("hua1.png")
    while True:
        pygame.display.update()
        DISPLAY.fill((255,255,255))
        DISPLAY.blit(text, ((DISPLAY.get_width() / 2) - (text.get_width() / 2),(DISPLAY.get_height()/4) - (text.get_height() / 2)))
        DISPLAY.blit(pygame.transform.scale(huawei_logo,(200,200)), ((DISPLAY.get_width() / 2) - (pygame.transform.scale(huawei_logo,(200,200)).get_width() / 2),(DISPLAY.get_height()/2) - (pygame.transform.scale(huawei_logo,(200,200)).get_height() / 2)))
        cont_button.draw(DISPLAY)
        false.draw(False) #stupid way of updating the false button while true button was performing its animation. false would dissappear otherwise.
        true.draw(True)
        false.draw(True)

        for event in pygame.event.get():
            cont_button.update(event, DISPLAY)
            true.activate(event)
            false.activate(event)

            if event.type == pygame.QUIT:
                quit()
            
        
        if cont_button.pressed:
            if true.active:
                msg_screen.draw(DISPLAY, "Correct! rip huawei.")
                break
            elif false.active:
                msg_screen.draw(DISPLAY, "WRONG! Have you been living under a rock?")
                cont_button.pressed = False
                break
            else:
                cont_button.pressed = False

def q4_draw(DISPLAY):
    player_turn = True
    screen = "main"
    battle_scene = pygame.transform.scale(pygame.image.load("poke1.jpg"), (1920,1080))
    oponent_hp = hp(DISPLAY, 400, 213, 400, 35)
    player_hp = hp(DISPLAY, 1385,603, 400, 35)
    items_btn = button((220,220,220), (170,170,170), 1050, 840, 200,100, "ITEMS")
    fight_btn = button((220,220,220), (170,170,170), 1300, 840, 200,100, "FIGHT")
    fight_btn.animate = False
    run_btn = button((220,220,220), (170,170,170), 1550, 840, 200,100, "RUN")
    run_btn.animate = False
    menu_btn = button((220,220,220), (170,170,170), 1800, 970, 100,50, "MENU")
    menu_btn.animate = False

    #attack buttons
    lightning_strike_btn = button((220,220,220), (170,170,170), 1660, 840, 200,100, "Lightning Bolt", (0,0,0), 25, 9,True, False)
    thunder_shock_btn = button((220,220,220), (170,170,170), 1200, 840, 200,100, "Thunder Shock", (0,0,0), 25, 7,True, False)
    electro_ball_btn = button((220,220,220), (170,170,170), 1430, 840, 200,100, "Electro Ball", (0,0,0), 25, 7, True, False)

    #healing potion
    healing_potion_btn = button((220,220,220), (170,170,170), 1200, 840, 200,100, "Healing Potion", (0,0,0), 25, 7,True, False)
    empty = False

    pygame.mixer.music.load("battle.mp3")
    pygame.mixer.music.play(0)
    time.sleep(0.5)
    radius = DISPLAY.get_width()/2
    for n in range(240):
        pygame.display.update()
        DISPLAY.fill((0,0,0))
        pygame.draw.circle(DISPLAY, (255,255,255), (int(DISPLAY.get_width()/2),int(DISPLAY.get_height()/2)), int(radius))
        radius -= radius/100
        time.sleep(0.01)

    while not oponent_hp.dead and not player_hp.dead:
        pygame.display.update()
        DISPLAY.blit(battle_scene, (0,0))
        oponent_hp.draw()
        player_hp.draw()

        if player_turn:
            if screen == "main":
                fight_btn.draw(DISPLAY)
                run_btn.draw(DISPLAY)
                items_btn.draw(DISPLAY)
                say(DISPLAY, "Defeat Squirtle!", (100,840))

            elif screen == "run":
                msg_screen.draw(DISPLAY, "You escaped. You earned nothing.")
                break

            elif screen == "fight":
                lightning_strike_btn.draw(DISPLAY)
                thunder_shock_btn.draw(DISPLAY)
                electro_ball_btn.draw(DISPLAY)
                menu_btn.draw(DISPLAY)

                if lightning_strike_btn.pressed:
                    say(DISPLAY, "Lightning Bolt was very effective!", (100,840))
                    pygame.display.update()
                    time.sleep(1)
                    oponent_hp.reduce(150)
                    lightning_strike_btn.pressed = False
                    player_turn = not player_turn
                
                if thunder_shock_btn.pressed:
                    say(DISPLAY, "Thunder Shock was not very effective.", (100,840))
                    pygame.display.update()
                    time.sleep(1)
                    oponent_hp.reduce(30)
                    thunder_shock_btn.pressed = False
                    player_turn = not player_turn
                
                if electro_ball_btn.pressed:
                    say(DISPLAY, "Squirtle dodged electrol ball!", (100,840))
                    pygame.display.update()
                    time.sleep(1)
                    electro_ball_btn.pressed = False
                    player_turn = not player_turn
                
                if menu_btn.pressed:
                    screen = "main"
                    menu_btn.pressed = False
                
            elif screen == "items":
                menu_btn.draw(DISPLAY)
                if not healing_potion_btn.pressed:
                    healing_potion_btn.draw(DISPLAY)

                if menu_btn.pressed:
                    screen = "main"
                    menu_btn.pressed = False
                
                if healing_potion_btn.pressed:
                    if not empty:
                        player_hp.rect.width = 400
                        player_hp.draw()
                        say(DISPLAY, "HP fully resored!", (100,840))
                        pygame.display.update()
                        time.sleep(1)
                        empty = True
                    


            if fight_btn.pressed:
                screen = "fight"
                fight_btn.pressed = False
            if run_btn.pressed:
                screen = "run"
                run_btn.pressed = False
            if items_btn.pressed:
                screen = "items"
                items_btn.pressed = False

            for event in pygame.event.get():
                if screen == "main":
                    fight_btn.update(event, DISPLAY)
                    run_btn.update(event, DISPLAY)
                    items_btn.update(event, DISPLAY)
                elif screen == "fight":
                    lightning_strike_btn.update(event, DISPLAY)
                    thunder_shock_btn.update(event, DISPLAY)
                    electro_ball_btn.update(event, DISPLAY)
                    menu_btn.update(event, DISPLAY)
                elif screen == "items":
                    menu_btn.update(event, DISPLAY)
                    if not healing_potion_btn.pressed:
                        healing_potion_btn.update(event, DISPLAY)
                if event.type == pygame.QUIT:
                    quit()
        else:
            say(DISPLAY, "Squirtle's Turn!", (100,820))
            say(DISPLAY, "Squirtle used Tackle!", (100, 870))
            pygame.display.update()
            time.sleep(2)
            player_hp.reduce(250)
            player_turn = not player_turn

    pygame.mixer.music.stop()   
    if oponent_hp.dead:
        msg_screen.draw(DISPLAY, "You win!")
    elif player_hp.dead:
        msg_screen.draw(DISPLAY, "You lost!")

def q5_draw(DISPLAY):
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    player_turn = True
    text = arial.render("Beat me at tic-tac toe.", True, (0,0,0))
    cross = pygame.transform.scale(pygame.image.load("cross.png"), (100,100))
    circle = pygame.transform.scale(pygame.image.load("circle.png"), (100,100))
    SQUARES = [[],[],[]]
    y_val = (DISPLAY.get_height()/2) - 155
    for row in range(3):
        x_val = (DISPLAY.get_width()/2) - 155
        for col in range(3):
            SQUARES[row].append(tictac.square(DISPLAY, (220,220,220), (180,180,180), x_val,y_val, 100,100))
            x_val += 105
        y_val += 105
    
    while True:
        pygame.display.update()
        DISPLAY.fill((200,200,255))
        DISPLAY.blit(text, ((DISPLAY.get_width() / 2) - (text.get_width() / 2),(DISPLAY.get_height()/4) - (text.get_height() / 2)))

        for row in SQUARES:
            for square in row:
                square.draw()
        
        for row in SQUARES:
            for square in row:
                if square.xo == "X":
                    DISPLAY.blit(cross, (square.rect.x,square.rect.y))
                elif square.xo == "Y":
                    DISPLAY.blit(circle,(square.rect.x,square.rect.y))



        for event in pygame.event.get():
            for row in SQUARES:
                for square in row:
                    square.update(event)

            if event.type == pygame.QUIT:
                quit()



#MAIN
msg_screen.draw(DISPLAY, "Very Basic Quiz.")

#1 + 1
q1_draw(DISPLAY)

#t/f question
q3_draw(DISPLAY)

#dot game
q2_draw(DISPLAY)

#pokemon
q4_draw(DISPLAY)

#tic tac toe
q5_draw(DISPLAY)

