f = open("input23.txt", "r")
connections = {}
for line in f:
    computer1, computer2 = line[:2], line[3:5]
    if not(computer1 in connections.keys()):
        connections[computer1] = [computer2]
    else:
        connections[computer1].append(computer2)
    if not(computer2 in connections.keys()):
        connections[computer2] = [computer1]
    else:
        connections[computer2].append(computer1)
list_networks = []
for computer1 in connections.keys():
    for computer2 in connections[computer1]:
        list_networks.append({computer1, computer2})

while len(list_networks) > 1:
    new_list_network = []
    for network in list_networks:
        candidates = []
        for candidate in connections[list(network)[0]]:
            if candidate not in network:
                is_in_network = True
                for computer in list(network)[1:]:
                    if candidate not in connections[computer]:
                        is_in_network = False
                        break
                if is_in_network:
                    candidates.append(candidate)
        for candidate in candidates:
            if (extended_network := network.union({candidate})) not in new_list_network:
                new_list_network.append(extended_network)
    list_networks = new_list_network
    print(len(list_networks[0]))
    print(len(list_networks))

network = list(list_networks[0])
network.sort()
s = ""
for computer in network:
    s += computer + ","
print(s[:-1])
