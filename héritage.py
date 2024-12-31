class person:
   def __init__(self,name,age):
     self.name="name"
     self.age="age"

class student(person):
   def __init__(self,student_id,note):
      self.student_id = student_id
      self.note = note 
      super(). __init__()
    
   def display_info(self):
        print(f"student id: {self.student_id}")
        print(f"note: {self.note}")
       