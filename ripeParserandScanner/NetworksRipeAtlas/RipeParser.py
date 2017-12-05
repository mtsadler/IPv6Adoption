import json
from pprint import pprint
import socket
import os

f = open('results.csv', "a+")
f.write("probeID, clientIP, clientName, serverIP, serverName, IPvX, Number of Hops, Average, Median, tunnel avg, tunnel med, tunnel hops\r\n")
folder = '/Users/mike/PycharmProjects/IPv6Adoption/ripeParserandScanner/NetworksRipeAtlas/RipeResults'
for filename in os.listdir(folder):
    filename = '/Users/mike/PycharmProjects/IPv6Adoption/ripeParserandScanner/NetworksRipeAtlas/RipeResults/'+ filename
    with open(filename) as data_file:
        data = json.load(data_file)
    pprint(data)
    myText = data[0]
    probeID = myText["prb_id"]
    webServer = myText["dst_name"]
    client = myText["from"]
    version = myText["af"]
    output = filename.split(".json")[0]
    try:
        serverSend = socket.gethostbyaddr(client)[0]
    except socket.herror:
        serverSend = ''
    try:
        serverRecv = socket.gethostbyaddr(webServer)[0]
    except socket.herror:
        serverRecv = ''
    print(output)
    print("client: " + client)
    print("server: " + webServer)
    print("IPv" + str(version))
    f.write(str(probeID) + ",")
    f.write(client + ",")
    f.write(serverSend + ",")
    f.write(webServer + ",")
    f.write(serverRecv + ",")
    f.write(str(version) + ",")
    hopNumber = 0
    medians = 0
    averages = 0
    skips = 0
    
    
    
    if version is 4 or 6:
        #analyzing hops and capturing the RTT for each hop
        for hop in myText["result"]:
            hopNumber = hop["hop"]
            hopData = hop["result"]
            if ("rtt" in hopData[0]) and ("rtt" in hopData[1]) and ("rtt" in hopData[2]):
                hopAvgRtt = (hopData[0]["rtt"] +hopData[1]["rtt"] + hopData[2]["rtt"])/3
                hopList = [hopData[0]["rtt"], hopData[1]["rtt"], hopData[2]["rtt"]]
                hopList.sort()
                averages = averages + hopAvgRtt
                medians = medians + hopList[1]
                # print("average RTT for hop#" + str(hopNumber) + ": " + str(hopAvgRtt))
                # print("median RTT for hop#" + str(hopNumber) + ": " + str(hopList[1]))
                #f.write("average RTT for hop#" + str(hopNumber) + ": " + str(hopAvgRtt) + "\r\n")
                #f.write("median RTT for hop#" + str(hopNumber) + ": " + str(hopList[1]) + "\r\n")
            else:
                skips = skips + 1
        print("number of hops: " + str(hopNumber))
        f.write(str(hopNumber) + ", ")
        # hopNumber = hopNumber - skips
        f.write(str(averages) + ",")
        f.write(str(medians) + "\r\n")
        # breaker = False
        # starterAvg = 0
        # starterMed = 0
        # enderAvg = 0
        # enderMed = 0
        # counter = 0
        # for something in range(1,hopNumber):
        #     if not breaker and something in myText["result"]:
        #         hop = myText["result"][something]
        #         hopPosition = hop["hop"]
        #         hopData = hop["result"]
        #         if "icmpext" in hopData[0]:
        #             starterAvg = (hopData[0]["rtt"]+hopData[1]["rtt"]+hopData[2]["rtt"])/3
        #             hopList = [hopData[0]["rtt"], hopData[1]["rtt"], hopData[2]["rtt"]]
        #             hopList.sort()
        #             starterMed = hopList[1]
        #             counter += 1
        #             for tunnelHops in range(something,hopNumber):
        #                 if 'icmpext' not in myText["result"][tunnelHops]["result"][0]:
        #                     if ("rtt" in myText["result"][tunnelHops]["result"][0]) and ("rtt" in myText["result"][tunnelHops]["result"][1]) and ("rtt" in myText["result"][tunnelHops]["result"][2]):
        #                         hopData = myText["result"][tunnelHops]["result"]
        #                         enderAvg = (hopData[0]["rtt"] + hopData[1]["rtt"] + hopData[2]["rtt"]) / 3
        #                         hopList = [hopData[0]["rtt"], hopData[1]["rtt"], hopData[2]["rtt"]]
        #                         hopList.sort()
        #                         enderMed = hopList[1]
        #                         breaker = True
        #                         break
        # f.write(str(enderAvg-starterAvg) + ",")
        # f.write(str(enderMed-starterMed) + ",")
        # f.write(str(counter) + "\r\n")