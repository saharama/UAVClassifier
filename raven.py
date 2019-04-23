#import json for load() and matplot for graph
#both internal libraries
import json
import matplotlib.pyplot as plt

import numpy as np


def dict_ignore_on_duplicates(ordered_pairs):
    """Reject duplicate keys."""
    d = {}
    for k, v in ordered_pairs:
        if k not in d:
           d[k] = v
    return d

#print packet count
#format= packet_index:sizeofPackets
with open('./intelData/10Mar1-01.json') as i:
    a = json.load(i, object_pairs_hook=dict_ignore_on_duplicates)

    sizeCounts = {}
    for packet in a:
        packet_size = int(packet['_source']['layers']['frame']['frame.len'])

        if packet_size in sizeCounts:
            sizeCounts[packet_size] = sizeCounts[packet_size] + 1
        else:
            sizeCounts[packet_size] = 1

    print("Packet Size")
    print("Print format= (packet size X: # of packets of size X)\n")
    print (sizeCounts)

#graph packet size vs frequency of size
#plt.plot(sizeCounts)
    fig1 = plt.figure()
    plt.scatter(list(sizeCounts.keys()), sizeCounts.values(), color='g')
    plt.grid()
    
#print relative time between packets
    timeCounts = {}
    for packet in a:
        packet_relTime = float(packet['_source']['layers']['frame']['frame.time_relative'])

        if packet_relTime in timeCounts:
            timeCounts[packet_relTime] = timeCounts[packet_relTime] + 1
        else:
            timeCounts[packet_relTime] = 1

    print(timeCounts)

#graph relative packet time vs frequency of relative time
    fig2 = plt.figure()
    plt.scatter(list(timeCounts.keys()), timeCounts.values(), color='r')
    plt.grid()
    plt.show()
