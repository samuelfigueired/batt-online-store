from flask import Flask, render_template, request, request, redirect, url_for

app = Flask(__name__)

# Lista de frutas (exemplo)


@app.route('/')
def index():
    return render_template('index.html')
##
# Rota para renderizar about.html
@app.route('/about')
def about():
    return render_template('about.html')

# Rota para renderizar contact.html e lidar com formulário de contato
@app.route('/contact')
def contact():
    return render_template('contact.html')



usuarios = {
    'usuario1': {'username': 'usuario1', 'password': 'senha1'},
    'usuario2': {'username': 'usuario2', 'password': 'senha2'}
}

# Rota para renderizar a página de login e processar o formulário
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Verificar se o usuário existe e a senha está correta
        if username in usuarios and usuarios[username]['password'] == password:
            # Se o login for bem-sucedido, redirecionar para página de sucesso
            return redirect(url_for('login_success', username=username))
        else:
            # Se o login falhar, renderizar a página de login novamente com uma mensagem de erro
            error_message = "Credenciais inválidas. Por favor, tente novamente."
            return render_template('login.html', error_message=error_message)
    
    # Se o método for GET, renderizar a página de login
    return render_template('login.html')

# Rota para exibir página de sucesso após o login
@app.route('/login-success/<username>')
def login_success(username):
    return render_template('loginSuccess.html', username=username)

@app.route('/produtos')
def produtos():
    return render_template('produtos.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

if __name__ == "__main__":
    app.run(debug=True)
