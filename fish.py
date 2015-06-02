class Fish:
    breathes_in_water = True
    skin = "scales"

    def __init__(self, fish_name, color):
        self.name = fish_name
        self.color = color
        
        

    def move(self, speed):
        print self.name + "is moving" + speed + "!!"
    #Python automatically puts "myfish" into the "self" variable

spencer = Fish ("Spencer", "Gold")
print spencer.move("slowly")
