import mariadb

def createConnection(): 
    global mydb
    mydb = mariadb.connect(host = "127.0.0.1", user = "root", password = "dnddbpass",  database="dnd")
    global cur  
    cur = mydb.cursor()
    print(mydb)

def initializeServerTable(server_id):
    cur.execute(
        f"CREATE TABLE IF NOT EXISTS server_{server_id} (playerID INT NOT NULL AUTO_INCREMENT,player_name VARCHAR(50) NOT NULL,player_title VARCHAR(50),armor INT default 0 NOT NULL,strength INT DEFAULT 0 NOT NULL,dexterity INT DEFAULT 0 NOT NULL,constitution INT DEFAULT 0 NOT NULL,intelligence INT DEFAULT 0 NOT NULL,wisdom INT DEFAULT 0 NOT NULL,charisma INT DEFAULT 0 NOT NULL, PRIMARY KEY (playerID));"
    )
    mydb.commit()
def createPlayer(server_id, player_name, armor, strength, dexterity, constitution, intelligence, wisdom, charisma):
    cur.execute(
        f"INSERT INTO server_{server_id} (player_name, armor, strength, dexterity, constitution, intelligence, wisdom, charisma) VALUES ('{player_name}',{armor},{strength},{dexterity},{constitution},{intelligence},{wisdom},{charisma});"
    )
    mydb.commit()

def viewPlayer(server_id, player_name):
    cur.execute(
        f"SELECT * FROM server_{server_id} WHERE player_name = '{player_name}';"
    )
    mydb.commit()
    return cur

def deletePlayer(server_id, player_name):
    cur.execute(
        f"DELETE FROM server_{server_id} WHERE player_name = '{player_name}';"
    )
    mydb.commit()

def updatePlayer(server_id, player_name, stat, updatedStat):
    cur.execute(
        f"UPDATE server_{server_id} SET {stat} = {updatedStat} WHERE player_name = '{player_name}';"
    )
    mydb.commit()

def getInv(server_id, player_name):
    cur.execute(
        f"SELECT items FROM server_{server_id} WHERE player_name = '{player_name}';"
    )
    mydb.commit()
    return cur

def updateInv():
    pass