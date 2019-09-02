class Cuenta:
  def __init__(self , cte , t, user):
    self.cantidad= cte
    self.tipo= t
    self.usuario= user
  def imprimirDetalles(self):
    print("cantidad:" , self.cantidad)
    print("el tipo es:" , self.tipo)
    print("nombre de usuario:" , self.usuario)


