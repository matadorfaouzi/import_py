class Player :
  #Constructure
  def __init__(self, Name, ht = 100) :
    self.Name = Name
    self.ht = ht
  #fonction affichage
  def Player_courant(self):
    print(f"Name player in this moment is : {self.Name} this hit points is {self.ht}")

  def take_damage(self, damage):
    self.ht -= damage
    print("this hit points is " , self.ht)
    return self.ht