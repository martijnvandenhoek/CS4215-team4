import numpy as np
from numpy import genfromtxt


def collector(raw_data):
    # Layout:
    #     /
    #   a/
    #   /_______
    #   |   b
    #  c|
    #   |
    #

    a_title = "Degree of Phobia"
    b_title = "Type of Therapy"
    c_title = "Gender"
    a_names = ["Mild", "Moderate", "Severe"]
    b_names = ["Desensitization", "Implosion", "Insight"]
    c_names = ["male", "female"]

    # Input definition
    # a = 3
    # b = 3
    # c = 2
    # r = 3
    # DATA = np.array(
    #     [
    #         [
    #             (10, 12, 10),
    #             (12, 9, 11),
    #             (13, 10, 9),
    #             (16, 11, 12),
    #             (14, 13, 11),
    #             (17, 15, 13)
    #         ],
    #         [
    #             (15, 12, 6),
    #             (12, 10, 7),
    #             (14, 11, 5),
    #             (17, 14, 10),
    #             (18, 13, 9),
    #             (16, 12, 11)
    #         ],
    #         [
    #             (13, 11, 10),
    #             (9, 7, 6),
    #             (11, 8, 8),
    #             (16, 10, 11),
    #             (12, 12, 10),
    #             (14, 14, 9)
    #         ]
    #     ]
    # )

    #Sample data for 2^k analysis, taken from the slides of lecture 1_2 slide 31.
    # a = 2
    # b = 2
    # c = 2
    # r = 3 # number of repetitions
    # DATA = np.array(
    #     [
    #         [
    #             (86, 58),
    #             (80, 62),
    #             (74, 60),
    #             (34, 22),
    #             (30, 18),
    #             (35, 20)
    #         ],
    #         [
    #             (50, 46),
    #             (55, 42),
    #             (54, 44),
    #             (11, 14),
    #             (15, 16),
    #             (19, 12)
    #         ]
    #     ]
    # )

    # a = 2
    # b = 2
    # c = 2
    # r = 3 # number of repetitions
    # DATA = np.array(
    #     [
    #         [
    #             (24.1, 17.6),
    #             (29.2, 18.8),
    #             (24.6, 23.2),
    #             (20.0, 14.8),
    #             (21.9, 10.3),
    #             (17.6, 11.3)
    #         ],
    #         [
    #             (14.6, 14.9),
    #             (15.3, 20.4),
    #             (12.3, 12.8),
    #             (16.1, 10.1),
    #             (9.3, 14.4),
    #             (10.8, 6.1)
    #         ]
    #     ]
    # )

    # Read the data and discard the column names
    raw_data = genfromtxt('data/24-10-2019_1324.csv', delimiter=',')
    raw_data = raw_data[1:]
    print raw_data

    levels_A = set(raw_data[:, 0])
    levels_B = set(raw_data[:, 1])
    levels_C = set(raw_data[:, 2])

    print levels_A
    print levels_B
    print levels_C

    indices_A = {}
    for level in levels_A:
        indices_A[level] = len(indices_A)
    indices_B = {}
    for level in levels_B:
        indices_B[level] = len(indices_B)
    indices_C = {}
    for level in levels_C:
        indices_C[level] = len(indices_C)

    print indices_A
    print indices_B
    print indices_C

    # CAB
    data_index = 4

    a = len(levels_A)
    b = len(levels_B)
    c = len(levels_C)
    r = 5 # number of repetitions
    DATA = np.zeros((c, a*r, b))

    for item in raw_data:
        item_A = item[0]
        item_B = item[1]
        item_C = item[2]
        item_R = item[3] - 1 # Mismatch between 0 and 1 indexed data.
        result = item[data_index]

        index_A = indices_A[item_A]
        index_B = indices_B[item_B]
        index_C = indices_C[item_C]

        DATA[index_C][index_A*r + int(item_R)][index_B] = result

    titles = [a_title, b_title, c_title]
    names = [a_names, b_names, c_names]
    parameters = [a, b, c, r]
    return titles, names, parameters, DATA


# titles, names, parameters, DATA = collector("a")
#
# print DATA