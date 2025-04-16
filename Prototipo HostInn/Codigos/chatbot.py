import sys
import sqlite3
import re
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton,
    QVBoxLayout, QWidget, QHBoxLayout, QLabel, QMessageBox
)
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt, QThread, Signal

DATABASE = "hotel.db"

class DatabaseWorker(QThread):
    finished = Signal(str)

    def __init__(self, query_type, **kwargs):
        super().__init__()
        self.query_type = query_type
        self.kwargs = kwargs

    def run(self):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        response = ""
        try:
            if self.query_type == "check_availability":
                cursor.execute("SELECT * FROM quartos WHERE disponivel = 1")
                quartos = cursor.fetchall()
                if quartos:
                    response = "Hotéis disponíveis:<br>" + "<br>".join(
                        [f"🏨 {q[1]} | Tipo: {q[2]:<8} | Preço: R${q[3]:.2f}/noite" 
                         for q in quartos]
                    )
                else:
                    response = "Não há quartos disponíveis no momento."
            elif self.query_type == "get_contact":
                response = f"📞 Telefone de contato: +55 11 98765-4321"
            elif self.query_type == "my_reservations":
                cursor.execute("""
                    SELECT r.id, q.numero, r.data_entrada, r.data_saida 
                    FROM reservas r
                    JOIN quartos q ON r.quarto_id = q.id
                    WHERE usuario = 'cliente'
                """)
                reservas = cursor.fetchall()
                if reservas:
                    response = "Reservas ativas:<br>" + "<br>".join(
                        [f"✅ ID: {r[0]} | Quarto: {r[1]} | Entrada: {r[2]} | Saída: {r[3]}" 
                         for r in reservas]
                    )
                else:
                    response = "Você não tem reservas ativas."
        except Exception as e:
            response = f"⚠️ Erro: {str(e)}"
        finally:
            conn.close()
            self.finished.emit(response)

