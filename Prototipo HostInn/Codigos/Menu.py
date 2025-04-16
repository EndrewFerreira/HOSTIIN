from PyQt6 import uic, QtWidgets
from PyQt6.QtCore import QDate, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QDate
import re
from PyQt6.QtWidgets import QLineEdit, QMessageBox, QMainWindow, QPushButton, QGridLayout, QDialog, QTableWidgetItem
import sys, pymysql, Tela_edicao, chatbot
from PyQt6.QtWidgets import (
    QDialog, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QDateEdit, QGridLayout, QMessageBox
)

banco = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="bd_teste2"
)

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        # self(self)
        # Carregar a interface gráfica
        uic.loadUi(r"C:\Users\11052806\Desktop\HostInn\HOSTIIN\Prototipo HostInn\Telas\tela_menu_principal.ui", self)
        icon_eye_closed = QIcon("Icones/visibility_off.png")
        self.setWindowTitle("HostInn")
        self.setFixedSize(801, 652)

        self.lineEdit_21.textChanged.connect(self.calcular)
        self.comboBox_4.currentTextChanged.connect(self.atualizar_valor_pagamento)
        self.lineEdit_23.textChanged.connect(self.atualizar_valor_pagamento)     

        # Configuração inicial dos widgets
        self.lineEdit_passwrd.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_passwrd_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.stackedMenu.setCurrentIndex(0)
        self.stackedWidget.hide()
        self.stackedWidget_2.hide()
        self.frame.hide()
        self.comboBox_4.currentTextChanged.connect(self.on_tipo_pagamento_changed)
        self.comboBox_5.currentTextChanged.connect(self.calcular_valor_parcela)
        self.lineEdit_23.textChanged.connect(self.calcular_valor_parcela)


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

        ##################### USUÁRIO ###################################
        self.bttn_user.clicked.connect(self.user_menu)
        self.bttn_newUser.clicked.connect(self.new_user)
        self.passButton_view.clicked.connect(self.password_view)
        self.Button_cadstr_2.clicked.connect(self.cadstr_user)
        self.bttn_listUser.clicked.connect(self.list_user)
        self.dellButton_2.clicked.connect(self.deletar_user)
        self.editButton_3.clicked.connect(self.editar_user)
        ##################### CLIENTE ###################################
        self.bttn_client.clicked.connect(self.client_menu)
        self.bttn_newClient.clicked.connect(self.new_client)
        self.Button_cadstr.clicked.connect(self.cadstr_clientes)
        self.bttn_listClient.clicked.connect(self.list_client)
        self.dellButton.clicked.connect(self.deletar_clientes)
        self.editButton.clicked.connect(self.editar_clientes)
        ##################### RESERVA ###################################
        self.bttn_reserva.clicked.connect(self.reserva_menu)
        self.bttn_nova_reserva.clicked.connect(self.nova_reserva)
        self.bttn_listar_reserva.clicked.connect(self.listar_reservas)
        self.bttn_close.clicked.connect(self.close_reserva)
        self.pushButton_buscar.clicked.connect(self.filtrar_clientes)
        self.bttn_confirm.clicked.connect(self.puxar_cliente)
        self.bttn_reservar.clicked.connect(self.reservar)
        self.bttn_listar_reserva.clicked.connect(self.listar_reservas)
        self.btn_cancel.clicked.connect(self.cancelar_reserva)
        self.botao_aplicar_filtro.clicked.connect(self.aplicar_filtro_reservas)
        ####################### FINANCEIRO ##############################
        self.bttn_financial.clicked.connect(self.financial_menu)
        self.bttn_movements.clicked.connect(self.movements_subMenu)
        self.bttn_newPayment.clicked.connect(self.novo_pagamento)
        self.bttn_validate.clicked.connect(self.validate_payment)
        self.bttn_voltar.clicked.connect(self.back_confirmation)
        self.bttn_confirm_2.clicked.connect(self.confirma_busca_financeiro)
        self.bttn_validate.clicked.connect(self.gerar_codigo)
        self.bttn_confirm_3.clicked.connect(self.salvar_pagamento)
        self.bttn_report.clicked.connect(self.report_subMenu)
        self.bttn_dashBoard.clicked.connect(self.dashboard)
        self.bttn_cashFlow.clicked.connect(self.financial_list)

        self.bttn_chatbot.clicked.connect(self.chatbot)

        self.bttn_back.clicked.connect(self.back_main_menu)
        self.bttn_back_2.clicked.connect(self.back_main_menu)
        self.bttn_back_3.clicked.connect(self.back_main_menu)
        self.btn_voltar.clicked.connect(self.back_main_menu)
        self.bttn_voltar_3.clicked.connect(self.back_main_menu)
        ##################### QUARTO ###################################
        self.btn_voltar_2.clicked.connect(self.back_roomlist_menu)
        self.btn_aplicar_filtros.clicked.connect(self.menu_list_all_room)
        self.bttn_rooms.clicked.connect(self.room_menu)
        self.btn_novo_quarto.clicked.connect(self.new_room)
        self.btn_listar_quartos.clicked.connect(self.menu_list_room)
        self.btn_tabelaq.clicked.connect(self.menu_list_all_room)
        self.btn_cadastrar_quarto.clicked.connect(self.cadastar_novo_quarto)
        self.btn_disponiveis.clicked.connect(self.listar_quartos_disponivel)
        self.btn_ocupados.clicked.connect(self.listar_quartos_ocupado)
        self.btn_manutencao.clicked.connect(self.listar_quartos_manutencao)
        self.btn_verifcacaoqt.clicked.connect(self.abrir_janela_verificacao_quartos)
        self.btn_editar_quarto.clicked.connect(self.editar_quarto)


    # ===========================( Funções de Navegação )=============================================
    def user_menu(self):
        self.stackedMenu.setCurrentIndex(2)

    def client_menu(self):
        self.stackedMenu.setCurrentIndex(1)

    def reserva_menu(self):
        self.stackedMenu.setCurrentIndex(5)

    def listar_reservas(self):
        self.stackedWidget.setCurrentIndex(8)
        self.stackedWidget.show()
        cursor = banco.cursor()
        comando_SQL = """
            SELECT
                r.ID_Reserva,
                c.Nome AS Cliente,
                q.Numero AS Numero_Quarto,
                r.Data_Checkin,
                r.Data_Checkout,
                r.Valor_Reserva,
                r.Status_reserva
            FROM reserva r
            JOIN clientes c ON r.ID_Cliente = c.ID_Cliente
            JOIN reserva_quartos rq ON r.ID_Reserva = rq.ID_Reserva
            JOIN quartos q ON rq.ID_Quartos = q.ID_Quartos
        """

        cursor.execute(comando_SQL)
        reservas = cursor.fetchall()

        self.tabela_lista_reserva.setRowCount(0)

        for row_num, row_data in enumerate(reservas):
            self.tabela_lista_reserva.insertRow(row_num)
            for col_num, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.tabela_lista_reserva.setItem(row_num, col_num, item)

    def nova_reserva(self):
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

        self.dateEdit_checkin.setDate(QDate.currentDate())
        self.dateEdit_checkout.setDate(QDate.currentDate())


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
    def new_room(self):
        self.stackedWidget.setCurrentIndex(6)
        self.stackedWidget_3.setCurrentIndex(1)
        self.stackedWidget.show()

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

        # Capturando os valores dos filtros
        numero_quarto = self.line_filtro_numero.text()  # Número do quarto
        tipo_quarto = self.combo_filtro_tipo.currentText()  # Tipo de quarto
        status_quarto = self.combo_filtro_stts.currentText()  # Status do quarto

        # Construindo a query dinâmica
        query = "SELECT * FROM quartos WHERE 1=1"  # 'WHERE 1=1' serve como base para adicionar condições

        # Aplicando o filtro de número de quarto
        if numero_quarto:
            query += f" AND numero LIKE '%{numero_quarto}%'"

        # Aplicando o filtro de tipo de quarto
        if tipo_quarto and tipo_quarto != "Todos":  # Adicione "Todos" como opção no ComboBox
            query += f" AND tipo = '{tipo_quarto}'"

        # Aplicando o filtro de status do quarto
        if status_quarto and status_quarto != "Todos":  # Adicione "Todos" como opção no ComboBox
            query += f" AND Status_quarto = '{status_quarto}'"

        # Executando a query com os filtros aplicados
        cursor = banco.cursor()
        cursor.execute(query)
        dados_lidos = cursor.fetchall()

        # Definir número de linhas e colunas (menos 1 coluna)
        self.tableWidget_2.setRowCount(len(dados_lidos))
        self.tableWidget_2.setColumnCount(5)  # Ajustado para ignorar a primeira coluna

        # Preenchendo a tabela com os dados filtrados
        for i, linha in enumerate(dados_lidos):
            dados_formatados = [
        linha[1],  # Numero
        linha[2],  # Tipo
        linha[4],  # Status_Quarto (vem antes de Valor_Tipo na interface, por isso foi ajustado)
        linha[3],  # Valor_Tipo
        linha[5],  # Capacidade
        linha[6]   # Descrição
    ]
            for j, valor in enumerate(dados_formatados):  # Pulando a primeira coluna
                self.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(valor)))

    # ===========================( CLIENTE )=============================================
    def new_client(self):
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget.show()
        self.lineEdit_cpf.setInputMask("000.000.000-00;_")
        self.lineEdit_phone.setInputMask("(00) 0 0000-0000;_")



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
        self.stackedWidget.setCurrentIndex(0)  # ou o índice correto da tela de clientes
        self.stackedWidget.show()
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM clientes")
        dados_lidos = cursor.fetchall()
        self.tableWidget.clearContents()  # Limpa os dados antigos
        print("⚡ Atualizando tabela de clientes!")

        self.tableWidget.setRowCount(len(dados_lidos))
        self.tableWidget.setColumnCount(5)  # Ajustado para ignorar a primeira coluna

        for i, linha in enumerate(dados_lidos):
            for j, valor in enumerate(linha[1:]):  # Pulando o ID
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(valor)))
        self.tableWidget.repaint()  # Força um repaint da tabela



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
            QMessageBox.warning(self, "Erro", "Selecione um cliente para editar.")
            return

        cursor = banco.cursor()
        cursor.execute("SELECT * FROM clientes")
        dados_lidos = cursor.fetchall()
        cliente = dados_lidos[linha]

        # Passando a função de atualização como callback
        self.tela_editar = Tela_edicao.EditWindow(atualizar_callback=self.list_client)
        self.tela_editar.puxar_cliente(cliente)
        self.tela_editar.show()



    # ===========================( USUÁRIO )=============================================
    def new_user(self):
        self.stackedWidget.setCurrentIndex(3)
        self.stackedWidget.show()
        self.lineEdit_cpf.setInputMask("000.000.000-00;_")


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

        self.tela_editar = Tela_edicao.EditWindow()         # <- sem passar user
        self.tela_editar.puxar_user(user)                   # <- passa aqui
        self.tela_editar.show()


   

    # ===========================( RESERVA )=============================================   
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

    def puxar_cliente(self):       
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

    def reservar(self):
        nome = self.lineEdit_name_3.text()
        cpf = self.lineEdit_cpf_2.text()
        email = self.lineEdit_email_3.text()
        phone = self.lineEdit_phone_2.text()
        endereco = self.lineEdit_endereco_2.text()
        numero_quarto = self.comboBox_numero.currentText()
        print("Número do quarto digitado:", numero_quarto)

        if not nome or not cpf or not email or not phone or not endereco or not numero_quarto:
            QMessageBox.warning(self, "Erro", "Todos os campos devem ser preenchidos!")
            return

        cursor = banco.cursor()
        comando_SQL = "SELECT id_cliente FROM clientes WHERE nome = %s AND cpf = %s"
        cursor.execute(comando_SQL, (nome, cpf,))
        resultado = cursor.fetchone()
        if not resultado:
            QMessageBox.warning(self, "Erro", "Cliente não encontrado!")
            return

        id_cliente = resultado[0]

        data_atual = QDate.currentDate()
        checkin = self.dateEdit_checkin.date().toString("yyyy-MM-dd")
        checkout = self.dateEdit_checkout.date().toString("yyyy-MM-dd")

        if checkin < data_atual.toString("yyyy-MM-dd") or checkout < data_atual.toString("yyyy-MM-dd"):
            QMessageBox.warning(self, "Erro", "Selecione uma data válida!")
            return

        valor_reserva = self.lineEdit_total.text()
        status = "Reservado"

        if not checkin or not checkout:
            QMessageBox.warning(self, "Erro", "Selecione um período de estadia!")
            return

        # Inserir a reserva
        comando_SQL = """
            INSERT INTO reserva (Data_Checkin, Data_Checkout, Valor_Reserva, Status_reserva, ID_Cliente)
            VALUES (%s, %s, %s, %s, %s)
        """
        dados = (checkin, checkout, valor_reserva, status, id_cliente)
        cursor.execute(comando_SQL, dados)

        cursor = banco.cursor()
        comando_SQL_2 = "SELECT ID_RESERVA FROM reserva WHERE ID_CLIENTE = %s AND DATA_CHECKIN = %s AND DATA_CHECKOUT = %s"
        cursor.execute(comando_SQL_2, (id_cliente, checkin, checkout))
        resultado2 = cursor.fetchone()

        id_reserva = resultado2[0]

        cursor = banco.cursor()
        comando_SQL_3 = "SELECT id_quartos FROM quartos WHERE numero = %s"
        cursor.execute(comando_SQL_3, (numero_quarto))
        resultado3 = cursor.fetchone()

        id_quarto = resultado3[0]

        dados2 =  (id_reserva,id_quarto)
        comando_SQL_4 = "INSERT INTO reserva_quartos (ID_Reserva, ID_Quartos) VALUES (%s,%s)"
        cursor.execute(comando_SQL_4,(dados2))

       
        comando_UPDATE_quarto = "UPDATE quartos SET Status_Quarto = %s WHERE Numero = %s"
        cursor.execute(comando_UPDATE_quarto, ("Ocupado", numero_quarto))

        banco.commit()
        QMessageBox.information(self, "Sucesso", "Reserva realizada com sucesso!")

    def cancelar_reserva(self):
        linha_selecionada = self.tabela_lista_reserva.currentRow()

        if linha_selecionada == -1:
            QMessageBox.warning(self, "Aviso", "Selecione uma reserva para cancelar.")
            return

        id_reserva_item = self.tabela_lista_reserva.item(linha_selecionada, 0)
        numero_quarto_item = self.tabela_lista_reserva.item(linha_selecionada, 2)

        if not id_reserva_item or not numero_quarto_item:
            QMessageBox.warning(self, "Erro", "Não foi possível obter os dados da reserva.")
            return

        id_reserva = id_reserva_item.text()
        numero_quarto = numero_quarto_item.text()

        resposta = QMessageBox.question(
            self,
            "Confirmação",
            "Tem certeza que deseja cancelar esta reserva?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if resposta == QMessageBox.StandardButton.Yes:
            # continua aqui...

            cursor = banco.cursor()

            # Atualiza status da reserva
            comando_update_reserva = "UPDATE reserva SET Status_reserva = %s WHERE ID_Reserva = %s"
            cursor.execute(comando_update_reserva, ("cancelado", id_reserva))

            # Atualiza status do quarto para "Disponível"
            comando_update_quarto = "UPDATE quartos SET Status_Quarto = %s WHERE Numero = %s"
            cursor.execute(comando_update_quarto, ("Disponível", numero_quarto))

            banco.commit()

            QMessageBox.information(self, "Sucesso", "Reserva cancelada com sucesso!")
            self.listar_reservas()  # Atualiza a tabela após cancelamento
            
    def aplicar_filtro_reservas(self):
        texto_busca = self.lineEdit_busca.text().strip().lower()
        filtro_selecionado = self.comboBox_filtro_2.currentText().strip().lower()

        # Mapeia os nomes do ComboBox exatamente como estão no Qt Designer
        filtros_map = {
            "id": "id",
            "cliente": "cliente",
            "quarto": "quarto",
            "check-in": "check-in",
            "check-out": "check-out",
            "valor": "valor",
            "status": "status"
        }

        filtro = filtros_map.get(filtro_selecionado)

        if not filtro:
            QMessageBox.warning(self, "Erro", f"Filtro '{filtro_selecionado}' inválido ou não encontrado.")
            return

        # Descobrir a coluna correspondente
        coluna_alvo = None
        for j in range(self.tabela_lista_reserva.columnCount()):
            header = self.tabela_lista_reserva.horizontalHeaderItem(j).text().strip().lower()
            if header == filtro:
                coluna_alvo = j
                break

        if coluna_alvo is None:
            QMessageBox.warning(self, "Erro", f"Coluna para filtro '{filtro_selecionado}' não encontrada.")
            return

        # Aplicar filtro nas linhas
        for i in range(self.tabela_lista_reserva.rowCount()):
            item = self.tabela_lista_reserva.item(i, coluna_alvo)
            if item and texto_busca in item.text().strip().lower():
                self.tabela_lista_reserva.setRowHidden(i, False)
            else:
                self.tabela_lista_reserva.setRowHidden(i, True)


    # ===========================( FINANCEIRO )=============================================
    def movements_subMenu(self):
        self.stackedsubMenu.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(4)
        self.stackedsubMenu.show()
        self.stackedWidget.show()

    def novo_pagamento(self):
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_2.show()

        cursor = banco.cursor()

        query = """
        SELECT 
            c.nome, 
            c.cpf, 
            r.data_checkin, 
            r.data_checkout, 
            r.valor_reserva, 
            r.status_reserva
        FROM reserva r
        JOIN clientes c ON r.id_cliente = c.id_cliente
        """

        cursor.execute(query)
        resultados = cursor.fetchall()

        colunas = ["Nome", "CPF", "Check-in", "Check-out", "Valor", "Status"]
        self.tableWidget_4.setRowCount(len(resultados))
        self.tableWidget_4.setColumnCount(len(colunas))
        self.tableWidget_4.setHorizontalHeaderLabels(colunas)

        for linha, dados in enumerate(resultados):
            for coluna, valor in enumerate(dados):
                item = QTableWidgetItem(str(valor))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.tableWidget_4.setItem(linha, coluna, item)

    def confirma_busca_financeiro(self):
        linha = self.tableWidget_4.currentRow()
        if linha == -1:
            QMessageBox.warning(self, "Erro", "Selecione uma reserva.")
            return
        
        # Pegando o nome do cliente da tabela
        nome_cliente = self.tableWidget_4.item(linha, 0).text()  # Coluna 0 -> Nome do Cliente

        cursor = banco.cursor()
        
        # Buscar dados do cliente
        cursor.execute("SELECT * FROM clientes WHERE nome = %s", (nome_cliente,))
        dados_cliente = cursor.fetchone()

        if not dados_cliente:
            QMessageBox.warning(self, "Erro", "Cliente não encontrado no banco de dados.")
            return

        # Preencher os campos do cliente
        self.lineEdit_9.setText(str(dados_cliente[1]))  # Nome
        self.lineEdit_10.setText(str(dados_cliente[2])) # CPF
        self.lineEdit_11.setText(str(dados_cliente[3])) # Telefone
        self.lineEdit_12.setText(str(dados_cliente[4])) # Email
        self.lineEdit_13.setText(str(dados_cliente[5])) # Endereço

        # Buscar dados da reserva vinculada ao cliente
        cursor.execute("""
            SELECT 
                r.data_checkin, 
                r.data_checkout, 
                r.valor_reserva, 
                r.status_reserva,
                q.numero,
                q.tipo
            FROM reserva r
            JOIN reserva_quartos rq ON r.id_reserva = rq.id_reserva
            JOIN quartos q ON rq.id_quartos = q.id_quartos
            WHERE r.id_cliente = %s
        """, (dados_cliente[0],))  # dados_cliente[0] deve ser o ID do cliente

        dados_reserva = cursor.fetchone()

        if dados_reserva:
            # Preencher os campos da reserva
            self.dateEdit.setDate(QDate.fromString(str(dados_reserva[0]), "yyyy-MM-dd")) # Checkin
            self.dateEdit_2.setDate(QDate.fromString(str(dados_reserva[1]), "yyyy-MM-dd")) # Checkout
            self.lineEdit_23.setText(f"{dados_reserva[2]:.2f}")
            self.lineEdit_14.setText(str(dados_reserva[5]))
            self.lineEdit_15.setText(str(dados_reserva[4]))
        else:
            QMessageBox.warning(self, "Erro", "Nenhuma reserva encontrada para este cliente.")

    def validate_payment(self):
        name = self.lineEdit_9.text().strip()      # Nome
        cpf = self.lineEdit_10.text().strip()      # CPF
        phone = self.lineEdit_11.text().strip()    # Telefone
        email = self.lineEdit_12.text().strip()    # Email
        endereco = self.lineEdit_13.text().strip() # Endereço

        checkin = self.dateEdit.date()
        checkout = self.dateEdit_2.date()

        self.dateEdit_3.setDate(QDate.currentDate())
        self.dateEdit_4.setDate(QDate.currentDate())

        # Validação de campos vazios
        if not name or not cpf or not email or not phone or not endereco:
            QMessageBox.warning(self, "Erro", "Todos os campos devem ser preenchidos!")
            return

        # Validação de data (ex: check-out não pode ser antes do check-in)
        if checkout <= checkin:
            QMessageBox.warning(self, "Erro", "A data de check-out deve ser após a data de check-in!")
            return

        # Se tudo estiver certo, prossegue
        self.stackedWidget_2.setCurrentIndex(1)
        self.stackedWidget_2.show()
        # self.formatar_valor(self.lineEdit_24)
        self.formatar_valor(self.lineEdit_23)
        self.formatar_valor(self.lineEdit_21)
        self.formatar_valor(self.lineEdit_20)
       

    def calcular_valor_parcela(self):
        try:
            parcelas_texto = self.comboBox_5.currentText().replace("x", "").strip()
            if not parcelas_texto.isdigit():
                raise ValueError("Parcela inválida")

            num_parcelas = int(parcelas_texto)
            total_texto = self.lineEdit_23.text().strip()

            if not total_texto:
                return  # Se estiver vazio, não tenta calcular

            # Remove "R$", espaços, pontos de milhar e troca vírgula por ponto
            total_texto = total_texto.replace("R$", "").replace(".", "").replace(",", ".").strip()

            total = float(total_texto)

            if total > 0 and num_parcelas > 0:
                valor_individual = total / num_parcelas
                self.lineEdit_24.setText(f"{valor_individual:.2f}")
            else:
                self.lineEdit_24.clear()
        except ValueError:
            self.lineEdit_24.clear()
        
        self.on_tipo_pagamento_changed()
        self.atualizar_valor_pagamento()


    def calcular(self):
        texto1 = self.lineEdit_21.text()
        texto2 = self.lineEdit_23.text()

        try:
            # Limpeza dos textos (remove R$, espaços, pontos e vírgulas)
            valor1 = float(texto1.replace("R$", "").replace(".", "").replace(",", ".").strip() or 0)
            valor2 = float(texto2.replace("R$", "").replace(".", "").replace(",", ".").strip() or 0)

            resultado = valor1 - valor2

            # Formata o resultado no estilo brasileiro
            resultado_formatado = f"R$ {resultado:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            self.lineEdit_20.setText(f"Resultado: {resultado_formatado}")
        except ValueError:
            self.lineEdit_20.setText("Resultado: erro de valor")    


    def on_tipo_pagamento_changed(self):
        tipo_pagamento = self.comboBox_4.currentText().strip().lower()

        # Combobox de parcelas
        if tipo_pagamento in ["dinheiro", "débito", "pix"]:
            self.comboBox_5.setCurrentText("1x")
            self.comboBox_5.setEnabled(False)
        else:
            self.comboBox_5.setEnabled(True)

        # Campos NSU e ID Transação
        if tipo_pagamento in ["crédito", "débito"]:
            self.lineEdit_nsu.setEnabled(True)
            self.lineEdit_id_trans.setEnabled(False)
        else:
            self.lineEdit_nsu.setEnabled(False)
            self.lineEdit_id_trans.setEnabled(False)

        # Campo lineEdit_21 (algo relacionado a PIX talvez?)
        if tipo_pagamento in ["crédito", "débito", "pix"]:
            self.lineEdit_21.setEnabled(False)
        else:
            self.lineEdit_21.setEnabled(True)

        # Campo de data
        if tipo_pagamento in ["crédito", "débito", "dinheiro"]:
            self.dateEdit_4.setEnabled(False)
        else:
            self.dateEdit_4.setEnabled(True)

        
    def formatar_valor(self, line_edit: QLineEdit):
        texto = line_edit.text().replace("R$", "").replace(",", ".").strip()
        try:
            valor = float(texto)
            texto_formatado = f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            line_edit.setText(texto_formatado)
        except ValueError:
            pass

    def atualizar_valor_pagamento(self):
        tipo_pagamento = self.comboBox_4.currentText().strip().lower()

        print("Tipo:", tipo_pagamento)
        print("Valor original:", self.lineEdit_23.text())

        if tipo_pagamento == "":
            print("ComboBox ainda vazia, não atualizando.")
            return

        if tipo_pagamento in ["pix", "crédito", "débito"]:
            texto = self.lineEdit_23.text()

            try:
                valor = float(
                    texto.replace("R$", "")
                        .replace(".", "")
                        .replace(",", ".")
                        .strip()
                )

                valor_formatado = f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
                print("Valor formatado:", valor_formatado)

                self.lineEdit_21.setText(valor_formatado)
            except ValueError:
                print("Erro ao converter valor")
                self.lineEdit_21.setText("Deu pau")
        else:
            print("Tipo de pagamento diferente, limpando valor.")
            self.lineEdit_21.clear()

    def gerar_codigo_unico(self, tabela, coluna):
        import random
        import string
        global banco

        def gerar_codigo_formatado():
            return ''.join(random.choices(string.digits, k=8))

        try:
            with banco.cursor() as cursor:
                while True:
                    codigo = gerar_codigo_formatado()
                    consulta = f"SELECT COUNT(*) FROM {tabela} WHERE {coluna} = %s"
                    cursor.execute(consulta, (codigo,))
                    resultado = cursor.fetchone()

                    if resultado[0] == 0:
                        return codigo
        except Exception as e:
            self.mostrar_erro(f"Erro ao gerar código único: {e}")
            return None
                
    def gerar_codigo(self):
        codigo = self.gerar_codigo_unico('financeiro', 'ID_Pagamento')
        self.lineEdit_18.setText(codigo)

    def salvar_pagamento(self):
        global banco

        id_pagamento = self.lineEdit_18.text()
        data = self.dateEdit_3.date().toString("yyyy-MM-dd")
        quant_parcelas = self.comboBox_5.currentText()
        tipo_pagamento = self.comboBox_4.currentText()
        bandeira_cart = self.comboBox_6.currentText()
        status = "Pago"
        cliente = self.lineEdit_9.text()
        checkin = self.dateEdit.date().toString("yyyy-MM-dd")
        checkout = self.dateEdit_2.date().toString("yyyy-MM-dd")


        # Buscar dados do cliente
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM clientes WHERE nome = %s", (cliente,))
        dados_cliente = cursor.fetchone()

        id_cliente = dados_cliente[0] if dados_cliente else None

        # Buscar dados da reserva
        cursor = banco.cursor()
        cursor.execute(
            "SELECT * FROM reserva WHERE Data_Checkin = %s AND Data_Checkout = %s",
            (checkin, checkout)
        )
        dados_reserva = cursor.fetchone()

        id_reserva = dados_reserva[0] if dados_reserva else None


        tipo = tipo_pagamento.lower()

        # Código do pagamento (NSU ou ID transação)
        if tipo in ["débito", "debito", "crédito", "credito"]:
            codigo_pagamento = self.lineEdit_nsu.text()
            if not codigo_pagamento:
                self.mostrar_erro("Por favor, preencha o NSU para pagamento com débito/crédito.")
                return
        elif tipo == "pix":
            codigo_pagamento = self.lineEdit_id_transacao.text()
            if not codigo_pagamento:
                self.mostrar_erro("Por favor, preencha o ID da transação para pagamento via Pix.")
                return
        else:
            codigo_pagamento = ""

        # Valores
        recebido_texto = self.lineEdit_21.text()
        devolvido_texto = self.lineEdit_20.text()

        # Se for dinheiro, os valores devem ser obrigatórios
        if tipo == "dinheiro":
            if not id_pagamento or not recebido_texto or not devolvido_texto or not tipo_pagamento:
                self.mostrar_erro("Todos os campos obrigatórios devem ser preenchidos!")
                return

        # Tenta remover a formatação
        try:
            recebido_valor = self.remover_formatacao_moeda(recebido_texto)
            devolvido_valor = self.remover_formatacao_moeda(devolvido_texto)
        except Exception as e:
            self.mostrar_erro(f"Erro ao formatar valores: {e}")
            return

        print(f"Recebido: {recebido_valor}, Devolvido: {devolvido_valor}")  # DEBUG

        try:
            with banco.cursor() as cursor:
                sql = """
                    INSERT INTO financeiro (
                        ID_Pagamento,
                        Data_Pagamento,
                        Valor_Recebido,
                        Valor_Devolvido,
                        Tipo_Pagamento,
                        Quant_parcelas,
                        Bandeira_Cartao,
                        codigo_pagamento,
                        Status_Pagamento,
                        ID_Cliente,
                        ID_Reserva
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                valores = (
                    id_pagamento,
                    data,
                    recebido_valor,
                    devolvido_valor,
                    tipo_pagamento,
                    quant_parcelas,
                    bandeira_cart,
                    codigo_pagamento,
                    status,
                    id_cliente,
                    id_reserva
                )
                cursor.execute(sql, valores)
                banco.commit()
                self.mostrar_sucesso("Pagamento salvo com sucesso!")
        except Exception as e:
            self.mostrar_erro(f"Erro ao salvar no banco: {e}")


    def remover_formatacao_moeda(self, valor):
        if not valor:
            return 0.0

        print(f"Valor original: {valor}")  # debug

        # Encontra o primeiro padrão de número monetário na string (ex: R$ 1.500,50 ou 1500,50)
        match = re.search(r'[\d\.,]+', valor)
        if not match:
            return 0.0

        numero_str = match.group(0)

        # Remove separador de milhar (.) e troca vírgula por ponto
        numero_str = numero_str.replace(".", "").replace(",", ".")

        print(f"Valor formatado: {numero_str}")  # debug

        try:
            return float(numero_str)
        except ValueError:
            return 0.0

    # Exibe mensagens de erro
    def mostrar_erro(self, mensagem):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Erro")
        msg.setText(mensagem)
        msg.exec()

    # Exibe mensagens de sucesso
    def mostrar_sucesso(self, mensagem):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Sucesso")
        msg.setText(mensagem)
        msg.exec()


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

    # ===========================( QUARTO )=============================================
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
        self.carregar_quartos()  # ← atualiza a comboBox com os quartos disponíveis
        # self.stackedWidget.setCurrentIndex(7)  # ← vai para a tela de reserva (troque o número se for diferente)


    #                        Visualização de Quartos Filtrados
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

    def abrir_janela_verificacao_quartos(self):
        dialog = QDialog()
        dialog.setWindowTitle("Verificar Disponibilidade dos Quartos")
        dialog.setFixedSize(500, 450)

        checkin = QDateEdit()
        checkin.setCalendarPopup(True)
        checkin.setDate(QDate.currentDate())

        checkout = QDateEdit()
        checkout.setCalendarPopup(True)
        checkout.setDate(QDate.currentDate().addDays(1))

        btn_verificar = QPushButton("Verificar")

        layout_datas = QHBoxLayout()
        layout_datas.addWidget(QLabel("Check-in:"))
        layout_datas.addWidget(checkin)
        layout_datas.addWidget(QLabel("Check-out:"))
        layout_datas.addWidget(checkout)

        layout_quartos = QGridLayout()
        botoes_quartos = []

        # Buscar quartos do banco
        cursor = banco.cursor()
        cursor.execute("SELECT ID_Quartos, Numero FROM quartos")
        quartos = cursor.fetchall()  # Ex: [(1, 101), (2, 102), ...]

        for i, (id_quarto, numero) in enumerate(quartos):
            btn = QPushButton(f"Quarto {numero}")
            btn.setFixedSize(100, 50)
            botoes_quartos.append((btn, id_quarto))
            row = i // 4
            col = i % 4
            layout_quartos.addWidget(btn, row, col)

        layout_principal = QVBoxLayout()
        layout_principal.addLayout(layout_datas)
        layout_principal.addWidget(btn_verificar)
        layout_principal.addLayout(layout_quartos)

        dialog.setLayout(layout_principal)

        def verificar():
            data_checkin = checkin.date().toString("yyyy-MM-dd")
            data_checkout = checkout.date().toString("yyyy-MM-dd")

            if checkin.date() >= checkout.date():
                QMessageBox.warning(dialog, "Erro", "Check-out deve ser após o check-in.")
                return

            for btn, id_quarto in botoes_quartos:
                comando = """
                    SELECT 1 FROM reserva r
                    JOIN reserva_quartos rq ON r.ID_Reserva = rq.ID_Reserva
                    WHERE rq.ID_Quartos = %s
                    AND r.Data_Checkin < %s AND r.Data_Checkout > %s
                """
                cursor.execute(comando, (id_quarto, data_checkout, data_checkin))
                resultado = cursor.fetchone()

                if resultado:
                    btn.setStyleSheet("background-color: red; color: white;")
                else:
                    btn.setStyleSheet("background-color: green; color: white;")

        btn_verificar.clicked.connect(verificar)
        dialog.exec()
    
    def editar_quarto(self):
        linha = self.tableWidget_2.currentRow()
        if linha == -1:
            QMessageBox.warning(self, "Erro", "Selecione um quarto para editar.")
            return

        cursor = banco.cursor()
        cursor.execute("SELECT * FROM quartos")
        dados = cursor.fetchall()
        quarto = dados[linha]

        self.tela_editar = Tela_edicao.EditWindow(atualizar_callback=self.menu_list_all_room)
        self.tela_editar.puxar_quarto(quarto)
        self.tela_editar.show()






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  
    window = MainMenu()  
    window.show() 
    sys.exit(app.exec())  


   
