# Imported libraries
import pygame
import math
import random

# Initialize game engine
pygame.init()


# Window
def draw_window(length, width, title):
    screen = pygame.display.set_mode((length,width))
    pygame.display.set_caption(title)
    return screen

screen = draw_window(800,600,'Major League Soccer')


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
''' add colors you use as RGB values here '''
def define_colors():
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

color_dict = define_colors()

DARKNESS = pygame.Surface((800,600))
DARKNESS.set_alpha(200)
DARKNESS.fill((0, 0, 0))

SEE_THROUGH = pygame.Surface((800, 180))
SEE_THROUGH.set_alpha(150)
SEE_THROUGH.fill((124, 118, 135))

def draw_cloud(x, y):
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x, y + 8, 10, 10])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 6, y + 4, 8, 8])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 10, y, 16, 16])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 20, y + 8, 10, 10])
    pygame.draw.rect(SEE_THROUGH, cloud_color, [x + 6, y + 8, 18, 10])


# Config
lights_on = True
day = True

def randomize_star_positions(num_stars):
    stars = []
    for n in range(num_stars):
        x = random.randrange(0, 800)
        y = random.randrange(0, 200)
        r = random.randrange(1, 2)
        stars.append([x, y, r, r])
    return stars
stars = randomize_star_positions(200)

def randomize_cloud_positions(num_clouds):
    clouds = []
    for i in range(num_clouds):
        x = random.randrange(-100, 1600)
        y = random.randrange(0, 150)
        clouds.append([x, y])    
    return clouds
