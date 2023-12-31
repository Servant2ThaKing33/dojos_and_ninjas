from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojo (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        result = connectToMySQL('dojos_ninjas').query_db(query,data)
        return result


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojo_ninja').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    

    @classmethod
    def get_dojo_with_ninja (cls , data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_ninjas').query_db(query , data)
        dojo = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                "id": row_from_db["ninjas.id"],
                "first_name": row_from_db["ninjas.first_name"],
                "last_name": row_from_db["ninja.last_name"],
                "age": row_from_db["ninja.age"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo

    
        

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if results == False:
            return False