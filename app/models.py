from app import db


class ExampleModel(db.Model):
    """Description of Model"""
    id = db.Column(db.Integer, primary_key=True)
    example_1 = db.Column(db.String(255))
    example_2 = db.Column(db.Integer, index=True, unique=False)

    def __repr__(self):
        return '<Question {}'.format(str(self.id) + ' ' + str(self.example_1) + ' '
                                     + str(self.example_2)
                                     )
