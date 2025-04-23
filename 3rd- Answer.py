import turtle

def draw_tree(branch_length, right_angle, left_angle, depth, reduction_factor):
    if depth > 0:
        # Draw the main branch
        turtle.forward(branch_length)
        
        # Draw the right branch
        turtle.right(angle)
        draw_tree(branch_length * reduction_factor, angle, depth - 1, reduction_factor)
        
        # Draw the left branch
        turtle.left(angle * 2)  # Turn left by double the angle
        draw_tree(branch_length * reduction_factor, angle, depth - 1, reduction_factor)
        
        # Return to the original position and orientation
        turtle.right(angle)  # Turn back to the right
        turtle.backward(branch_length)  # Go back to the previous branch

def main():
    # Get user input
    left_angle = float(input("Enter the left branch angle (in degrees): "))
    right_angle = float(input("Enter the right branch angle (in degrees): "))
    starting_length = float(input("Enter the starting branch length: "))
    recursion_depth = int(input("Enter the recursion depth: "))
    reduction_factor = float(input("Enter the branch length reduction factor (e.g., 0.7): "))

    # Set up the turtle
    turtle.speed(0)  # Fastest drawing speed
    turtle.left(90)  # Start facing upwards
    turtle.up()
    turtle.backward(100)  # Move the turtle down to start drawing
    turtle.down()
    
    # Draw the tree
    draw_tree(starting_length, right_angle, left_angle, recursion_depth, reduction_factor)
    
    # Finish up
    turtle.done()

if __name__ == "__main__":
    main()
