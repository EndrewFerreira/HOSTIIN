<<<<<<< HEAD:Prototipo HostInn/Codigos/Tela_inical.py
from PyQt6 import uic, QtWidgets
from PyQt6.QtGui import QIcon,QPixmap
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtWidgets import QMessageBox, QLineEdit
import pymysql, sys
import Menu


banco = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="bd_teste2"
)

def verificar_permissao():
    cursor = banco.cursor()
    # Atenção: coloque os valores de string entre aspas na query
    comando_SQL = "SELECT COUNT(Permissao) FROM usuarios WHERE Permissao = 'Administrador'"
    cursor.execute(comando_SQL)
    resultado = cursor.fetchone()

    # Se o resultado existir e o count for maior que 0, esconde o botão
    if resultado and resultado[0] > 0:
        login_register.bttn_alterindex_2.hide()

def alter_reg():
    login_register.stackedWidget.setCurrentIndex(1)

def alter_log():
    login_register.stackedWidget.setCurrentIndex(0)

def password_view():
    """
    Alterna o modo de exibição das senhas e troca os ícones dos botões de visualização.
    """
    if login_register.lineEdit_passwrd.echoMode() == QLineEdit.EchoMode.Password:
        login_register.lineEdit_passwrd.setEchoMode(QLineEdit.EchoMode.Normal)
        login_register.lineEdit_passwrd_2.setEchoMode(QLineEdit.EchoMode.Normal)
        login_register.lineEdit_passwrd_3.setEchoMode(QLineEdit.EchoMode.Normal)
        login_register.bttn_passwrdview.setIcon(icon_eye_open)
        login_register.bttn_passwrdview_2.setIcon(icon_eye_open)
    else:
        login_register.lineEdit_passwrd.setEchoMode(QLineEdit.EchoMode.Password)
        login_register.lineEdit_passwrd_2.setEchoMode(QLineEdit.EchoMode.Password)
        login_register.lineEdit_passwrd_3.setEchoMode(QLineEdit.EchoMode.Password)
        login_register.bttn_passwrdview.setIcon(icon_eye_closed)
        login_register.bttn_passwrdview_2.setIcon(icon_eye_closed)

def login():
    global menu
    user = login_register.lineEdit_user_2.text()
    passwrd = login_register.lineEdit_passwrd_3.text()

    cursor = banco.cursor()
    comando_SQL = "SELECT Senha FROM usuarios WHERE Usuario = %s"
    cursor.execute(comando_SQL, (user,))
    resultado = cursor.fetchone()

    if resultado:
        senha_bd = resultado[0]
        if passwrd == senha_bd:
            QMessageBox.information(login_register, "Sucesso", "Login realizado com sucesso!")
            login_register.close()  # Fecha a tela de login
            menu = Menu.MainMenu()  # Exibe a tela do menu
            menu.show()
        else:
            QMessageBox.warning(login_register, "Erro", "Senha incorreta!")
    else:
        QMessageBox.warning(login_register, "Erro", "Usuário não encontrado!")


def forgot_password():
    login_register.stackedWidget.setCurrentIndex(3)

def buscar_cad():
    cpf = login_register.lineEdit_cpf.text()
    bday = login_register.lineEdit_bday.text()

    if not cpf or not bday:
        QMessageBox.warning(login_register, "Erro", "Preencha CPF e data de nascimento.")
        return

    cursor = banco.cursor()
    comando_SQL = "SELECT CPF, BDAY FROM usuarios WHERE CPF = %s AND BDAY = %s"
    cursor.execute(comando_SQL, (cpf, bday))
    resultado = cursor.fetchone()

    if not resultado:
        QMessageBox.warning(login_register, "Erro", "Dados incorretos ou inexistentes.")
        return

    QMessageBox.information(login_register, "Recuperação de senha", "Dados encontrados. Redefina sua senha.")
    login_register.stackedWidget.setCurrentIndex(2)  

