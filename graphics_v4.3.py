import pygame
import math
import random

# Window
def draw_window(length, width, title):
    ''' 
    functions creates the viewing window for the game using length and width parameters

    param length - The length of the viewing window
    param width -  The width of the viewing window
    param title - The title of the window that shows at the top when running the program

    '''
    screen = pygame.display.set_mode((length, width))
    pygame.display.set_caption(title)
    return screen


# Colors
def define_colors():
    ''' 
    function that add colors you use as RGB values here 

    no params

    '''
    color_dict = {'RED': (255, 0, 0),
                  'GREEN': (52, 166, 36),
                  'BLUE': (29, 116, 248),
                  'WHITE': (255, 255, 255),
                  'BLACK': (0, 0, 0),
                  'ORANGE': (255, 125, 0),
                  'DARK_BLUE': (18, 0, 91),
                  'DARK_GREEN': (0, 94, 0),
                  'GRAY': (130, 130, 130),
                  'YELLOW': (255, 255, 110),
                  'SILVER': (200, 200, 200),
                  'DAY_GREEN': (41, 129, 29),
                  'NIGHT_GREEN': (0, 64, 0),
                  'BRIGHT_YELLOW': (255, 244, 47),
                  'NIGHT_GRAY': (104, 98, 115),
                  'ck': (127, 33, 33)}
    return color_dict


def draw_cloud(x, y):
    '''
    functions draws invidiual clouds that float in the background of the game

    param x - x position of an individual cloud
    param y - y position of an individual cloud

    '''
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x, y + 8, 10, 10])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 6, y + 4, 8, 8])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 10, y, 16, 16])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 20, y + 8, 10, 10])
    pygame.draw.rect(SEE_THROUGH, cloud_color, [x + 6, y + 8, 18, 10])


def randomize_star_positions(num_stars, stars_x0_pos, stars_xf_pos, stars_y0_pos, stars_yf_pos, min_star_size, max_star_size):
    '''
    function that positions the stars in random positions when set to night

    param num_stars - total amount of stars
    param stars_x0_pos - initial x position of the stars
    param stars_xf_pos - final x position of the stars
    param stars_y0_pos - initial y position of the stars
    param stars_yf_pos - final y position of the stars
    param min_star_size - minimum size of the stars
    param max_star_size - maximum size of the stars

    '''
    stars = []
    for n in range(num_stars):
        x = random.randrange(stars_x0_pos, stars_xf_pos)
        y = random.randrange(stars_y0_pos, stars_yf_pos)
        r = random.randrange(min_star_size, max_star_size)
        stars.append([x, y, r, r])
    return stars


def randomize_cloud_positions(num_clouds, cloud_x0_pos, cloud_xf_pos, cloud_y0_pos, cloud_yf_pos):
    '''
    function that randomizes the positions of the clouds in the game

    param num_clouds - total number of clouds
    param cloud_x0_pos - initial position of the clouds
    param cloud_xf_pos - final position of the clouds
    param cloud_y0_pos - initial position of the clouds
    param cloud_yf_pos - final position of the clouds

    '''
    clouds = []
    for i in range(num_clouds):
        x = random.randrange(cloud_x0_pos, cloud_xf_pos)
        y = random.randrange(cloud_y0_pos, cloud_yf_pos)
        clouds.append([x, y])
    return clouds


def draw_fence(fence_rail_xpos, fence_post_ypos):
    '''

    function that draws the fence behind the score goal

    param fence_rail_xpos - x position of the fence rail
    param fence_post_ypos - y position of the fence post

    '''
    '''fence'''
    y = fence_post_ypos
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, color_dict['NIGHT_GRAY'], [[x + 2, y], [x + 2, y + 15], [x, y + 15], [x, y]])

    y = fence_post_ypos
    for x in range(5, 800, 3):
        pygame.draw.line(screen, color_dict['NIGHT_GRAY'], [x, y], [x, y + 15], 1)

    x = fence_rail_xpos
    for y in range(170, 185, 4):
        pygame.draw.line(screen, color_dict['NIGHT_GRAY'], [x, y], [x + 800, y], 1)


