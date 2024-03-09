from clonepinterest import database, app
from clonepinterest.models import Usuario, Foto

with app.app_context():
    database.create_all()