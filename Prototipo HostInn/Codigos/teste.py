from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,
    QHBoxLayout, QDateEdit, QGridLayout, QMessageBox
)
from PySide6.QtCore import QDate
import sys

class JanelaReserva(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Verificador de Disponibilidade")
        self.setFixedSize(400, 400)

        self.checkin = QDateEdit()
        self.checkin.setCalendarPopup(True)
        self.checkin.setDate(QDate.currentDate())

        self.checkout = QDateEdit()
        self.checkout.setCalendarPopup(True)
        self.checkout.setDate(QDate.currentDate().addDays(1))

        self.btn_verificar = QPushButton("Verificar Disponibilidade")
        self.btn_verificar.clicked.connect(self.verificar_disponibilidade)

        layout_datas = QHBoxLayout()
        layout_datas.addWidget(QLabel("Check-in:"))
        layout_datas.addWidget(self.checkin)
        layout_datas.addWidget(QLabel("Check-out:"))
        layout_datas.addWidget(self.checkout)

        self.layout_quartos = QGridLayout()

        # Simulando 6 quartos
        self.quartos = []
        for i in range(6):
            btn = QPushButton(f"Quarto {101 + i}")
            btn.setFixedSize(100, 50)
            self.quartos.append(btn)
            row = i // 3
            col = i % 3
            self.layout_quartos.addWidget(btn, row, col)

        layout_principal = QVBoxLayout()
        layout_principal.addLayout(layout_datas)
        layout_principal.addWidget(self.btn_verificar)
        layout_principal.addLayout(self.layout_quartos)

        self.setLayout(layout_principal)

        # Banco de dados falso (reservas existentes)
        # Cada tupla representa (ID_Quarto, Checkin, Checkout)
        self.reservas_existentes = [
            (101, QDate(2025, 4, 10), QDate(2025, 4, 13)),
            (102, QDate(2025, 4, 8), QDate(2025, 4, 15)),
            (104, QDate(2025, 4, 5), QDate(2025, 4, 9)),
        ]

    def verificar_disponibilidade(self):
        checkin = self.checkin.date()
        checkout = self.checkout.date()

        if checkin >= checkout:
            QMessageBox.warning(self, "Erro", "Check-out deve ser após o check-in.")
            return

        for i, btn in enumerate(self.quartos):
            numero_quarto = 101 + i
            disponivel = True

            for reserva in self.reservas_existentes:
                id_quarto, r_checkin, r_checkout = reserva

                if id_quarto == numero_quarto:
                    # Verifica se há conflito de datas
                    if not (checkout <= r_checkin or checkin >= r_checkout):
                        disponivel = False
                        break

            if disponivel:
                btn.setStyleSheet("background-color: green; color: white;")
            else:
                btn.setStyleSheet("background-color: red; color: white;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaReserva()
    janela.show()
    sys.exit(app.exec())
