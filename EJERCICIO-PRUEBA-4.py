import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QStackedLayout, QComboBox, QCheckBox, QLabel,
    QDial, QGroupBox, QRadioButton, QLineEdit, QSlider,
    QPushButton, QTextEdit
)


# ==============================================================================
# 1. CLASE DE LA VENTANA PRINCIPAL
# ==============================================================================
class PanelControlMultiVista(QMainWindow):
    def __init__(self):
        super().__init__()  # Inicializa QMainWindow

        # Configuración básica de la ventana
        self.setWindowTitle("Panel de Control Domótico")  # Título de la barra superior
        self.setMinimumSize(520, 420)  # Tamaño mínimo permitido

        # Layout principal vertical: arriba el menú desplegable, abajo la vista activa
        layout_principal = QVBoxLayout()

        # --- BARRA DE NAVEGACIÓN SUPERIOR ---
        self.cmb_vistas = QComboBox()  # Desplegable que actúa como selector de pestañas
        self.cmb_vistas.addItems(["Climatización", "Iluminación", "Consola"])
        self.cmb_vistas.setCurrentIndex(0)  # Selecciona la primera vista por defecto
        layout_principal.addWidget(self.cmb_vistas)

        # ======================================================================
        # VISTA 1: CLIMATIZACIÓN (Índice 0 en el QStackedLayout)
        # ======================================================================
        vista_clima = QWidget()  # Contenedor raíz de esta pantalla
        grid_clima = QGridLayout()  # Rejilla para alinear etiquetas y controles

        # Interruptor general del módulo
        self.chk_activado = QCheckBox("Sistema Activado")
        grid_clima.addWidget(self.chk_activado, 0, 0, 1, 2)  # Ocupa las 2 columnas

        # Control giratorio de temperatura (QDial)
        self.lbl_temperatura = QLabel("Temperatura: 16 °C")
        self.dial_temp = QDial()
        self.dial_temp.setRange(16, 30)  # Limita el giro entre 16 °C y 30 °C
        grid_clima.addWidget(self.lbl_temperatura, 1, 0)
        grid_clima.addWidget(self.dial_temp, 1, 1)

        # Caja visual agrupadora (QGroupBox) para aislar los botones de radio
        self.grupo_modo = QGroupBox("Modo")
        layout_modo = QHBoxLayout()
        self.rbt_frio = QRadioButton("Frío")
        self.rbt_calor = QRadioButton("Calor")
        self.rbt_frio.setChecked(True)  # "Frío" seleccionado por defecto
        layout_modo.addWidget(self.rbt_frio)
        layout_modo.addWidget(self.rbt_calor)
        self.grupo_modo.setLayout(layout_modo)
        grid_clima.addWidget(self.grupo_modo, 2, 0, 1, 2)

        # Campo de hora que reacciona al pulsar la tecla Enter
        self.lbl_hora = QLabel("Hora de encendido (HH:MM):")
        self.txt_hora = QLineEdit()
        self.txt_hora.setPlaceholderText("Ej: 08:30")
        grid_clima.addWidget(self.lbl_hora, 3, 0)
        grid_clima.addWidget(self.txt_hora, 3, 1)

        vista_clima.setLayout(grid_clima)  # Asignamos la rejilla al contenedor de la vista 1

        # ======================================================================
        # VISTA 2: ILUMINACIÓN (Índice 1 en el QStackedLayout)
        # ======================================================================
        vista_luz = QVBoxLayout()
        widget_luz = QWidget()  # Contenedor raíz de esta pantalla

        # Fila 1: Barra deslizante (QSlider) horizontal para regular el porcentaje
        fila_slider = QHBoxLayout()
        self.lbl_intensidad = QLabel("Intensidad: 0%")
        self.slider_luz = QSlider(Qt.Orientation.Horizontal)
        self.slider_luz.setRange(0, 100)  # Rango de 0% a 100%
        fila_slider.addWidget(self.lbl_intensidad)
        fila_slider.addWidget(self.slider_luz)
        vista_luz.addLayout(fila_slider)

        # Fila 2: Desplegable para elegir funcionamiento Manual o Programado
        fila_modo_luz = QHBoxLayout()
        lbl_modo_luz = QLabel("Modo de funcionamiento:")
        self.cmb_modo_luz = QComboBox()
        self.cmb_modo_luz.addItems(["Manual", "Programado"])
        self.cmb_modo_luz.setCurrentIndex(0)
        fila_modo_luz.addWidget(lbl_modo_luz)
        fila_modo_luz.addWidget(self.cmb_modo_luz)
        vista_luz.addLayout(fila_modo_luz)

        # Fila 3: Casillas de verificación para los 7 días de la semana
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

        # Fila 4: Botón para volcar la configuración al registro de la consola
        self.btn_guardar_luz = QPushButton("Guardar Iluminación")
        vista_luz.addWidget(self.btn_guardar_luz)

        widget_luz.setLayout(vista_luz)

        # ======================================================================
        # VISTA 3: CONSOLA DE REGISTROS (Índice 2 en el QStackedLayout)
        # ======================================================================
        vista_consola = QWidget()
        layout_consola = QVBoxLayout()
        self.txt_consola = QTextEdit()  # Área de texto multilínea para logs
        self.txt_consola.setReadOnly(True)  # Impide que el usuario escriba directamente en ella
        layout_consola.addWidget(self.txt_consola)
        vista_consola.setLayout(layout_consola)

        # ======================================================================
        # APILADO DE VISTAS (QStackedLayout)
        # ======================================================================
        # Apila múltiples widgets uno encima de otro; solo muestra uno cada vez
        self.tarxetas = QStackedLayout()
        self.tarxetas.addWidget(vista_clima)  # Índice 0
        self.tarxetas.addWidget(widget_luz)  # Índice 1
        self.tarxetas.addWidget(vista_consola)  # Índice 2

        layout_principal.addLayout(self.tarxetas)

        # Contenedor central obligatorio para QMainWindow
        contenedor = QWidget()
        contenedor.setLayout(layout_principal)
        self.setCentralWidget(contenedor)

        # ======================================================================
        # CONEXIÓN DE SEÑALES Y SLOTS
        # ======================================================================
        # Cuando cambia la opción del desplegable superior, cambia la vista visible
        self.cmb_vistas.currentIndexChanged.connect(self.cambiar_vista)

        # Señales de la Vista 1 (Climatización)
        self.chk_activado.stateChanged.connect(self.activar_climatizacion)
        self.dial_temp.valueChanged.connect(self.actualizar_temperatura)
        self.txt_hora.returnPressed.connect(self.comprobar_hora)  # Se dispara al pulsar Enter

        # Señales de la Vista 2 (Iluminación)
        self.slider_luz.valueChanged.connect(self.actualizar_intensidad)
        self.cmb_modo_luz.currentIndexChanged.connect(self.bloquear_dias)
        self.btn_guardar_luz.clicked.connect(self.guardar_iluminacion)

        # --- ESTADOS INICIALES ---
        # Ejecutamos manualmente estos métodos al arrancar para bloquear controles desactivados
        self.activar_climatizacion(0)  # 0 = desmarcado -> deshabilita controles de clima
        self.bloquear_dias(0)  # 0 = "Manual" -> deshabilita los checkboxes de días

    # ==========================================================================
    # 2. SLOTS DE NAVEGACIÓN Y LÓGICA DE VISTAS
    # ==========================================================================
    def cambiar_vista(self, indice):
        # Sincroniza el índice del QComboBox con la tarjeta visible en QStackedLayout
        if indice >= 0:
            self.tarxetas.setCurrentIndex(indice)

    # --- Lógica Vista 1: Climatización ---
    def activar_climatizacion(self, estado):
        # En PyQt, stateChanged pasa 2 cuando está marcado (Checked) y 0 si está desmarcado
        habilitado = (estado == 2)
        self.lbl_temperatura.setEnabled(habilitado)
        self.dial_temp.setEnabled(habilitado)
        self.grupo_modo.setEnabled(habilitado)
        self.lbl_hora.setEnabled(habilitado)
        self.txt_hora.setEnabled(habilitado)

    def actualizar_temperatura(self, valor):
        # Recibe automáticamente el nuevo número del QDial cada vez que se gira
        self.lbl_temperatura.setText(f"Temperatura: {valor} °C")

    def comprobar_hora(self):
        hora = self.txt_hora.text().strip()

        # Primera validación: longitud exacta de 5 caracteres y dos puntos en el centro (HH:MM)
        if len(hora) != 5 or hora[2] != ":":
            self.txt_consola.setText(self.txt_consola.toPlainText() + f"[{hora}] Error, formato inválido\n")
            return

        # Segunda validación: comprobar que horas (0-23) y minutos (0-59) sean números válidos
        try:
            horas = int(hora[0:2])
            minutos = int(hora[3:5])
            if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
                self.txt_consola.setText(self.txt_consola.toPlainText() + f"[{hora}] Error, formato inválido\n")
            else:
                self.txt_consola.setText(self.txt_consola.toPlainText() + f"[{hora}] Hora correcta\n")
        except ValueError:
            # Salta si el usuario escribió letras en lugar de números (ej. "ab:cd")
            self.txt_consola.setText(self.txt_consola.toPlainText() + f"[{hora}] Error, formato inválido\n")

    # --- Lógica Vista 2: Iluminación ---
    def actualizar_intensidad(self, valor):
        # Recibe el valor actual del QSlider mientras se arrastra
        self.lbl_intensidad.setText(f"Intensidad: {valor}%")

    def bloquear_dias(self, indice):
        # Si el índice es 0 ("Manual"), habilitar es False; si es 1 ("Programado"), es True
        habilitar = (indice != 0)
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

        # Recorremos cada checkbox para construir una cadena con las iniciales marcadas
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

        # Añadimos una nueva línea al historial de la Vista 3 (Consola)
        resumen = f"Iluminación -> Modo: {modo} | Intensidad: {intensidad}% | Días: {dias}\n"
        self.txt_consola.setText(self.txt_consola.toPlainText() + resumen)


# ==============================================================================
# 3. PUNTO DE ENTRADA DE LA APLICACIÓN
# ==============================================================================
if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)  # Crea la instancia de la aplicación
    ventana = PanelControlMultiVista()  # Crea nuestra ventana
    ventana.show()  # Muestra la ventana en pantalla
    sys.exit(aplicacion.exec())  # Inicia el bucle de eventos hasta cerrar