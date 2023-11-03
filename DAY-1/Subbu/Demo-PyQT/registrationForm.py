import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QRadioButton, QComboBox

class RegistrationForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registration Form")
        self.setGeometry(100, 100, 400, 400)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        self.name_input = QLineEdit()
        self.email_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        gender_layout = QHBoxLayout()
        male_radio = QRadioButton("Male")
        female_radio = QRadioButton("Female")
        gender_layout.addWidget(male_radio)
        gender_layout.addWidget(female_radio)

        country_combo = QComboBox()
        country_combo.addItem("Select Country")
        country_combo.addItem("USA")
        country_combo.addItem("Canada")
        country_combo.addItem("UK")

        register_button = QPushButton("Register")

        main_layout.addWidget(QLabel("Registration Form"))
        main_layout.addWidget(QLabel("Name:"))
        main_layout.addWidget(self.name_input)
        main_layout.addWidget(QLabel("Email:"))
        main_layout.addWidget(self.email_input)
        main_layout.addWidget(QLabel("Password:"))
        main_layout.addWidget(self.password_input)
        main_layout.addWidget(QLabel("Gender:"))
        main_layout.addLayout(gender_layout)
        main_layout.addWidget(QLabel("Country:"))
        main_layout.addWidget(country_combo)
        main_layout.addWidget(register_button)

        register_button.clicked.connect(self.register)

    def register(self):
        name = self.name_input.text()
        email = self.email_input.text()
        password = self.password_input.text()
        gender = "Male" if self.sender().parent().findChildren(QRadioButton)[0].isChecked() else "Female"
        country = self.sender().parent().findChildren(QComboBox)[0].currentText()

        if not name or not email or not password or not gender or country == "Select Country":
            print("Please fill in all fields.")
        else:
            print(f"Registration successful!\nName: {name}\nEmail: {email}\nPassword: {password}\nGender: {gender}\nCountry: {country}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec_())
