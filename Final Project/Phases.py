import Classes as cl
from pygame import *
from pygame.sprite import *
from numpy import *
import matplotlib.pyplot as plt

resolution = (1080, 720)


# Menu to show when starting game
def Start_Menu():
    main_frame = display.set_mode(resolution)
    flag = True

    # create and group sprites
    play_button = cl.Button("Play", 540, 360, fontsize=30)
    how_button = cl.Button("How to Play", 540, 400, fontsize=30)
    exit_button = cl.Button("Exit", 540, 440, fontsize=30)
    game_label = cl.Button("Welcome to MasterMind!", 540, 120, fontsize=50)
    start_menu_labels = Group(game_label)
    start_menu_buttons1 = Group(play_button, how_button, exit_button)

    # main loop
    while flag:
        main_frame.fill(cl.grey)
        start_menu_labels.draw(main_frame)
        start_menu_buttons1.draw(main_frame)
        display.update()

        for ev in event.get():

            # button hovering implementation
            for sprite in start_menu_buttons1:
                if sprite.rect.collidepoint(mouse.get_pos()):
                    sprite.change_colour(cl.white)
                else:
                    sprite.change_colour(cl.black)

            # checks for event type quit
            if ev.type == QUIT:
                pygame.quit()
                exit()

            # checks for event type mouse button down
            elif ev.type == MOUSEBUTTONDOWN:

                # play button implementation
                if play_button.rect.collidepoint(mouse.get_pos()):
                    Difficulty_Menu()

                # how button implementation
                if how_button.rect.collidepoint(mouse.get_pos()):
                    How_Menu()

                if exit_button.rect.collidepoint(mouse.get_pos()):
                    flag = False


# menu to show when help button is clicked
def How_Menu():
    main_frame = display.set_mode(resolution)
    breaker = True

    # creating sprites
    howtoplay_label = cl.Button("How to Play: ", 10, 100, fontsize=48, align="left")
    text_wall1 = cl.Button("The aim of the game is to find the code generated using educated guesses.", 100, 200,
                           fontsize=30, align="left")
    text_wall2 = cl.Button("You get 10 guesses every game. You will receive feedback every guess.", 100, 240,
                           fontsize=30, align="left")
    text_wall3 = cl.Button("Yellow peg means the colour of one of the balls is correct but in the wrong position,",
                           100, 280, fontsize=30, align="left")
    text_wall4 = cl.Button("while Green peg means the colour and position of one ball is correct.", 100, 320,
                           fontsize=30, align="left")
    text_wall5 = cl.Button("If the player chooses easy, the code will be given in terminal.", 100, 360,
                           fontsize=30, align="left")
    text_wall6 = cl.Button("If the player chooses hard, two additional colours will come into play.", 100, 40,
                           fontsize=30, align="left")
    back_button = cl.Button("Back to Menu", 10, 680, fontsize=24, align="left")

    # grouping sprites
    help_menu_sprites = Group(howtoplay_label, text_wall1, text_wall2, text_wall3, text_wall4, text_wall5, text_wall6,
                              back_button)

    # main loop
    while breaker:
        main_frame.fill(cl.grey)
        help_menu_sprites.draw(main_frame)
        display.update()

        for ev in event.get():

            # check if mouse is hovering back button
            if back_button.rect.collidepoint(mouse.get_pos()):
                back_button.change_colour(cl.white)
            else:
                back_button.change_colour(cl.black)

            # checks for event type quit
            if ev.type == QUIT:
                pygame.quit()
                exit()


            elif ev.type == MOUSEBUTTONDOWN:

                # back button implementation
                if back_button.rect.collidepoint(mouse.get_pos()):
                    breaker = False


