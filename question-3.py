import turtle

def draw_tree(branch_length, right_angle, left_angle, depth, reduction_factor, max_depth):
    if depth > 0:
        # Set color: brown for trunk, green for everything else
        if depth == max_depth:
            turtle.color("brown")  # trunk
            turtle.pensize(10)
        else:
            turtle.color("green")        # branches + leaves
            turtle.pensize(max(1, depth + 1))

        # Draw the current branch
        turtle.forward(branch_length)

        # Right branch
        turtle.right(right_angle)
        draw_tree(branch_length * reduction_factor, right_angle, left_angle, depth - 1, reduction_factor, max_depth)

        # Left branch
        turtle.left(right_angle + left_angle)
        draw_tree(branch_length * reduction_factor, right_angle, left_angle, depth - 1, reduction_factor, max_depth)

        # Return to the previous position and direction
        turtle.right(left_angle)
        turtle.backward(branch_length)

def main():
    # User input
    left_angle = float(input("Enter the left branch angle (in degrees): "))
    right_angle = float(input("Enter the right branch angle (in degrees): "))
    starting_length = float(input("Enter the starting branch length: "))
    recursion_depth = int(input("Enter the recursion depth: "))
    reduction_factor = float(input("Enter the branch length reduction factor (e.g., 0.7): "))

    # Turtle setup
    turtle.speed(0)
    
    turtle.pensize(2)
    turtle.left(90)
    turtle.up()
    turtle.backward(100)
    turtle.down()

    # Draw the tree
    draw_tree(starting_length, right_angle, left_angle, recursion_depth, reduction_factor, recursion_depth)

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()


