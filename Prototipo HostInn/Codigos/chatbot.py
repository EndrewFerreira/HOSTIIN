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
        self.kwargs     = {}

    def set_query(self, query_type, **kwargs):
        self.query_type = query_type
        self.kwargs     = kwargs

    def run(self):
        try:
            conn   = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor(dictionary=True)
            response = ""

            if self.query_type == "check_availability":
                cursor.execute("""
                    SELECT Numero, Tipo, Valor_Tipo, Status_Quarto
                      FROM quartos
                     WHERE Status_Quarto = 'Disponível'
                """)
                rows = cursor.fetchall()
                if rows:
                    response = "Quartos disponíveis:<br>" + "<br>".join(
                        f"🏨 Quarto {r['Numero']} | Tipo: {r['Tipo']} | R${r['Valor_Tipo']:.2f}/noite"
                        for r in rows
                    )
                else:
                    response = "Não há quartos disponíveis."

            elif self.query_type == "get_contact":
                response = "📞 +55 11 98765-4321<br>✉️ contato@hostinn.com.br"

            elif self.query_type == "my_reservations":
                cpf = self.kwargs.get('cpf')
                if not cpf:
                    response = "Informe seu CPF para consultar reservas."
                else:
                    cursor.execute("""
                        SELECT r.ID_Reserva, q.Numero, r.Data_Checkin, r.Data_Checkout, r.Valor_Reserva
                          FROM reserva r
                          JOIN clientes c ON r.ID_Cliente = c.ID_Cliente
                          JOIN reserva_quartos rq ON r.ID_Reserva = rq.ID_Reserva
                          JOIN quartos q ON rq.ID_Quartos = q.ID_Quartos
                         WHERE c.CPF = %s AND r.Status_reserva = 'Ativa'
                    """, (cpf,))
                    rows = cursor.fetchall()
                    if rows:
                        response = "Suas reservas:<br>" + "<br>".join(
                            f"✅ ID {r['ID_Reserva']} | Quarto {r['Numero']} | "
                            f"{r['Data_Checkin'].strftime('%d/%m/%Y')}→{r['Data_Checkout'].strftime('%d/%m/%Y')} | R${r['Valor_Reserva']:.2f}"
                            for r in rows
                        )
                    else:
                        response = "Você não tem reservas ativas."

            elif self.query_type == "client_info":
                cpf = self.kwargs.get('cpf')
                if not cpf:
                    response = "Informe seu CPF para consultar dados."
                else:
                    cursor.execute("""
                        SELECT Nome, Email, Telefone, Endereco
                          FROM clientes
                         WHERE CPF = %s
                    """, (cpf,))
                    r = cursor.fetchone()
                    if r:
                        response = (
                            f"👤 Nome: {r['Nome']}<br>"
                            f"✉️ Email: {r['Email']}<br>"
                            f"📞 Tel: {r['Telefone']}<br>"
                            f"🏠 Endereço: {r['Endereco']}"
                        )
                    else:
                        response = "Cliente não encontrado."

            self.finished.emit(response)

        except mysql.connector.Error as e:
            self.error.emit(f"Erro no DB: {e}")
        except Exception as e:
            self.error.emit(f"Erro inesperado: {e}")
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
        # Avatar e botão de ajuda
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

        self.help_button = QPushButton("Como posso ajudar?")
        self.help_button.setObjectName("help_button")
        self.help_button.clicked.connect(self.show_help_menu)

        # Área de chat
        self.chat_area   = QTextEdit(readOnly=True)
        self.chat_area.setFont(QFont("Segoe UI", 11))
        self.chat_area.setReadOnly(True)
        self.chat_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        # Input e enviar
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Digite sua mensagem...")
        self.input_field.setFont(QFont("Segoe UI", 11))
        self.input_field.returnPressed.connect(self.process_message)

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

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.avatar_label, alignment=Qt.AlignmentFlag.AlignHCenter)
        left_layout.addWidget(self.help_button, alignment=Qt.AlignmentFlag.AlignHCenter)
        left_layout.addStretch()

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.chat_area)
        right_layout.addLayout(input_layout)

        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout, 1)
        main_layout.addLayout(right_layout, 3)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def _get_stylesheet(self):
        return """
QMainWindow { background: #1e1e1e; }
QTextEdit { background: #2d2d2d; color: #e0e0e0; border-radius:10px; padding:10px; }
QLineEdit { background: #3d3d3d; color:white; border-radius:15px; padding:8px; }
QPushButton { background:#4CAF50; color:white; border-radius:15px; padding:8px; }
QPushButton:hover { background:#45a049; }
QPushButton#help_button { background:qlineargradient(x1:0,y1:0,x2:1,y2:1,stop:0 #6a1b9a, stop:1 #ab47bc); }
"""

    def show_help_menu(self):
        help_text = (
            "🌟 <b style='color:#FFEB3B;'>Menu de Ajuda</b><br><br>"
            "🏨 1 - Ver quartos disponíveis<br>"
            "📞 2 - Telefone de contato<br>"
            "📅 3 - Minhas reservas (informe CPF)<br>"
            "👤 4 - Meus dados cadastrais (informe CPF)<br>"
        )
        self._append_message(help_text, sender='bot')

    def process_message(self):
        msg = self.input_field.text().strip()
        if not msg:
            return
        self.input_field.clear()

        cpf_match = re.search(r"(\d{11}|\d{3}\.\d{3}\.\d{3}-\d{2})", msg)
        if cpf_match:
            self.client_cpf = re.sub(r"\D", "", cpf_match.group())
            display = msg.replace(cpf_match.group(), "[CPF]")
        else:
            display = msg

        self._append_message(display, sender='user')
        self.send_button.setEnabled(False)
        self.input_field.setEnabled(False)

        low = msg.lower()
        if low in ('ajuda','help','menu','?','5'):
            self.show_help_menu()
            self._enable_ui()
        elif re.search(r'(telefone|contato|2)', low):
            self._run_query('get_contact')
        elif re.search(r'(quartos?|disponíveis?|1)', low):
            self._run_query('check_availability')
        elif re.search(r'(reservas?|minhas reservas|3)', low):
            if not self.client_cpf:
                self._append_message("ℹ️ Use: 3 123.456.789-00", 'bot')
                self._enable_ui()
            else:
                self._run_query('my_reservations', cpf=self.client_cpf)
        elif re.search(r'(meus dados|cadastro|4)', low):
            if not self.client_cpf:
                self._append_message("ℹ️ Use: 4 123.456.789-00", 'bot')
                self._enable_ui()
            else:
                self._run_query('client_info', cpf=self.client_cpf)
        else:
            self._append_message("⚠️ Comando não reconhecido. Digite 'ajuda'.", 'bot')
            self._enable_ui()

    def _run_query(self, qtype, **kwargs):
        thread = QThread(self)
        worker = DatabaseWorker()
        worker.set_query(qtype, **kwargs)
        worker.moveToThread(thread)

        thread.started.connect(worker.run)
        worker.finished.connect(self._on_finished)
        worker.error.connect(self._on_error)

        worker.finished.connect(thread.quit)
        worker.error.connect(thread.quit)
        worker.finished.connect(worker.deleteLater)
        worker.error.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)

        thread.start()

    def _on_finished(self, resp):
        self._append_message(resp, sender='bot')
        self._enable_ui()

    def _on_error(self, err):
        self._append_message(err, sender='bot')
        self._enable_ui()

    def _enable_ui(self):
        self.send_button.setEnabled(True)
        self.input_field.setEnabled(True)
        self.input_field.setFocus()

    def _append_message(self, text, sender):
        html = text.replace("\n","<br>")
        if sender == 'user':
            box = f"""
<div style='margin:10px; float:right; clear:both; background:#3d3d3d; padding:10px; border-radius:10px;'>
<b style='color:white;'>Você:</b><br>{html}
</div>
"""
        else:
            box = f"""
<div style='margin:10px; float:left; clear:both; background:#2d2d2d; padding:10px; border-radius:10px;'>
<b style='color:#e0e0e0;'>Assistente:</b><br>{html}
</div><div style='clear:both;'></div>
"""
        self.chat_area.insertHtml(box)
        self.chat_area.verticalScrollBar().setValue(self.chat_area.verticalScrollBar().maximum())

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
