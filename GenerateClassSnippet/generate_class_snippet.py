import json

# j = '{"action": "print", "method": "onData", "data": "Madan Mohan"}'
j = json.load(open(".\\response.json"))
j_str = json.dumps(j)


class Payload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j_str)


p = Payload(j_str)
print(p.Marker)

# with open(".\\response.json") as f:
#    response_syntax = json.load(f)

# response_syntax_str = json.dumps(response_syntax)

# class ResponseClass(object):
#    def __init__(self, d):
#        self.__dict__ = json.loads(response_syntax_str)


# response = ReseponseClass(response_syntax_str)
# pprint.pprint(response["Contents"][0], width=1)
