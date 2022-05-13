states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])


# print(states_needed)
# print(stations)

# greedy algorithm to find a solution
final_stations = set()

while states_needed: # while there are still uncovered states
    best_station = None
    states_covered = set() # used to store new covered states
    for station, states_of_station in stations.items():
        # calculate set intersection - set of uncovered states that this station covers
        still_uncovered = states_needed & states_of_station
        # compare number of uncovered states that could be added to number of states 
        if len(still_uncovered) > len(states_covered):
            best_station = station
            states_covered = still_uncovered
            print(states_covered)

    # add best station to final_stations set
    final_stations.add(best_station)
    # remove states that are now covered
    states_needed -= states_covered

print(final_stations)
