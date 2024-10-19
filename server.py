from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = b'\x0f;\xf2Ke7UZx\x7f/\x90 \xa5zp\x06\xbd\xf6\xe7\x81\xb2u@'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
migrate = Migrate(app, db)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
@login_required
def index():
    if current_user.is_authenticated:
        users = User.query.all()
        return render_template('index.html', users=users)
    return redirect(url_for('login'))


@app.route('/add', methods=['POST'])
@login_required
def add_user():
    name = request.form['name']
    email = request.form['email']

    # Verificar si el email ya existe
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        flash(f'The email {email} is already registered. Please use a different email.')
        return redirect(url_for('index'))

    # Si el email no existe, se procede a agregar el nuevo usuario
    password = generate_password_hash(request.form['password'], method='pbkdf2:sha256')
    new_user = User(name=name, email=email, password=password)

    db.session.add(new_user)
    db.session.commit()
    flash('User added successfully!')

    return redirect(url_for('index'))


@app.route('/delete/<int:id>')
@login_required
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('user deleted successfully!')
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Buscar usuario por email
        user = User.query.filter_by(email=email).first()

        if user:
            # Verificar que la contraseña es correcta
            if check_password_hash(user.password, password):
                login_user(user)  # Loguear al usuario
                return redirect(url_for('index'))
            else:
                flash('Invalid credentials. Please try again.')
        else:
            flash('User not found. Please register first.')

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)