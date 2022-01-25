from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create(cls, data):
        query = (
            "INSERT INTO dojos (name, location, language, comment) "
            "VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        )
        return connectToMySQL('dojo_survey').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = ("SELECT * FROM dojos;")
        results = connectToMySQL('dojo_survey').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one(cls, data):
        query = (
            "SELECT * FROM dojos WHERE id = %(id)s;"
        )
        results = connectToMySQL('dojo_survey').query_db(query, data)
        print(results)
        return cls(results[0])

    @staticmethod
    def validator(form_data):
        is_valid = True
        if len(form_data['name']) < 3:
            flash("Name must be at least 3 characters long.")
            is_valid = False
        if len(form_data['location']) < 3:
            flash("Dojo Location must be at least 3 characters long.")
            is_valid = False
        if len(form_data['language']) < 1:
            flash("Coding Language must be selected")
            is_valid = False
        if len(form_data['comment']) < 1:
            flash("Comment must have at least 1 word")
            is_valid = False
        return is_valid