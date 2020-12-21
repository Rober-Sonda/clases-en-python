class Autos:
  def __init__(self, **kwargs):
    self.marca = kwargs.get("marca", "volvo")
    self.modelo = kwargs.get("modelo","2040")

    