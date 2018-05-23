# Python


class Monster(object):
	def __init__(self, name, hp=10):
		self.name = name
		self.hp = hp

	def take_damage(self, damage):
		# print(self.name + " takes " + str(hp) + " damage")
		self.hp -= damage
		self.death()
		print("%s takes %d damage, and has %d health left" % (self.name, damage, self.hp))

	def __del__(self):
		print("%s is dead" % (self.name))


	def death(self):
		if self.hp < 1:
			self.__del__()

class Character(object):
	def __init__(self, name, hp=10):
		# do stuff
		self.name = name
		self.hp = hp

	def attack(self, monster):
		if monster == None:
			print("No monster called %s" % (monster))
		monster.take_damage(5)

class Barbarian(Character):
	def __init__(self, name):
		super().__init__(name, 30)

	def attack(self, monster):
		monster.take_damage(10)

	def rage(self):
		pass

class Mage(Character):
	def fireball(self):
		pass

m = Mage("Tom")
b = Barbarian("Sam")
o = Monster("Kobold")


b.attack(o)
m.attack(o)
