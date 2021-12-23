class Character:
    def __init__(self, character_name, character_description):
        self.name = character_name
        self.description = character_description
        self.conversation = None
    def describe(self):
        print( self.name )
        print( self.description )
    def set_conversation(self, conversation):
        self.conversation = conversation
    def fight(self, combat_item):
        print(self.name + " will not fight")
        return True


        
class Enemy(Character):
  enemies_defeated = 0
  def __init__(self, character_name, character_description):
    super().__init__(character_name, character_description)
    self.weakness = None
    
  def set_weakness(self,weakness):
    self.weakness = weakness
  def get_weakness(self):
    return self.weakness
  def fight(self, combat_item):
    if combat_item == self.weakness:
        print(" " + self.name + " killed with " + combat_item )
        Enemy.enemies_defeated += 1
        return True
    else:
        print(self.name + " shooted you")
        return False
  def get_defeated(self):
    return Enemy.enemies_defeated
  def set_defeated(self, number_defeated):
    Enemy.enemies_defeated = number_defeated
class Friend(Enemy):
  def __init__(self, character_name, character_description):
    super().__init__(character_name, character_description)
    self.feeling = None
  
