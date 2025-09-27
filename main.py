from PySide6.QtWidgets import QApplication, QDialog, QWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt
import sys
import os


def resource_path(path: str):
    if getattr(sys, "frozen", False):
        return os.path.join(sys._MEIPASS, path)
    return path


def error_dialog(message: str, parent: QWidget = None):
    error_box = QMessageBox(parent)
    error_box.setIcon(QMessageBox.Critical)
    error_box.setWindowTitle("Error")
    error_box.setText(message)
    error_box.setStandardButtons(QMessageBox.Ok)
    error_box.exec()


def load_ui(path: str):
    full_path = resource_path(path)
    ui_file = QFile(full_path)
    if not ui_file.open(QFile.ReadOnly):
        error_dialog(f"Failed to open UI file: {full_path}")
        sys.exit(1)
    loader = QUiLoader()
    ui = loader.load(ui_file)
    ui_file.close()
    if ui is None:
        error_dialog(f"Failed to load UI file: {full_path}")
        sys.exit(1)
    return ui


def hexToMC(hex_code: str, use_essentials: bool = False):
    hex_code = hex_code.lstrip("#")
    if len(hex_code) != 6:
        error_dialog("Hex code must be 6 characters long (e.g. #RRGGBB)")
        return None

    delimeter = "&" if use_essentials else "§"
    converted = delimeter + "x"
    for c in hex_code:
        if c not in "0123456789abcdefABCDEF":
            error_dialog("Hex code must only contain hexadecimal characters (0-9, A-F)")
            return None
        converted += delimeter + c
    return converted


def main():
    app = QApplication([])

    ui = load_ui("main.ui")
    output = load_ui("output.ui")
    output.okbtnbox.accepted.connect(output.accept)

    ui.setFixedSize(ui.size())
    ui.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
    ui.setWindowFlag(Qt.WindowCloseButtonHint, True)
    ui.setWindowFlag(Qt.WindowMaximizeButtonHint, False)

    output.setFixedSize(output.size())
    output.setWindowFlags(output.windowFlags() & ~Qt.WindowMaximizeButtonHint)

    def on_convert():
        hex_code = ui.hexInput.text().strip()
        use_essentials = ui.useEssential.isChecked()
        result = hexToMC(hex_code, use_essentials)
        if result is not None:
            output.output.setText(result)
            output.exec()

    ui.convertbtn.clicked.connect(on_convert)

    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
