import sqlite3
import json
conn = sqlite3.connect('mysqlairport.db')
c = conn.cursor()
c.execute('''CREATE TABLE airports(code text, lat text, lon text, name text, city text, state text, 
		country text, woeid text, tz text, phone text, type text, email, text 
		url text, runway_length text, elev text, icao text, direct_flights text, carriers text)''')
# c.execute('''CREATE TABLE airports(code text, lat real)''')
with open('airports.json') as json_file:
	new_json = json.loads(json_file.read())
	for info in new_json:
		v_l = []
		v  = info.values()
		for i in v:
			v_l.append(i)
		c.execute("INSERT INTO airports VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
		(v_l[0], v_l[1], v_l[2], v_l[3], v_l[4], v_l[5], v_l[6], v_l[7], v_l[8], v_l[9], v_l[10], 
			v_l[11], v_l[12], v_l[13], v_l[14], v_l[15], v_l[16], v_l[17]))
conn.commit()
c.close()
conn.close()
