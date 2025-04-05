from PyQt6 import uic, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QLineEdit, QMainWindow, QMessageBox
import pymysql
import sys

# Conexão com o banco de dados
banco = pymysql.connect(
    host="localhost",
    user="root",
    passwd="#mortadela1507",
    database="bd_teste2"
)

class EditWindow(QMainWindow):
    def __init__(self, user_data):  # Agora aceita o argumento user_data
        super().__init__()
        uic.loadUi("Telas/tela_editar.ui", self)

        # Inicializa os ícones
        self.icon_eye_open = QIcon("Icones/visibility.png")
        self.icon_eye_closed = QIcon("Icones/visibility_off.png")

        # Configurações de senha
        self.lineEdit_passwrd.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_passwrd_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.passButton_view.setIcon(self.icon_eye_closed)

        # Conecta o botão de visualização de senha
        self.passButton_view.clicked.connect(self.password_view)

        # Chama o método para preencher os dados do usuário
        self.puxar_user(user_data)

    def puxar_user(self, user_data):
        self.stackedWidget.setCurrentIndex(1)
        """Preenche os campos com os dados do usuário selecionado"""
        self.lineEdit_name_2.setText(user_data[1])  # Nome
        self.lineEdit_user.setText(user_data[2])  # Usuário
        self.lineEdit_email_2.setText(user_data[3])  # Email
        self.lineEdit_passwrd.setText(user_data[4])  # Senha
        self.lineEdit_passwrd_2.setText(user_data[4])  # Confirmação de Senha

        # Guarda o ID do usuário para atualizações
        self.user_id = user_data[0]

        # Conecta o botão de salvar à função de atualização
        self.editButton_2.clicked.connect(self.atualizar_user_dados)

    def password_view(self):
        """Alterna o modo de visualização das senhas e troca os ícones."""
        if self.lineEdit_passwrd.echoMode() == QLineEdit.EchoMode.Password:
            self.lineEdit_passwrd.setEchoMode(QLineEdit.EchoMode.Normal)
            self.lineEdit_passwrd_2.setEchoMode(QLineEdit.EchoMode.Normal)
            self.passButton_view.setIcon(self.icon_eye_open)
        else:
            self.lineEdit_passwrd.setEchoMode(QLineEdit.EchoMode.Password)
            self.lineEdit_passwrd_2.setEchoMode(QLineEdit.EchoMode.Password)
            self.passButton_view.setIcon(self.icon_eye_closed)

    def atualizar_user_dados(self):
        """Atualiza os dados do usuário no banco."""
        novo_nome = self.lineEdit_name_2.text()
        novo_usuario = self.lineEdit_user.text()
        novo_email = self.lineEdit_email_2.text()
        novo_senha = self.lineEdit_passwrd.text()
        Conf_novo_senha = self.lineEdit_passwrd_2.text()

        if novo_senha != Conf_novo_senha:
            QMessageBox.warning(self, "Erro", "As senhas não coincidem!")
            return

        cursor = banco.cursor()
        comando_SQL = "UPDATE usuarios SET nome=%s, usuario=%s, email=%s, senha=%s WHERE ID_Usuario=%s"
        cursor.execute(comando_SQL, (novo_nome, novo_usuario, novo_email, novo_senha, self.user_id))
        banco.commit()

        QMessageBox.information(self, "Sucesso", "Dados atualizados com sucesso!")
        self.close()  # Fecha a tela após a edição

    def puxar_cliente(self, user_data):
        self.stackedWidget.setCurrentIndex(0)
        """Preenche os campos com os dados do usuário selecionado"""
        self.lineEdit_name.setText(user_data[1])  # Nome
        self.lineEdit_cpf.setText(user_data[2])  # Usuário
        self.lineEdit_email.setText(user_data[3])  # Email
        self.lineEdit_phone.setText(user_data[4])  # Telefone
        self.lineEdit_endereco.setText(user_data[5])  # Endereço

        # Guarda o ID do usuário para atualizações
        self.user_id = user_data[0]

        # Conecta o botão de salvar à função de atualização
        self.editButton.clicked.connect(self.atualizar_user_dados)

    def atualizar_user_dados(self):
        """Atualiza os dados do usuário no banco."""
        novo_nome = self.lineEdit_name_2.text()
        novo_usuario = self.lineEdit_user.text()
        novo_email = self.lineEdit_email_2.text()
        novo_senha = self.lineEdit_passwrd.text()
        Conf_novo_senha = self.lineEdit_passwrd_2.text()

        if novo_senha != Conf_novo_senha:
            QMessageBox.warning(self, "Erro", "As senhas não coincidem!")
            return

        cursor = banco.cursor()
        comando_SQL = "UPDATE usuarios SET nome=%s, usuario=%s, email=%s, senha=%s WHERE ID_Usuario=%s"
        cursor.execute(comando_SQL, (novo_nome, novo_usuario, novo_email, novo_senha, self.user_id))
        banco.commit()

        QMessageBox.information(self, "Sucesso", "Dados atualizados com sucesso!")
        self.close()  # Fecha a tela após a edição