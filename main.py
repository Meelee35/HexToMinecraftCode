from PySide6.QtWidgets import QApplication, QDialog, QWidget, QMessageBox, QStyleFactory
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import sys
import os

def error_dialog(message: str, parent: QWidget=None):
  error_box = QMessageBox(parent)
  error_box.setIcon(QMessageBox.Critical)  # red error icon
  error_box.setWindowTitle("Error")
  error_box.setText(message)
  error_box.setStandardButtons(QMessageBox.Ok)
  error_box.exec()



def load_ui(path: str):
  ui_file = QFile(path)
  ui_file.open(QFile.ReadOnly)
  loader = QUiLoader()
  ui = loader.load(ui_file)
  ui_file.close()
  return ui


def hexToMC(hex_code: str, use_essentials: bool=False):
  hex_code = hex_code.lstrip('#')
  if len (hex_code) != 6:
    raise ValueError("Invalid hex color code")
  

app = QApplication([])
if sys.platform.startswith("linux"):
    # Let Qt pick up the desktop environment theme
    os.environ["QT_QPA_PLATFORMTHEME"] = os.environ.get("QT_QPA_PLATFORMTHEME", "gtk2")
elif sys.platform.startswith("win"):
    # Windows uses its native style automatically
    pass
ui = load_ui("main.ui")
ui.show()
app.exec()