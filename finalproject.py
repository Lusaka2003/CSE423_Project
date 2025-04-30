
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
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
obstacle_y=0
cloud2=random.randint(200,600) 
cloud3=random.randint(-400,400) 
cloud4=random.randint(200,600)

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
    global cloud1_x,cloud1_y,cloud2_x,cloud2_y,cloud3_x,cloud3_y,cloud4_x,cloud4_y,s,snowman_x,snowman_y,obstacle_x,obstacle_y

    glPushMatrix()  # Save the current matrix state
    glColor3f(1, 1, 1)
    glTranslatef(0+snowman_x, 0+snowman_y, 0)
    glTranslatef(0, 250, 0)  
    gluSphere(gluNewQuadric(), 50, 10, 10) # Take cube size as the parameter
    glTranslatef(0, 70, 0) 
    gluSphere(gluNewQuadric(), 30, 10, 10)
    glTranslatef(0, -70, 0) 
    glTranslatef(0, 60, 0) 
    glRotatef(180, 1, 0, 0)
    glColor3f(1.0, 0.647, 0.0)
    gluCylinder(gluNewQuadric(), 10, 5, 40, 10, 10)
    glRotatef(-180, 1, 0, 0)
    glTranslatef(0, -60, 0) 
    glTranslatef(0, -250, 0) 
    glTranslatef(snowman_x, 0, 0)
    glPopMatrix() 
    #cloud1 part1
    glPushMatrix()
    glColor3f(0.85, 0.85, 0.85)
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
# Restore the previous matrix state


def keyboardListener(key, x, y):
    """
    Handles keyboard inputs for player movement, gun rotation, camera updates, and cheat mode toggles.


    """

    global camera_pos
    x, y, z = camera_pos
    # Move camera up (UP arrow key)
    if key == b'm':
        z+=1

    # Move camera down (DOWN arrow key)
    if key == b'z':
        z-=1
    # moving camera left (LEFT arrow key)
    if key == b'l':
        x -= 1  # Small angle decrement for smooth movement

    # moving camera right (RIGHT arrow key)
    if key == b'r':
        x += 1  # Small angle increment for smooth movement

    camera_pos = (x, y, z)
    # # Move forward (W key)
    # if key == b'w':  

    # # Move backward (S key)
    # if key == b's':

    # # Rotate gun left (A key)
    # if key == b'a':

    # # Rotate gun right (D key)
    # if key == b'd':

    # # Toggle cheat mode (C key)
    # if key == b'c':

    # # Toggle cheat vision (V key)
    # if key == b'v':

    # # Reset the game if R key is pressed
    # if key == b'r':


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
        snowman_x-= 5 # Small angle decrement for smooth movement

    # moving camera right (RIGHT arrow key)
    if key == GLUT_KEY_RIGHT:
        snowman_x+= 5  # Small angle increment for smooth movement
    camera_pos = (x, y, z)

def mouseListener(button, state, x, y):
    """
    Handles mouse inputs for firing bullets (left click) and toggling camera mode (right click).
    """
        # # Left mouse button fires a bullet
        # if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:

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
    global s,inc,dec,obstacle_y,obstacle_x,cloud1_x,cloud1_y,cloud2_x,cloud2_y,cloud3_x,cloud3_y,cloud4_x,cloud4_y
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
    obstacle_y+=0.2
    if cloud1_y>900:
        cloud1_x=random.randint(300,600)
        cloud1_y=-900
    cloud1_y+=0.2
    if cloud2_y>900:
        cloud2_x=random.randint(-700,-300)
        cloud2_y=-900
    cloud2_y+=0.2
    if cloud3_y>900:
        cloud3_x=random.randint(300,600)
        cloud3_y=-900
    cloud3_y+=0.2
    if cloud4_y>900:
        cloud4_x=random.randint(-700,-300)
        cloud4_y=-900
    cloud4_y+=0.2
    
    # Ensure the screen updates with the latest changes
    glutPostRedisplay()


def showScreen():
    """
    Display function to render the game scene:
    - Clears the screen and sets up the camera.
    - Draws everything of the screen
    """
    # Clear color and depth buffers
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
    
    glColor3f(0.529, 0.808, 0.922)
    glVertex3f(-GRID_LENGTH, GRID_LENGTH, 0)
    glVertex3f(GRID_LENGTH, GRID_LENGTH, 0)
    glVertex3f(GRID_LENGTH, -GRID_LENGTH, 0)
    glVertex3f(-GRID_LENGTH, -GRID_LENGTH, 0)

    # glVertex3f(GRID_LENGTH, -GRID_LENGTH, 0)
    # glVertex3f(0, -GRID_LENGTH, 0)
    # glVertex3f(0, 0, 0)
    # glVertex3f(GRID_LENGTH, 0, 0)


    # glColor3f(0.7, 0.5, 0.95)
    # glVertex3f(-GRID_LENGTH, -GRID_LENGTH, 0)
    # glVertex3f(-GRID_LENGTH, 0, 0)
    # glVertex3f(0, 0, 0)
    # glVertex3f(0, -GRID_LENGTH, 0)

    # glVertex3f(GRID_LENGTH, GRID_LENGTH, 0)
    # glVertex3f(GRID_LENGTH, 0, 0)
    # glVertex3f(0, 0, 0)
    # glVertex3f(0, GRID_LENGTH, 0)
    glEnd()

    # Display game info text at a fixed screen position
    draw_text(10, 770, f"A Random Fixed Position Text")
    draw_text(10, 740, f"See how the position and variable change?: {rand_var}")

    draw_shapes()

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
