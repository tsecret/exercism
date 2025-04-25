class SpaceAge:
    def __init__(self, seconds: int):
      self.table = {
        'Mercury': 0.2408467,
        'Venus': 0.61519726,
        'Earth': 1.0,
        'Mars': 1.8808158,
        'Jupiter': 11.862615,
        'Saturn': 29.447498,
        'Uranus': 84.016846,
        'Neptune': 164.79132,
      }

      self.years = seconds / 60 / 60 / 24 / 365.25

    def round(self, number: float) -> float:
      return round(number, 2)

    def on_earth(self) -> float:
      return self.round(self.years / self.table['Earth'])

    def on_mercury(self) -> float:
      return self.round(self.years / self.table['Mercury'])

    def on_venus(self) -> float:
      return self.round(self.years / self.table['Venus'])

    def on_mars(self) -> float:
      return self.round(self.years / self.table['Mars'])

    def on_jupiter(self) -> float:
      return self.round(self.years / self.table['Jupiter'])

    def on_saturn(self) -> float:
      return self.round(self.years / self.table['Saturn'])

    def on_uranus(self) -> float:
      return self.round(self.years / self.table['Uranus'])

    def on_neptune(self) -> float:
      return self.round(self.years / self.table['Neptune'])
