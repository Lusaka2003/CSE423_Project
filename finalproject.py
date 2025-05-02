from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math
# Camera-related variables
camera_pos = (0,500,500)

fovY = 120  # Field of view
GRID_LENGTH = 1200  # Length of grid lines
rand_var = 423

cloud1_x=500
cloud1_y=450
cloud2_x=-600
cloud2_y=400
cloud3_x=-800
cloud3_y=-100
cloud4_x=900
cloud4_y=-650
inc=True
dec=False
s=0
snowman_x=0
snowman_y=0
obstacle_x=0
obstacle_y=-300
lives=3
collision_happened=False
night_mode=False
pause=False
score=0
Game_over=False
power_up_x=-80
power_up_y=-1000
gun_power=1
powerup=False
enemy_x = random.randint(-500, 500)
enemy_y = -800
enemy_hit = False
i=random.choice([-0.1,0.1])

bullet_active = False
bullet_x = 0
bullet_y = 0
bullet_angle = 90  # default straight up

# Nose angle (rotatable with 'a' key)
nose_angle = 90
enemy_radius=50

def draw_text(x, y, text, font=GLUT_BITMAP_HELVETICA_18):
    glColor3f(1,1,1)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    
    # Set up an orthographic projection that matches window coordinates
    gluOrtho2D(0, 1000, 0, 800)  # left, right, bottom, top

    
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    
    # Draw text at (x, y) in screen coordinates
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(font, ord(ch))
    
    # Restore original projection and modelview matrices
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)


def draw_shapes():
    global cloud1_x,cloud1_y,cloud2_x,cloud2_y,cloud3_x,cloud3_y,cloud4_x,cloud4_y,s,snowman_x,snowman_y,obstacle_x,obstacle_y,collision_happened
    global enemy_x,enemy_y
    glPushMatrix()  # Save the current matrix state
    if collision_happened==True and night_mode==False:
        glColor3f(0.529, 0.808, 0.922)
    elif collision_happened==True and night_mode==True:
        glColor3f(0.05, 0.05, 0.2)
    else:
        glColor3f(1, 1, 1)
    glTranslatef(0+snowman_x, 0+snowman_y, 0)
    glTranslatef(0, 250, 0)  
    gluSphere(gluNewQuadric(), 50, 10, 10) # Take cube size as the parameter
    glTranslatef(0, 70, 0) 
    gluSphere(gluNewQuadric(), 30, 10, 10)
    glTranslatef(0, -70, 0) 
    glTranslatef(0, 60, 0) 
    glRotatef(180, 1, 0, 0)
    glRotatef(nose_angle, 0, 1, 0) 
    glColor3f(1.0, 0.647, 0.0)
    gluCylinder(gluNewQuadric(), 10, 5, 40, 10, 10)
    glRotatef(-180, 1, 0, 0)
    glTranslatef(0, -60, 0) 
    glTranslatef(0, -250, 0) 
    glTranslatef(snowman_x, 0, 0)
    glPopMatrix() 
    #cloud1 part1
    glPushMatrix()
    if night_mode==False:
        glColor3f(0.85, 0.85, 0.85)
    else:
        glColor3f(0.55, 0.55, 0.55)
    glTranslatef(cloud1_x, cloud1_y, 0)
    gluSphere(gluNewQuadric(), 60, 10, 10)
    glPopMatrix()

    # Cloud1 part 2
    glPushMatrix()
    glTranslatef(cloud1_x+80, cloud1_y, 0)  # Use actual world coordinates, not relative
    gluSphere(gluNewQuadric(), 60, 10, 10)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(cloud2_x, cloud2_y, 0)  # Use actual world coordinates, not relative
    gluSphere(gluNewQuadric(), 60, 10, 10)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(cloud2_x+80, cloud2_y, 0)  # Use actual world coordinates, not relative
    gluSphere(gluNewQuadric(), 60, 10, 10)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(cloud3_x, cloud3_y, 0)  # Use actual world coordinates, not relative
    gluSphere(gluNewQuadric(), 60, 10, 10)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(cloud3_x+80, cloud3_y, 0)  # Use actual world coordinates, not relative
    gluSphere(gluNewQuadric(), 60, 10, 10)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(cloud4_x, cloud4_y, 0)  # Use actual world coordinates, not relative
    gluSphere(gluNewQuadric(), 60, 10, 10)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(cloud4_x+80, cloud4_y, 0)  # Use actual world coordinates, not relative
    gluSphere(gluNewQuadric(), 60, 10, 10)
    glPopMatrix() 

    glPushMatrix()

    glScalef(1 + s, 1 + s, 1 + s)  # Scale everything together
    glTranslatef(obstacle_x, obstacle_y, 0)  # Apply vertical shift to all parts

    glColor3f(0.545, 0.1, 0.0)  # Dark red
    glRotatef(90, 0, 1, 0)
    gluCylinder(gluNewQuadric(), 10, 10, 500, 20, 20)


    glPopMatrix()

    #pause_button
    if not pause:
        glPushMatrix()

        glTranslatef(0, 800, 0)  # Apply vertical shift to all parts

        glColor3f(0.9, 0.9, 0.0)  # yellow
        glRotatef(180, 0, 1, 0)
        gluCylinder(gluNewQuadric(), 10, 10, 50, 20, 20)
        glRotatef(-180, 0, 1, 0)
        glTranslatef(50, 0, 0)
        glRotatef(180, 0, 1, 0)
        gluCylinder(gluNewQuadric(), 10, 10, 50, 20, 20)

        glPopMatrix()

    #play_button
    else:
        glPushMatrix()

        glTranslatef(0, 750, 0)  # Apply vertical shift to all parts

        glColor3f(0.9, 0.9, 0.0)  # yellow
        glRotatef(90, 0, 1, 0)
        gluCylinder(gluNewQuadric(), 30, 0, 70, 20, 20)


        glPopMatrix()

    glPushMatrix()
    glColor3f(0, 0, 0)  # Red color
    glTranslatef(enemy_x, enemy_y, 0)
    gluSphere(gluNewQuadric(), 40, 10, 10)
    glPopMatrix()

