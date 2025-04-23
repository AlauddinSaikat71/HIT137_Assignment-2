import turtle

def draw_tree(branch_length, right_angle, left_angle, depth, reduction_factor):
    if depth > 0:
        # Draw the main branch
        turtle.forward(branch_length)
        
        # Draw the right branch
        turtle.right(right_angle)
        draw_tree(branch_length * reduction_factor, right_angle, left_angle, depth - 1, reduction_factor)
        
        # Return to the main branch and draw the left branch
        turtle.left(right_angle + left_angle)
        draw_tree(branch_length * reduction_factor, right_angle, left_angle, depth - 1, reduction_factor)
        
        # Return to the original orientation and position
        turtle.right(left_angle)
        turtle.backward(branch_length)

def main():
    # Get user input
    left_angle = float(input("Enter the left branch angle (in degrees): "))
    right_angle = float(input("Enter the right branch angle (in degrees): "))
    starting_length = float(input("Enter the starting branch length: "))
    recursion_depth = int(input("Enter the recursion depth: "))
    reduction_factor = float(input("Enter the branch length reduction factor (e.g., 0.7): "))

    # Set up the turtle
    turtle.speed(0)
    turtle.left(90)
    turtle.up()
    turtle.backward(100)
    turtle.down()
    
    # Draw the tree
    draw_tree(starting_length, right_angle, left_angle, recursion_depth, reduction_factor)
    
    # Finish up
    turtle.done()

if __name__ == "__main__":
    main()

