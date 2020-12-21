class Player:
  poder = "DARDO MAGICO"
  vocacion = "No posee"
  speed = "1000"

  def __init__(self, **kwargs):
    self.nombre = input("Elije un nombre -> ")
    self.vida = kwargs.get("vida", 50)
    self.mana = kwargs.get("mana", 50)
  
  def __str__(self):
    return ("Nombre: {}\nvida : {}\nmana : {}\nvocacion : {}\npoder : {}".format(
            self.nombre,
            self.vida,
            self.mana,
            self.vocacion,
            self.lanzar_poder()))

  def lanzar_poder(self):
    return self.poder
  

class Knight(Player):
  poder = "Exori"
  vocacion = "Knight"
  speed = "1700"

class Sorcerer(Player):
  poder = "Te reviento"
  vocacion = "Sorcerer"
  speed = "250"

class Druida(Player):
  poder = "Druid Attack"
  vocacion = "Druida"
  speed = "este es lenteja 100"

class Paladin(Player):
  poder = "Espadium al Medium"
  vocacion ="Paladin"
  speed = "te re parto al diome 2900"