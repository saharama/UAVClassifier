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
#format= packet_index:relative-timeofPackets
with open('./intelData/10Mar1-01.json') as i:
	a = json.load(i, object_pairs_hook=dict_ignore_on_duplicates)

	timeIndex1 = {}
	for packet in a:
		packet_relTime = float(packet['_source']['layers']['frame']['frame.time_relative'])

		if packet_relTime in timeIndex1:
			timeIndex1[packet_relTime] = packet_relTime
		else:
			timeIndex1[packet_relTime] = 0

	print("Packet relative-time")
	print("Print format= (packet relative-time X: # of packets of relative-time X)\n")
	print (timeIndex1)

	#graph packet relative-time vs frequency of relative-time
	#plt.plot(timeCounts1)
	fig1 = plt.figure()
	plt.scatter(list(timeIndex1.keys()), timeIndex1.values(), color='g')
	#plt.grid()
	plt.show()

'''
with open('./intelData/10Mar2-01.json') as i:
	a = json.load(i, object_pairs_hook=dict_ignore_on_duplicates)

	timeCounts2 = {}
	for packet in a:
		packet_relTime = float(packet['_source']['layers']['frame']['frame.time_relative'])

		if packet_relTime in timeCounts2:
			timeCounts2[packet_relTime] = timeCounts2[packet_relTime] + 1
		else:
			timeCounts2[packet_relTime] = 1

	print("Packet relative-time")
	print("Print format= (packet relative-time X: # of packets of relative-time X)\n")
	print (timeCounts2)

	#graph packet relative-time vs frequency of relative-time
	#plt.plot(timeCounts2)
	#fig1 = plt.figure()
	plt.scatter(list(timeCounts2.keys()), timeCounts2.values(), color='r')
	#plt.grid()

with open('./intelData/10Mar3-01.json') as i:
	a = json.load(i, object_pairs_hook=dict_ignore_on_duplicates)

	timeCounts3 = {}
	for packet in a:
		packet_relTime = float(packet['_source']['layers']['frame']['frame.time_relative'])

		if packet_relTime in timeCounts3:
			timeCounts3[packet_relTime] = timeCounts3[packet_relTime] + 1
		else:
			timeCounts3[packet_relTime] = 1

	print("Packet relative-time")
	print("Print format= (packet relative-time X: # of packets of relative-time X)\n")
	print (timeCounts3)

	#graph packet relative-time vs frequency of relative-time
	#plt.plot(timeCounts)
#	fig1 = plt.figure()
	plt.scatter(list(timeCounts3.keys()), timeCounts3.values(), color='b')
	plt.grid()
	plt.title('Correlation of Packet-relative-time Frequency for 3 Trials')
	plt.xlabel('Packet relative-time')
	plt.ylabel('Number of Packets')

	#plt.xlim(0, 50)

	plt.gca().legend(('Trial 1','Trial 2', 'Trial 3'))

	plt.show()
'''
