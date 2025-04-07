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

# def buscar_cad():
#     global login_register, menu
#     cpf = login_register.lineEdit_cpf.text()
#     bday = login_register.lineEdit_bday.text()


#     cursor = banco.cursor()
#     comando_SQL = "SELECT CPF, BDAY FROM usuarios WHERE CPF= %s AND BDAY = %s"
#     cursor.execute(comando_SQL, (cpf,bday))
#     cpf_bday = cursor.fetchall()

#     result_cpf = str(cpf_bday[0])
#     result_bday = str(cpf_bday[1])
    
#     if cpf == result_cpf and bday == result_bday:
#         print("sucesso")
def buscar_cad():
    # Acessando os valores do CPF e BDAY na interface do usuário
    global login_register, menu
    cpf = login_register.lineEdit_cpf.text()
    bday = login_register.lineEdit_bday.text()

    # Criação do cursor para executar comandos SQL
    cursor = banco.cursor()

    # Comando SQL para buscar o CPF e BDAY no banco de dados
    comando_SQL = "SELECT CPF, BDAY FROM usuarios WHERE CPF = %s AND BDAY = %s"
    cursor.execute(comando_SQL, (cpf, bday))

    # Obtendo os resultados da consulta SQL
    cpf_bday = cursor.fetchall()

    # Verificar se o resultado retornado é válido e contém os dados esperados
    if len(cpf_bday) > 0:
        # A consulta retornou pelo menos uma linha, agora extraímos os valores
        result_cpf, result_bday = cpf_bday[0]  # Isso extrai diretamente CPF e BDAY da tupla retornada
        
        # Verificando se o CPF e BDAY fornecidos coincidem com o banco de dados
        if cpf == result_cpf and bday == result_bday:
            print("Sucesso")
        else:
            print("CPF ou data de nascimento incorretos.")
    else:
        print("Nenhum resultado encontrado para o CPF e data de nascimento fornecidos.")



# def reset_password(): #incompleto

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

    # Limpa os campos após o cadastro
    login_register.lineEdit_name.setText("")
    login_register.lineEdit_user.setText("")
    login_register.lineEdit_email.setText("")
    login_register.lineEdit_passwrd.setText("")
    login_register.lineEdit_passwrd_2.setText("")

# Cria a aplicação antes de qualquer operação gráfica
app = QtWidgets.QApplication(sys.argv)

# Defina os ícones (ajuste os caminhos para os seus arquivos PNG)
icon_eye_open = QIcon("Icones/visibility.png")
icon_eye_closed = QIcon("Icones/visibility_off.png")

#===========================( Login/ Cadastro )=============================================
<<<<<<< HEAD
login_register = uic.loadUi(r"C:\Users\11052806\Desktop\HostInn\HOSTIIN\Prototipo HostInn\Telas\TELA_LOGIN_CADASTRO_2.ui")
=======
login_register = uic.loadUi(r"C:\Users\57090816\OneDrive - SENAC PA - EDU\MAIS ATUALIZADO\HOSTIIN-1\Prototipo HostInn\Telas\TELA_LOGIN_CADASTRO_2.ui")
>>>>>>> 6e3cfb38e6dae790bf00259f7b1bb09d2e26bb73
login_register.setWindowTitle("HostInn")
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
# login_register.bttn_reset_password.clicked.connect(reset_password)

# Define os ícones iniciais dos botões de visualização de senha
login_register.bttn_passwrdview.setIcon(icon_eye_closed)
# login_register.bttn_passwrdview_2.setIcon(icon_eye_closed)

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
