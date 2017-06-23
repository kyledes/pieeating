
class MetaAbility():

    def to_json(self):
        meta = {}
        json_abilities = []
        meta['name'] = self.title
        for ability in self.abilities:
            json_abilities.append(ability.to_json())
        meta['abilities'] = json_abilities
        return meta

    def __init__(self, meta_title, abilities):
        self.title = meta_title
        self.abilities = abilities