def sun_moon(sun_moon_xpos, sun_moon_ypos, sun_moon_size):
    '''
    function draws the sun/moon in the sky for day and night

    param sun_moon_xpos - x position of the sun/moon
    param sun_moon_ypos - y position of the sun/moon
    param sun_moon_size - size of the sun/moon

    '''
    if day:
        pygame.draw.ellipse(screen, color_dict['BRIGHT_YELLOW'], [sun_moon_xpos, sun_moon_ypos, sun_moon_size, sun_moon_size])
    else:
        pygame.draw.ellipse(screen, color_dict['WHITE'], [sun_moon_xpos, sun_moon_ypos, sun_moon_size, sun_moon_size])
        pygame.draw.ellipse(screen, sky_color, [sun_moon_xpos + 10, sun_moon_ypos - 5, sun_moon_size, sun_moon_size])


def draw_clouds():
    '''
    function that draws the clouds in the game by calling a separate function to draw the individual clouds

    no params

    '''
    for c in clouds:
        draw_cloud(c[0], c[1])
    screen.blit(SEE_THROUGH, (0, 0))


def draw_boundary_lines():
    '''
    function that draws the boundary lines of the soccer field

    no params

    '''
    #out of bounds lines
    pygame.draw.line(screen, color_dict['WHITE'], [0, 580], [800, 580], 5)
    #left
    pygame.draw.line(screen, color_dict['WHITE'], [0, 360], [140, 220], 5)
    pygame.draw.line(screen, color_dict['WHITE'], [140, 220], [660, 220], 3)
    #right
    pygame.draw.line(screen, color_dict['WHITE'], [660, 220], [800, 360], 5)


def draw_safety_circle():
    '''
    function that draws the safety circle in the middle of the soccer field

    no params

    '''
    #safety circle
    pygame.draw.ellipse(screen, color_dict['WHITE'], [240, 500, 320, 160], 5)


#18 yard line goal box
def draw_goal_boxes():
    '''
    function that draws the outer boxes in front of the soccer goal

    no params

    '''
    pygame.draw.line(screen, color_dict['WHITE'], [260, 220], [180, 300], 5)
    pygame.draw.line(screen, color_dict['WHITE'], [180, 300], [620, 300], 3)
    pygame.draw.line(screen, color_dict['WHITE'], [620, 300], [540, 220], 5)
    #6 yard line goal box
    pygame.draw.line(screen, color_dict['WHITE'], [310, 220], [270, 270], 3)
    pygame.draw.line(screen, color_dict['WHITE'], [270, 270], [530, 270], 2)
    pygame.draw.line(screen, color_dict['WHITE'], [530, 270], [490, 220], 3)


def draw_goal_box_arc():
    '''
    function that draws the outer arc in front of the soccer goal

    no params

    '''
    #arc at the top of the goal box
    pygame.draw.arc(screen, color_dict['WHITE'], [330, 280, 140, 40], math.pi, 2 * math.pi, 5)


def draw_score_board_pole():
    '''
    function that draws the pole of the scoreboard

    no params

    '''
    #score board pole
    pygame.draw.rect(screen, color_dict['GRAY'], [390, 120, 20, 70])


def draw_score_board():
    '''
    function that draws the scoreboard

    no params

    '''
    #score board
    pygame.draw.rect(screen, color_dict['BLACK'], [300, 40, 200, 90])
    pygame.draw.rect(screen, color_dict['WHITE'], [302, 42, 198, 88], 2)


def draw_goal():
    '''
    function that draws the soccer goal

    no params

    '''
    #goal
    pygame.draw.rect(screen, color_dict['WHITE'], [320, 140, 160, 80], 5)
    pygame.draw.line(screen, color_dict['WHITE'], [340, 200], [460, 200], 3)
    pygame.draw.line(screen, color_dict['WHITE'], [320, 220], [340, 200], 3)
    pygame.draw.line(screen, color_dict['WHITE'], [480, 220], [460, 200], 3)
    pygame.draw.line(screen, color_dict['WHITE'], [320, 140], [340, 200], 3)
    pygame.draw.line(screen, color_dict['WHITE'], [480, 140], [460, 200], 3)


