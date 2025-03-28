from PyQt6 import uic, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QLineEdit, QMessageBox, QMainWindow, QPushButton, QGridLayout, QDialog
import sys, pymysql, Tela_edicao, chatbot

banco = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="bd_teste2"
)

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        # Carregar a interface gráfica
        uic.loadUi("Telas/tela_menu_principal.ui", self)
        icon_eye_closed = QIcon("Icones/visibility_off.png")
        self.setWindowTitle("HostInn")
        self.setFixedSize(801, 652)
        

        # Configuração inicial dos widgets
        self.lineEdit_passwrd.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_passwrd_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.stackedMenu.setCurrentIndex(0)
        self.stackedWidget.hide()
        self.stackedWidget_2.hide()
        self.frame.hide()

        self.passButton_view.setIcon(icon_eye_closed)
        # Conectando eventos
        self.comboBox_numero.currentIndexChanged.connect(self.atualizar_tipo)
        self.comboBox_tipo.currentIndexChanged.connect(self.atualizar_valor_quarto)
        self.dateEdit_checkin.dateChanged.connect(self.calcular_total)
        self.dateEdit_checkout.dateChanged.connect(self.calcular_total)
        self.lineEdit_valor.textChanged.connect(self.calcular_total)

        # Carregando os quartos disponíveis na comboBox
        self.carregar_quartos()

        # ===========================( Conexões de Botões )=============================================
        # Menu principal
        self.bttn_user.clicked.connect(self.user_menu)
        self.bttn_newUser.clicked.connect(self.new_user)
        self.passButton_view.clicked.connect(self.password_view)
        self.Button_cadstr_2.clicked.connect(self.cadstr_user)
        self.bttn_listUser.clicked.connect(self.list_user)
        self.dellButton_2.clicked.connect(self.deletar_user)
        self.editButton_3.clicked.connect(self.editar_user)

        self.bttn_client.clicked.connect(self.client_menu)
        self.bttn_newClient.clicked.connect(self.new_client)
        self.Button_cadstr.clicked.connect(self.cadstr_clientes)
        self.bttn_listClient.clicked.connect(self.list_client)
        self.dellButton.clicked.connect(self.deletar_clientes)
        self.editButton.clicked.connect(self.editar_clientes)

        self.bttn_reserva.clicked.connect(self.reserva_menu)
        self.bttn_close.clicked.connect(self.close_reserva)
        self.pushButton_buscar.clicked.connect(self.filtrar_clientes)
        self.bttn_confirm.clicked.connect(self.Reservar_cliente)


        self.bttn_financial.clicked.connect(self.financial_menu)
        self.bttn_movements.clicked.connect(self.movements_subMenu)
        self.bttn_newPayment.clicked.connect(self.new_payment)
        self.bttn_validate.clicked.connect(self.validate_payment)
        self.bttn_voltar.clicked.connect(self.back_confirmation)

        self.bttn_report.clicked.connect(self.report_subMenu)
        self.bttn_dashBoard.clicked.connect(self.dashboard)
        self.bttn_cashFlow.clicked.connect(self.financial_list)

        self.bttn_chatbot.clicked.connect(self.chatbot)

        # Botão de voltar
        self.bttn_back.clicked.connect(self.back_main_menu)
        self.bttn_back_2.clicked.connect(self.back_main_menu)
        self.bttn_back_3.clicked.connect(self.back_main_menu)
        self.btn_voltar.clicked.connect(self.back_main_menu)

        self.btn_voltar_2.clicked.connect(self.back_roomlist_menu)

        self.bttn_rooms.clicked.connect(self.room_menu)
        self.btn_novo_quarto.clicked.connect(self.new_room)
        self.btn_listar_quartos.clicked.connect(self.menu_list_room)
        self.btn_tabelaq.clicked.connect(self.menu_list_all_room)
        self.btn_cadastrar_quarto.clicked.connect(self.cadastar_novo_quarto)
        
        self.btn_disponiveis.clicked.connect(self.listar_quartos_disponivel)
        self.btn_ocupados.clicked.connect(self.listar_quartos_ocupado)
        self.btn_manutencao.clicked.connect(self.listar_quartos_manutencao)

    # ===========================( Funções de Navegação )=============================================
    def user_menu(self):
        self.stackedMenu.setCurrentIndex(2)

    def client_menu(self):
        self.stackedMenu.setCurrentIndex(1)

    def reserva_menu(self):
        self.stackedWidget.setCurrentIndex(7)
        self.stackedWidget.show()

        cursor = banco.cursor()
        cursor.execute("SELECT * FROM clientes")
        dados_lidos = cursor.fetchall()

        # Definir número de linhas e colunas (menos 1 coluna)
        self.tableWidget_6.setRowCount(len(dados_lidos))
        self.tableWidget_6.setColumnCount(5)  # Ajustado para ignorar a primeira coluna

        for i, linha in enumerate(dados_lidos):
            for j, valor in enumerate(linha[1:]):  # Pulando a primeira coluna
                self.tableWidget_6.setItem(i, j, QtWidgets.QTableWidgetItem(str(valor)))


    def close_reserva(self):
        self.stackedWidget.hide()

    def financial_menu(self):
        self.stackedMenu.setCurrentIndex(3)

    def room_menu(self):
        self.stackedMenu.setCurrentIndex(4)

    def back_main_menu(self):
        self.stackedMenu.setCurrentIndex(0)
        self.stackedWidget.hide()
        self.stackedWidget_2.hide()
        self.stackedsubMenu.hide()

    def back_roomlist_menu(self):
        self.stackedWidget.setCurrentIndex(6)
        self.stackedWidget_3.setCurrentIndex(0)

    def menu_list_room(self):
        self.stackedWidget.setCurrentIndex(6)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget.show()

    def menu_list_all_room(self):
        self.stackedMenu.setCurrentIndex(4)
        self.stackedWidget.setCurrentIndex(5)

        cursor = banco.cursor()
        cursor.execute("SELECT * FROM quartos")
        dados_lidos = cursor.fetchall()

        # Definir número de linhas e colunas (menos 1 coluna)
        self.tableWidget_2.setRowCount(len(dados_lidos))
        self.tableWidget_2.setColumnCount(5)  # Ajustado para ignorar a primeira coluna

        for i, linha in enumerate(dados_lidos):
            for j, valor in enumerate(linha[1:]):  # Pulando a primeira coluna
                self.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(valor)))

    # ===========================( Cliente )=============================================
    def new_client(self):
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget.show()

    def cadstr_clientes(self):
        name = self.lineEdit_name.text()
        cpf = self.lineEdit_cpf.text()
        email = self.lineEdit_email.text()
        telefone = self.lineEdit_phone.text()
        endereco = self.lineEdit_endereco.text()

        cursor = banco.cursor()
        comando_SQL = "INSERT INTO clientes (Nome, CPF, Email, Telefone, Endereco) VALUES (%s, %s, %s, %s, %s)"
        dados = (str(name), str(cpf), str(email), str(telefone), str(endereco))
        cursor.execute(comando_SQL, dados)
        banco.commit()
        QMessageBox.warning(self, "Sucesso", "Cadastro realizado com Sucesso!")

        self.lineEdit_name.setText("")
        self.lineEdit_cpf.setText("")
        self.lineEdit_email.setText("")
        self.lineEdit_phone.setText("")
        self.lineEdit_endereco.setText("")

    def list_client(self):
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget.show()

        cursor = banco.cursor()
        cursor.execute("SELECT * FROM clientes")
        dados_lidos = cursor.fetchall()

        # Definir número de linhas e colunas (menos 1 coluna)
        self.tableWidget.setRowCount(len(dados_lidos))
        self.tableWidget.setColumnCount(5)  # Ajustado para ignorar a primeira coluna

        for i, linha in enumerate(dados_lidos):
            for j, valor in enumerate(linha[1:]):  # Pulando a primeira coluna
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(valor)))

    def deletar_clientes(self):
        linha = self.tableWidget.currentRow()
        if linha == -1:
            QMessageBox.warning(self, "Erro", "Selecione um cliente para deletar.")
            return

        cursor = banco.cursor()
        cursor.execute("SELECT ID_Cliente FROM clientes")
        dados_lidos = cursor.fetchall()
        valor_id = dados_lidos[linha][0]
        cursor.execute("DELETE FROM clientes WHERE ID_Cliente = %s", (valor_id,))
        banco.commit()

        self.tableWidget.removeRow(linha)
        QMessageBox.information(self, "Sucesso", "Cliente deletado com sucesso!")

    def editar_clientes(self):
        linha = self.tableWidget.currentRow()
        if linha == -1:
            QMessageBox.warning(self, "Erro", "Selecione um usuário para editar.")
            return

        cursor = banco.cursor()
        cursor.execute("SELECT * FROM clientes")
        dados_lidos = cursor.fetchall()
        user = dados_lidos[linha]

        self.tela_editar = Tela_edicao.EditWindow(user)
        self.tela_editar.show()

    # ===========================( Usuário )=============================================
    def new_user(self):
        self.stackedWidget.setCurrentIndex(3)
        self.stackedWidget.show()

    def cadstr_user(self):
        name = self.lineEdit_name_2.text()
        user = self.lineEdit_user.text()
        email = self.lineEdit_email_2.text()
        passwrd = self.lineEdit_passwrd.text()
        passwrd_conf = self.lineEdit_passwrd_2.text()

        if not name or not user or not email or not passwrd or not passwrd_conf:
            QMessageBox.warning(self, "Erro", "Todos os campos devem ser preenchidos!")
            return

        cursor = banco.cursor()
        comando_SQL = "SELECT usuario FROM usuarios WHERE usuario = %s"
        cursor.execute(comando_SQL, (user,))
        resultado = cursor.fetchone()

        if resultado:
            QMessageBox.warning(self, "Erro", "Usuário já existente!")
            return

        cursor = banco.cursor()
        comando_SQL = "SELECT email FROM usuarios WHERE email = %s"
        cursor.execute(comando_SQL, (email,))
        resultado = cursor.fetchone()

        if resultado:
            QMessageBox.warning(self, "Erro", "E-mail já existente!")
            return

        if passwrd != passwrd_conf:
            QMessageBox.warning(self, "Erro", "As senhas não coincidem!")
            return

        comando_SQL = "INSERT INTO usuarios (nome, usuario, email, senha) VALUES (%s, %s, %s, %s)"
        dados = (str(name), str(user), str(email), str(passwrd))
        cursor.execute(comando_SQL, dados)
        banco.commit()

        QMessageBox.information(self, "Sucesso", "Cadastro realizado com sucesso!")

        self.lineEdit_name_2.setText("")
        self.lineEdit_user.setText("")
        self.lineEdit_email_2.setText("")
        self.lineEdit_passwrd.setText("")
        self.lineEdit_passwrd_confirm.setText("")

    def password_view(self):
        icon_eye_open = QIcon("Icones/visibility.png")
        icon_eye_closed = QIcon("Icones/visibility_off.png")
        """
        Alterna o modo de exibição das senhas e troca os ícones dos botões de visualização.
        """
        # Verifica o modo atual de exibição (Password ou Normal)
        if self.lineEdit_passwrd.echoMode() == QLineEdit.EchoMode.Password:
            # Muda para visualização normal (texto visível)
            self.lineEdit_passwrd.setEchoMode(QLineEdit.EchoMode.Normal)
            self.lineEdit_passwrd_2.setEchoMode(QLineEdit.EchoMode.Normal)
            # Atualiza os ícones para o olho aberto
            self.passButton_view.setIcon(icon_eye_open)
        else:
            # Muda para o modo de senha (texto oculto)
            self.lineEdit_passwrd.setEchoMode(QLineEdit.EchoMode.Password)
            self.lineEdit_passwrd_2.setEchoMode(QLineEdit.EchoMode.Password)
            # Atualiza os ícones para o olho fechado
            self.passButton_view.setIcon(icon_eye_closed)

    def list_user(self):
        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget.show()

        cursor = banco.cursor()
        cursor.execute("SELECT * FROM usuarios")
        dados_lidos = cursor.fetchall()

        # Definir número de linhas e colunas (menos 1 coluna)
        self.tableWidget_5.setRowCount(len(dados_lidos))
        self.tableWidget_5.setColumnCount(5)  # Ajustado para ignorar a primeira coluna

        for i, linha in enumerate(dados_lidos):
            for j, valor in enumerate(linha[1:]):  # Pulando a primeira coluna
                self.tableWidget_5.setItem(i, j, QtWidgets.QTableWidgetItem(str(valor)))

    def deletar_user(self):
        linha = self.tableWidget_5.currentRow()
        if linha == -1:
            QMessageBox.warning(self, "Erro", "Selecione um UsuÃ¡rio para deletar.")
            return
        
        cursor = banco.cursor()
        cursor.execute("SELECT ID_usuario FROM usuarios")
        dados_lidos = cursor.fetchall()
        
        valor_id = dados_lidos[linha][0]
        cursor.execute("DELETE FROM usuarios WHERE ID_usuario = %s", (valor_id,))
        banco.commit()
        
        self.tableWidget_5.removeRow(linha)
        QMessageBox.information(self, "Sucesso", "UsuÃ¡rio deletado com sucesso!")

    def editar_user(self):
        linha = self.tableWidget_5.currentRow()
        if linha == -1:
            QMessageBox.warning(self, "Erro", "Selecione um usuário para editar.")
            return

        cursor = banco.cursor()
        cursor.execute("SELECT * FROM usuarios")
        dados_lidos = cursor.fetchall()
        user = dados_lidos[linha]

        self.tela_editar = Tela_edicao.EditWindow(user)
        self.tela_editar.show()

    def new_room(self):
        self.stackedWidget.setCurrentIndex(6)
        self.stackedWidget_3.setCurrentIndex(1)
        self.stackedWidget.show()

    # ===========================( Reserva )=============================================
    def carregar_quartos(self):
        """Preenche a comboBox com os números dos quartos disponíveis."""
        cursor = banco.cursor()
        cursor.execute("SELECT Numero, Tipo FROM quartos WHERE Status_Quarto = 'Disponível'")
        quartos = cursor.fetchall()

        self.comboBox_numero.clear()
        self.comboBox_tipo.clear()
        self.lineEdit_valor.clear()
        self.lineEdit_total.clear()  # Limpa o total

        self.quartos_dict = {}  # Dicionário para armazenar {numero_quarto: tipo}

        for numero, tipo in quartos:
            self.comboBox_numero.addItem(str(numero))
            self.quartos_dict[str(numero)] = tipo

        if self.comboBox_numero.count() > 0:
            self.atualizar_tipo()

    def atualizar_tipo(self):
        """Atualiza a comboBox de tipo com base no número do quarto selecionado."""
        numero_selecionado = self.comboBox_numero.currentText()
        if numero_selecionado in self.quartos_dict:
            self.comboBox_tipo.clear()
            self.comboBox_tipo.addItem(self.quartos_dict[numero_selecionado])
            self.atualizar_valor_quarto()

    def atualizar_valor_quarto(self):
        """Busca o valor do quarto no banco e exibe no lineEdit."""
        tipo_selecionado = self.comboBox_tipo.currentText()

        if tipo_selecionado:
            cursor = banco.cursor()
            cursor.execute("SELECT Valor_Tipo FROM quartos WHERE Tipo = %s LIMIT 1", (tipo_selecionado,))
            resultado = cursor.fetchone()

            if resultado:
                self.lineEdit_valor.setText(str(resultado[0]))  # Exibe o valor no campo
            else:
                self.lineEdit_valor.clear()

        self.calcular_total()  # Atualiza o total após mudar o valor do quarto

    def calcular_total(self):
        """Calcula a quantidade de dias e multiplica pelo valor do quarto."""
        checkin = self.dateEdit_checkin.date()
        checkout = self.dateEdit_checkout.date()

        if checkin >= checkout:
            self.lineEdit_total.clear()  # Limpa o total se a data for inválida
            return

        dias = checkin.daysTo(checkout)  # Calcula a diferença de dias

        try:
            valor_diaria = float(self.lineEdit_valor.text())  # Pega o valor do quarto
            total = dias * valor_diaria  # Multiplica pelos dias
            self.lineEdit_total.setText(f"{total:.2f}")  # Exibe o total formatado
        except ValueError:
            self.lineEdit_total.clear()  # Limpa se o valor não for válido

    def carregar_clientes(self, filtro_campo=None, filtro_valor=None):
        """Carrega os clientes na tabela, com ou sem filtro."""
        cursor = banco.cursor()

        if filtro_campo and filtro_valor:
            consulta = f"SELECT Nome, CPF, Email, Telefone, Endereco FROM clientes WHERE {filtro_campo} LIKE %s"
            cursor.execute(consulta, (f"%{filtro_valor}%",))  # Busca parcial (LIKE)
        else:
            consulta = "SELECT Nome, CPF, Email, Telefone, Endereco FROM clientes"
            cursor.execute(consulta)

        clientes = cursor.fetchall()

        # Atualizando a QTableWidget
        self.tableWidget_6.setRowCount(0)  # Limpa a tabela antes de preencher

        for row_idx, cliente in enumerate(clientes):
            self.tableWidget_6.insertRow(row_idx)
            for col_idx, dado in enumerate(cliente):
                self.tableWidget_6.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(dado)))

    def filtrar_clientes(self):
        """Filtra os clientes com base na ComboBox e no valor digitado."""
        campo = self.comboBox_filtro.currentText()
        valor = self.lineEdit_filtro.text().strip()

        if valor:
            self.carregar_clientes(campo, valor)
        else:
            self.carregar_clientes()  # Se não há valor, carrega todos os clientes 

    def Reservar_cliente(self):       
        linha = self.tableWidget_6.currentRow()
        if linha == -1:
            QMessageBox.warning(self, "Erro", "Selecione um cliente para editar.")
            return
        
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM clientes")
        dados_lidos = cursor.fetchall()
        
        clientes = dados_lidos[linha]     
        self.lineEdit_name_3.setText(str(clientes[1]))
        self.lineEdit_cpf_2.setText(str(clientes[2]))
        self.lineEdit_email_3.setText(str(clientes[3]))
        self.lineEdit_phone_2.setText(str(clientes[4]))
        self.lineEdit_endereco_2.setText(str(clientes[5]))     

    # ===========================( Financeiro )=============================================
    def movements_subMenu(self):
        self.stackedsubMenu.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(4)
        self.stackedsubMenu.show()
        self.stackedWidget.show()

    def new_payment(self):
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_2.show()

    def validate_payment(self):
        self.stackedWidget_2.setCurrentIndex(1)
        self.stackedWidget_2.show()

    def report_subMenu(self):
        self.stackedsubMenu.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(4)
        self.stackedsubMenu.show()
        self.stackedWidget.show()

    def dashboard(self):
        self.stackedWidget_2.setCurrentIndex(3)
        self.stackedWidget_2.show()

    def financial_list(self):
        self.stackedWidget_2.setCurrentIndex(4)
        self.stackedWidget_2.show()

    def back_confirmation(self):
        self.stackedWidget_2.setCurrentIndex(0)

    # ===========================( Quarto )=============================================
    def cadastar_novo_quarto(self):
        numero_quarto = self.linha_numero_quarto.text()
        tipo_quarto = self.combo_tipo.currentText()
        status = self.combo_stts.currentText()
        preco = self.linha_preco.text()
        capacidade = self.linha_capacidade.text()
        descricao = self.linha_desc.text()

        cursor = banco.cursor()
        comando_SQL = ('INSERT INTO quartos (Numero, Tipo, Status_Quarto, '
                       'Valor_Tipo, Capacidade_Quarto, Descricao) '
                       'VALUES (%s, %s, %s, %s, %s, %s)')
        dados = (int(numero_quarto), str(tipo_quarto), str(status), int(preco), str(capacidade), str(descricao))
        cursor.execute(comando_SQL, dados)
        banco.commit()

        self.linha_numero_quarto.clear()
        self.linha_preco.clear()
        self.linha_capacidade.clear()
        self.linha_desc.clear()

        QMessageBox.information(self, "Sucesso", "Novo quarto registrado com sucesso!")

    # ===========================( Visualização de Quartos Filtrados )=============================================
    def listar_quartos_filtrados(self, filtro_status):
        """Abre uma janela com um grid layout exibindo botões quadrados para os quartos com status filtrado."""
        dialog = QDialog(self)
        dialog.setWindowTitle(f"Quartos {filtro_status}")
        dialog.setFixedSize(400, 300)
        layout = QGridLayout(dialog)
        
        cursor = banco.cursor()
        # Filtra os quartos pelo status
        comando_SQL = "SELECT Numero, Status_Quarto FROM quartos WHERE Status_Quarto = %s"
        cursor.execute(comando_SQL, (filtro_status,))
        quartos = cursor.fetchall()
        
        colunas = 3
        for index, quarto in enumerate(quartos):
            numero = quarto[0]
            # Cria um botão para o quarto filtrado
            btn = QPushButton(str(numero), dialog)
            btn.setFixedSize(90, 80)
            # Define a cor com base no status informado
            if filtro_status.lower() in ['disponível', 'disponivel']:
                cor = 'green'
            elif filtro_status.lower() == 'ocupado':
                cor = 'red'
            elif filtro_status.lower() in ['em manutenção', 'em manutencao']:
                cor = 'rgb(255,174,11)'
            else:
                cor = 'gray'
            btn.setStyleSheet(f"background-color: {cor}; font-weight: bold;")
            
            row = index // colunas
            col = index % colunas
            layout.addWidget(btn, row, col)
        
        dialog.setLayout(layout)
        dialog.exec()

    def listar_quartos_disponivel(self):
        self.listar_quartos_filtrados("Disponível")

    def listar_quartos_ocupado(self):
        self.listar_quartos_filtrados("Ocupado")

    def listar_quartos_manutencao(self):
        self.listar_quartos_filtrados("Em manutenção")

    def chatbot(self):
        global Chatbot
        Chatbot = chatbot.ChatBotWindow()
        Chatbot.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Defina os ícones (ajuste os caminhos para os seus arquivos PNG)