# Restore the previous matrix state
def draw_power_ups():
    global obstacle_x,obstacle_y,s,power_up_x,power_up_y
    if power_up_y<200:
        glPushMatrix()
        glColor3f(0.75,0.5,1.0)
        glTranslatef(power_up_x, power_up_y, 0)  # Use actual world coordinates, not relative
        glScalef(1 + 2*s, 1 + 2*s, 1 + 2*s) 
        gluSphere(gluNewQuadric(), 60, 10, 10)
        glPopMatrix()
def draw_bullet():
    if bullet_active:
        glPushMatrix()
        glColor3f(1, 0, 0)
        glTranslatef(bullet_x, bullet_y, 0)
        glutSolidSphere(10, 10, 10)
        glPopMatrix()
def update_bullet():
    global bullet_active, bullet_x, bullet_y, score
    if bullet_active:
        speed = 15
        rad = math.radians(bullet_angle)
        bullet_x += speed * math.cos(rad)
        bullet_y += speed * math.sin(rad)

        # Check collision with enemy
        dx = bullet_x - enemy_x
        dy = bullet_y - enemy_y
        distance = math.sqrt(dx * dx + dy * dy)
        if distance < enemy_radius:
            bullet_active = False
            score += 1
            print("Hit! Score:", score)

        # Deactivate bullet if offscreen
        if abs(bullet_x) > 1000 or abs(bullet_y) > 1000:
            bullet_active = False

def keyboardListener(key, x, y):
    global camera_pos,night_mode,Game_over,lives,cloud1_x,cloud1_y,cloud2_x,cloud2_y,cloud3_x,cloud3_y,cloud4_x,cloud4_y,s,snowman_x,snowman_y,obstacle_x,obstacle_y,inc,dec,collision_happened,score
    global nose_angle, bullet_active, bullet_x, bullet_y, bullet_angle
    x, y, z = camera_pos
    # Move camera up (UP arrow key)
    if key == b'm':
        if z<500:
            z+=5

    # Move camera down (DOWN arrow key)
    if key == b'z':
        if z>=350:
            z-=5
    # moving camera left (LEFT arrow key)
    if key == b'l':
        x -= 1  # Small angle decrement for smooth movement

    # moving camera right (RIGHT arrow key)
    if key == b'r':
        x += 1  # Small angle increment for smooth movement
    if key == b'n':  
        night_mode=not night_mode

    if key == b'\r':
        Game_over=False
        lives=3
        cloud1_x=500
        cloud1_y=450
        cloud2_x=-600
        cloud2_y=400
        cloud3_x=-800
        cloud3_y=-100
        cloud4_x=900
        cloud4_y=-650
        inc=True
        dec=False
        s=0
        snowman_x=0
        snowman_y=0
        obstacle_x=0
        obstacle_y=-300
        collision_happened=False
        score=0
    
    if key == b'a':
        nose_angle = (nose_angle + 10) % 360
    elif key == b' ' and not bullet_active:
        bullet_active = True
        bullet_x = snowman_x  # or adjust slightly if nose is offset
        bullet_y = snowman_y + 250
        bullet_angle = nose_angle
    camera_pos = (x, y, z)