def draw_light_poles(light_pole1_xpos, light_pole1_ypos, light_pole1_width, light_pole1_height, light_pole2_xpos, light_pole2_ypos, light_pole2_width, light_pole2_height):
    '''
    function that draws two light poles

    param light_pole1_xpos - x position of the first light pole
    param light_pole1_ypos - y position of the first light pole
    param light_pole1_width - width of the first light pole
    param light_pole1_height - height of the first light pole
    param light_pole2_xpos - x position of the second light pole
    param light_pole2_ypos - y position of the second light pole
    param light_pole2_width - width of the second light pole
    param light_pole2_height - height of the second light pole
    '''
    #light pole 1
    pygame.draw.rect(screen, color_dict['GRAY'], [light_pole1_xpos, light_pole1_ypos, light_pole1_width, light_pole1_height])
    pygame.draw.ellipse(screen, color_dict['GRAY'], [light_pole1_xpos, light_pole1_ypos + 135, light_pole1_width, 10])
    #light pole 2
    pygame.draw.rect(screen, color_dict['GRAY'], [light_pole2_xpos, light_pole2_ypos, light_pole2_width, light_pole2_height])
    pygame.draw.ellipse(screen, color_dict['GRAY'], [light_pole2_xpos, light_pole2_ypos + 135, light_pole2_width, 10])


