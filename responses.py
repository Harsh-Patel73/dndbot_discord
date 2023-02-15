import random
import db


def handle_response(message, server_id) -> str: 
    p_message = message.lower()
    p_message = p_message.split()

    if p_message[0] == 'setup':
        db.initializeServerTable(server_id)
        return 'Success'

    if p_message[0] == 'createplayer':
        db.createPlayer(server_id, p_message[1], p_message[2], p_message[3], p_message[4], p_message[5], p_message[6], p_message[7], p_message[8])
        return f'created player {p_message[1]}'

    if p_message[0] == 'viewplayer':
        for i in db.viewPlayer(server_id, p_message[1]):
            return i

    if p_message[0] == 'deleteplayer': 
        db.deletePlayer(server_id, p_message[1])
        return f'deleted player {p_message[1]}'

    if p_message[0] == 'updateplayer':
        db.updatePlayer(server_id, p_message[1], p_message[2], p_message[3])
        return f'updated {p_message[2]} to {p_message[3]} for player {p_message[1]}'

    if p_message[0] == 'getplayerinventory':
        for i in db.getInv(server_id, p_message[1]):
            return i

    if p_message == 'updateplayerinventory':
        pass

    if p_message == 'd4':
        m = str(random.randint(1,4))
        return m
    
    if p_message == 'd6':
        m = str(random.randint(1,6))
        return m
    
    if p_message == 'd8':
        m = str(random.randint(1,8))
        return m

    if p_message == 'd10':
        m = str(random.randint(1,10))
        return m

    if p_message == 'd12':
        m = str(random.randint(1,12))
        return m

    if p_message == 'd20':
        m = str(random.randint(1,20))
        return m

    if p_message == 'help':
        return "This is a help message."

