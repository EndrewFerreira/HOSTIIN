from PyQt6.QtWidgets import QApplication, QDialog, QPushButton, QGridLayout, QMainWindow

class TelaQuartos(QDialog):
    def __init__(self, quartos_disponiveis, colunas=3):
        super().__init__()
        self.setWindowTitle("Quartos Disponíveis")
        self.setFixedSize(350, 300)  # Tamanho fixo da janela

        layout = QGridLayout()  # Usamos um Grid Layout

        # Criando botões e posicionando na grade
        for index, quarto in enumerate(quartos_disponiveis):
            btn = QPushButton(f"Quarto {quarto}", self)
            btn.clicked.connect(lambda _, q=quarto: self.selecionar_quarto(q))

            # Define a posição do botão na grade
            row = index // colunas  # Calcula a linha
            col = index % colunas   # Calcula a coluna
            layout.addWidget(btn, row, col)

        self.setLayout(layout)

    def selecionar_quarto(self, numero_quarto):
        print(f"Quarto {numero_quarto} selecionado!")
        self.accept()  # Fecha a janela

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestão de Hotel")
        self.setGeometry(100, 100, 400, 300)

        btn_mostrar_quartos = QPushButton("Ver Quartos Disponíveis", self)
        btn_mostrar_quartos.setGeometry(100, 100, 200, 50)
        btn_mostrar_quartos.clicked.connect(self.mostrar_quartos)

    def mostrar_quartos(self):
        quartos_disponiveis = [101, 102, 103, 201, 202, 203, 301, 302]  # Lista de quartos
        dialog = TelaQuartos(quartos_disponiveis, colunas=3)  # Define 3 colunas na grade
        dialog.exec()  # Abre a janela modal

app = QApplication([])
janela = MainWindow()
janela.show()
app.exec()

