from flask_app.config.mysqlconnection import connectToMySQL


class dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        @classmethod
        def save(cls, data):
            query = "INSERT INTO dojo (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
            result = connectToMySQL('dojo_ninja').query_db(query,data)
            return result
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojo_ninja').query_db(query)
        dojos = []
        for dojos in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if results == False:
            return False