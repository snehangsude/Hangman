try:
  import requests
except ModuleNotFoundError:
    print("[-] Requirements not satisfied!\n\trun 'pip install -r requirements.txt'\n\t\tOR\n\trun 'pip3 install -r requirements.txt'")
    quit()
  
stages = ['''
  +----+
  |    
  X    
 /|\   
 / \   
       
=========''', '''
  +----+
  |    
  O    
 /|\   
 / \   
       
=========
''', '''
  +----+
  |    
  O    
 /|\   
 /     
       
=========
''', '''
  +----+
  |    
  O    
 /|\   
       
       
=========
''', '''
  +----+
  |    
  O    
 /|   
       
       
=========''', '''
  +----+
  |    
  O    
  |    
       
       
=========
''', '''
  +----+
  |    
  O    
       
       
       
=========
''', '''
  +----+
  |    
       
       
       
       
=========
''', '''
  +----+
       
       
   
       
       
=========
''', '''
   ----+
       
       
   
       
       
=========
''']

URL = "https://random-word-api.herokuapp.com//word?number=500"
words = requests.get(URL).json()

