import mysql.connector 

cnx = mysql.connector.connect(
 #host ="35.205.135.16",
  host ="localhost", 
  user="root",
  password="Magali_1984",
  port='3306',
  database='cryptos',
  auth_plugin='mysql_native_password'
  )

date= input( "date")
name = input("name")
bot = input("bot")
balence = input("balence")

data = (date, name, bot, balence)
print(type(data))
cursor = cnx.cursor()
query = "INSERT INTO  get_balence (dates, user_name, bot_name, balence) VALUES  (%s, %s , %s, %s)"
cursor.execute(query, data)

#query = "select * from get_balence"
#df =cursor.execute(query)

cnx.commit()
cursor.close()
cnx.close()
print("execution Done")
