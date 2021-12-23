import room
import item
import character

locker = room.Room("Locker Room")
locker.set_description("This is locker room where you stole all the gold from")
manager = room.Room("Manager Cabin")
manager.set_description("Creepy room with dust, broken paintings and torn curtains")
security = room.Room("Security Cabin")
security.set_description("security with broken bed and blood on the floor")
backOffice = room.Room("Back Office")
security.set_description("Back office with a escape door to run with all gold")
locker.link_room(manager, "north")
manager.link_room(locker, "south")
manager.link_room(security, "east")
security.link_room(manager, "wests")
Pritesh = character.Enemy("Pritesh", "Head security gaurd of bank")
Pritesh.set_conversation("Put your hands up! Surrender yourself")
Pritesh.set_weakness("knife")
friendTheif = character.Friend("Friend", "Another theif that helped loot gold")
friendTheif.set_conversation("Common, lets get out from here")
friendTheif.set_weakness("gun")
police = character.Enemy("Police", "Spain SPD")
police.set_conversation("Surrender to police, put your wepons down")
police.set_weakness("knife")
security.set_character(police)
gun = item.Item("gun")
gun.set_description("Gun with bullets inside")
manager.set_item(gun)
knife = item.Item("knife")
knife.set_description("Knife that can kill someone even with one scratch")
security.set_item(knife)
security.set_character(friendTheif)
manager.set_character(Pritesh)
current_room = locker
pocket = []
dead = False

while dead == False:
  print ("""\nYou have stolen gold from Bank of Spain, you are in the bank now and want to escape.
                            +&-
                          _.-^-._    .--.
                       .-'   _   '-. |__|
                      /     |_|     \|  |
                     / BANK OF SPAIN \  |
                    /|     _____     |\ |
                     |    |==|==|    |  |
 |---|---|---|---|---|    |--|--|    |  |
 |---|---|---|---|---|    |==|==|    |  |
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
""")        
  current_room.get_details()
  inhabitant = current_room.get_character()
  if inhabitant is not None:
    inhabitant.describe()
  
  item = current_room.get_item()
  if item is not None:
    item.describe()    
  command = input("Input> ")    
  if command in ["south", "north", "west", "east"]:
    current_room = current_room.move(command)
  elif command == "fight":
    if inhabitant is not None:
      print("You want to fight with?")
      fight_with = input()
 
      if fight_with in pocket:
        if inhabitant.fight(fight_with) == True:
          print("Fight won")
          current_room.character = None
          if inhabitant.get_defeated() == 2:
            print("Enemy kill")
            dead = True
          else:
            print("You got kill")
            print("Game end")
            dead = True
      else:
        print("Object " + fight_with + "not found")    
  elif command == "loot":
    if inhabitant == None:
      print("No one to loot from")
    elif isinstance(inhabitant,character.Friend):
      print("Not allowed to loot from friend")
    else:
      print("Choose object to fight:")
      fight_with = input()
      if inhabitant.fight(fight_with) == True:
        print("Item stollen")
      else:
        print("Fight lost")
        print("End of game")
        dead = True     
  elif command == "grab":
    if current_room.get_item() != None:
      print("Added " + item.get_name() + " in your pocket")
      pocket.append(current_room.get_item())
      current_room.set_item(None)
    else:
      print("Object not found to grab")
  else:
    print("Unknown command " + command)
      
  
  
  
      
      
        
  
  
        



