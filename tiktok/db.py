from email.base64mime import header_encode
import sqlite3
from symbol import file_input

dd = ['trending', 'foryou', 'foryoupage', 'fyp', 'storytime', 'coming2america', 'treding', 'team07', 'viralvideo', 'moment', 'lovestory', 'view', 'foryou', 'foryoupage', 'fyp', 'tiktok', 'viral', 'funny', 'trend', 'trending', 'funny', 'lol', 'fyp', 'trending', 'foryoupage', 'sayitright', 'fyp', 'biginkenergy', 'petsoftiktok', 'petlife', 'viral', 'trending', '', 'bellletstalk', 'xgamesmode', 'xyzbca', 'asmr', 'satisfying', 'trending', 'viral', 'fyp', 'foryou', 'foryoupage', '4u', 'duet', 'fypシ', 'fypg', 'fu', 'arlostrong', 'fypシ', '4yp', 'trending', 'viral', 'k9softiktok', 'tiktokdogs', '', 'fyp', 'viral', 'gnb', 'share', 'trend', 
'trending', 'verifyme', 'couple', 'foryou', 'fyp', 'viral', 'baby', 'mommydaughter', 'fypシ', 'trending', 'foryou', 'foryoupage', 'fyp', 'viral', 'trending', 'hospital', 'foryou', 'foryoupage', 'trending', 'fypシ', 'xyzbca', 'earthday', 'foryourpage', 'fup', '', '', '', '', '', 'whamos', 'fyp', 'trending', 'fyp', 'foryoupage', 'fypage', '2022', 'blessed', 'trending', 'zenitsu', 
'demonslayer', 'wtf', 'awesome', 'cool', 'viral', 'wtf', 'happy', 'yes', 'blowup', 'fypageシ', 'pov', 'duet', 'yes', 'thankyou', 'loveyou', 'cosplay', 'workout', 'motivation', 'fyp', 'tourettes', 'foryou', 'tourettesawareness', 'lockdown', 'viral', 'funny', 'trending', 'painting', 'artistsoftiktok', 'trending', 'fyp', '', 'foryou', 'fyp', 'foryoupage', 'trending', 'viral', 'tennis', 'football', 'tictactoe', 'challenge', 'xyzbca', 'funny', 'sports', 'foryou', 'fyp', 'foryoupage', 'tiktok', 'comedy', 'trending', 'trend', 'funny', '', 'stitch', 'fyp', 'foryoupage', 'lenovojustbeyou', 'petlife', 'petsoftiktok', 'trending', 'fyp', 'funny', 'babyanddad', 'cutetoddler', 'viral', 'trending', 'bunnies', 'foryou', 'girldad', 'comedy', 'trend', '4u', 'trending', 
'fyp', 'fypage', 'twilightsaga', 'taylorlautner', 'taydome', 'robertpattinson', 'viral', 'couplegoals', 'fyp', 'foryou', 'mellocair', 'wdym', 'whatdoyoumeme', 'trending', 'homecooked', 'cashappinbio', 'minecraft', 'foryou', 'foryoupage', 'minecraftbuild', 'mc', 'build', 'viral', 'trending', 'fernandoarmy', 'foryou', 'fy', 'fouryoupage', 'viral', 'trend', 'trending', 'paperplane', 'tutorial', '', '', 'dancer', 'choreography', 'trending', 'slumberparty', 'ashnikko', 'lgbt', 'brisbane', 'twerk', 'kmstudios', 'australia', 'dancetok', 'justiceforjohnnydepp', 'partnerwork', 'lesbian', '', 'trending', 'featureme', 'featurethis', 'viral', 'fyp', 'comedy', 'foryoupage', 'foryou', 'animal', 'lion', 'tiger', 'fyp', 'edit', 'pet', 'cat', 'fup', 'animals', 'nature', 'wild', 'wildlife', 'viral', 'zoo', 'trend', 'trending', 'safari', 'foru', 'awareness', 'learn', 'learnontiktok', 'edutok', 'education', '', 'ctcvoicebox', 'dayinmylife', 'oikosonetrip', 'rock', 'soul', 'fyp', 'cover', '365days', 'iseered', 'sing', 'singer', 'foryou', 'viral', 'trending', 'xyzbca', 'fyp', 'foryou', 'foryoupage', 'catsoftiktok', 'fantheory', 'tiktokfitness', 'trending', 'duet', '', 'satisfying', 'asmr', 'crushing', 'fyp', 'crushit', 'foryoupage', 'glass', 'trending', 'foryou', 'fyp', 'foryoupage', 'fyp', 'tiktok', 'viral', 'funny', 'trending', 'trend', 'fyp', 'fypシ', 'funny', 'funnyclip', 'meme', 'comedy', 'viral', 'trending', 'strange', 'lmao', 'hilarious', 'dailydoseofinternet', 'xyzabc']

