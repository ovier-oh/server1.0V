from server import app, db, User
from werkzeug.security import generate_password_hash

# Asegurarse de que las operaciones de base de datos estén dentro del contexto de la aplicación
with app.app_context():
    # Verificar si el usuario ya existe
    existing_user = User.query.filter_by(email="ovier@example.com").first()

    if existing_user:
        print(f"El usuario con el correo {existing_user.email} ya existe.")
    else:
        # Crear el primer usuario administrador si no existe
        admin = User(
            name="OvierObregon",
            email="ovier@example.com",
            password=generate_password_hash("root1234", method='pbkdf2:sha256'),
            is_admin=True  # Asegurarse de que el usuario es un administrador
        )

        # Agregar el usuario administrador a la base de datos
        db.session.add(admin)
        db.session.commit()

        print("Usuario administrador creado exitosamente.")
