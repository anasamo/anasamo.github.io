import json
import argparse
import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')
c = conn.cursor()
with open("bugs.json") as f:
    data = json.load(f)

df = pd.DataFrame(data)
df.to_sql('bugs', conn)

domain_map = {
'dbms' : 'Database Management Systems'
}


common_where_clause = "(resolution IN ('confirmed', 'fixed', 'open') OR resolution IS NULL)"
for domain, count in c.execute('SELECT domain, COUNT(*) FROM bugs WHERE ' + common_where_clause + ' GROUP BY domain;').fetchall():
    print('<h2>%s (%d bugs)</h2>' % (domain_map[domain], count))
    for system, count in c.execute(("SELECT system, COUNT(*) FROM bugs WHERE domain = '%s' AND " + common_where_clause + " GROUP BY system") % (domain,)).fetchall():
        print('<h3>%s (%d bugs)</h3>' % (system, count))
        for title, url, found_by, resolution in c.execute(("SELECT title, url, reported_by, resolution FROM bugs WHERE domain='%s' AND system='%s' AND " + common_where_clause + ";") % (domain, system)).fetchall():
            print('<details>')
            print('<summary>%s</summary>'% (title, ))
            if resolution is None:
                resolution = 'unconfirmed'
            print('Status: %s<br />' % (resolution, ))
            print('Link: <a href="%s">%s</a> <br />' % (url, url))
            print('</details>')
