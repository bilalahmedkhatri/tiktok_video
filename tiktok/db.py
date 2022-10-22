from email.header import Header
from xmlrpc.client import DateTime
import psycopg2
from datetime import date, datetime

dd = ['trending', 'foryou', 'foryoupage', 'fyp', 'storytime', 'coming2america', 'treding', 'team07', 'viralvideo', 'moment', 'lovestory', 'view', 'foryou', 'foryoupage', 'fyp', 'tiktok', 'viral', 'funny', 'trend', 'trending', 'funny', 'lol', 'fyp', 'trending', 'foryoupage', 'sayitright', 'fyp', 'biginkenergy', 'petsoftiktok', 'petlife', 'viral', 'trending', '', 'bellletstalk', 'xgamesmode', 'xyzbca', 'asmr', 'satisfying', 'trending', 'viral', 'fyp', 'foryou', 'foryoupage', '4u', 'duet', 'fypシ', 'fypg', 'fu', 'arlostrong', 'fypシ', '4yp', 'trending', 'viral', 'k9softiktok', 'tiktokdogs', '', 'fyp', 'viral', 'gnb', 'share', 'trend',
      'trending', 'verifyme', 'couple', 'foryou', 'fyp', 'viral', 'baby', 'mommydaughter', 'fypシ', 'trending', 'foryou', 'foryoupage', 'fyp', 'viral', 'trending', 'hospital', 'foryou', 'foryoupage', 'trending', 'fypシ', 'xyzbca', 'earthday', 'foryourpage', 'fup', '', '', '', '', '', 'whamos', 'fyp', 'trending', 'fyp', 'foryoupage', 'fypage', '2022', 'blessed', 'trending', 'zenitsu',
      'demonslayer', 'wtf', 'awesome', 'cool', 'viral', 'wtf', 'happy', 'yes', 'blowup', 'fypageシ', 'pov', 'duet', 'yes', 'thankyou', 'loveyou', 'cosplay', 'workout', 'motivation', 'fyp', 'tourettes', 'foryou', 'tourettesawareness', 'lockdown', 'viral', 'funny', 'trending', 'painting', 'artistsoftiktok', 'trending', 'fyp', '', 'foryou', 'fyp', 'foryoupage', 'trending', 'viral', 'tennis', 'football', 'tictactoe', 'challenge', 'xyzbca', 'funny', 'sports', 'foryou', 'fyp', 'foryoupage', 'tiktok', 'comedy', 'trending', 'trend', 'funny', '', 'stitch', 'fyp', 'foryoupage', 'lenovojustbeyou', 'petlife', 'petsoftiktok', 'trending', 'fyp', 'funny', 'babyanddad', 'cutetoddler', 'viral', 'trending', 'bunnies', 'foryou', 'girldad', 'comedy', 'trend', '4u', 'trending',
      'fyp', 'fypage', 'twilightsaga', 'usman', 'usman', 'usman', 'usman', 'usman', 'usman', 'usman', 'usman', 'bilal', 'taylorlautner', 'taydome', 'robertpattinson', 'viral', 'couplegoals', 'fyp', 'foryou', 'mellocair', 'wdym', 'whatdoyoumeme', 'trending', 'homecooked', 'cashappinbio', 'minecraft', 'foryou', 'foryoupage', 'minecraftbuild', 'mc', 'build', 'viral', 'trending', 'fernandoarmy', 'foryou', 'fy', 'fouryoupage', 'viral', 'trend', 'trending', 'paperplane', 'tutorial', '', '', 'dancer', 'choreography', 'trending', 'slumberparty', 'ashnikko', 'lgbt', 'brisbane', 'twerk', 'kmstudios', 'australia', 'dancetok', 'justiceforjohnnydepp', 'partnerwork', 'lesbian', '', 'trending', 'featureme', 'featurethis', 'viral', 'fyp', 'comedy', 'foryoupage', 'foryou', 'animal', 'lion', 'tiger', 'fyp', 'edit', 'pet', 'cat', 'fup', 'animals', 'nature', 'wild', 'wildlife', 'viral', 'zoo', 'trend', 'trending', 'safari', 'foru', 'awareness', 'learn', 'learnontiktok', 'edutok', 'education', '', 'ctcvoicebox', 'dayinmylife', 'oikosonetrip', 'rock', 'soul', 'fyp', 'cover', '365days', 'iseered', 'sing', 'singer', 'foryou', 'viral', 'trending', 'xyzbca', 'fyp', 'foryou', 'foryoupage', 'catsoftiktok', 'fantheory', 'tiktokfitness', 'trending', 'duet', '', 'satisfying', 'asmr', 'crushing', 'fyp', 'crushit', 'foryoupage', 'glass', 'trending', 'foryou', 'fyp', 'foryoupage', 'fyp', 'tiktok', 'viral', 'funny', 'trending', 'trend', 'fyp', 'fypシ', 'funny', 'funnyclip', 'meme', 'comedy', 'viral', 'trending', 'strange', 'lmao', 'hilarious', 'dailydoseofinternet', 'xyzabc']


def create_connection(sqlite_file=None):
    try:
        conn = psycopg2.connect(
            user="tiktokapi",
            password="tiktokapi",
            host="127.0.0.1",
            port="5432",
            database="TikTokApi",
        )
        return conn
    except psycopg2.DatabaseError as error:
        raise error