def reset_password(): #mano bora ver se agora vai
    cpf = login_register.lineEdit_cpf.text()
    bday = login_register.lineEdit_bday.text()
    nova_senha = login_register.lineEdit_user_7.text()
    confirmar_senha = login_register.lineEdit_passwrd_8.text()

    if not nova_senha or not confirmar_senha:
        QMessageBox.warning(login_register, "Erro", "Preencha os campos de nova senha.")
        return

    if nova_senha != confirmar_senha:
        QMessageBox.warning(login_register, "Erro", "As senhas não coincidem.")
        return

    cursor = banco.cursor()
    comando_update = "UPDATE usuarios SET Senha = %s WHERE CPF = %s AND BDAY = %s"
    cursor.execute(comando_update, (nova_senha, cpf, bday))
    banco.commit()

    QMessageBox.information(login_register, "Sucesso", "Senha redefinida com sucesso!")
    login_register.stackedWidget.setCurrentIndex(0)

    # Limpa os campos
    login_register.lineEdit_cpf.setText("")
    login_register.lineEdit_bday.setText("")
    login_register.lineEdit_user_7.setText("")
    login_register.lineEdit_passwrd_8.setText("")

def new_reg():
    name = login_register.lineEdit_name.text()
    user = login_register.lineEdit_user.text()
    email = login_register.lineEdit_email.text()
    permissao = login_register.comboBox.currentText()
    passwrd = login_register.lineEdit_passwrd.text()
    passwrd_conf = login_register.lineEdit_passwrd_2.text()
    cpf = login_register.lineEdit_2.text()
    bday = login_register.dateEdit_2.text()
    # bday = login_register.dateEdit_2.setDate(QDate.fromString(str(), "yyyy-MM-dd"))

    if not name or not user or not email or not passwrd or not passwrd_conf:
        QMessageBox.warning(login_register, "Erro", "Todos os campos devem ser preenchidos!")
        return

    cursor = banco.cursor()
    comando_SQL = "SELECT usuario FROM usuarios WHERE usuario = %s"
    cursor.execute(comando_SQL, (user,))
    resultado = cursor.fetchone()

    if resultado:
        QMessageBox.warning(login_register, "Erro", "Usuário já existente!")
        return

    cursor = banco.cursor()
    comando_SQL = "SELECT email FROM usuarios WHERE email = %s"
    cursor.execute(comando_SQL, (email,))
    resultado = cursor.fetchone()

    if resultado:
        QMessageBox.warning(login_register, "Erro", "E-mail já existente!")
        return

    if passwrd != passwrd_conf:
        QMessageBox.warning(login_register, "Erro", "As senhas não coincidem!")
        return

    comando_SQL = "INSERT INTO usuarios (nome, usuario, permissao, email, senha, CPF, BDAY) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    dados = (name, user, permissao, email, passwrd, cpf, bday)
    cursor.execute(comando_SQL, dados)
    banco.commit()

    QMessageBox.information(login_register, "Sucesso", "Cadastro realizado com sucesso!")

    login_register.stackedWidget.setCurrentIndex(0)
    cursor = banco.cursor()
    # Atenção: coloque os valores de string entre aspas na query
    comando_SQL = "SELECT COUNT(Permissao) FROM usuarios WHERE Permissao = 'Administrador'"
    cursor.execute(comando_SQL)
    resultado = cursor.fetchone()

    # Se o resultado existir e o count for maior que 0, esconde o botão
    if resultado and resultado[0] > 0:
        login_register.bttn_alterindex_2.hide()

    # Limpa os campos após o cadastro
    login_register.lineEdit_name.setText("")
    login_register.lineEdit_user.setText("")
    login_register.lineEdit_email.setText("")
    login_register.lineEdit_passwrd.setText("")
    login_register.lineEdit_passwrd_2.setText("")

# Cria a aplicação antes de qualquer operação gráfica
app = QtWidgets.QApplication(sys.argv)

# Defina os ícones (ajuste os caminhos para os seus arquivos PNG)
icon_eye_open = QIcon(r"C:\Users\11054836\Desktop\PI\HOSTIIN\Prototipo HostInn\Icones\visibility.pngg")
icon_eye_closed = QIcon(r"C:\Users\11054836\Desktop\PI\HOSTIIN\Prototipo HostInn\Icones\visibility_off.png")