def create_connection(sqlite_file=None):

    try:
        if sqlite_file:
            conn = sqlite3.connect(sqlite_file)
        else:
            conn = sqlite3.connect('tiktok.db')
        return conn

    except sqlite3.Error as error:
        raise (
            "An error is occured while connecting to the datebase",
            error.args[0]
        )

def create_table(header, db_name, file_name=None):
    
    # for initial storage
    c_db_header = ""
    len_for_comma = 1
    conn = create_connection(file_name)
    c = conn.cursor()

    # for insert columns
    for c_header in header:
        if len(header) != len_for_comma:
            c_db_header += f"'{c_header}'" + ", "
        else:
            c_db_header += c_header  
        len_for_comma += 1
    try:
        c.execute(f"""CREATE TABLE {db_name}({c_db_header})""")
        print(f'new table {db_name} created')
    except sqlite3.OperationalError as e:
        raise e

    conn.commit()
    conn.close()
    
def add_data(header, tiktok_data, db_name, file_name=None):
    
    # for initial storage
    c_db_header = ""
    i_db_header = ""
    len_for_comma = 1
    conn = create_connection(file_name)
    c = conn.cursor()

    # for DB header
    for c_header in header:
        c_db_header += c_header + ", "
    
    # for insert columns
    for i_header in header:
        x = i_header.split(" ")[0]
        if len(header) != len_for_comma:
            i_db_header += x + ", "
        else:
            i_db_header += x  
        len_for_comma += 1

    # print(c_db_header)
    # print(i_db_header)
    
    try:
        c.execute(f"""CREATE TABLE IF NOT EXISTS {db_name}("{c_db_header}")""")
        
        for db_data in tiktok_data:
            print(f"INSERT INTO {db_name}({i_db_header}) VALUES ({db_data})")
            # c.execute("INSERT INTO test_hashtag (name) VALUES ('bilal')")
            c.execute(f"INSERT INTO {db_name}({i_db_header}) VALUES ('{db_data}')")
        
        print('successfully added')
        
    except sqlite3.OperationalError as e:
        raise ("An error has occured", e)

    conn.commit()
    conn.close()

def single_search(header, search_data, db_name, file_name=""):
    conn = create_connection(file_name)
    c = conn.cursor()
    print(db_name)
    d = c.execute("select * from '%s' where %s = %s" %(db_name, header, search_data))
    # d = c.execute("select * from %s where %s" %(db_name, search_data))
    return d

def remove_rows(db_name, file_name=None):
    conn = create_connection(file_name)
    print(db_name, conn)
    c = conn.cursor()
    c_sql = f"""create table {db_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)"""
    # sql = f"delete from {damb_ne} where name"
    # try:
    v = c.execute(c_sql)
    print(v)
    # print('remove')
    conn.commit()
    conn.close()
    print('closed')
    
def drop_table(db_name, file_name=None):
    conn = create_connection(file_name)
    c = conn.cursor()
    try:
        c.execute("drop table %s" %(db_name))
    except sqlite3.OperationalError as e:
        return {'message': "Table not fount!", 'error' : e.args[0]}
    conn.commit()
    conn.close()
    return True

table_row = [
    'Personid AUTOINCREMENT PRIMARY KEY',
    'LastName varchar(255) NOT NULL',
    'FirstName varchar(255)',
    'Age int',
]

print(create_table(table_row, 'new_table1'))
# print(add_data(['name',], dd, 'test_hashtag'))
# print(drop_table('new_table5'))
# print(remove_rows('test_hashtag'))