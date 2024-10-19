from server import app, db, User
from werkzeug.security import generate_password_hash

# Asegurarse de que las operaciones de base de datos estén dentro del contexto de la aplicación
with app.app_context():
    # Crear el primer usuario administrador
    admin = User(name="OvierObregon", email="ovier@example.com",
                 password=generate_password_hash("root1234", method='pbkdf2:sha256'))

    # Agregar el usuario administrador a la base de datos
    db.session.add(admin)
    db.session.commit()

    print("Usuario administrador creado exitosamente.")