#===========================( Login/ Cadastro )=============================================
login_register = uic.loadUi(r"C:\Users\11054836\Desktop\PI\HOSTIIN\Prototipo HostInn\Telas\Login_Cadastro_1.ui")
login_register.setWindowTitle("HostInn")
login_register.lineEdit_2.setInputMask("000.000.000-00;_")
login_register.stackedWidget.setCurrentIndex(0)
login_register.lineEdit_passwrd.setEchoMode(QLineEdit.EchoMode.Password)
login_register.lineEdit_passwrd_2.setEchoMode(QLineEdit.EchoMode.Password)
login_register.lineEdit_passwrd_3.setEchoMode(QLineEdit.EchoMode.Password)

# Conecta os botões com suas funções
login_register.bttn_alterindex_2.clicked.connect(alter_reg)
login_register.bttn_register.clicked.connect(new_reg)
login_register.bttn_alterindex.clicked.connect(alter_log)
login_register.bttn_passwrdview.clicked.connect(password_view)
login_register.bttn_passwrdview_2.clicked.connect(password_view)
login_register.bttn_login.clicked.connect(login)
login_register.bttn_forgotpassword.clicked.connect(forgot_password)
login_register.bttn_search_user.clicked.connect(buscar_cad)
login_register.bttn_alterindex_4.clicked.connect(alter_log)
login_register.bttn_back_login.clicked.connect(alter_log)
login_register.bttn_reset_password.clicked.connect(reset_password)

# Define os ícones iniciais dos botões de visualização de senha
login_register.bttn_passwrdview.setIcon(icon_eye_closed)
login_register.bttn_passwrdview_2.setIcon(icon_eye_closed)

# Chama a função de verificação de permissão ao carregar a tela
verificar_permissao()

login_register.show()
sys.exit(app.exec())




# Cria a aplicação
app = QtWidgets.QApplication(sys.argv)
login_register = MainWindow()
login_register.setWindowTitle("HostInn")
login_register.show()
sys.exit(app.exec())

=======
from PyQt6 import uic, QtWidgets
from PyQt6.QtGui import QIcon,QPixmap
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtWidgets import QMessageBox, QLineEdit
import pymysql, sys
import Menu


banco = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="bd_teste2"
)

def verificar_permissao():
    cursor = banco.cursor()
    # Atenção: coloque os valores de string entre aspas na query
    comando_SQL = "SELECT COUNT(Permissao) FROM usuarios WHERE Permissao = 'Administrador'"
    cursor.execute(comando_SQL)
    resultado = cursor.fetchone()

    # Se o resultado existir e o count for maior que 0, esconde o botão
    if resultado and resultado[0] > 0:
        login_register.bttn_alterindex_2.hide()

def alter_reg():
    login_register.stackedWidget.setCurrentIndex(1)

def alter_log():
    login_register.stackedWidget.setCurrentIndex(0)

def password_view():
    """
    Alterna o modo de exibição das senhas e troca os ícones dos botões de visualização.
    """
    if login_register.lineEdit_passwrd.echoMode() == QLineEdit.EchoMode.Password:
        login_register.lineEdit_passwrd.setEchoMode(QLineEdit.EchoMode.Normal)
        login_register.lineEdit_passwrd_2.setEchoMode(QLineEdit.EchoMode.Normal)
        login_register.lineEdit_passwrd_3.setEchoMode(QLineEdit.EchoMode.Normal)
        login_register.bttn_passwrdview.setIcon(icon_eye_open)
        login_register.bttn_passwrdview_2.setIcon(icon_eye_open)
    else:
        login_register.lineEdit_passwrd.setEchoMode(QLineEdit.EchoMode.Password)
        login_register.lineEdit_passwrd_2.setEchoMode(QLineEdit.EchoMode.Password)
        login_register.lineEdit_passwrd_3.setEchoMode(QLineEdit.EchoMode.Password)
        login_register.bttn_passwrdview.setIcon(icon_eye_closed)
        login_register.bttn_passwrdview_2.setIcon(icon_eye_closed)

