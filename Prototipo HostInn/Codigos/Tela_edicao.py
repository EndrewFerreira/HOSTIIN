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
        uic.loadUi(r"C:\Users\ferre\Desktop\PI\HOSTIIN\Prototipo HostInn\Telas\Editar.ui", self)

        self.atualizar_callback = atualizar_callback

        # Inicializa os ícones
        self.icon_eye_open = QIcon(r"C:\Users\11054836\Desktop\PI\HOSTIIN\Prototipo HostInn\Icones\visibility.png")
        self.icon_eye_closed = QIcon(r"C:\Users\11054836\Desktop\PI\HOSTIIN\Prototipo HostInn\Icones\visibility_off.png")

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
        self.lineEdit_email_3.setText(user_data[4])      # Email
        self.lineEdit_passwrd.setText(user_data[5])    # Senha
        self.lineEdit_passwrd_2.setText(user_data[5])    # Confirmar senha
        self.combo_permissao_edit.setCurrentText(user_data[6])  # <- Correção aqui

        print("Dados recebidos do usuário:", user_data)

        self.user_id = user_data[0]
        self.editButton_2.clicked.connect(self.atualizar_user_dados)
        self.editButton_2.setFocus()

    

    def atualizar_user_dados(self):
        novo_nome = self.lnedituser_nome.text()
        novo_usuario = self.lineEdit_user.text()
        novo_email = self.lineEdit_email_3.text()
        novo_senha = self.lineEdit_passwrd_2.text()
        conf_novo_senha = self.lineEdit_passwrd.text()
        nova_permissao = self.combo_permissao_edit.currentText()  # <- pega o texto selecionado no comboBox

        if novo_senha != conf_novo_senha:
            QMessageBox.warning(self, "Erro", "As senhas não coincidem!")
            return

        cursor = banco.cursor()
        comando_SQL = """
            UPDATE usuarios
            SET nome=%s, usuario=%s, email=%s, senha=%s, permissao=%s
            WHERE ID_Usuario=%s
        """
        cursor.execute(comando_SQL, (novo_nome, novo_usuario, novo_email, novo_senha, nova_permissao, self.user_id))
        banco.commit()

        QMessageBox.information(self, "Sucesso", "Dados do usuário atualizados com sucesso!")
        if self.atualizar_callback:
            self.atualizar_callback()
            QApplication.processEvents()
        self.close()


    def puxar_cliente(self, user_data):
        self.stackedWidget.setCurrentIndex(0)  # Página de edição de cliente
        self.lineEdit_nome_cliente.setText(user_data[1])
        self.lineEdit_cpf.setText(user_data[2])
        self.linenovoemail.setText(user_data[3])
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

    def puxar_quarto(self, dados_quarto):
        self.stackedWidget.setCurrentIndex(2)  # Página de edição de quartos (ajuste o índice conforme necessário)

        self.line_novonumero.setText(str(dados_quarto[1]))         # Número do quarto
        self.combo_novotipo.setCurrentText(dados_quarto[2])        # Tipo do quarto
        self.combo_novostts.setCurrentText(dados_quarto[3])        # Status (Disponível, Ocupado, etc.)
        self.line_novopreco.setText(str(dados_quarto[4]))          # Valor
        self.line_novacap.setText(dados_quarto[5])                 # Capacidade
        self.line_novadesc.setText(dados_quarto[6])                # Descrição
      

        self.quarto_id = dados_quarto[0]  # Armazena o ID do quarto para atualização

        self.btn_salvar_edit_quarto.clicked.connect(self.atualizar_quarto_dados)
        self.btn_salvar_edit_quarto.setFocus()

    def atualizar_quarto_dados(self):
        numero = self.line_novonumero.text()
        tipo = self.combo_novotipo.currentText()
        status = self.combo_novostts.currentText()
        valor = self.line_novopreco.text()
        capacidade = self.line_novacap.text()
        descricao = self.line_novadesc.text()

        if not all([numero, tipo, status, valor, capacidade]):
            QMessageBox.warning(self, "Erro", "Por favor, preencha todos os campos obrigatórios.")
            return

        try:
            cursor = banco.cursor()
            comando_SQL = """
                UPDATE quartos
                SET Numero=%s, Tipo=%s, Status_Quarto=%s, Valor_Tipo=%s, Capacidade_Quarto=%s, Descricao=%s
                WHERE ID_Quartos=%s
            """
            cursor.execute(comando_SQL, (numero, tipo, status, valor, capacidade, descricao, self.quarto_id))
            banco.commit()

            QMessageBox.information(self, "Sucesso", "Dados do quarto atualizados com sucesso!")

            if self.atualizar_callback:
                print("Chamando atualizar_callback()")
                self.atualizar_callback()
                QApplication.processEvents()  # Atualiza a tela que chamou

            self.close()

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao atualizar dados do quarto: {str(e)}")