def specialKeyListener(key, x, y):
    """
    Handles special key inputs (arrow keys) for adjusting the camera angle and height.
    """
    global snowman_x,snowman_y,camera_pos
    x, y, z = camera_pos
    # Move camera up (UP arrow key)
    if key == GLUT_KEY_UP:
        z+=1

    # Move camera down (DOWN arrow key)
    if key == GLUT_KEY_DOWN:
        z-=1
    # moving camera left (LEFT arrow key)
    if key == GLUT_KEY_LEFT:
        snowman_x-= 10 # Small angle decrement for smooth movement

    # moving camera right (RIGHT arrow key)
    if key == GLUT_KEY_RIGHT:
        snowman_x+= 10  # Small angle increment for smooth movement
    
    
    camera_pos = (x, y, z)

def mouseListener(button, state, x, y):
    """
    Handles mouse inputs for firing bullets (left click) and toggling camera mode (right click).
    """
        # # Left mouse button fires a bullet
    global pause
    new_y=700-y
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN :
        print(x)
        if new_y<=680 and new_y>=640 and x>=490 and x<=530:
            pause=not pause


        # # Right mouse button toggles camera tracking mode
        # if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:


def setupCamera():

    glMatrixMode(GL_PROJECTION)  # Switch to projection matrix mode
    glLoadIdentity()  # Reset the projection matrix
    # Set up a perspective projection (field of view, aspect ratio, near clip, far clip)
    gluPerspective(fovY, 1.25, 0.1, 1000) # Think why aspect ration is 1.25?
    glMatrixMode(GL_MODELVIEW)  # Switch to model-view matrix mode
    glLoadIdentity()  # Reset the model-view matrix

    # Extract camera position and look-at target
    x, y, z = camera_pos
    # Position the camera and set its orientation
    gluLookAt(x, 0, z,   # Camera position (x, y, z) - in front and slightly above
              0, 0, 0,       # Target: look at the origin
              0, 1, 0)  # Up vector (z-axis)


