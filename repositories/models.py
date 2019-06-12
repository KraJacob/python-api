from pymongo import MongoClient
import traceback


#La classe des publications 

class Country():
    def __init__(self, name, capital_city):
        self.name = name
        self.capital_city = capital_city


class Comments():
    def __init__(self, id, autor, date, idpublication, content, tags, likes, dislike, idstartup):
        self.id = id
        self.autor = autor
        self.date = date
        self.idpublication = idpublication
        self.content = content
        self.tags = tags
        self.likes = likes
        self.dislike = dislike
        self.idstartup = idstartup


class Post():
    def __init__(self, _id, post_date, id_startup, startup_name, social_network, url_on_social_network, post_url, post_contenu, post_autor,
                 post_creation_date, nbr_like, nbr_dislike, nbr_share, tags):
        self._id = _id
        self.id_startup = id_startup
        self.post_date = post_date        
        self.startup_name = startup_name
        self.social_network = social_network
        self.url_on_social_network = url_on_social_network
        self.post_url = post_url
        self.post_autor= post_autor
        self.post_contenu = post_contenu
        self.nbr_like = nbr_like
        self.nbr_dislike = nbr_dislike
        self.nbr_share = nbr_share
        self.tags = tags

class Personnel():
    def __init__(self, id_pers, name, firstname, birthday, role, id_startup, country):
        self.id_pers = id_pers
        self.name = name
        self.firstname = firstname
        self.birthday = birthday
        self.role = role
        self.id_startup = id_startup
        self.country = country        


def mongoConnection(mongo_url, mongo_database, collection):
    try:
        url = "mongodb://" + mongo_url + ":27017"
        conn = MongoClient(url)

        # database
        db = conn[mongo_database]

        # Created or Switched to the given collection
        return db[collection]
    except Exception:
        print(traceback.format_exc())
        return None