# menu to choose difficulty
def Difficulty_Menu():
    flag = True
    main_frame = display.set_mode(resolution)

    # create and group sprites
    game_label = cl.Button("Welcome to MasterMind!", 540, 120, fontsize=50)
    easy_button = cl.Button("Easy", 540, 200, fontsize=30)
    medium_button = cl.Button("Medium", 540, 240, fontsize=30)
    hard_button = cl.Button("Hard", 540, 280, fontsize=30)
    back_button = cl.Button("Back to Menu", 10, 680, fontsize=24, align="left")
    diff_menu_labels = Group(game_label)
    diff_menu_buttons = Group(easy_button, medium_button, hard_button, back_button)

    while flag:
        main_frame.fill(cl.grey)
        diff_menu_labels.draw(main_frame)
        diff_menu_buttons.draw(main_frame)
        display.update()

        for ev in event.get():

            # button hovering implementation
            for sprite in diff_menu_buttons:
                if sprite.rect.collidepoint(mouse.get_pos()):
                    sprite.change_colour(cl.white)
                else:
                    sprite.change_colour(cl.black)

            # checks for event type quit
            if ev.type == QUIT:
                pygame.quit()
                exit()

            # check for event type mouse button down
            elif ev.type == MOUSEBUTTONDOWN:

                # back button implementation
                if back_button.rect.collidepoint(mouse.get_pos()):
                    flag = False

                # easy button implementation
                elif easy_button.rect.collidepoint(mouse.get_pos()):
                    Game_Menu("easy")
                    flag = False

                # medium button implementation
                elif medium_button.rect.collidepoint(mouse.get_pos()):
                    Game_Menu("medium")
                    flag = False

                # hard button implementation
                elif hard_button.rect.collidepoint(mouse.get_pos()):
                    Game_Menu("hard")
                    flag = False


# Menu used to show end of game
def End_Game_Menu(tries, time_taken):

    main_frame = display.set_mode(resolution)
    flag = True

    back_button = cl.Button("Back to Menu", 540, 700, fontsize=40, color=(0, 0, 0))
    show_button = cl.Button("Show Graph", 540, 650, fontsize=40, color=(0,0,0))

    if tries <= 10:

        result_label = cl.Button("Congratulations! You won in %d tries" % (tries-1), 540, 400, fontsize=80, color=(0, 0, 0))
    else:
        result_label = cl.Button("Better luck next time!", 540, 400, fontsize=80, color=(0, 0, 0))

    time_label = cl.Button("It took you " + str(time_taken[-1]) + "s to finish", 540,500, fontsize=80, color=(0,0,0))

    buttons = Group(back_button, show_button)
    labels = Group(result_label, time_label)

    while flag:
        main_frame.fill(cl.grey)
        labels.draw(main_frame)
        buttons.draw(main_frame)
        display.update()

        for ev in event.get():

            # check if mouse is hovering over buttons group
            for sprite in buttons:
                if sprite.rect.collidepoint(mouse.get_pos()):
                    sprite.change_colour(cl.white)
                else:
                    sprite.change_colour(cl.black)

            # checks for event type quit
            if ev.type == QUIT:
                pygame.quit()
                exit()

            if ev.type == MOUSEBUTTONDOWN:

                # back button implementation
                if back_button.rect.collidepoint(mouse.get_pos()):
                    flag = False
                # show button implementation
                elif show_button.rect.collidepoint(mouse.get_pos()):
                    # Graphing time of confirm to confirm
                    plt.clf()
                    ax = plt.subplot()
                    ax.plot(time_taken,"-o")
                    ax.set_ylabel("Time of Confirm/s")
                    ax.set_xlabel("Confirm Number")
                    ax.set_ylim(bottom=0)
                    ax.set_xlim(left=0)
                    plt.show()


