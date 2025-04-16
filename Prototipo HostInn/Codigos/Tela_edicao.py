from PyQt6 import uic, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QLineEdit, QMainWindow, QMessageBox
from PyQt6.QtCore import pyqtSignal
import pymysql
from PyQt6.QtWidgets import QApplication
import sys

# Conexão com o banco de dados
banco = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="bd_teste2"
)

class EditWindow(QMainWindow):
    def __init__(self, atualizar_callback=None):
        super().__init__()
        uic.loadUi(r"C:\Users\11054836\Desktop\PI\HOSTIIN\Prototipo HostInn\Telas\tela_editar.ui", self)

        self.atualizar_callback = atualizar_callback

        # Inicializa os ícones
        self.icon_eye_open = QIcon("Icones/visibility.png")
        self.icon_eye_closed = QIcon("Icones/visibility_off.png")

        # Configurações de senha
        self.lineEdit_passwrd.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_passwrd_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.passButton_view.setIcon(self.icon_eye_closed)

        # Conecta o botão de visualização de senha
        self.passButton_view.clicked.connect(self.password_view)

        # Variável para guardar o tipo de edição (cliente ou usuário)
        self.user_id = None

    def puxar_user(self, user_data):
        self.stackedWidget.setCurrentIndex(1)
        self.lnedituser_nome.setText(user_data[1])     # Nome
        self.lineEdit_user.setText(user_data[2])       # Usuario
        self.lineEdit_email_3.setText(user_data[4])    # Email
        self.lineEdit_passwrd.setText(user_data[5])    # Senha
        self.lineEdit_passwrd_2.setText(user_data[5])  # Confirmar senha
        print("Dados recebidos do usuário:", user_data)

        self.user_id = user_data[0]
        self.editButton_2.clicked.connect(self.atualizar_user_dados)
        self.editButton_2.setFocus()

    def puxar_cliente(self, user_data):
        self.stackedWidget.setCurrentIndex(0)  # Página de edição de cliente
        self.lineEdit_nome_cliente.setText(user_data[1])
        self.lineEdit_cpf.setText(user_data[2])
        self.lineEdit_email_3.setText(user_data[3])
        self.linha_novophone.setText(user_data[4])
        self.lineEdit_endereco.setText(user_data[5])
        self.user_id = user_data[0]

        self.btn_salvar_edit_cliente.clicked.connect(self.atualizar_cliente_dados)
        self.btn_salvar_edit_cliente.setFocus()

    def password_view(self):
        if self.lineEdit_passwrd.echoMode() == QLineEdit.EchoMode.Password:
            self.lineEdit_passwrd.setEchoMode(QLineEdit.EchoMode.Normal)
            self.lineEdit_passwrd_2.setEchoMode(QLineEdit.EchoMode.Normal)
            self.passButton_view.setIcon(self.icon_eye_open)
        else:
            self.lineEdit_passwrd.setEchoMode(QLineEdit.EchoMode.Password)
            self.lineEdit_passwrd_2.setEchoMode(QLineEdit.EchoMode.Password)
            self.passButton_view.setIcon(self.icon_eye_closed)

    def atualizar_user_dados(self):
        novo_nome = self.lnedituser_nome.text()
        novo_usuario = self.lineEdit_user.text()
        novo_email = self.lineEdit_email_3.text()
        novo_senha = self.lineEdit_passwrd.text()
        conf_novo_senha = self.lineEdit_passwrd_2.text()

        if novo_senha != conf_novo_senha:
            QMessageBox.warning(self, "Erro", "As senhas não coincidem!")
            return

        cursor = banco.cursor()
        comando_SQL = "UPDATE usuarios SET nome=%s, usuario=%s, email=%s, senha=%s WHERE ID_Usuario=%s"
        cursor.execute(comando_SQL, (novo_nome, novo_usuario, novo_email, novo_senha, self.user_id))
        banco.commit()

        QMessageBox.information(self, "Sucesso", "Dados do usuário atualizados com sucesso!")
        if self.atualizar_callback:
            self.atualizar_callback()
            QApplication.processEvents()  # Força a atualização da GUI
        self.close()


           
    def atualizar_cliente_dados(self):
        novo_nome = self.lineEdit_nome_cliente.text()
        novo_cpf = self.lineEdit_cpf.text()
        novo_email = self.linenovoemail.text()
        novo_telefone = self.linha_novophone.text()
        novo_endereco = self.lineEdit_endereco.text()

        cursor = banco.cursor()
        comando_SQL = """
            UPDATE clientes
            SET nome=%s, cpf=%s, email=%s, telefone=%s, endereco=%s
            WHERE ID_Cliente=%s
        """
        cursor.execute(comando_SQL, (novo_nome, novo_cpf, novo_email, novo_telefone, novo_endereco, self.user_id))
        banco.commit()

        QMessageBox.information(self, "Sucesso", "Dados do cliente atualizados com sucesso!")

        if self.atualizar_callback:
            self.atualizar_callback()
            QApplication.processEvents()  # Força a atualização da GUI

        self.close()
