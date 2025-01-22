def get_base_string(current_x, current_y):
    return 'X: {:8d}, Y: {:3d} | '.format(current_x, current_y)


def print_base_positions():
    initial_x = 0
    initial_y = 0
    current_x = initial_x
    current_y = initial_y
    width = 3
    height = 3
    output = ""
    for i in range(1, 100):
        current_x += current_x + width
        current_y = current_y + height
        output += get_base_string(current_x, current_y)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_base_positions()

    # modules_and_packages.execute()
    #
    # strings.execute()
    #
    # object_orientation.execute()
    #
    # exceptions.execute()
    #
    # miscellaneous.execute()