# Main game menu
def Game_Menu(difficulty):

    # variables to get time
    time_start = time.get_ticks()
    time_of_confirm = [0.0]

    main_frame = display.set_mode(resolution)
    flag = True

    # colours used
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    purple = (255, 0, 255)
    cyan = (0, 255, 255)
    white = (255, 255, 255)
    brown = (160, 82, 45)
    colours = ['red', 'green', 'blue', 'yellow', 'purple']

    # if difficulty is hard, two more colours are added
    if difficulty == 'hard':
        colours.append('white')
        colours.append('cyan')

    # balls for choice
    red_ball = cl.Ball(420, 680, red, size=40)
    green_ball = cl.Ball(480, 680, green, size=40)
    blue_ball = cl.Ball(540, 680, blue, size=40)
    yellow_ball = cl.Ball(600, 680, yellow, size=40)
    purple_ball = cl.Ball(660, 680, purple, size=40)
    white_ball = cl.Ball(360, 680, white, size=40)
    cyan_ball = cl.Ball(720, 680, cyan, size=40)

    # balls for code input
    codeball1 = cl.Ball(380, 620, size=70)
    codeball2 = cl.Ball(480, 620, size=70)
    codeball3 = cl.Ball(580, 620, size=70)
    codeball4 = cl.Ball(680, 620, size=70)

    # pegs for showing result
    peg1 = cl.Ball(790, 620, size=10)
    peg2 = cl.Ball(810, 620, size=10)
    peg3 = cl.Ball(830, 620, size=10)
    peg4 = cl.Ball(850, 620, size=10)

    # game variables
    code_words = random.choice(colours, 4, replace=True)
    code = []

    # converting words into rgb of colour
    for x in code_words:
        if x == 'red':
            code.append(red)

        elif x == 'green':
            code.append(green)

        elif x == 'blue':
            code.append(blue)

        elif x == 'yellow':
            code.append(yellow)

        elif x == 'purple':
            code.append(purple)

        elif x == 'white':
            code.append(white)

        elif x == 'cyan':
            code.append(cyan)

    if difficulty == "easy":
        print(code_words)

    correct_colour = 0
    correct_place = 0
    correct = 0
    counter = 1

    # buttons for the menu
    confirm_button = cl.Button("Confirm", 1060, 660, fontsize=40, color=(100, 100, 100), backcolor=(0, 0, 0),
                               align="right")
    guesses_button = cl.Button("Guess No: 1/10", 130, 20, fontsize=40)

    # grouping sprites
    choice_balls = Group(red_ball, green_ball, blue_ball, yellow_ball, purple_ball)
    codeballs = Group(codeball1, codeball2, codeball3, codeball4)
    pegs = Group(peg1, peg2, peg3, peg4)
    pegs_list = [peg1, peg2, peg3, peg4]
    buttons = Group(confirm_button, guesses_button)
    history_balls = Group()
    history_pegs = Group()

    # declaring a function for deglowing
    def deglow_all():
        red_ball.deglow()
        green_ball.deglow()
        blue_ball.deglow()
        yellow_ball.deglow()
        purple_ball.deglow()

    # if hard is chosen, the choice of white and cyan are added
    if difficulty == 'hard':
        choice_balls.add(white_ball, cyan_ball)

        def deglow_all():
            red_ball.deglow()
            green_ball.deglow()
            blue_ball.deglow()
            yellow_ball.deglow()
            purple_ball.deglow()
            cyan_ball.deglow()
            white_ball.deglow()

    choice = None

    # main game loop
    while flag:

        if counter > 10 or correct == 4:
            flag = False
            End_Game_Menu(counter, time_of_confirm)

        # filling and drawing the screen
        main_frame.fill(cl.grey)
        draw.rect(main_frame, brown, (320, 0, 420, 720))
        choice_balls.draw(main_frame)
        codeballs.draw(main_frame)
        buttons.draw(main_frame)
        history_balls.draw(main_frame)
        history_pegs.draw(main_frame)
        display.update()

        for ev in event.get():

            # checks for event type quit
            if ev.type == QUIT:
                pygame.quit()
                exit()

            # background changing implementation for confirm_button
            if confirm_button.rect.collidepoint(mouse.get_pos()):
                confirm_button.change_backcolour((255, 255, 255))
            else:
                confirm_button.change_backcolour((0, 0, 0))

            # mouse button down events
            if ev.type == MOUSEBUTTONDOWN:

                # confirm button implementation
                if confirm_button.rect.collidepoint(mouse.get_pos()):

                    time_of_confirm.append((time.get_ticks() - time_start)/1000)
                    counter += 1
                    correct = 0
                    guesses_button.update_message("Guesses: %d/10" % counter)

                    # convert guess into list
                    guess = [codeball1.get_colour(), codeball2.get_colour(), codeball3.get_colour(),
                             codeball4.get_colour()]

                    # copying balls
                    for ball in codeballs:
                        history_balls.add(ball.reproduce(40))

                    # moving history balls up
                    for ball in history_balls:
                        temp_position = ball.get_position()
                        ball.move(temp_position[0], temp_position[1] - 60)

                    # get the amount of corrects
                    for x in range(4):
                        if code[x] == guess[x]:
                            correct += 1
                            correct_place += 1

                    # get amount of correct position
                    temp_code = code[:]
                    for x in range(4):
                        if guess[x] in temp_code:
                            correct_colour += 1
                            for i in range(4):
                                if temp_code[i] == guess[x]:
                                    temp_code[i] = None
                                    break

                    correct_colour -= correct_place

                    # correct counting and changing colour of pegs
                    for i in range(4):
                        if correct_place > 0:
                            pegs_list[i].change_colour(green)
                            correct_place -= 1

                        elif correct_colour > 0:
                            pegs_list[i].change_colour(yellow)
                            correct_colour -= 1

                        else:
                            pegs_list[i].change_colour((0, 0, 0))

                    # copying pegs
                    for peg in pegs:
                        history_pegs.add(peg.reproduce(10))

                    # moving pegs
                    for peg in history_pegs:
                        temp_position = peg.get_position()
                        peg.move(temp_position[0], temp_position[1] - 60)

                # ball mouse collision implementation
                elif red_ball.rect.collidepoint(mouse.get_pos()):
                    deglow_all()
                    red_ball.glow()
                    choice = red_ball

                elif green_ball.rect.collidepoint(mouse.get_pos()):
                    deglow_all()
                    green_ball.glow()
                    choice = green_ball

                elif blue_ball.rect.collidepoint(mouse.get_pos()):
                    deglow_all()
                    blue_ball.glow()
                    choice = blue_ball

                elif yellow_ball.rect.collidepoint(mouse.get_pos()):
                    deglow_all()
                    yellow_ball.glow()
                    choice = yellow_ball

                elif purple_ball.rect.collidepoint(mouse.get_pos()):
                    deglow_all()
                    purple_ball.glow()
                    choice = purple_ball

                elif cyan_ball.rect.collidepoint(mouse.get_pos()):
                    if difficulty == "hard":
                        deglow_all()
                        cyan_ball.glow()
                        choice = cyan_ball

                elif white_ball.rect.collidepoint(mouse.get_pos()):
                    if difficulty == "hard":
                        deglow_all()
                        white_ball.glow()
                        choice = white_ball

                # code ball colour implementation
                elif codeball1.rect.collidepoint(mouse.get_pos()):
                    if choice is None:
                        pass
                    else:
                        codeball1.change_colour(choice.get_colour())

                elif codeball2.rect.collidepoint(mouse.get_pos()):
                    if choice is None:
                        pass
                    else:
                        codeball2.change_colour(choice.get_colour())

                elif codeball3.rect.collidepoint(mouse.get_pos()):
                    if choice is None:
                        pass
                    else:
                        codeball3.change_colour(choice.get_colour())

                elif codeball4.rect.collidepoint(mouse.get_pos()):
                    if choice is None:
                        pass
                    else:
                        codeball4.change_colour(choice.get_colour())

                else:
                    choice = None
                    deglow_all()
