import pygame
import random

# INITIALIZATION
pygame.init()

# SCREEN
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game")
font = pygame.font.Font(None, 36)
titfont = pygame.font.Font(None, 30)

# COLORS
HOT_PINK = (255, 105, 180)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

# GUESS THE NUMBER
def gtn():
    number_input = ""
    input_active = False
    ai_choice = random.randint(1, 100)
    round = 0

    gtn_running = True
    while gtn_running:
        screen.fill(BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gtn_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 420 <= x <= 420+200 and 240 <= y <= 240+50:
                    input_active = True
                else:
                    input_active = False
                if 150 <= x <= 150+69 and 310 <= y <= 310+20:
                    gtn_running = False
            if event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_RETURN:
                    if round <= 8:
                        if int(number_input) == ai_choice:
                            result = font.render(f"You Choose: {number_input} -----> YOU WIN", True, GREEN)
                        else:
                            if int(number_input) > ai_choice:
                                round += 1
                                result = font.render(f"You Choose: {number_input} -----> HIGH | Chance Left {10 - round}", True, RED)
                            else:
                                round += 1
                                result = font.render(f"You Choose: {number_input} -----> LOW | Chance Left {10 - round}", True, ORANGE)
                    else:
                        result = font.render(f"YOU LOSE, AI CHOOSE: {ai_choice}", True, RED)
                elif event.key == pygame.K_BACKSPACE:
                    number_input = number_input[:-1]
                else:
                    if event.unicode.isdigit():
                        number_input += event.unicode

        label = font.render("GUESS THE NUMBER: ", True, WHITE) # WIDTH = 267
        screen.blit(label, (150, 250))
        name_box = pygame.draw.rect(screen, RED if input_active else WHITE, (420, 240, 200, 50), 2)
        screen.blit(font.render(number_input, True, WHITE), (430, 250))
        back = font.render("BACK", True, WHITE)
        screen.blit(back, (150, 310))

        if "result" in locals():
            screen.blit(result, (150, 410))

        pygame.display.flip()


# ROCK PAPER SCISSOR
def rps():
    rps_running = True
    while rps_running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rps_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                ai_choose = random.choice(["ROCK", "PAPER", "SCISSOR"])
                x, y = pygame.mouse.get_pos()
                if 350 <= x <= 350+71 and 210 <= y <= 210+20:
                    if ai_choose == "ROCK":
                        result = font.render(f"AI CHOOSED: {ai_choose} You Choose: ROCK -----> DRAW", True, WHITE)
                    elif ai_choose == "PAPER":
                        result = font.render(f"AI CHOOSED: {ai_choose} You Choose: ROCK -----> AI WIN", True, RED)
                    elif ai_choose == "SCISSOR":
                        result = font.render(f"AI CHOOSED: {ai_choose} You Choose: ROCK -----> YOU WIN", True, GREEN)
                    else:
                        print("ERROR")
                if 350 <= x <= 350+81 and 260 <= y <= 260+20:
                    if ai_choose == "ROCK":
                        result = font.render(f"AI CHOOSED: {ai_choose} You Choose: PAPER -----> YOU WIN", True, GREEN)
                    elif ai_choose == "PAPER":
                        result = font.render(f"AI CHOOSED: {ai_choose} You Choose: PAPER -----> DRAW", True, WHITE)
                    elif ai_choose == "SCISSOR":
                        result = font.render(f"AI CHOOSED: {ai_choose} You Choose: PAPER -----> AI WIN", True, RED)
                    else:
                        print("ERROR")
                if 350 <= x <= 350+111 and 310 <= y <= 310+20:
                    if ai_choose == "ROCK":
                        result = font.render(f"AI CHOOSED: {ai_choose} You Choose: SCISSOR -----> AI WIN", True, RED)
                    elif ai_choose == "PAPER":
                        result = font.render(f"AI CHOOSED: {ai_choose} You Choose: SCISSOR -----> YOU WIN", True, GREEN)
                    elif ai_choose == "SCISSOR":
                        result = font.render(f"AI CHOOSED: {ai_choose} You Choose: SCISSOR -----> DRAW", True, WHITE)
                    else:
                        print("ERROR")
                if 350 <= x <= 350+69 and 360 <= y <= 360+20:
                    rps_running = False

        for i, option in enumerate(["ROCK", "PAPER", "SCISSOR", "BACK"]):
            text = font.render(option, True, HOT_PINK)
            screen.blit(text, (350, 210 + i*50))
            #71,81,111,69

        if "result" in locals():
            screen.blit(result, (100, 410))

        pygame.display.flip()


# MAIN MENU
running = True
while running:

    screen.fill(HOT_PINK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 300 <= x <= 300+279 and 210 <= y <= 210+20:
                rps()
            if 300 <= x <= 300+252 and 260 <= y <= 260+20:
                gtn()
            if 300 <= x <= 300+60 and 310 <= y <= 310+20:
                running = False

    for i, option in enumerate(["ROCK-PAPER-SCISSOR", "GUESS THE NUMBER", "EXIT"]):
        text = font.render(option, True, BLACK)
        screen.blit(text, (300, 210 + i*50))

    box1 = pygame.draw.rect(screen, RED, (0, 0, 800, 40))
    box2 = pygame.draw.rect(screen, RED, (0, 560, 800, 40))
    box3 = pygame.draw.rect(screen, RED, (0, 0, 40, 600))
    box4 = pygame.draw.rect(screen, RED, (760, 0, 40, 600))
    tit = titfont.render("WELCOME TO ROCK PAPER SCISSOR AND GUESS THE NUMBER GAME", True, WHITE)
    screen.blit(tit, (40,12))

    pygame.display.flip()

pygame.quit()