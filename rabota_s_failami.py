def reader(filename):
    import json
    try:
        with open(filename, 'r') as f_obj:
             vse_zada4i = json.load(f_obj)
        return vse_zada4i  
    except Exception as e:
        print (e)
        return []
        

def writer(filename, vse_zada4i):    
    import json    
    try:
        with open(filename, 'w') as f_obj:
            json.dump(vse_zada4i, f_obj)
    except Exception as e:
        print(e) 
