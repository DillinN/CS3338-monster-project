class Monster:
    def __init__(itself, name,size):
        itself.name = name
        
        itself.size = size 
        
    def attack(itself, location):
        print(f"{itself.name} attacks {location}")
        
    def __str__(itself):
        return f"Monster is {itself.name} and is the size of {itself.size} "
    
    def __eq__(itself, random):
        return itself.name == random.name and itself.size == random.size
    
    def __add__(itself, random):
        return Monster(itself.name + random.name, itself.size + random.size)
        
firstMonster = Monster("kaiju", 500)

secoundMonster = Monster("sukuna" , 100)

thirdMonster = Monster("kaiju" , 500)

print(firstMonster)
firstMonster.attack("Japan")

print(firstMonster == thirdMonster)
combinedMonster = firstMonster + secoundMonster

print(combinedMonster)
        