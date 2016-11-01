import github
import sns
import db
from datetime import datetime


def job():
    print '-----job started-----'
    print datetime.utcnow()
    repos = github.get_hot_repos()
    for repo in repos:
        if not db.has_posted(repo):
            if sns.post(repo):
                db.posted(repo)
            break


"""
def run():
    job()
    schedule.every(int(os.getenv('INTERVAL_MINUTES', '5'))).minutes.do(job)

    while 1:
        schedule.run_pending()
        time.sleep(1)
"""
