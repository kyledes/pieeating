import re





class Ability:

    #parenthetical = re.compile('(.*)')

    def assign_associations(self):
        if self.association_split is None:
            return
        if len(self.association_split) >= 1:
            self.primary = self.association_split[0].strip()

        if len(self.association_split) >=2:
            self.seconday = self.association_split[1].strip()

        if len(self.association_split) >= 3:
            self.tertiary = self.association_split[2].strip()


    def __init__(self, title, association, description):
        title_text = title.strong.get_text()
        #print(self.parenthetical.match(title_text))
        if title_text.find("(") != -1:
            self.parenthetical_text = title_text[title_text.find("(")+1:title_text.find(")")]
            self.title = title_text[0:title_text.find("(")-1].strip('"')
        else:
            self.title = title_text

        #self.title = title
        self.association = association.get_text()
        self.association_split = self.association.split('\n')
        self.assign_associations()

        self.description = description.get_text()