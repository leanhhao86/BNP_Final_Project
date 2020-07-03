import sqlite3

class database:
    def __init__(self):
        self.server_path = 'server_db.db'
        self.conn = None
        self.cursor = None

        self.__connect()

    def __connect(self):
        try:
            self.conn = sqlite3.connect(self.server_path)
            self.cursor = self.conn.cursor()
            print("Connect successly")
        except:
            print("Connect unsuccessly")

    def __checkSQLi(self, *args):
        return False

    def __query(self, query):
        if self.__checkSQLi(query):
            return

        print(query)
        self.cursor.execute(query)
        if "INSERT" in query.upper():
            print("[INSERT]")
            self.conn.commit()
            return
        elif "SELECT" in query.upper():
            print("[SELECT]")
            record = self.cursor.fetchall()
            return record

    def authenticate(self, username, password):
        query = ''' SELECT * FROM ACCOUNT '''
        record = self.__query(query)
        
        for row in record:
            print(row)
            if row[0] == username and row[1] == password:
                return True
        
        return False

    def signup(self, username, password):
        try:
            query = ''' SELECT * FROM ACCOUNT '''
            record = self.__query(query)
            
            for row in record:
                if username == row[0]:
                    return False

            query = f''' INSERT INTO ACCOUNT(USERNAME, PASSWORD, SCORE) VALUES('{username}','{password}',0); '''
            self.__query(query)
            return True
        except:
            return False

    
            
    

        