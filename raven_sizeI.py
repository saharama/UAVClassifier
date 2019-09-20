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

	sizeCounts1 = {}
	for packet in a:
		packet_size = int(packet['_source']['layers']['frame']['frame.len'])

		if packet_size in sizeCounts1:
			sizeCounts1[packet_size] = sizeCounts1[packet_size] + 1
		else:
			sizeCounts1[packet_size] = 1

	print("Packet Size")
	print("Print format= (packet size X: # of packets of size X)\n")
	print (sizeCounts1)

	#graph packet size vs frequency of size
	#plt.plot(sizeCounts1)
	fig1 = plt.figure()
	plt.scatter(list(sizeCounts1.keys()), sizeCounts1.values(), color='g')
	#plt.grid()

with open('./intelData/10Mar2-01.json') as i:
	a = json.load(i, object_pairs_hook=dict_ignore_on_duplicates)

	sizeCounts2 = {}
	for packet in a:
		packet_size = int(packet['_source']['layers']['frame']['frame.len'])

		if packet_size in sizeCounts2:
			sizeCounts2[packet_size] = sizeCounts2[packet_size] + 1
		else:
			sizeCounts2[packet_size] = 1

	print("Packet Size")
	print("Print format= (packet size X: # of packets of size X)\n")
	print (sizeCounts2)

	#graph packet size vs frequency of size
	#plt.plot(sizeCounts2)
	#fig1 = plt.figure()
	plt.scatter(list(sizeCounts2.keys()), sizeCounts2.values(), color='r')
	#plt.grid()

with open('./intelData/10Mar3-01.json') as i:
	a = json.load(i, object_pairs_hook=dict_ignore_on_duplicates)

	sizeCounts3 = {}
	for packet in a:
		packet_size = int(packet['_source']['layers']['frame']['frame.len'])

		if packet_size in sizeCounts3:
			sizeCounts3[packet_size] = sizeCounts3[packet_size] + 1
		else:
			sizeCounts3[packet_size] = 1

	print("Packet Size")
	print("Print format= (packet size X: # of packets of size X)\n")
	print (sizeCounts3)

	#graph packet size vs frequency of size
	#plt.plot(sizeCounts)
#	fig1 = plt.figure()
	plt.scatter(list(sizeCounts3.keys()), sizeCounts3.values(), color='b')
	plt.grid()
	plt.title('Correlation of Packet-Size Frequency for 3 Trials')
	plt.xlabel('Packet Size')
	plt.ylabel('Number of Packets')

	#plt.xlim(0, 50)

	plt.gca().legend(('Trial 1','Trial 2', 'Trial 3'))

	plt.show()
