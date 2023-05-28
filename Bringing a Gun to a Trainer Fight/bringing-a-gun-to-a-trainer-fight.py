from math import sqrt
from numpy import zeros


def computeDist(p1, p2):
    # Compute the Euclidean distance between two points
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def computeGCD(x, y):
    # Compute the greatest common divisor using the Euclidean algorithm
    while(y):
        x, y = y, x % y
    return abs(x)


def get_entity_position_from_room_number(entity, room_number, dimensions):
    # Calculate the actual position of an entity within a room given the room number and dimensions
    r_x, r_y = room_number
    e_x, e_y = entity
    dim_x, dim_y = dimensions

    res_x = dim_x*r_x + e_x if r_x % 2 == 0 else dim_x*r_x + (dim_x - e_x)
    res_y = dim_y*r_y + e_y if r_y % 2 == 0 else dim_y*r_y + (dim_y - e_y)

    return (res_x, res_y)


def solution(dimensions, your_position, trainer_position, distance):
    dim_x, dim_y = dimensions
    m_x, m_y = your_position

    # Calculate the number of rooms in each direction based on the given distance
    num_rooms_above_x_axis = (distance + m_y)//dim_y + 1
    num_rooms_below_x_axis = (distance - m_y)//dim_y + 1
    num_rooms_left_of_y_axis = (distance - m_x)//dim_x + 1
    num_rooms_right_of_y_axis = (distance + m_x)//dim_x + 1

    # Calculate the width and height of the matrix based on the number of rooms
    w = (num_rooms_right_of_y_axis + num_rooms_left_of_y_axis)*dim_x + 1
    h = (num_rooms_above_x_axis + num_rooms_below_x_axis)*dim_y + 1

    # Calculate the offset values for the matrix coordinates
    x_offset = num_rooms_left_of_y_axis*dim_x
    y_offset = num_rooms_below_x_axis*dim_y

    # Create a matrix to represent the rooms and entities
    matrix = zeros(shape=(w, h))
    for i in range(-1*num_rooms_left_of_y_axis, num_rooms_right_of_y_axis):
        for j in range(-1*num_rooms_below_x_axis, num_rooms_above_x_axis):
            tv_x, tv_y = get_entity_position_from_room_number(
                trainer_position, [i, j], dimensions)

            mv_x, mv_y = get_entity_position_from_room_number(
                your_position, [i, j], dimensions)

            # Set the matrix values to represent the trainer and your positions
            matrix[tv_x+x_offset][tv_y+y_offset] = 1
            matrix[mv_x+x_offset][mv_y+y_offset] = 2

    hits = 0
    shots_taken = set()
    for i in range(-1*num_rooms_left_of_y_axis, num_rooms_right_of_y_axis):
        for j in range(-1*num_rooms_below_x_axis, num_rooms_above_x_axis):
            t_x, t_y = get_entity_position_from_room_number(
                trainer_position, [i, j], dimensions)
            if distance < computeDist([t_x, t_y], your_position):
                continue
            delta_y = t_y - m_y
            delta_x = t_x - m_x
            d = computeGCD(delta_y, delta_x)
            delta_y = int(delta_y/d)
            delta_x = int(delta_x/d)
            if (delta_y, delta_x) in shots_taken:
                continue
            shots_taken.add((delta_y, delta_x))
            ray_x, ray_y = m_x + x_offset, m_y + y_offset
            while True:
                ray_x += delta_x
                ray_y += delta_y
                entity = matrix[ray_x][ray_y]
                if entity == 1:
                    hits += 1
                    break
                elif entity == 2:
                    break
    return hits


if __name__ == "__main__":
    # Example usage
    print(solution([3, 2], [1, 1], [2, 1], 4))
    print(solution([300, 275], [150, 150], [185, 100], 500))
