import sys
import mysql.connector
import re
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton,
    QVBoxLayout, QWidget, QHBoxLayout, QLabel, QMessageBox, QDialog
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QObject

# Configurações do banco de dados
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'bd_teste2'
}

class DatabaseWorker(QObject):
    finished = pyqtSignal(str)
    error = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.query_type = None
        self.kwargs = {}

    def set_query(self, query_type, **kwargs):
        self.query_type = query_type
        self.kwargs = kwargs

    def run(self):
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor(dictionary=True)
            response = ""
            
            if self.query_type == "check_availability":
                cursor.execute("""
                    SELECT q.ID_Quartos, q.Numero, q.Tipo, q.Valor_Tipo, q.Status_Quarto
                    FROM quartos q
                    WHERE q.Status_Quarto = 'Disponível'
                """)
                quartos = cursor.fetchall()
                if quartos:
                    response = "Quartos disponíveis:<br>" + "<br>".join(
                        [f"🏨 Quarto {q['Numero']} | Tipo: {q['Tipo']:<8} | Preço: R${q['Valor_Tipo']:.2f}/noite | Status: {q['Status_Quarto']}" 
                         for q in quartos]
                    )
                else:
                    response = "Não há quartos disponíveis no momento."
                    
            elif self.query_type == "get_contact":
                response = "📞 Telefone de contato: +55 11 98765-4321<br>✉️ Email: contato@hostinn.com.br"
                
            elif self.query_type == "my_reservations":
                if 'cpf' not in self.kwargs:
                    response = "Por favor, informe seu CPF para consultar reservas."
                else:
                    cursor.execute("""
                        SELECT r.ID_Reserva, q.Numero, r.Data_Checkin, r.Data_Checkout, r.Valor_Reserva
                        FROM reserva r
                        JOIN clientes c ON r.ID_Cliente = c.ID_Cliente
                        JOIN reserva_quartos rq ON r.ID_Reserva = rq.ID_Reserva
                        JOIN quartos q ON rq.ID_Quartos = q.ID_Quartos
                        WHERE c.CPF = %s AND r.Status_reserva = 'Ativa'
                    """, (self.kwargs['cpf'],))
                    reservas = cursor.fetchall()
                    
                    if reservas:
                        response = "Suas reservas ativas:<br>" + "<br>".join(
                            [f"✅ ID: {r['ID_Reserva']} | Quarto: {r['Numero']} | Entrada: {r['Data_Checkin'].strftime('%d/%m/%Y')} | Saída: {r['Data_Checkout'].strftime('%d/%m/%Y')} | Valor: R${r['Valor_Reserva']:.2f}" 
                             for r in reservas]
                        )
                    else:
                        response = "Você não tem reservas ativas."
                        
            elif self.query_type == "client_info":
                if 'cpf' not in self.kwargs:
                    response = "Por favor, informe seu CPF para consultar seus dados."
                else:
                    cursor.execute("""
                        SELECT Nome, Email, Telefone, Endereco
                        FROM clientes
                        WHERE CPF = %s
                    """, (self.kwargs['cpf'],))
                    cliente = cursor.fetchone()
                    
                    if cliente:
                        response = f"""
                        Seus dados cadastrais:<br>
                        👤 Nome: {cliente['Nome']}<br>
                        ✉️ Email: {cliente['Email']}<br>
                        📞 Telefone: {cliente['Telefone']}<br>
                        🏠 Endereço: {cliente['Endereco']}
                        """
                    else:
                        response = "Cliente não encontrado. Verifique o CPF informado."
            
            self.finished.emit(response)
            
        except mysql.connector.Error as e:
            self.error.emit(f"⚠️ Erro no banco de dados: {str(e)}")
        except Exception as e:
            self.error.emit(f"⚠️ Erro inesperado: {str(e)}")
        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

class ChatBotWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, False)
        
        # Inicializa variáveis importantes primeiro
        self.client_cpf = None
        self.thread = None
        self.worker = None
        
        self.setWindowTitle("HostInn - Assistente Virtual")
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)
        self.setMinimumSize(800, 600)
        self.setMaximumSize(800, 600)
        
        # Configura a UI primeiro
        self._setup_ui()
        
        # Depois configura a thread
        self._setup_thread()
        
        self.setStyleSheet(self._get_stylesheet())

    def _setup_thread(self):
        """Configura a thread para operações de banco de dados"""
        self.thread = QThread()
        self.worker = DatabaseWorker()
        self.worker.moveToThread(self.thread)
        
        # Conecta os sinais
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self._handle_thread_response)
        self.worker.error.connect(self._handle_thread_error)
        
        # Aplicar stylesheet
        self.setStyleSheet(self._get_stylesheet())

    def _setup_ui(self):
        """Configura todos os componentes da interface"""
        self._setup_avatar()
        self._setup_chat_area()
        self._setup_input_field()
        self._setup_help_button()
        self._setup_layouts()
        self._connect_signals()

    def _setup_avatar(self):
        """Configura a área do avatar"""
        self.avatar_label = QLabel()
        self.avatar_label.setFixedSize(150, 150)
        self.avatar_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.avatar_label.setStyleSheet("border-radius: 75px; background-color: #3d3d3d;")
        
        try:
            pixmap = QPixmap("curupira.png")  # Ajuste o caminho
            if not pixmap.isNull():
                pixmap = pixmap.scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                self.avatar_label.setPixmap(pixmap)
            else:
                self.avatar_label.setText("Avatar")
        except Exception as e:
            print(f"Erro ao carregar avatar: {e}")
            self.avatar_label.setText("Avatar")

    def _setup_chat_area(self):
        """Configura a área de conversação"""
        self.chat_area = QTextEdit()
        self.chat_area.setFont(QFont("Segoe UI", 11))
        self.chat_area.setReadOnly(True)
        self.chat_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

    def _setup_input_field(self):
        """Configura o campo de entrada"""
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Digite sua mensagem...")
        self.input_field.setFont(QFont("Segoe UI", 11))
        
        self.send_button = QPushButton("Enviar")
        self.send_button.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        self.send_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                border-radius: 15px;
                padding: 12px 24px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

    def _setup_help_button(self):
        """Configura o botão de ajuda"""
        self.help_button = QPushButton("Como posso ajudar?")
        self.help_button.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        self.help_button.setObjectName("help_button")

    def _setup_layouts(self):
        """Configura os layouts da interface"""
        # Layout de entrada
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.send_button)

        # Layout esquerdo
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.avatar_label, alignment=Qt.AlignmentFlag.AlignHCenter)
        left_layout.addWidget(self.help_button, alignment=Qt.AlignmentFlag.AlignHCenter)
        left_layout.addStretch()
        left_layout.setContentsMargins(20, 20, 20, 20)

        # Layout direito
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.chat_area)
        right_layout.addLayout(input_layout)
        right_layout.setContentsMargins(20, 20, 20, 20)

        # Layout principal
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout, 1)
        main_layout.addLayout(right_layout, 3)
        main_layout.setSpacing(20)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def _get_stylesheet(self):
        """Retorna o CSS para estilização"""
        return """
            QMainWindow {
                background-color: #1e1e1e;
            }
            QTextEdit {
                background-color: #2d2d2d;
                color: #e0e0e0;
                border-radius: 10px;
                padding: 15px;
            }
            QLineEdit {
                background-color: #3d3d3d;
                color: white;
                border-radius: 15px;
                padding: 10px;
                margin: 0 10px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 15px;
                padding: 12px 24px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QLabel {
                color: #e0e0e0;
            }
            QPushButton#help_button {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                            stop:0 #6a1b9a, stop:1 #ab47bc);
                color: white;
                border-radius: 20px;
                padding: 12px;
                margin: 10px;
                width: 150px;
            }
            QPushButton#help_button:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                            stop:0 #ab47bc, stop:1 #6a1b9a);
            }
        """

    def _setup_thread(self):
        """Configura a thread para operações de banco de dados"""
        self.thread = QThread()
        self.worker = DatabaseWorker()
        self.worker.moveToThread(self.thread)
        
        self.thread.started.connect(lambda: self.worker.run())
        self.worker.finished.connect(self._handle_thread_response)
        self.worker.error.connect(self._handle_thread_error)
        self.worker.finished.connect(self.thread.quit)
        self.worker.error.connect(self.thread.quit)
        self.thread.finished.connect(self._enable_ui)

    def _connect_signals(self):
        """Conecta todos os sinais e slots"""
        self.send_button.clicked.connect(self.process_message)
        self.input_field.returnPressed.connect(self.process_message)
        self.help_button.clicked.connect(self.show_help_menu)

    def _handle_thread_response(self, response):
        """Trata respostas bem-sucedidas da thread"""
        self.show_response(response)

    def _handle_thread_error(self, error_msg):
        """Trata erros da thread"""
        self.show_response(error_msg)

    def _enable_ui(self, enabled=True):
        """Ativa/desativa componentes da UI"""
        self.input_field.setEnabled(enabled)
        self.send_button.setEnabled(enabled)
        self.help_button.setEnabled(enabled)
        if enabled:
            self.input_field.setFocus()

    def _format_cpf(self, cpf):
        """Formata um CPF para exibição: 123.456.789-00"""
        if cpf and len(cpf) == 11 and cpf.isdigit():
            return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        return cpf

    def _validate_cpf(self, cpf):
        """Valida se o CPF tem 11 dígitos numéricos"""
        return cpf and len(cpf) == 11 and cpf.isdigit()

    def show_help_menu(self):
        """Exibe o menu de ajuda"""
        help_message = """
        🌟 <b style='color: #FFEB3B;'>Menu de Ajuda</b> 🌟<br><br>
        <span style='color: #BBDEFB;'>
        🏨 1 - Ver quartos disponíveis<br>
        📞 2 - Telefone de contato<br>
        📅 3 - Minhas reservas (informe CPF)<br>
        👤 4 - Meus dados cadastrais (informe CPF)<br>
        ❓ 5 - Ajuda<br>
        </span>
        """
        self.show_response(help_message)

    def _display_user_message(self, message):
        """Exibe a mensagem do usuário no chat"""
        # Remove CPF da mensagem exibida
        message_display = re.sub(r'\d{3}\.?\d{3}\.?\d{3}-?\d{2}', '', message).strip()
        
        # Substitui \n por <br> ANTES de usar na f-string
        message_html = message_display.replace('\n', '<br>')
        
        formatted = f"""
        <div style='margin:15px 0; padding:12px; 
                    background:#3d3d3d; border-radius:15px; max-width:70%; 
                    float:right; clear:both;'>
            <span style='color:white; font-weight:bold;'>Você:</span><br>
            {message_html}  <!-- Aqui não há mais \n -->
        </div>
        """
        self.chat_area.insertHtml(formatted)
        self.chat_area.ensureCursorVisible()

    def show_response(self, response):
        """Exibe a resposta do assistente no chat"""
        # Formata CPFs na resposta (se houver)
        formatted_response = re.sub(
            r'(\d{3})(\d{3})(\d{3})(\d{2})',
            r'\1.\2.\3-\4',
            response.replace("\n", "<br>")
        )
        
        bot_message = f"""
        <div style='margin:15px 0; padding:12px; 
                    background:#2d2d2d; border-radius:15px; max-width:70%; 
                    float:left; clear:both;'>
            <span style='color:#e0e0e0; font-weight:bold;'>Assistente:</span><br>
            {formatted_response}
        </div>
        <div style='clear:both;'></div>
        """
        self.chat_area.insertHtml(bot_message)
        self.chat_area.verticalScrollBar().setValue(
            self.chat_area.verticalScrollBar().maximum()
        )

    def process_message(self):
        """Processa a mensagem do usuário"""
        message = self.input_field.text().strip()
        self.input_field.clear()
        
        if not message:
            return
        
        # Extrai CPF da mensagem
        cpf_match = re.search(r'(\d{3}\.?\d{3}\.?\d{3}-?\d{2}|\d{11})', message)
        if cpf_match:
            raw_cpf = cpf_match.group()
            self.client_cpf = re.sub(r'[^\d]', '', raw_cpf)  # Remove formatação
        
        # Exibe mensagem do usuário (ocultando CPF)
        display_msg = message.replace(raw_cpf, "[CPF]") if cpf_match else message
        self._display_user_message(display_msg)
        
        # Desativa UI durante processamento
        self._enable_ui(False)
        
        message_lower = message.lower()
        
        if self._is_help_request(message_lower):
            self.show_help_menu()
            self._enable_ui(True)
        elif self._is_contact_request(message_lower):
            self._process_contact_request()
        elif self._is_room_check(message_lower):
            self._process_room_check()
        elif self._is_reservation_check(message_lower):
            self._process_reservation_check()
        elif self._is_client_info_request(message_lower):
            self._process_client_info_request()
        else:
            self.show_response("⚠️ Comando não reconhecido. Digite 'ajuda' para ver opções.")
            self._enable_ui(True)

    def _is_help_request(self, message):
        """Verifica se é uma requisição de ajuda"""
        return re.fullmatch(r'(ajuda|help|\?|menu|5)', message, re.IGNORECASE)
    
    def _is_contact_request(self, message):
        """Verifica se é uma requisição de contato"""
        return re.fullmatch(r'(telefone|contato|2)', message, re.IGNORECASE)
    
    def _is_room_check(self, message):
        """Verifica se é uma consulta de quartos"""
        return re.search(r'(quartos?|disponíveis?|1)', message, re.IGNORECASE)
        
    def _is_reservation_check(self, message):
        """Verifica se é uma consulta de reservas"""
        return re.search(r'(reservas?|minhas reservas|3)', message, re.IGNORECASE)
        
    def _is_client_info_request(self, message):
        """Verifica se é uma consulta de dados cadastrais"""
        return re.search(r'(meus dados|cadastro|4)', message, re.IGNORECASE)

    def _process_contact_request(self):
        """Processa requisição de contato"""
        self.worker.set_query("get_contact")
        self.thread.start()

    def _process_room_check(self):
        """Processa consulta de quartos disponíveis"""
        self.worker.set_query("check_availability")
        self.thread.start()

    def _process_reservation_check(self):
        """Processa consulta de reservas"""
        if not self._validate_cpf(self.client_cpf):
            self.show_response("ℹ️ Formato para consultar reservas:<br><b>3 123.456.789-00</b>")
            self._enable_ui(True)
        else:
            self.worker.set_query("my_reservations", cpf=self.client_cpf)
            self.thread.start()

    def _process_client_info_request(self):
        """Processa consulta de dados cadastrais"""
        if not self._validate_cpf(self.client_cpf):
            self.show_response("ℹ️ Formato para consultar dados:<br><b>4 123.456.789-00</b>")
            self._enable_ui(True)
        else:
            self.worker.set_query("client_info", cpf=self.client_cpf)
            self.thread.start()

    def closeEvent(self, event):
        """Garante que a thread seja encerrada corretamente"""
        if hasattr(self, 'thread') and self.thread.isRunning():
            self.thread.quit()
            self.thread.wait()
        event.accept()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = ChatBotWindow()
#     window.show()
#     sys.exit(app.exec())