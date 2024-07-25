import os
import sys
import subprocess
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QWidget,
                             QComboBox, QMessageBox)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
import whisper

general_font = "Poppins"

class SRTApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.script_directory = os.path.dirname(os.path.abspath(__file__))
        self.setWindowIcon(QIcon('img/logo.png'))
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Caption Craft')
        self.setStyleSheet("background-color: #FBFCFD;")  # Light grey background
        self.setFixedSize(600, 350)  # Fixed window size

        layout = QVBoxLayout()

        # Status Label with custom font and padding
        self.statusLabel = QLabel('Select a file and model, then press "Run".', self)
        self.statusLabel.setFont(QFont(general_font, 14, QFont.Medium))
        self.statusLabel.setAlignment(Qt.AlignCenter)
        self.statusLabel.setStyleSheet("padding: 10px; color: #071B29;")  # Dark grey text
        layout.addWidget(self.statusLabel)



        """
        Browse File Button
        """
        # Button to browse files with style
        self.btnBrowse = QPushButton('Browse File', self)
        self.btnBrowse.setFont(QFont(general_font, 14))
        self.btnBrowse.setStyleSheet("QPushButton { background-color: #193052; color: white; border-radius: 8px; padding: 12px; }"
                                     "QPushButton:hover { background-color: #192535; }")
        self.btnBrowse.clicked.connect(self.showFileDialog)
        layout.addWidget(self.btnBrowse)


        """
        Spacer
        """
        spacer = QWidget()
        spacer.setFixedHeight(20) 
        layout.addWidget(spacer)





        """
        Model Dropdown
        """

        # Title
        dropdownTitleLabel = QLabel("Select Model:", self)  # Create a label for the dropdown title
        dropdownTitleLabel.setFont(QFont(general_font, 14, QFont.Medium))  # Set font for the title
        dropdownTitleLabel.setStyleSheet("padding: 10px; color: #071B29;")  # Dark grey text
        layout.addWidget(dropdownTitleLabel)  # Add the title label to the layout

        # Dropdown for model selection with enhanced style
        self.modelDropdown = QComboBox(self)
        available_models = whisper.available_models()
        available_models.sort(key=len)

        # Predefined order
        order = ["tiny", "base", "small", "medium", "large"]

        # Create a dictionary that maps each item to its index in the order
        # Items not in the order get a default index that puts them at the end of the list
        order_index = {key: i for i, key in enumerate(order)}
        default_index = len(order)  # Any item not found gets this index

        # Now, sort the list with our custom key
        sorted_items = sorted(available_models, key=lambda x: order_index.get(x, default_index))


        self.modelDropdown.addItems(sorted_items)
        self.modelDropdown.setFont(QFont(general_font, 16))  # Large, readable font

        # Custom stylesheet for the dropdown
        self.modelDropdown.setStyleSheet("""
    QComboBox {
        background-color: white;
        color: black;
        border: 2px solid #ccc;
        border-radius: 10px;
        padding-left: 10px;
        min-height: 40px;
    }
    QComboBox::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 30px;
        border-left: 1px solid #ccc;
    }
    QComboBox::down-arrow {
        image: url('/Users/royalfi/Downloads/down 1.png');                  

    }
""")
    
        layout.addWidget(self.modelDropdown)



        """
        Spacer
        """
        spacer = QWidget()
        spacer.setFixedHeight(20) 
        layout.addWidget(spacer)


        """
        Run Button
        """
        # Run button with style and icon
        self.btnRun = QPushButton('Create subtitles!', self)
        self.btnRun.setFont(QFont(general_font, 14))
        self.btnRun.setStyleSheet("QPushButton { background-color: #28a745; color: white; border-radius: 8px; padding: 12px; }"
                                  "QPushButton:hover { background-color: #157B1B;}")
        self.btnRun.clicked.connect(self.runScript)
        layout.addWidget(self.btnRun)

        centralWidget = QWidget(self)
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
        self.show()

    def showFileDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Select a video file", "",
                                                  "Video Files (*.mp4 *.avi *.mkv *.mov)", options=options)
        if fileName:
            self.filePath = fileName
            # Update the label with a truncated version of the filename if it's too long
            displayFileName = (fileName[:50] + '...') if len(fileName) > 53 else fileName
            self.statusLabel.setText(f'Selected File: {displayFileName}')
            self.statusLabel.setFont(QFont(general_font, 10, QFont.Medium))

    def runScript(self):
        if not hasattr(self, 'filePath'):
            self.showError()
            return
        model_name = self.modelDropdown.currentText()
        if sys.platform == "darwin":  # macOS
            command = f'''osascript -e 'tell application "Terminal" to do script "cd \\"{self.script_directory}\\" && python3 SrtAi.py \\"{self.filePath}\\" {model_name}"' '''
        elif sys.platform == "win32":  # Windows
            command = f'''cmd /c "cd /d "{self.script_directory}"  && python SrtAi.py "{self.filePath}" {model_name}"'''
        try:
            subprocess.run(command, shell=True, check=True)
            self.statusLabel.setText("Script is running in a new terminal...")
            # Change to 'finished' message after the script completes TODO
            
        except subprocess.CalledProcessError as e:
            self.statusLabel.setText(f"Failed to run script: {str(e)}")


    def showError(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("Please select a file before running the script.")
        msgBox.setWindowTitle("Error")
        # Apply stylesheet to QMessageBox to change text color to red
        msgBox.setStyleSheet("QLabel { color: red; } QPushButton { width: 80px; } QMessageBox { background-color: white; }")
        msgBox.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SRTApp()
    sys.exit(app.exec_())
