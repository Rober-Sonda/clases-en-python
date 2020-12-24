class Transporte:
  
  def __init__(self, **kwargs):
    self.tipotransporte = kwargs.get("tipotransporte","None")
    self.navegacion = kwargs.get("navegacion","None")

  def __str__(self):
    return "{}\n{}\n".format(self.tipotransporte,
    self.navegacion)

class Avion(Transporte):
  
    def __init__(self, **kwargs):
      self.marca = kwargs.get("marca","None")
      self.modelo = kwargs.get("modelo","None")
      self.tipotransporte = kwargs.get("tipotransporte","None")
      self.navegacion = kwargs.get("navegacion","None")

    def __str__(self):
      return "{}\n{}\n{}\n{}\n".format(self.marca, self.modelo, self.tipotransporte,
      self.navegacion)