clouds = randomize_cloud_positions(20)

    
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




    pygame.draw.rect(screen, field_color, [0, 180, 800 , 420])
    pygame.draw.rect(screen, stripe_color, [0, 180, 800, 42])
    pygame.draw.rect(screen, stripe_color, [0, 264, 800, 52])
    pygame.draw.rect(screen, stripe_color, [0, 368, 800, 62])
    pygame.draw.rect(screen, stripe_color, [0, 492, 800, 82])


    def draw_fence():
        '''fence'''
        y = 170
        for x in range(5, 800, 30):
            pygame.draw.polygon(screen, color_dict['NIGHT_GRAY'], [[x + 2, y], [x + 2, y + 15], [x, y + 15], [x, y]])

        y = 170
        for x in range(5, 800, 3):
            pygame.draw.line(screen, color_dict['NIGHT_GRAY'], [x, y], [x, y + 15], 1)

        x = 0
        for y in range(170, 185, 4):
            pygame.draw.line(screen, color_dict['NIGHT_GRAY'], [x, y], [x + 800, y], 1)

        if day:
            pygame.draw.ellipse(screen, color_dict['BRIGHT_YELLOW'], [520, 50, 40, 40])
        else:
            pygame.draw.ellipse(screen, color_dict['WHITE'], [520, 50, 40, 40]) 
            pygame.draw.ellipse(screen, sky_color, [530, 45, 40, 40])
    draw_fence()

    
    def draw_clouds():    
        for c in clouds:
            draw_cloud(c[0], c[1])
        screen.blit(SEE_THROUGH, (0, 0))
    draw_clouds()   
    
    def draw_boundary_lines():
        #out of bounds lines
        pygame.draw.line(screen, color_dict['WHITE'], [0, 580], [800, 580], 5)
        #left
        pygame.draw.line(screen, color_dict['WHITE'], [0, 360], [140, 220], 5)
        pygame.draw.line(screen, color_dict['WHITE'], [140, 220], [660, 220], 3)
        #right
        pygame.draw.line(screen, color_dict['WHITE'], [660, 220], [800, 360], 5)
    draw_boundary_lines()

    def draw_safety_circle():
        #safety circle
        pygame.draw.ellipse(screen, color_dict['WHITE'], [240, 500, 320, 160], 5)
    draw_safety_circle()

    #18 yard line goal box
    def draw_goal_boxes():
        pygame.draw.line(screen, color_dict['WHITE'], [260, 220], [180, 300], 5)
        pygame.draw.line(screen, color_dict['WHITE'], [180, 300], [620, 300], 3)
        pygame.draw.line(screen, color_dict['WHITE'], [620, 300], [540, 220], 5)
        #6 yard line goal box
        pygame.draw.line(screen, color_dict['WHITE'], [310, 220], [270, 270], 3)
        pygame.draw.line(screen, color_dict['WHITE'], [270, 270], [530, 270], 2)
        pygame.draw.line(screen, color_dict['WHITE'], [530, 270], [490, 220], 3)
    draw_goal_boxes()

    def draw_goal_box_arc():
        #arc at the top of the goal box
        pygame.draw.arc(screen, color_dict['WHITE'], [330, 280, 140, 40], math.pi, 2 * math.pi, 5)
    draw_goal_box_arc()

    def draw_score_board_pole():
        #score board pole
        pygame.draw.rect(screen, color_dict['GRAY'], [390, 120, 20, 70])
    draw_score_board_pole()

    def draw_score_board():
        #score board
        pygame.draw.rect(screen, color_dict['BLACK'], [300, 40, 200, 90])
        pygame.draw.rect(screen, color_dict['WHITE'], [302, 42, 198, 88], 2)
    draw_score_board()

    def draw_goal():
        #goal
        pygame.draw.rect(screen, color_dict['WHITE'], [320, 140, 160, 80], 5)
        pygame.draw.line(screen, color_dict['WHITE'], [340, 200], [460, 200], 3)
        pygame.draw.line(screen, color_dict['WHITE'], [320, 220], [340, 200], 3)
        pygame.draw.line(screen, color_dict['WHITE'], [480, 220], [460, 200], 3)
        pygame.draw.line(screen, color_dict['WHITE'], [320, 140], [340, 200], 3)
        pygame.draw.line(screen, color_dict['WHITE'], [480, 140], [460, 200], 3)
    draw_goal()

    def draw_light_poles():
        #light pole 1
        pygame.draw.rect(screen, color_dict['GRAY'], [150, 60, 20, 140])
        pygame.draw.ellipse(screen, color_dict['GRAY'], [150, 195, 20, 10])
        #light pole 2
        pygame.draw.rect(screen, color_dict['GRAY'], [630, 60, 20, 140])
        pygame.draw.ellipse(screen, color_dict['GRAY'], [630, 195, 20, 10])
    draw_light_poles()

    def draw_lights():
        #lights for pole 1
        pygame.draw.line(screen, color_dict['GRAY'], [110, 60], [210, 60], 2)
        pygame.draw.ellipse(screen, light_color, [110, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [130, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [150, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [170, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [190, 40, 20, 20])
        pygame.draw.line(screen, color_dict['GRAY'], [110, 40], [210, 40], 2)
        pygame.draw.ellipse(screen, light_color, [110, 20, 20, 20])
        pygame.draw.ellipse(screen, light_color, [130, 20, 20, 20])
        pygame.draw.ellipse(screen, light_color, [150, 20, 20, 20])
        pygame.draw.ellipse(screen, light_color, [170, 20, 20, 20])
        pygame.draw.ellipse(screen, light_color, [190, 20, 20, 20])
        pygame.draw.line(screen, color_dict['GRAY'], [110, 20], [210, 20], 2)
        #lights for pole 2
        pygame.draw.line(screen, color_dict['GRAY'], [590, 60], [690, 60], 2)
        pygame.draw.ellipse(screen, light_color, [590, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [610, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [630, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [650, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [670, 40, 20, 20])
        pygame.draw.line(screen, color_dict['GRAY'], [590, 40], [690, 40], 2)
        pygame.draw.ellipse(screen, light_color, [590, 20, 20, 20])
        pygame.draw.ellipse(screen, light_color, [610, 20, 20, 20])
        pygame.draw.ellipse(screen, light_color, [630, 20, 20, 20])
        pygame.draw.ellipse(screen, light_color, [650, 20, 20, 20])
        pygame.draw.ellipse(screen, light_color, [670, 20, 20, 20])
        pygame.draw.line(screen, color_dict['GRAY'], [590, 20], [690, 20], 2)
    draw_lights()

    def draw_net():
        #net
        pygame.draw.line(screen, color_dict['WHITE'], [325, 140], [341, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [330, 140], [344, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [335, 140], [347, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [340, 140], [350, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [345, 140], [353, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [350, 140], [356, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [355, 140], [359, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [360, 140], [362, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [364, 140], [365, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [368, 140], [369, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [372, 140], [373, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [376, 140], [377, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [380, 140], [380, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [384, 140], [384, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [388, 140], [388, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [392, 140], [392, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [396, 140], [396, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [400, 140], [400, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [404, 140], [404, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [408, 140], [408, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [412, 140], [412, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [416, 140], [416, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [420, 140], [420, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [424, 140], [423, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [428, 140], [427, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [432, 140], [431, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [436, 140], [435, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [440, 140], [438, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [445, 140], [441, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [450, 140], [444, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [455, 140], [447, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [460, 140], [450, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [465, 140], [453, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [470, 140], [456, 200], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [475, 140], [459, 200], 1)
        #net part 2
        pygame.draw.line(screen, color_dict['WHITE'], [320, 140], [324, 216], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [320, 140], [326, 214], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [320, 140], [328, 212], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [320, 140], [330, 210], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [320, 140], [332, 208], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [320, 140], [334, 206], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [320, 140], [336, 204], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [320, 140], [338, 202], 1)
        #net part 3
        pygame.draw.line(screen, color_dict['WHITE'], [480, 140], [476, 216], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [480, 140], [474, 214], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [480, 140], [472, 212], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [480, 140], [470, 210], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [480, 140], [468, 208], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [480, 140], [466, 206], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [480, 140], [464, 204], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [480, 140], [462, 202], 1)
        #net part 4
        pygame.draw.line(screen, color_dict['WHITE'], [324, 144], [476, 144], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [324, 148], [476, 148], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [324, 152], [476, 152], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [324, 156], [476, 156], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [324, 160], [476, 160], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [324, 164], [476, 164], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [324, 168], [476, 168], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [324, 172], [476, 172], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [324, 176], [476, 176], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [335, 180], [470, 180], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [335, 184], [465, 184], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [335, 188], [465, 188], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [335, 192], [465, 192], 1)
        pygame.draw.line(screen, color_dict['WHITE'], [335, 196], [465, 196], 1)
    draw_goal()

    def draw_stands():
        #stands right
        pygame.draw.polygon(screen, color_dict['RED'], [[680, 220], [800, 340], [800, 290], [680, 180]])
        pygame.draw.polygon(screen, color_dict['WHITE'], [[680, 180], [800, 100], [800, 290]])
        #stands left
        pygame.draw.polygon(screen, color_dict['RED'], [[120, 220], [0, 340], [0, 290], [120, 180]])
        pygame.draw.polygon(screen, color_dict['WHITE'], [[120, 180], [0, 100], [0, 290]])
        #people
    draw_stands()
    
    def draw_flags():
        #corner flag right
        pygame.draw.line(screen, color_dict['BRIGHT_YELLOW'], [140, 220], [135, 190], 3)
        pygame.draw.polygon(screen, color_dict['RED'], [[132, 190], [125, 196], [135, 205]])
        #corner flag left
        pygame.draw.line(screen, color_dict['BRIGHT_YELLOW'], [660, 220], [665, 190], 3)
        pygame.draw.polygon(screen, color_dict['RED'], [[668, 190], [675, 196], [665, 205]]) 
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