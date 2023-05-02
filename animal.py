class animal(self, name, age):
    def __init__(self, name, age):
      self.name = name
      self.age = age

    def speak(self):
        print("울음소리")


class dog(animal):
  def __init__(name,age):
   super().__init__(name, age)

  def speak(self):
     print("월월")

class cat(animal):
  def __init__(name,age):
   super().__init__(name, age)

  def speak(self):
     print("야옹")