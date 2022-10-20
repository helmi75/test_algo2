
import mysql.connector 
class ConnectBbd:
    def __init__(self, host, port, user, password, database, auth_plugin):      
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.auth_plugin =auth_plugin
        self.cnx = mysql.connector.connect(host=self.host,
                                    user=self.user, 
                                    password=self.password,
                                    port=self.port,
                                    database=self.database,
                                    auth_plugin=self.auth_plugin)   

    def insert(self, data):  
      cursor =self.cnx.cursor()      
      query = "INSERT INTO  get_balence (dates, user_name, bot_name, balence) VALUES  (%s, %s , %s, %s)"
      cursor.execute(query, data)
      self.cnx.commit()
      cursor.close()
      self.cnx.close()
      return print("done")

    #def delete(self, data)




con = ConnectBbd('localhost','3306','root','Magali_1984','cryptos','mysql_native_password')
con.insert(("2022-05-21","helmi","cocotier","0€"))
