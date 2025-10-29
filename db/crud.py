from db.models import Article

def get_all_articles(db):
    return db.query(Article).order_by(Article.collected_date.desc()).all()

def get_articles_sitename(db, siteName):
    return db.query(Article).filter(Article.siteName == siteName).all()