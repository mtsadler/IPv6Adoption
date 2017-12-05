from datetime import datetime
from ripe.atlas.cousteau import (
  Traceroute,
  AtlasSource,
  AtlasCreateRequest
)

f = open('/Users/mike/Desktop/653/IPv6Adoption-master/resultsALL.txt', "w+")
ATLAS_API_KEY = "33131a47-6906-4f83-89af-754ef905c4bd"
probeIDs = ["25355", "30001", "23697", "13805", "11236", "6277", "33144", "33493", "33144", "31689", "30045", "28013", "26389", "25355", "25283", "23463", "23367", "21283", "18019", "17901", "16703", "15724", "13964", "13734", "12833", "6044", "6030"]
websiteIDs = ["www.google.com", "www.facebook.com","www.baidu.com", "www.wikipedia.org", "www.yahoo.com", "www.reddit.com", "www.amazon.com", "www.twitter.com", "www.vk.com", "www.live.com", "www.instagram.com", "www.sohu.com", "www.weibo.com", "www.linkedin.com", "www.netflix.com"]
protocolVersions = [4,6]
for probeID in probeIDs:
    for websiteID in websiteIDs:
        for protocolVersion in protocolVersions:
            traceroute = Traceroute(
                af=protocolVersion,
                target= websiteID,
                description = "[" + str(probeID) + " /// " + str(websiteID) + " /// " + str(protocolVersion) + "]",
                protocol = "ICMP",
            )

            source = AtlasSource(type="probes", value=probeID, requested=1)

            atlas_request = AtlasCreateRequest(
                start_time=datetime.utcnow(),
                key=ATLAS_API_KEY,
                measurements= [traceroute],
                sources=[source],
                is_oneoff=True
            )

            (is_success, response) = atlas_request.create()
            if is_success:
                f.write(str(response["measurements"]) + "[" + str(probeID) + " /// " + str(websiteID) + " /// " + str(protocolVersion) + "]" + "\r\n")