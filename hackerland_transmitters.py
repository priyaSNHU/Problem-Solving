# HACKERRANK PROBLEM LINK: https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem

def transmitters_required(houses_list, range_transmitters):
    houses_list = sorted(houses_list)
    start_house = houses_list[0]
    last_house = houses_list[0]
    transmitters_count = 0
    for house in houses_list:
        distance_house = house - last_house
        transmitter_coverage = house - start_house
        if distance_house > range_transmitters:
            last_house = house
            start_house = house
            tansmitters_count += 1
        elif transmitter coverage <= range_transmitters:
            last_house = house
    return range_transmitters

        
        
