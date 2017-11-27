from datetime import datetime
from ripe.atlas.cousteau import (
  Traceroute,
  AtlasSource,
  AtlasCreateRequest
)

ATLAS_API_KEY = "33131a47-6906-4f83-89af-754ef905c4bd"
probeID = "21283"
websiteID ="http://elsrv2.cs.umass.edu/fakebook/"

traceroute = Traceroute(
    af=4,
    target= websiteID,
    description = websiteID.join(probeID),
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
