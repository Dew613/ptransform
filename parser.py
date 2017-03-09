from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
        takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
     ident: set the transform matrix to the identity matrix - 
     scale: create a scale matrix, 
        then multiply the transform matrix by the scale matrix - 
        takes 3 arguments (sx, sy, sz)
     translate: create a translation matrix, 
        then multiply the transform matrix by the translation matrix - 
        takes 3 arguments (tx, ty, tz)
     rotate: create a rotation matrix,
        then multiply the transform matrix by the rotation matrix -
        takes 2 arguments (axis, theta) axis should be x, y or z
     yrotate: create an y-axis rotation matrix,
        then multiply the transform matrix by the rotation matrix -
        takes 1 argument (theta)
     zrotate: create an z-axis rotation matrix,
        then multiply the transform matrix by the rotation matrix -
        takes 1 argument (theta)
     apply: apply the current transformation matrix to the 
        edge matrix
     display: draw the lines of the edge matrix to the screen
        display the screen
     save: draw the lines of the edge matrix to the screen
        save the screen to a file -
        takes 1 argument (file name)
     quit: end parsing

See the file script for an example of the file format
"""

def parse_file( fname, points, transform, screen, color ):
    f=open(fname, "r")
    print "opened script\n"
    line = f.readline()
    
    while (line !="" and line!="quit"):
        
        if (line == "line\n"):
            line = f.readline()
            args = line.split()
            add_edge(points, int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]))
            print "edge made\n"
            
        elif (line == "ident\n"):
            ident(transform)
            print "transform reset\n"
            
        elif (line == "scale\n"):
            line = f.readline()
            args = line.split()
            matrix = make_scale( int(args[0]), int(args[1]), int(args[2]))
            matrix_mult(matrix, transform)
            print "picture scaled\n"

        elif (line=="move\n"):
            line = f.readline()
            args = line.split()
            matrix=make_translate( int(args[0]), int(args[1]), int(args[2]))
            matrix_mult(matrix, transform)
            print "picture moved\n"

        elif (line=="rotate\n"):
            line=f.readline()
            args=line.split()
            if (args[0]=="x"):
                matrix=make_rotX(int(args[1]))
            elif (args[0] =="y"):
                matrix=make_rotY(int(args[1]))
            elif (args[0] =="z"):
                matrix=make_rotZ(int(args[1]))
            matrix_mult(matrix, transform)
            print "picture rotated\n"
            
        elif(line=="apply\n"):
            matrix_mult(transform, points)
            print "changes applied\n"

        elif(line=="display\n"):
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
            print "display activated\n"

        elif(line=="save\n"):
            line=f.readline()
            args=line.split()
            save_extension(screen,args[0])
            print "imaged saved\n"
        else:
            print "Command not recognized\n"
            
        line=f.readline()

    f.close
    print "closed script"

    
