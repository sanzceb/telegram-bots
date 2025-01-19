import csv

class Fixture:
    def __init__(self, fixtureID):
        self.fixture = Fixture._obj_with_id('fixture.csv', fixtureID) 

    @staticmethod
    def _obj_with_id(filename, ID):
        with open(filename, newline='') as file:
            objs = csv.DictReader(file)
            for obj in objs:
                if obj['ID'] == ID:
                    return obj
        return None
    
    @property
    def home(self):
        return self._home
    
    @property 
    def away(self):
        return self._away

    @property
    def matchday(self):
        return self._matchday
    
    @property
    def stadium(self):
        return self._stadium
    
    def __getattr__(self, name):
        if name not in {'_home', '_away', '_matchday', '_stadium'}:
            raise AttributeError
        prop = name[1:]
        value = self.fixture[prop]
        if name in {'_home', '_away'}:
            self.__setattr__(name, Fixture._obj_with_id('club.csv', value))
        else:
            filename = f'{prop}.csv'
            self.__setattr__(name, Fixture._obj_with_id(filename, value))
        return self.__getattribute__(name)

    def __repr__(self):
        return (f"{self.home['name_en']} - {self.away['name_en']}"
            f", {self.matchday['date']}, {self.stadium['name']}"
            f", ({self.stadium['city']})")
            
    
class FixtureTable:
    def __init__(self):
        self._fixtures = {}
    
    def upcoming_fixtures(self, team):
        result = {}
        # Get the home fixtures
        # Get the away fixtures
        # join
        return result
    
    def _upcoming_fixtures(self, team):
        pass

if __name__ == '__main__':
    fixture = Fixture('1')
    print(fixture)