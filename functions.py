#functions.py
def text_to_list(fin):  
    '''
    Reads a text file with fields separeted 
    by semicolon and returns a list of rows.
    Each row a is a list and represents 
    one line from a text file.  
    '''
    result = [] 
    lines = fin.readlines()
    for line in lines:      
        row = []
        row = line.split(";")
        result.append(row)
    return result
	
def connect_to_sqlite(dbname):
    import sqlite3 as lite
    #create the connection to the database
    conn = lite.connect(dbname)
    return conn