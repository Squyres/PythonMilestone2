import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class UserInfoApp(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the UI
        self.init_ui()

    def init_ui(self):
        # Set up window title and size
        self.setWindowTitle('User Information Form')
        self.setGeometry(300, 300, 300, 200)

        # Create widgets
        self.first_name_label = QLabel('First Name:')
        self.first_name_input = QLineEdit(self)

        self.last_name_label = QLabel('Last Name:')
        self.last_name_input = QLineEdit(self)

        self.phone_number_label = QLabel('Phone Number:')
        self.phone_number_input = QLineEdit(self)

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.clicked.connect(self.print_info)

        self.result_label = QLabel('', self)

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.first_name_label)
        layout.addWidget(self.first_name_input)
        layout.addWidget(self.last_name_label)
        layout.addWidget(self.last_name_input)
        layout.addWidget(self.phone_number_label)
        layout.addWidget(self.phone_number_input)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def print_info(self):
        # Get input values
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        phone_number = self.phone_number_input.text()

        # Print results to the screen (in the result label)
        self.result_label.setText(f"Name: {first_name} {last_name}\nPhone: {phone_number}")
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Phone Number: {phone_number}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserInfoApp()
    window.show()
    sys.exit(app.exec_())
