import records
from datetime import datetime
import os

db = records.Database(os.environ["DATABASE_URL"])
db.query('CREATE TABLE IF NOT EXISTS repos (id int PRIMARY KEY, pubtime timestamp)')


def posted(repo):
    print 'posted: ' + repo['full_name']
    db.query('INSERT INTO repos (id, pubtime) VALUES(:id, :pubtime)', id=repo['id'], pubtime=datetime.utcnow())


def has_posted(repo):
    rows = db.query('SELECT * FROM repos WHERE id=:id', id=repo['id'])
    return len(rows.all())
