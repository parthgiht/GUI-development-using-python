import json

class Database:

    def Add_data(self,First_name,Last_name,Email,Password):
        
        try:
            with open ('TextSense Database.json','r') as rf:
                if rf.read().strip(): 
                    rf.seek(0)  
                    database = json.load(rf)
                else:
                    database = {}
        except FileNotFoundError:
            database = {}


        if Email in database:
            return 0
        else:
            database[Email] = [First_name,Last_name,Password]
            with open('TextSense Database.json','w') as wf:
                json.dump(database,wf)
            return 1
        
    def Search(self,Email,Password):

        with open('TextSense Database.json','r') as rf:
            database = json.load(rf)

            if Email in database:
                if database[Email][2] == Password:
                    return 1
                else:
                    return 0
            else:
                return 0
            
