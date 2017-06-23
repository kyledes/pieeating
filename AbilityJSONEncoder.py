from json import JSONEncoder


class AbilityJSONEncoder(JSONEncoder):

    def default(self, o):
        try:
            return o.__json()
        except AttributeError:
            JSONEncoder.default(self, o)