def draw_lights():
    '''
    functions that draws the individual lights on each light pole

    no params

    '''
    #lights for pole 1
    pygame.draw.line(screen, color_dict['GRAY'], [110, 60], [210, 60], 2)
    pygame.draw.line(screen, color_dict['GRAY'], [110, 40], [210, 40], 2)
    pygame.draw.line(screen, color_dict['GRAY'], [110, 20], [210, 20], 2)
    n = 110
    for i in range(5):
        pygame.draw.ellipse(screen, light_color, [n, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [n, 20, 20, 20])
        n += 20
    #lights for pole 2
    pygame.draw.line(screen, color_dict['GRAY'], [590, 60], [690, 60], 2)
    pygame.draw.line(screen, color_dict['GRAY'], [590, 40], [690, 40], 2)
    pygame.draw.line(screen, color_dict['GRAY'], [590, 20], [690, 20], 2)
    n = 590
    for i in range(5):
        pygame.draw.ellipse(screen, light_color, [n, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [n, 20, 20, 20])
        n += 20


def draw_net():
    '''
    functions that draws the individual nets of the soccer goal

    no params

    '''
    #net
    n, k = 325, 341
    for i in range(8):
        pygame.draw.line(screen, color_dict['WHITE'], [n, 140], [k, 200], 1)
        n += 5
        k += 3
    n, k = 364, 365
    for i in range(4):
        pygame.draw.line(screen, color_dict['WHITE'], [n, 140], [k, 200], 1)
        n += 4
        k += 4
    n, k = 380, 380
    for i in range(11):
        pygame.draw.line(screen, color_dict['WHITE'], [n, 140], [k, 200], 1)
        n += 4
        k += 4
    n, k = 424, 423
    for i in range(4):
        pygame.draw.line(screen, color_dict['WHITE'], [n, 140], [k, 200], 1)
        n += 4
        k += 4
    n, k = 440, 438
    for i in range(8):
        pygame.draw.line(screen, color_dict['WHITE'], [n, 140], [k, 200], 1)
        n += 5
        k += 3
    #net part 2
    n, k = 324, 216
    for i in range(8):
        pygame.draw.line(screen, color_dict['WHITE'], [320, 140], [n, k], 1)
        n += 2
        k -= 2
    #net part 3
    n, k = 476, 216
    for i in range(8):
        pygame.draw.line(screen, color_dict['WHITE'], [480, 140], [n, k], 1)
        n -= 2
        k -= 2
    #net part 4
    n = 144
    for i in range(9):
        pygame.draw.line(screen, color_dict['WHITE'], [324, n], [476, n], 1)
        n += 4
    pygame.draw.line(screen, color_dict['WHITE'], [335, 180], [470, 180], 1)
    pygame.draw.line(screen, color_dict['WHITE'], [335, 184], [465, 184], 1)
    pygame.draw.line(screen, color_dict['WHITE'], [335, 188], [465, 188], 1)
    pygame.draw.line(screen, color_dict['WHITE'], [335, 192], [465, 192], 1)
    pygame.draw.line(screen, color_dict['WHITE'], [335, 196], [465, 196], 1)


def draw_stands():
    '''
    function that draws the audience stands on the left and right side of the window

    no params

    '''
    #stands right
    pygame.draw.polygon(screen, color_dict['RED'], [[680, 220], [800, 340], [800, 290], [680, 180]])
    pygame.draw.polygon(screen, color_dict['WHITE'], [[680, 180], [800, 100], [800, 290]])
    #stands left
    pygame.draw.polygon(screen, color_dict['RED'], [[120, 220], [0, 340], [0, 290], [120, 180]])
    pygame.draw.polygon(screen, color_dict['WHITE'], [[120, 180], [0, 100], [0, 290]])
    #people


def draw_flags():
    '''
    function that draws the flags on the left and right side of the soccer field

    no params

    '''
    #corner flag right
    pygame.draw.line(screen, color_dict['BRIGHT_YELLOW'], [140, 220], [135, 190], 3)
    pygame.draw.polygon(screen, color_dict['RED'], [[132, 190], [125, 196], [135, 205]])
    #corner flag left
    pygame.draw.line(screen, color_dict['BRIGHT_YELLOW'], [660, 220], [665, 190], 3)
    pygame.draw.polygon(screen, color_dict['RED'], [[668, 190], [675, 196], [665, 205]])


def main():
    '''
    main function that runs the program

    no params

    '''
    # Initialize game engine
    pygame.init()

    global screen, color_dict, DARKNESS, SEE_THROUGH, day, clouds, light_color, sky_color, field_color, stripe_color, cloud_color
    screen = draw_window(800, 600, 'Major League Soccer')

    # Timer
    clock = pygame.time.Clock()
    refresh_rate = 60

    color_dict = define_colors()

    DARKNESS = pygame.Surface((800, 600))
    DARKNESS.set_alpha(200)
    DARKNESS.fill((0, 0, 0))

    SEE_THROUGH = pygame.Surface((800, 180))
    SEE_THROUGH.set_alpha(150)
    SEE_THROUGH.fill((124, 118, 135))

    # Config
    lights_on = True
    day = True

    stars = randomize_star_positions(200, 0, 800, 0, 200, 1, 2)

    clouds = randomize_cloud_positions(20, -100, 1600, 0, 150)

    # Game loop
    done = False

    while not done:
        # Event processing (React to key presses, mouse clicks, etc.)
        ''' for now, we'll just check to see if the X is clicked '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    lights_on = not lights_on
                elif event.key == pygame.K_d:
                    day = not day

        # Game logic (Check for collisions, update points, etc.)
        ''' leave this section alone for now '''
        if lights_on:
            light_color = color_dict['YELLOW']
        else:
            light_color = color_dict['SILVER']

        if day:
            sky_color = color_dict['BLUE']
            field_color = color_dict['GREEN']
            stripe_color = color_dict['DAY_GREEN']
            cloud_color = color_dict['WHITE']
        else:
            sky_color = color_dict['DARK_BLUE']
            field_color = color_dict['DARK_GREEN']
            stripe_color = color_dict['NIGHT_GREEN']
            cloud_color = color_dict['NIGHT_GRAY']

        for c in clouds:
            c[0] -= 0.5

            if c[0] < -100:
                c[0] = random.randrange(800, 1600)
                c[1] = random.randrange(0, 150)

        # Drawing code (Describe the picture. It isn't actually drawn yet.)
        screen.fill(sky_color)
        SEE_THROUGH.fill(color_dict['ck'])
        SEE_THROUGH.set_colorkey(color_dict['ck'])

        if not day:
            #stars
            for s in stars:
                pygame.draw.ellipse(screen, color_dict['WHITE'], s)

        pygame.draw.rect(screen, field_color, [0, 180, 800, 420])
        pygame.draw.rect(screen, stripe_color, [0, 180, 800, 42])
        pygame.draw.rect(screen, stripe_color, [0, 264, 800, 52])
        pygame.draw.rect(screen, stripe_color, [0, 368, 800, 62])
        pygame.draw.rect(screen, stripe_color, [0, 492, 800, 82])

        draw_fence(0, 170)

        sun_moon(520, 50, 40)

        draw_clouds()

        draw_boundary_lines()

        draw_safety_circle()

        draw_goal_boxes()

        draw_goal_box_arc()

        draw_score_board_pole()

        draw_score_board()

        draw_goal()

        draw_light_poles(150, 60, 20, 140, 630, 60, 20, 140)

        draw_lights()

        draw_net()

        draw_goal()

        draw_stands()

        draw_flags()

        # DARKNESS
        if not day and not lights_on:
            screen.blit(DARKNESS, (0, 0))

        #pygame.draw.polygon(screen, BLACK, [[200, 200], [50,400], [600, 500]], 10)

        ''' angles for arcs are measured in radians (a pre-cal topic) '''
        #pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
        #pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)

        # Update screen (Actually draw the picture in the window.)
        pygame.display.flip()

        # Limit refresh rate of game loop
        clock.tick(refresh_rate)

    # Close window and quit
    pygame.quit()

main()