def create_table(header, db_name, file_name=None):

    # for initial storage
    c_db_header = ""
    len_for_comma = 1
    conn = create_connection(file_name)
    c = conn.cursor()

    # for insert columns header
    for c_header in header:
        if len(header) != len_for_comma:
            c_db_header += c_header + ", "
        else:
            c_db_header += c_header
        len_for_comma += 1

    try:
        c.execute(f"""CREATE TABLE {db_name}({c_db_header})""")
        print(f'new table {db_name} created')
    except psycopg2.OperationalError as e:
        raise e

    conn.commit()
    conn.close()


def insert_data(header, tiktok_data, db_name):
    conn = create_connection()
    c = conn.cursor()
    try:
        for db_data in tiktok_data:
            c.execute(f"""
                INSERT INTO {db_name}({str(header[0])}, {str(header[1])}, {str(header[2])})
                VALUES ('{db_data}', 1, '{datetime.now()}')
                ON CONFLICT DO NOTHING;
            """)
            if c.rowcount == 0:
                c.execute(f"""
                    INSERT INTO {db_name}({str(header[0])})
                    VALUES ('{db_data}')
                    ON CONFLICT ({str(header[0])}) 
                    DO UPDATE SET {str(header[1])} = (SELECT {str(header[1])} FROM {db_name} where {str(header[0])} = '{db_data}')  + 1;
                """)
    except psycopg2.OperationalError as error:
        raise error
    conn.commit()
    conn.close()

# insert_data()


def get_data(header, db_name):
    top_hashtags = []
    conn = create_connection()
    c = conn.cursor()
    try:
        c.execute(f"""
            SELECT {str(header[0])}, {str(header[1])} FROM {db_name}
            WHERE {str(header[3])} IS NULL
            limit 50;
            """)
        top_hashtags_1 = c.fetchall()
        if c.rowcount >= 1:
            print(
                "  <---- getting hashtags from null DateTime in database { 5 random hashtags }---->")
            print("  <---- Updating updated DataTime for next prediction ---->")
            for update_datetime in top_hashtags_1:
                c.execute(f"""
                    UPDATE {db_name} SET {str(header[3])} = '{datetime.now()}'
                    WHERE {str(header[0])} = '{update_datetime[0]}' AND {str(header[1])} = {update_datetime[1]}
                """)
        if c.rowcount == 0:
            print(
                "  <---- If not null DateTime then take data updated DateTime { 5 random hashtags }---->")
            c.execute(f"""
                SELECT {str(header[0])}, {str(header[1])} FROM {db_name}
                ORDER BY {str(header[3])}
                limit 5;
            """)
            data_available = c.fetchall()
            print("  <---- Updating updated DataTime for next prediction ---->")
            for update_datetime in data_available:
                c.execute(f"""
                    UPDATE {db_name} SET {str(header[3])} = '{datetime.now()}'
                    WHERE {str(header[0])} = '{update_datetime[0]}' AND {str(header[1])} = {update_datetime[1]}
                """)
        if top_hashtags_1:
            top_hashtags = top_hashtags_1
        elif data_available:
            top_hashtags = data_available

    except psycopg2.OperationalError as error:
        raise error
    conn.commit()
    conn.close()
    print('     successfully gotted 5 oldest hashtags \n')
    return top_hashtags


def single_search(header, search_data, db_name, file_name=""):
    conn = create_connection(file_name)
    c = conn.cursor()
    print(db_name)
    d = c.execute("select * from '%s' where %s = %s" %
                  (db_name, header, search_data))
    return d


def remove_rows(header, db_name, file_name=None):
    # for initial storage
    c_db_header = ""
    len_for_comma = 1
    conn = create_connection(file_name)
    c = conn.cursor()

    # for insert columns header
    for c_header in header:
        if len(header) != len_for_comma:
            c_db_header += f"'{c_header}'" + ", "
        else:
            c_db_header += c_header
        len_for_comma += 1
    sql = f"delete from {db_name} where {c_db_header} not null"
    print(sql)
    # try:
    v = c.execute(sql)
    print(v.rowcount)
    # print('remove')
    conn.commit()
    conn.close()
    print('closed')


def drop_table(db_name, file_name=None):
    conn = create_connection(file_name)
    c = conn.cursor()
    try:
        c.execute("drop table %s" % (db_name))
    except sqlite3.OperationalError as e:
        return {'message': "Table not fount!", 'error': e.args[0]}
    conn.commit()
    conn.close()
    return True


table_row = [
    'Pid AUTOINCREMENT PRIMARY KEY',
    # 'Personid AUTOINCREMENT PRIMARY KEY',
    # 'LastName varchar(255) NOT NULL',
    'LastName varchar(255) UNIQUE NOT NULL',
    # 'FirstName varchar(255)',
    # 'Age int',
]

header = ['hashtag', 'count_hashtag', 'created_at', 'updated_at', ]
table_name = "video_editor_hashtag"
# print(create_table(table_row, 'new_table2'))
# print(insert_data(header, dd, table_name))
# print(get_data(header, table_name))
# print(drop_table('new_table2'))
# print(remove_rows(['name',], 'test_hashtag'))
