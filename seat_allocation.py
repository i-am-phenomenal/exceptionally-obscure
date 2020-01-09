#  AIRCRAFT SEAT ALLOCATION
# Note -> A  value "X" in the matrix signifies that the seat is taken or alloted.

import numpy


def check_if_row_available(seats, row_number):
    row = seats[row_number]
    slice_object = slice(2, 6, 1)
    mid_elements = row[slice_object]
    if "X" not in mid_elements:
        return True
    else:
        return False


def assign_mid_seats(seats, row_number):
    row = seats[row_number]
    slice_object = slice(2, 6, 1)
    mid_elements = row[slice_object]
    for iter in range(0, len(row)):
        if row[iter] in mid_elements:
            row[iter] = "X"
        else:
            pass
    seats[row_number] = row
    return seats


def assign_corner_seats(seats, row_number):
    row = seats[row_number]
    for iter in range(0, len(row)):
        if iter in [0, 1, 6, 7]:
            row[iter] = "X"
        else:
            pass

    seats[row_number] = row
    return seats


def are_corner_seats_available(seats, row_number):
    row = seats[row_number]
    for iter in range(0, len(row)):
        if iter in [0, 1, 6, 7] and row[iter] is "X":
            return False
        else:
            pass
    print("ROW ", row)
    return True

# WIP ->  use the recursive approach to move to secodn and third row respectively if first row fails


def allocate_four_seats(requested_seats):
    global seats
    for row in range(3):
        for col in range(8):
            if row == 0:
                if check_if_row_available(seats, 0):
                    return assign_mid_seats(seats, 0)

                else:
                    if are_corner_seats_available(seats, 0):
                        return assign_corner_seats(seats, 0)
                    else:
                        row += 1

            elif row == 1:
                print("I am ata row 2")
                if check_if_row_available(seats, 1):
                    return assign_mid_seats(seats, 1)
                else:
                    if are_corner_seats_available(seats, 0):
                        return assign_corner_seats(seats, 1)
                    else:
                        row += 1

            elif row == 2:
                if check_if_row_available(seats, 2):
                    return assign_mid_seats(seats, 2)
                else:
                    if are_corner_seats_available(seats, 2):
                        return assign_corner_seats(seats, 2)
                    else:
                        row += 1


seat_columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
first_row = ["1" + y for y in seat_columns]
second_row = ["2" + y for y in seat_columns]
third_row = ["3" + y for y in seat_columns]

seats = numpy.array([first_row, second_row, third_row])

requested_seats = 4

seats = allocate_four_seats(requested_seats)

updated = allocate_four_seats(seats)
another_updated = allocate_four_seats(updated)
updated_1 = allocate_four_seats(another_updated)
print(updated_1)
