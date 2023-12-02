from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from tables import team, color, Player, state

def print_ans(result):
    for row in result:    
        for col in row:
            print(col)
            

def query1(engine, use_mpg, min_mpg, max_mpg, use_ppg, min_ppg, max_ppg, use_rpg, min_rpg, max_rpg, use_apg, min_apg, max_apg, use_spg, min_spg, max_spg, use_bpg, min_bpg, max_bpg):
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(Player)
    if use_mpg:
        query = query.filter(Player.mpg >= min_mpg).filter(Player.mpg <= max_mpg)
    if use_ppg:
        query = query.filter(Player.ppg >= min_ppg).filter(Player.ppg <= max_ppg)
    if use_rpg:
        query = query.filter(Player.rpg >= min_rpg).filter(Player.rpg <= max_rpg)
    if use_apg:
        query = query.filter(Player.apg >= min_apg).filter(Player.apg <= max_apg)
    if use_spg:
        query = query.filter(Player.spg >= min_spg).filter(Player.spg <= max_spg)
    if use_bpg:
        query = query.filter(Player.bpg >= min_bpg).filter(Player.bpg <= max_bpg)
    results = query.all()
    print("PLAYER_ID TEAM_ID UNIFORM_NUM FIRST_NAME LAST_NAME MPG PPG RPG APG SPG BPG")
    for player in results:
        print(f"{player.player_id} {player.team_id} {player.uniform_num} {player.first_name} {player.last_name} {player.mpg} {player.ppg} {player.rpg} {player.apg} {player.spg} {player.bpg}")

def query2(engine, team_color):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(team.name).join(color, team.color_id == color.color_id).filter(color.name == team_color).all()
    print("NAME")
    print_ans(result)

def query3(engine, team_name):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Player.first_name, Player.last_name)\
                   .join(team, team.team_id == Player.team_id)\
                   .filter(team.name == team_name)\
                   .order_by(Player.ppg.desc()).all()
    print("FIRST_NAME LAST_NAME")
    for row in result:
        full_name = row[0] + ' ' + row[1]
        print(full_name, end=' ')
        print('')

def query4(engine, team_state, team_color):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Player.uniform_num, Player.first_name, Player.last_name)\
        .join(team, team.team_id == Player.team_id)\
        .join(state, state.state_id == team.state_id)\
        .join(color, color.color_id == team.color_id)\
        .filter(state.name == team_state)\
        .filter(color.name == team_color).all()
    print("UNIFORM_NUM FIRST_NAME LAST_NAME")
    for row in result:
        print(row[0], row[1], row[2])

def query5(engine, num_wins):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Player.first_name, Player.last_name, team.name, team.wins).join(team, team.team_id == Player.team_id).filter(team.wins > num_wins)
    print("FIRST_NAME LAST_NAME NAME WINS")
    for row in result:
        print(row[0], row[1], row[2], row[3])