import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QStackedLayout, QComboBox, QCheckBox, QLabel,
    QDial, QGroupBox, QRadioButton, QLineEdit, QSlider,
    QPushButton, QTextEdit
)


class PanelControlMultiVista(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Panel de Control Domótico")
        self.setMinimumSize(520, 420)

        layout_principal = QVBoxLayout()

        # 1. Selector superior de vistas
        self.cmb_vistas = QComboBox()
        self.cmb_vistas.addItems(["Climatización", "Iluminación", "Consola"])
        self.cmb_vistas.setCurrentIndex(0)
        layout_principal.addWidget(self.cmb_vistas)

        # ======================================================================
        # VISTA 1: CLIMATIZACIÓN
        # ======================================================================
        vista_clima = QWidget()
        grid_clima = QGridLayout()

        self.chk_activado = QCheckBox("Sistema Activado")
        grid_clima.addWidget(self.chk_activado, 0, 0, 1, 2)

        # Control de temperatura con QDial
        self.lbl_temperatura = QLabel("Temperatura: 16 °C")
        self.dial_temp = QDial()
        self.dial_temp.setRange(16, 30)
        grid_clima.addWidget(self.lbl_temperatura, 1, 0)
        grid_clima.addWidget(self.dial_temp, 1, 1)

        # QGroupBox con QRadioButton para el modo
        self.grupo_modo = QGroupBox("Modo")
        layout_modo = QHBoxLayout()
        self.rbt_frio = QRadioButton("Frío")
        self.rbt_calor = QRadioButton("Calor")
        self.rbt_frio.setChecked(True)
        layout_modo.addWidget(self.rbt_frio)
        layout_modo.addWidget(self.rbt_calor)
        self.grupo_modo.setLayout(layout_modo)
        grid_clima.addWidget(self.grupo_modo, 2, 0, 1, 2)

        # Hora de encendido con validación al pulsar Enter
        self.lbl_hora = QLabel("Hora de encendido (HH:MM):")
        self.txt_hora = QLineEdit()
        self.txt_hora.setPlaceholderText("Ej: 08:30")
        grid_clima.addWidget(self.lbl_hora, 3, 0)
        grid_clima.addWidget(self.txt_hora, 3, 1)

        vista_clima.setLayout(grid_clima)

        # ======================================================================
        # VISTA 2: ILUMINACIÓN
        # ======================================================================
        vista_luz = QVBoxLayout()
        widget_luz = QWidget()

        # Intensidad con QSlider horizontal
        fila_slider = QHBoxLayout()
        self.lbl_intensidad = QLabel("Intensidad: 0%")
        self.slider_luz = QSlider(Qt.Orientation.Horizontal)
        self.slider_luz.setRange(0, 100)
        fila_slider.addWidget(self.lbl_intensidad)
        fila_slider.addWidget(self.slider_luz)
        vista_luz.addLayout(fila_slider)

        # Selector de modo Manual / Programado
        fila_modo_luz = QHBoxLayout()
        lbl_modo_luz = QLabel("Modo de funcionamiento:")
        self.cmb_modo_luz = QComboBox()
        self.cmb_modo_luz.addItems(["Manual", "Programado"])
        self.cmb_modo_luz.setCurrentIndex(0)
        fila_modo_luz.addWidget(lbl_modo_luz)
        fila_modo_luz.addWidget(self.cmb_modo_luz)
        vista_luz.addLayout(fila_modo_luz)

        # Checkboxes de los días de la semana
        fila_dias = QHBoxLayout()
        self.chk_lunes = QCheckBox("Lunes")
        self.chk_martes = QCheckBox("Martes")
        self.chk_miercoles = QCheckBox("Miércoles")
        self.chk_jueves = QCheckBox("Jueves")
        self.chk_viernes = QCheckBox("Viernes")
        self.chk_sabado = QCheckBox("Sábado")
        self.chk_domingo = QCheckBox("Domingo")

        fila_dias.addWidget(self.chk_lunes)
        fila_dias.addWidget(self.chk_martes)
        fila_dias.addWidget(self.chk_miercoles)
        fila_dias.addWidget(self.chk_jueves)
        fila_dias.addWidget(self.chk_viernes)
        fila_dias.addWidget(self.chk_sabado)
        fila_dias.addWidget(self.chk_domingo)
        vista_luz.addLayout(fila_dias)

        self.btn_guardar_luz = QPushButton("Guardar Iluminación")
        vista_luz.addWidget(self.btn_guardar_luz)

        widget_luz.setLayout(vista_luz)

        # ======================================================================
        # VISTA 3: CONSOLA
        # ======================================================================
        vista_consola = QWidget()
        layout_consola = QVBoxLayout()
        self.txt_consola = QTextEdit()
        self.txt_consola.setReadOnly(True)
        layout_consola.addWidget(self.txt_consola)
        vista_consola.setLayout(layout_consola)

        # ======================================================================
        # APILADO DE VISTAS (QStackedLayout)
        # ======================================================================
        self.tarxetas = QStackedLayout()
        self.tarxetas.addWidget(vista_clima)
        self.tarxetas.addWidget(widget_luz)
        self.tarxetas.addWidget(vista_consola)

        layout_principal.addLayout(self.tarxetas)

        contenedor = QWidget()
        contenedor.setLayout(layout_principal)
        self.setCentralWidget(contenedor)

        # ======================================================================
        # CONEXIONES DE SEÑALES Y SLOTS (SIN LAMBDA)
        # ======================================================================
        self.cmb_vistas.currentIndexChanged.connect(self.cambiar_vista)

        # Conexiones Vista 1
        self.chk_activado.stateChanged.connect(self.activar_climatizacion)
        self.dial_temp.valueChanged.connect(self.actualizar_temperatura)
        self.txt_hora.returnPressed.connect(self.comprobar_hora)

        # Conexiones Vista 2
        self.slider_luz.valueChanged.connect(self.actualizar_intensidad)
        self.cmb_modo_luz.currentIndexChanged.connect(self.bloquear_dias)
        self.btn_guardar_luz.clicked.connect(self.guardar_iluminacion)

        # Estados iniciales
        self.activar_climatizacion(0)
        self.bloquear_dias(0)

    # --- Slots de navegación ---
    def cambiar_vista(self, indice):
        if indice >= 0:
            self.tarxetas.setCurrentIndex(indice)

    # --- Slots Vista 1 (Climatización) ---
    def activar_climatizacion(self, estado):
        habilitado = (estado == 2)
        self.lbl_temperatura.setEnabled(habilitado)
        self.dial_temp.setEnabled(habilitado)
        self.grupo_modo.setEnabled(habilitado)
        self.lbl_hora.setEnabled(habilitado)
        self.txt_hora.setEnabled(habilitado)

    def actualizar_temperatura(self, valor):
        self.lbl_temperatura.setText(f"Temperatura: {valor} °C")

    def comprobar_hora(self):
        hora = self.txt_hora.text().strip()
        if len(hora) != 5 or hora[2] != ":":
            self.txt_consola.setText(self.txt_consola.toPlainText() + f"[{hora}] Error, formato inválido\n")
            return

        try:
            horas = int(hora[0:2])
            minutos = int(hora[3:5])
            if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
                self.txt_consola.setText(self.txt_consola.toPlainText() + f"[{hora}] Error, formato inválido\n")
            else:
                self.txt_consola.setText(self.txt_consola.toPlainText() + f"[{hora}] Hora correcta\n")
        except ValueError:
            self.txt_consola.setText(self.txt_consola.toPlainText() + f"[{hora}] Error, formato inválido\n")

    # --- Slots Vista 2 (Iluminación) ---
    def actualizar_intensidad(self, valor):
        self.lbl_intensidad.setText(f"Intensidad: {valor}%")

    def bloquear_dias(self, indice):
        habilitar = (indice != 0)  # Si es 0 ("Manual") -> False; si es 1 ("Programado") -> True
        self.chk_lunes.setEnabled(habilitar)
        self.chk_martes.setEnabled(habilitar)
        self.chk_miercoles.setEnabled(habilitar)
        self.chk_jueves.setEnabled(habilitar)
        self.chk_viernes.setEnabled(habilitar)
        self.chk_sabado.setEnabled(habilitar)
        self.chk_domingo.setEnabled(habilitar)

    def guardar_iluminacion(self):
        intensidad = self.slider_luz.value()
        modo = self.cmb_modo_luz.currentText()
        dias = ""

        if self.chk_lunes.isChecked():
            dias += "L "
        if self.chk_martes.isChecked():
            dias += "M "
        if self.chk_miercoles.isChecked():
            dias += "X "
        if self.chk_jueves.isChecked():
            dias += "J "
        if self.chk_viernes.isChecked():
            dias += "V "
        if self.chk_sabado.isChecked():
            dias += "S "
        if self.chk_domingo.isChecked():
            dias += "D "

        if dias == "":
            dias = "Ninguno"

        resumen = f"Iluminación -> Modo: {modo} | Intensidad: {intensidad}% | Días: {dias}\n"
        self.txt_consola.setText(self.txt_consola.toPlainText() + resumen)


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = PanelControlMultiVista()
    ventana.show()
    sys.exit(aplicacion.exec())