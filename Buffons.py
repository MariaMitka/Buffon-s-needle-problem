
import random
import math



def buffons_needle(num_throws, needle_length, line_spacing):
    # initial cash
    hits = 0


    for _ in range(num_throws):
        # random angle between 0 and π/2
        theta = random.uniform(0, math.pi / 2)

        # random distance rfom the closest line
        distance = random.uniform(0, line_spacing / 2 )

        # if needle crosses the line
        if distance <= (needle_length / 2) * math.sin(theta):
            hits += 1

    # compute the pi
    estimated_pi = (2 * needle_length * num_throws) / (hits * line_spacing)


    return estimated_pi

def buffons_needle_large (num_throws, needle_length, line_spacing):
    # initial cash
    hits = 0
    thetal = math.asin(line_spacing / needle_length)
    for _ in range(num_throws):
        theta = random.uniform(0, math.pi / 2)


    # if needle cross the line
        if line_spacing/needle_length <= math.sin(theta):
            hits += 1

    # calculate the pi
    estimatedpi =(num_throws*((-2*needle_length/line_spacing)*math.cos(thetal)) + (2*needle_length/line_spacing) -2*thetal)/(hits-num_throws)
    return estimatedpi
# parameters of the experiment
needle_length = 1.0
line_spacing = 2.0
num_throws = 1000000

# performing the experiment

if needle_length <= line_spacing:
    estimated_pi = buffons_needle(num_throws, needle_length, line_spacing)
    print(f"Η εκτίμηση για το π είναι: {estimated_pi}")
elif needle_length > line_spacing:
    estimatedpi = buffons_needle_large(num_throws, needle_length, line_spacing)
    print(f"Η εκτίμηση για το π είναι: {estimatedpi}")

