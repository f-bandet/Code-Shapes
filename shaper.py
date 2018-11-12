### 
### Author: Faye Bandet
### Course: CSC 110
### Description: This is a program that prints out several shapes via text.
###
from os import _exit as exit
###Main function
def main():
    shape = input('Enter shape to display: \n')
    arrow_char = input('Enter arrow character: \n')
    height = int(input('Enter row-area height: \n'))
    while shape.lower() != 'house' and shape.lower() != 'plumbbob' and shape.lower() != 'hourglass':
        print('!!! Enter a different shape !!!')
        shape = input('Enter shape to display: \n')
        arrow_char = input('Enter arrow character: \n')
        height = int(input('Enter row-area height: \n'))
    print()
    shape_printer(shape,arrow_char,height)

def shape_printer(shape,arrow_char,height):    
    '''
    This function prints the shape, arrow characters, and height
    of the shape. 
    Shape: shape should be a string
    Arrow character: should be a one character string
    Height: this should be a numerical value
    '''
    if shape.lower() == 'house': 
        up_arrow(arrow_char)
        dashes(height)
    if shape.lower() == 'plumbbob':
        up_arrow(arrow_char)
        dashes(height)
        down_arrow(arrow_char)
    if shape.lower() == 'hourglass':
        dashes(height)
        down_arrow(arrow_char)
        up_arrow(arrow_char)
        dashes(height)
        
def up_arrow(c):
    '''
    This prints the upwards facing arrow.
    C is the one string character that equals the arrow character.
    '''
    print (' '*5 +c)
    print (' '*4 + c*3)
    print (' '*3 + c*5)
    print (' '*2 + c*7)
    print (' '*1 + c*9)
    print (c * 11)
    
def down_arrow(c):
    '''
    This prints the downwards facing arrow.
    C is the one string character that equals the arrow character.
    '''
    print (c * 11)
    print (' '*1 + c*9)
    print (' '*2 + c*7)
    print (' '*3 + c*5)
    print (' '*4 + c*3)
    print (' '*5 +c)
    
def dashes(h):
    '''
    This prints the dashes for the shape
    H is the height input, an integer.
    '''
    i=0
    while i < h:
        print('|---------|')
        i+=1
    
main()

### Function for upwards arrow