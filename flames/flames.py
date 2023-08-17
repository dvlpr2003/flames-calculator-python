class Flames :
  def __init__(self, fname,lname):
    self.name1 = []
    self.name2 =[]
    for _ in fname:
      self.name1.append(_)
    for _ in lname:
      self.name2.append(_)
    self.flames = ['f','l','a','m','e','s']
  def remove_letters (self):
    if len(self.name1)>len(self.name2):
      for f in self.name1[:]:
        for l in self.name2:
          if f == l:
            x = self.name1.index(f)
            y = self.name1.index(l)
            self.name1.pop(x)
            self.name2.pop(y)
    elif len(self.name2) > len(self.name1):


      for f in self.name2[:]:
        for l in self.name1:
          if f == l:
            x = self.name1.index(f)
            y = self.name1.index(l)
            self.name1.pop(x)
            self.name2.pop(y)
 
  def flames_process(self):
 
    total = len(self.name1) + len(self.name2)
    
    process = True
    while process :
      div = total//len(self.flames)
      
      self.flames.pop(div-1)
      if len(self.flames)==2:
        remainder = total%len(self.flames)
        self.flames.pop(remainder-1)
        process = False


    

    