def login():
    global menu
    user = login_register.lineEdit_user_2.text()
    passwrd = login_register.lineEdit_passwrd_3.text()

    cursor = banco.cursor()
    comando_SQL = "SELECT Senha FROM usuarios WHERE Usuario = %s"
    cursor.execute(comando_SQL, (user,))
    resultado = cursor.fetchone()

    if resultado:
        senha_bd = resultado[0]
        if passwrd == senha_bd:
            QMessageBox.information(login_register, "Sucesso", "Login realizado com sucesso!")
            login_register.close()  # Fecha a tela de login
            menu = Menu.MainMenu()  # Exibe a tela do menu
            menu.show()
        else:
            QMessageBox.warning(login_register, "Erro", "Senha incorreta!")
    else:
        QMessageBox.warning(login_register, "Erro", "Usuário não encontrado!")


def forgot_password():
    login_register.stackedWidget.setCurrentIndex(3)

def buscar_cad():
    cpf = login_register.lineEdit_cpf.text()
    bday = login_register.lineEdit_bday.text()

    if not cpf or not bday:
        QMessageBox.warning(login_register, "Erro", "Preencha CPF e data de nascimento.")
        return

    cursor = banco.cursor()
    comando_SQL = "SELECT CPF, BDAY FROM usuarios WHERE CPF = %s AND BDAY = %s"
    cursor.execute(comando_SQL, (cpf, bday))
    resultado = cursor.fetchone()

    if not resultado:
        QMessageBox.warning(login_register, "Erro", "Dados incorretos ou inexistentes.")
        return

    QMessageBox.information(login_register, "Recuperação de senha", "Dados encontrados. Redefina sua senha.")
    login_register.stackedWidget.setCurrentIndex(2)  

def reset_password(): #mano bora ver se agora vai
    cpf = login_register.lineEdit_cpf.text()
    bday = login_register.lineEdit_bday.text()
    nova_senha = login_register.lineEdit_user_7.text()
    confirmar_senha = login_register.lineEdit_passwrd_8.text()

    if not nova_senha or not confirmar_senha:
        QMessageBox.warning(login_register, "Erro", "Preencha os campos de nova senha.")
        return

    if nova_senha != confirmar_senha:
        QMessageBox.warning(login_register, "Erro", "As senhas não coincidem.")
        return

    cursor = banco.cursor()
    comando_update = "UPDATE usuarios SET Senha = %s WHERE CPF = %s AND BDAY = %s"
    cursor.execute(comando_update, (nova_senha, cpf, bday))
    banco.commit()

    QMessageBox.information(login_register, "Sucesso", "Senha redefinida com sucesso!")
    login_register.stackedWidget.setCurrentIndex(0)

    # Limpa os campos
    login_register.lineEdit_cpf.setText("")
    login_register.lineEdit_bday.setText("")
    login_register.lineEdit_user_7.setText("")
    login_register.lineEdit_passwrd_8.setText("")

