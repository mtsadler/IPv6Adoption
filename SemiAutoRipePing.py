from datetime import datetime
from ripe.atlas.cousteau import (
  Traceroute,
  AtlasSource,
  AtlasCreateRequest
)

ATLAS_API_KEY = "33131a47-6906-4f83-89af-754ef905c4bd"
probeIDs = ["21283", "24988"]
websiteIDs = ["www.google.com", "www.facebook.com"]

for probeID in probeIDs:
    for websiteID in websiteIDs:
        traceroute = Traceroute(
            af=6,
            target= websiteID,
            description = websiteID.join(probeID).join("ipv6"),
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