def idle():
    """
    Idle function that runs continuously:
    - Triggers screen redraw for real-time updates.
    """
    global s,inc,dec,obstacle_y,obstacle_x,cloud1_x,cloud1_y,cloud2_x,cloud2_y,cloud3_x,cloud3_y,cloud4_x,cloud4_y,snowman_x,lives,collision_happened,Game_over
    global power_up_x,power_up_y,gun_power,powerup, enemy_x,enemy_y,enemy_hit,i
    if pause==False and Game_over==False:
        if inc:
            if s>=0.05:
                inc=False
                dec=True
            s+=0.0001
        if dec:
            if s<=0.0001:
                inc=True
                dec=False
            s-=0.0001
        if obstacle_y>=850:
            obstacle_x=random.randint(-600,400)
            obstacle_y=-800
        obstacle_y+=0.4
        if cloud1_y>900:
            cloud1_x=random.randint(300,600)
            cloud1_y=-900
        cloud1_y+=0.4
        if cloud2_y>900:
            cloud2_x=random.randint(-700,-300)
            cloud2_y=-900
        cloud2_y+=0.4
        if cloud3_y>900:
            cloud3_x=random.randint(300,600)
            cloud3_y=-900
        cloud3_y+=0.4
        if cloud4_y>900:
            cloud4_x=random.randint(-700,-300)
            cloud4_y=-900
        cloud4_y+=0.4
        if power_up_y>900:
            power_up_x=random.randint(-700,-300)
            power_up_y=-4000
        power_up_y+=0.4
        if obstacle_x>=0 and snowman_x>=obstacle_x:
            if (-obstacle_x + snowman_x) < 500 and abs(obstacle_y - 250) < 20:
                if not collision_happened:
                    lives -= 1
                    collision_happened = True
            elif abs(obstacle_x - snowman_x) >= 500 or abs(obstacle_y - 250) >= 20:
                collision_happened = False
        elif obstacle_x<0 and snowman_x>=obstacle_x:
            if (-obstacle_x + snowman_x) < 500 and abs(obstacle_y - 250) < 20:
                if not collision_happened:
                    lives -= 1
                    collision_happened = True
            elif abs(obstacle_x - snowman_x) >= 500 or abs(obstacle_y - 250) >= 20:
                collision_happened = False

        if abs(-power_up_x + snowman_x) < 50 and abs(power_up_y - snowman_y) < 2:
            if not powerup:
                gun_power+=1
                powerup = True
        elif abs(power_up_x - snowman_x) >= 50 or abs(power_up_y - snowman_y) >= 2:
            powerup = False

        if enemy_y >= 900:
            enemy_x = random.randint(-500, 500)
            i=random.choice([-0.1,0.1])
            enemy_y = -800
            enemy_hit = False

        enemy_y += 0.5
        enemy_x+=i

        # Collision check with snowman
        dx = snowman_x - enemy_x
        dy = snowman_y + 250 - enemy_y  # Match vertical snowman position
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance < 80 and not enemy_hit:  # 80 = approx radius sum
            lives -= 1
            enemy_hit = True
            print("Collision with enemy! Lives left:", lives)
            if lives <= 0:
                Game_over = True

    else:
        pass


    if lives==0:
        Game_over=True
    
    update_bullet()
    
    
    # Ensure the screen updates with the latest changes
    glutPostRedisplay()


def showScreen():
    """
    Display function to render the game scene:
    - Clears the screen and sets up the camera.
    - Draws everything of the screen
    """
    # Clear color and depth buffers
    global night_mode
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()  # Reset modelview matrix
    glViewport(0, 0, 1000, 700)  # Set viewport size

    setupCamera()  # Configure camera perspective

    # Draw a random points
    glPointSize(20)
    glBegin(GL_POINTS)
    glVertex3f(-GRID_LENGTH, GRID_LENGTH, 0)
    glEnd()

    # Draw the grid (game floor)
    glBegin(GL_QUADS)
    if night_mode==True:
        glColor3f(0.05, 0.05, 0.2)
    else:
        glColor3f(0.529, 0.808, 0.922)
    glVertex3f(-GRID_LENGTH, GRID_LENGTH, 0)
    glVertex3f(GRID_LENGTH, GRID_LENGTH, 0)
    glVertex3f(GRID_LENGTH, -GRID_LENGTH, 0)
    glVertex3f(-GRID_LENGTH, -GRID_LENGTH, 0)

    glEnd()

    # Display game info text at a fixed screen position
    draw_text(10, 770, f"Welcome to Sky Drop Survival")
    draw_text(10, 740, f"Remaining lives: {lives}")
    draw_text(10, 710, f"Total Score: {score}")
    # draw_text(10, 680, f"Total Score: {power_up_y,power_up_x}")
    # draw_text(10, 650, f"Total Score: {snowman_y,snowman_x}")
    draw_text(10, 680, f"Gun Power: {gun_power}")
    if Game_over:
        draw_text(450, 450, f"GAME OVER")
        draw_text(450, 420, f"PRESS ENTER TO RESTART")

    draw_shapes()
    draw_power_ups()
    draw_bullet()
    # Swap buffers for smooth rendering (double buffering)
    glutSwapBuffers()


# Main function to set up OpenGL window and loop
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)  # Double buffering, RGB color, depth test
    glutInitWindowSize(1000, 700)  # Window size
    glutInitWindowPosition(0, 0)  # Window position
    wind = glutCreateWindow(b"3D OpenGL Intro")  # Create the window

    glutDisplayFunc(showScreen)  # Register display function
    glutKeyboardFunc(keyboardListener)  # Register keyboard listener
    glutSpecialFunc(specialKeyListener)
    glutMouseFunc(mouseListener)
    glutIdleFunc(idle)  # Register the idle function to move the bullet automatically

    glutMainLoop()  # Enter the GLUT main loop

if __name__ == "__main__":
    main()

