from smile_lowercase_API import LowrSmileService

from smile_lowercase_pb2 import LowerSmileRequest

def test_lowersmile():
    service = LowrSmileService()
    request = LowerSmileRequest (user_id=1)
    response = service.lowersmile(request, None)
    assert len(response.LowerSmiles) ==2
