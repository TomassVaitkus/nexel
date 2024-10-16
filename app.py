from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)

# Flask-Mail konfigūracija
app.config['MAIL_SERVER'] = 'smtp.hostinger.com'  # Galite naudoti kitą SMTP serverį
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'info@tomasvaitkus.lt'  # Jūsų el. paštas
app.config['MAIL_PASSWORD'] = '1985Diablo5891_'  # Jūsų el. pašto slaptažodis
app.config['MAIL_DEFAULT_SENDER'] = 'info@tomasvaitkus.lt'  # Siuntėjas

mail = Mail(app)

@app.route('/')
def home():
    return render_template('apie.html')

@app.route('/apie')
def apie():
    return render_template('apie.html')

@app.route('/paslaugos')
def paslaugos():
    return render_template('paslaugos.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/kontaktai', methods=['GET', 'POST'])
def kontaktai():
    if request.method == 'POST':
        vardas = request.form['name']
        email = request.form['email']
        zinute = request.form['message']

        # Sukuriame žinutę, kurią norime išsiųsti el. paštu
        msg = Message('Nauja užklausa iš ' + vardas,
                      recipients=['info@tomasvaitkus.lt'])  # Pakeisk su adresu, į kurį norite gauti užklausas
        msg.body = f'Vardas: {vardas}\nEl. paštas: {email}\n\nŽinutė:\n{zinute}'

        # Išsiunčiame el. laišką
        mail.send(msg)

        flash('Jūsų užklausa sėkmingai išsiųsta!', 'success')
        return redirect(url_for('success'))

    return render_template('kontaktai.html')

if __name__ == '__main__':
    app.secret_key = 'slaptas_raktas'
    app.run(debug=True)