def new_reg():
    name = login_register.lineEdit_name.text()
    user = login_register.lineEdit_user.text()
    email = login_register.lineEdit_email.text()
    permissao = login_register.comboBox.currentText()
    passwrd = login_register.lineEdit_passwrd.text()
    passwrd_conf = login_register.lineEdit_passwrd_2.text()
    cpf = login_register.lineEdit_2.text()
    bday = login_register.dateEdit_2.text()
    # bday = login_register.dateEdit_2.setDate(QDate.fromString(str(), "yyyy-MM-dd"))

    if not name or not user or not email or not passwrd or not passwrd_conf:
        QMessageBox.warning(login_register, "Erro", "Todos os campos devem ser preenchidos!")
        return

    cursor = banco.cursor()
    comando_SQL = "SELECT usuario FROM usuarios WHERE usuario = %s"
    cursor.execute(comando_SQL, (user,))
    resultado = cursor.fetchone()

    if resultado:
        QMessageBox.warning(login_register, "Erro", "Usuário já existente!")
        return

    cursor = banco.cursor()
    comando_SQL = "SELECT email FROM usuarios WHERE email = %s"
    cursor.execute(comando_SQL, (email,))
    resultado = cursor.fetchone()

    if resultado:
        QMessageBox.warning(login_register, "Erro", "E-mail já existente!")
        return

    if passwrd != passwrd_conf:
        QMessageBox.warning(login_register, "Erro", "As senhas não coincidem!")
        return

    comando_SQL = "INSERT INTO usuarios (nome, usuario, permissao, email, senha, CPF, BDAY) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    dados = (name, user, permissao, email, passwrd, cpf, bday)
    cursor.execute(comando_SQL, dados)
    banco.commit()

    QMessageBox.information(login_register, "Sucesso", "Cadastro realizado com sucesso!")

    login_register.stackedWidget.setCurrentIndex(0)
    cursor = banco.cursor()
    # Atenção: coloque os valores de string entre aspas na query
    comando_SQL = "SELECT COUNT(Permissao) FROM usuarios WHERE Permissao = 'Administrador'"
    cursor.execute(comando_SQL)
    resultado = cursor.fetchone()

    # Se o resultado existir e o count for maior que 0, esconde o botão
    if resultado and resultado[0] > 0:
        login_register.bttn_alterindex_2.hide()

    # Limpa os campos após o cadastro
    login_register.lineEdit_name.setText("")
    login_register.lineEdit_user.setText("")
    login_register.lineEdit_email.setText("")
    login_register.lineEdit_passwrd.setText("")
    login_register.lineEdit_passwrd_2.setText("")

# Cria a aplicação antes de qualquer operação gráfica
app = QtWidgets.QApplication(sys.argv)

# Defina os ícones (ajuste os caminhos para os seus arquivos PNG)
icon_eye_open = QIcon(r"C:\Users\11054836\Desktop\PI\HOSTIIN\Prototipo HostInn\Icones\visibility.png")
icon_eye_closed = QIcon(r"C:\Users\11054836\Desktop\PI\HOSTIIN\Prototipo HostInn\Icones\visibility_off.png")

#===========================( Login/ Cadastro )=============================================
login_register = uic.loadUi(r"C:\Users\10816146\Desktop\PI\HOSTIIN\Prototipo HostInn\Telas\Login_Cadastro_1.ui")
login_register.setWindowTitle("HostInn")
login_register.lineEdit_2.setInputMask("000.000.000-00;_")
login_register.stackedWidget.setCurrentIndex(0)
login_register.lineEdit_passwrd.setEchoMode(QLineEdit.EchoMode.Password)
login_register.lineEdit_passwrd_2.setEchoMode(QLineEdit.EchoMode.Password)
login_register.lineEdit_passwrd_3.setEchoMode(QLineEdit.EchoMode.Password)

# Conecta os botões com suas funções
login_register.bttn_alterindex_2.clicked.connect(alter_reg)
login_register.bttn_register.clicked.connect(new_reg)
login_register.bttn_alterindex.clicked.connect(alter_log)
login_register.bttn_passwrdview.clicked.connect(password_view)
login_register.bttn_passwrdview_2.clicked.connect(password_view)
login_register.bttn_login.clicked.connect(login)
login_register.bttn_forgotpassword.clicked.connect(forgot_password)
login_register.bttn_search_user.clicked.connect(buscar_cad)
login_register.bttn_alterindex_4.clicked.connect(alter_log)
login_register.bttn_back_login.clicked.connect(alter_log)
login_register.bttn_reset_password.clicked.connect(reset_password)

# Define os ícones iniciais dos botões de visualização de senha
login_register.bttn_passwrdview.setIcon(icon_eye_closed)
login_register.bttn_passwrdview_2.setIcon(icon_eye_closed)

# Chama a função de verificação de permissão ao carregar a tela
verificar_permissao()

login_register.show()
sys.exit(app.exec())




# Cria a aplicação
app = QtWidgets.QApplication(sys.argv)
login_register = MainWindow()
login_register.setWindowTitle("HostInn")
login_register.show()
sys.exit(app.exec())

>>>>>>> 5cb9a243d3fa85041bb15418dc05b5bdabc7e122:Prototipo HostInn/Codigos/Tela_inicial.py
