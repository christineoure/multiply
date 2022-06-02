class Student:
    
    def __init__(self, first_name, second_name, age, country):
        self.first_name = first_name
        self.second_name = second_name
        self.country = country
        self.age = age

    def fullname(self):
      return f"Hello {self.first_name} {self.second_name} you are {self.age} years old and your counrty is {self.country}"
    
    def year_of_birth(self):
       return f"You were born in {2022 - self.age}"

    def initials(self):
      return f"Your initials are {self.first_name[0]}.{self.second_name[0]}"




    #def initials(self):
      # x = (fullname)
      # name_list = x.split()

      # initials = ""

      # for name in name_list:  
      #   initials += name[0].upper()  
      # return initials