class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hotéis & Reservas")
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.setMinimumSize(800, 600)
        self.setMaximumSize(800, 600)
        self.setStyleSheet(self._get_stylesheet())
        
        self._setup_avatar()
        self._setup_chat_area()
        self._setup_input_field()
        self._setup_layouts()
        self._connect_signals()

        # Keep track of running threads
        self.current_thread = None

    def _get_stylesheet(self):
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
                color: white;  /* Texto branco */
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
        """

    def _setup_avatar(self):
        self.avatar_label = QLabel()
        self.avatar_label.setFixedSize(150, 150)
        self.avatar_label.setAlignment(Qt.AlignCenter)
        self.avatar_label.setStyleSheet("border-radius: 75px; background-color: #3d3d3d;")
        
        pixmap = QPixmap(R"C:\Users\11054836\Desktop\PI\HOSTIIN\Prototipo HostInn\Icones\curupira.png")
        if pixmap.isNull():
            QMessageBox.warning(self, "Erro", "Imagem curupira.png não encontrada!")
            self.avatar_label.setText("Imagem não carregada")
        else:
            pixmap = pixmap.scaled(150, 150, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            self.avatar_label.setPixmap(pixmap)
            self.avatar_label.setMask(pixmap.mask())

    def _setup_chat_area(self):
        self.chat_area = QTextEdit()
        self.chat_area.setFont(QFont("Segoe UI", 11))
        self.chat_area.setReadOnly(True)
        self.chat_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

    def _setup_input_field(self):
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Digite sua mensagem...")
        self.input_field.setFont(QFont("Segoe UI", 11))
        
        self.send_button = QPushButton("Enviar")
        self.send_button.setFont(QFont("Segoe UI", 10, QFont.Bold))
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

    def _setup_layouts(self):
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.send_button)

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.avatar_label, alignment=Qt.AlignHCenter)
        self.help_button = QPushButton("Como posso ajudar?")
        self.help_button.setFont(QFont("Segoe UI", 10, QFont.Bold))
        self.help_button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                            stop:0 #6a1b9a, stop:1 #ab47bc);
                color: white;
                border-radius: 20px;
                padding: 12px;
                margin: 10px;
                width: 150px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                            stop:0 #ab47bc, stop:1 #6a1b9a);
            }
        """)
        left_layout.addWidget(self.help_button, alignment=Qt.AlignHCenter)
        left_layout.addStretch()
        left_layout.setContentsMargins(20, 20, 20, 20)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.chat_area)
        right_layout.addLayout(input_layout)
        right_layout.setContentsMargins(20, 20, 20, 20)

        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout, 1)
        main_layout.addLayout(right_layout, 3)
        main_layout.setSpacing(20)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def show_help_menu(self):
        help_message = """
        🌟 <b style='color: #FFEB3B;'>Menu de Ajuda</b> 🌟<br><br>
        <span style='color: #BBDEFB;'>
        📌 1 - Ver quartos disponíveis<br>
        📞 2 - Telefone de contato<br>
        ❓ 3 - Ajuda<br>
        </span>
        """
        self.show_response(help_message)

    def _connect_signals(self):
        self.send_button.clicked.connect(self.process_message)
        self.input_field.returnPressed.connect(self.process_message)
        self.help_button.clicked.connect(self.show_help_menu)
      
    def process_message(self):
        message = self.input_field.text().strip().lower()
        self.input_field.clear()
        
        if not message:
            return
        
        self._display_user_message(message)
        
        if self._is_help_request(message):
            self.show_help_menu()
        elif self._is_contact_request(message):
            self._fetch_contact_info()
        elif self._is_room_check(message):
            self._check_room_availability()
        else:
            self.show_response(f"⚠️ Comando não reconhecido. Digite 'ajuda' para ver opções.")

    def _display_user_message(self, message):
        formatted = """
        <div style='margin:15px 0; padding:12px; 
                    background:#3d3d3d; border-radius:15px; max-width:70%; 
                    float:right; clear:both;' >
            <span style='color:white; font-weight:bold;'>Você:</span><br>
            {}
        </div>
        """.format(message.replace('\n', '<br>'))
        self.chat_area.insertHtml(formatted)

    def _is_help_request(self, message):
        return re.fullmatch(r'(ajuda|help|\?|menu)', message, re.IGNORECASE)
    
    def _is_contact_request(self, message):
        return re.fullmatch(r'(telefone|contato)', message, re.IGNORECASE)
    
    def _is_room_check(self, message):
        return re.search(r'(quartos?|disponíveis?)', message, re.IGNORECASE)

    def _fetch_contact_info(self):
        worker = DatabaseWorker("get_contact")
        worker.finished.connect(self.show_response)
        self._start_thread(worker)

    def _check_room_availability(self):
        worker = DatabaseWorker("check_availability")
        worker.finished.connect(self.show_response)
        self._start_thread(worker)

    def _start_thread(self, worker):
        # Ensure the thread is not already running
        if self.current_thread is not None and self.current_thread.isRunning():
            self.current_thread.quit()
            self.current_thread.wait()
        
        self.current_thread = worker
        worker.start()

    def closeEvent(self, event):
        if self.current_thread is not None and self.current_thread.isRunning():
            self.current_thread.quit()
            self.current_thread.wait()
        event.accept()

    def show_response(self, response):
        formatted_response = response.replace("\n", "<br>")
        bot_message = f"""
        <div style='margin:15px 0; padding:12px; 
                    background:#2d2d2d; border-radius:15px; max-width:70%; 
                    float:left; clear:both;'>
            <span style='color:#e0e0e0; font-weight:bold;'>HotelBot:</span><br>
            {formatted_response}
        </div>
        """
        self.chat_area.insertHtml(bot_message)
        self.chat_area.verticalScrollBar().setValue(
            self.chat_area.verticalScrollBar().maximum()
        )

def create_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS quartos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero TEXT NOT NULL,
            tipo TEXT NOT NULL,
            preco REAL NOT NULL,
            disponivel INTEGER DEFAULT 1
        )
    ''')
    
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quarto_id INTEGER NOT NULL,
            usuario TEXT NOT NULL,
            data_entrada TEXT NOT NULL,
            data_saida TEXT NOT NULL,
            FOREIGN KEY (quarto_id) REFERENCES quartos(id)
        )
    ''')
    
    cursor.executemany(''' 
        INSERT OR IGNORE INTO quartos (numero, tipo, preco, disponivel)
        VALUES (?, ?, ?, ?)
    ''', [
        ("101", "Standard", 250.00, 1),
        ("102", "Luxo", 450.00, 1),
        ("201", "Suíte", 800.00, 0)
    ])
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    app = QApplication(sys.argv)
    window = ChatBotWindow()
    window.show()
    sys.exit(app.exec())