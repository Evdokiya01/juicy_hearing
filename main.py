from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QRadioButton, QGridLayout
from random import randint
import sys
from gtts import gTTS
from io import BytesIO
from pygame import mixer

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        # Создаем списки слов и слов, с которыми их будут выводить
        self.word_choice_level2 = {"Accept": ["Accept", "Except", "Access"], "Except": ["Accept", "Except", "Access"],
                                   "Access": ["Accept", "Except", "Access"],
                                   "Principal": ["Principal", "Principle", "Prinful"],
                                   "Principle": ["Principal", "Principle", "Prinful"],
                                   "Prinful": ["Principal", "Principle", "Prinful"],
                                   "Lose": ["Lose", "Loose", "lease"], "Loose": ["Lose", "Loose", "lease"],
                                   "lease": ["Lose", "Loose", "lease"],
                                   "Beside": ["Beside", "Besides", "Based"], "Besides": ["Beside", "Besides", "Based"],
                                   "Based": ["Beside", "Besides", "Based"],
                                   "Ensure": ["Ensure", "Insure", "Enousured"],
                                   "Insure": ["Ensure", "Insure", "Enousured"],
                                   "Enousured": ["Ensure", "Insure", "Enousured"],
                                   "Diary": ["Diary", "Dairy", "Deary"], "Dairy": ["Diary", "Dairy", "Deary"],
                                   "Deary": ["Diary", "Dairy", "Deary"],
                                   "Sensitive": ["Sensitive", "Sensible", "Sensetive"],
                                   "Sensible": ["Sensitive", "Sensible", "Sensetive"],
                                   "Sensetive": ["Sensitive", "Sensible", "Sensetive"],
                                   "Bare": ["Bare", "Bear", "Beer"], "Bear": ["Bare", "Bear", "Beer"],
                                   "Beer": ["Bare", "Bear", "Beer"],
                                   "Affect": ["Affect", "Effect", "Efect"], "Effect": ["Affect", "Effect", "Efect"],
                                   "Efect": ["Affect", "Effect", "Efect"],
                                   "Quite": ["Quite", "Quiet", "Quit"], "Quiet": ["Quite", "Quiet", "Quit"],
                                   "Quit": ["Quite", "Quiet", "Quit"],
                                   "Alone": ["Alone", "Along", "Aloned"], "Along": ["Alone", "Along", "Aloned"],
                                   "Aloned": ["Alone", "Along", "Aloned"],
                                   "Cereal": ["Cereal", "Serial", "Cereals"], "Serial": ["Cereal", "Serial", "Cereals"],
                                   "Cereals": ["Cereal", "Serial", "Cereals"],
                                   "Stationary": ["Stationary", "Stationery", "Stateonery"],
                                   "Stationery": ["Stationary", "Stationery", "Stateonery"],
                                   "Stateonery": ["Stationary", "Stationery", "Stateonery"],
                                   "Conscience": ["Conscience", "Conscious", "Consience"],
                                   "Conscious": ["Conscience", "Conscious", "Consience"],
                                   "Consience": ["Conscience", "Conscious", "Consience"],
                                   "Storey": ["Storey", "Story", "Store"], "Story": ["Storey", "Story", "Store"],
                                   "Store": ["Storey", "Story", "Store"],
                                   "Right": ["Right", "Wright", "Wing"], "Wright": ["Right", "Wright", "Wing"],
                                   "Wing": ["Right", "Wright", "Wing"],
                                   "Patience": ["Patience", "Patients", "Patents"],
                                   "Patients": ["Patience", "Patients", "Patents"],
                                   "Patents": ["Patience", "Patients", "Patents"],
                                   "Compliment": ["Compliment", "Complement", "Compleement"],
                                   "Complement": ["Compliment", "Complement", "Compleement"],
                                   "Compleement": ["Compliment", "Complement", "Compleement"],
                                   "Peace": ["Peace", "Piece", "Pace"], "Piece": ["Peace", "Piece", "Pace"],
                                   "Pace": ["Peace", "Piece", "Pace"],
                                   "Ate": ["Ate", "Eight", "Aight"], "Eight": ["Ate", "Eight", "Aight"],
                                   "Aight": ["Ate", "Eight", "Aight"],
                                   "Buy": ["Buy", "By", "Bye"], "By": ["Buy", "By", "Bye"],
                                   "Bye": ["Buy", "By", "Bye"],
                                   "Cell": ["Cell", "Sell", "sill"], "Sell": ["Cell", "Sell", "sill"],
                                   "sill": ["Cell", "Sell", "sill"],
                                   "Dew": ["Dew", "Do", "Due"], "Do": ["Dew", "Do", "Due"],
                                   "Due": ["Dew", "Do", "Due"],
                                   "Fairy": ["Fairy", "Ferry", "Faire"], "Ferry": ["Fairy", "Ferry", "Faire"],
                                   "Faire": ["Fairy", "Ferry", "Faire"],
                                   "Flour": ["Flour", "Flower", "Fouler"], "Flower": ["Flour", "Flower", "Fouler"],
                                   "Fouler": ["Flour", "Flower", "Fouler"],
                                   "For": ["For", "Four", "Fur"], "Four": ["For", "Four", "Fur"],
                                   "Fur": ["For", "Four", "Fur"],
                                   "Hear": ["Hear", "Here", "Hare"], "Here": ["Hear", "Here", "Hare"],
                                   "Hare": ["Hear", "Here", "Hare"],
                                   "Hour": ["Hour", "Our", "How"], "Our": ["Hour", "Our", "How"],
                                   "How": ["Hour", "Our", "How"],
                                   "Know": ["Know", "No", "Now"], "No": ["Know", "No", "Now"],
                                   "Now": ["Know", "No", "Now"],
                                   "Knight": ["Knight", "Night", "Nite"], "Night": ["Knight", "Night", "Nite"],
                                   "Nite": ["Knight", "Night", "Nite"],
                                   "Mail": ["Mail", "Males", "Male"], "Males": ["Mail", "Males", "Male"],
                                   "Male": ["Mail", "Males", "Male"],
                                   "Marry": ["Marry", "Merry", "Mery"], "Merry": ["Marry", "Merry", "Mery"],
                                   "Mery": ["Marry", "Merry", "Mery"],
                                   "Meat": ["Meat", "Meet", "Met"], "Meet": ["Meat", "Meet", "Met"],
                                   "Met": ["Meat", "Meet", "Met"],
                                   "Pair": ["Pair", "Pear", "Par"], "Pear": ["Pair", "Pear", "Par"],
                                   "Par": ["Pair", "Pear", "Par"],
                                   "Rites": ["Rites", "Write", "Rite"], "Write": ["Rites", "Write", "Rite"],
                                   "Rite": ["Rites", "Write", "Rite"],
                                   "Sight": ["Sight", "Site", "Sit"], "Site": ["Sight", "Site", "Sit"],
                                   "Sit": ["Sight", "Site", "Sit"],
                                   "Son": ["Son", "Sun", "Sin"], "Sun": ["Son", "Sun", "Sin"],
                                   "Sin": ["Son", "Sun", "Sin"],
                                   "Their": ["Their", "There", "They’re"], "There": ["Their", "There", "They’re"],
                                   "They’re": ["Their", "There", "They’re"],
                                   "To": ["To", "Too", "Two"], "Too": ["To", "Too", "Two"],
                                   "Two": ["To", "Too", "Two"],
                                   "One": ["One", "Won", "On"], "Won": ["One", "Won", "On"],
                                   "On": ["One", "Won", "On"],
                                   "Wait": ["Wait", "Weight", "Weak"], "Weight": ["Wait", "Weight", "Weak"],
                                   "Weak": ["Wait", "Weight", "Weak"],
                                   "Wear": ["Wear", "Where", "Were"], "Where": ["Wear", "Where", "Were"],
                                   "Were": ["Wear", "Where", "Were"], }

        self.words_level2 = ["Accept", "Except", "Access",
                             "Principal", "Principle", "Prinful",
                             "Lose", "Loose", "lease",
                             "Beside", "Besides", "Based",
                             "Ensure", "Insure", "Enousured",
                             "Diary", "Dairy", "Deary",
                             "Sensitive", "Sensible", "Sensetive",
                             "Bare", "Bear", "Beer",
                             "Affect", "Effect", "Efect",
                             "Quite", "Quiet", "Quit",
                             "Alone", "Along", "Aloned",
                             "Cereal", "Serial", "Cereals",
                             "Stationary", "Stationery", "Stateonery",
                             "Conscience", "Conscious", "Consience",
                             "Storey", "Story", "Store",
                             "Right", "Wright", "Wing",
                             "Patience", "Patients", "Patents",
                             "Compliment", "Complement", "Compleement",
                             "Peace", "Piece", "Pace",
                             "Ate", "Eight", "Aight",
                             "Buy", "By", "Bye",
                             "Cell", "Sell", "sill",
                             "Dew", "Do", "Due",
                             "Fairy", "Ferry", "Faire",
                             "Flour", "Flower", "Fouler",
                             "For", "Four", "Fur",
                             "Hear", "Here", "Hare",
                             "Hour", "Our", "How",
                             "Know", "No", "Now",
                             "Knight", "Night", "Nite",
                             "Mail", "Male", "Male",
                             "Marry", "Merry", "Mery",
                             "Meat", "Meet", "Meat",
                             "Pair", "Pear", "Par",
                             "Right", "Write", "Rite",
                             "Sight", "Site", "Sit",
                             "Son", "Sun", "Sin",
                             "Their", "There", "They’re",
                             "To", "Too", "Two",
                             "One", "Won", "On",
                             "Wait", "Weight", "Weak",
                             "Wear", "Where", "Were"]

        self.word_choice_level1 = {"Accept": ["Accept", "Except"], "Except": ["Accept", "Except"],
                                   "Principal": ["Principal", "Principle"],
                                   "Principle": ["Principal", "Principle"],
                                   "Lose": ["Lose", "Loose"], "Loose": ["Lose", "Loose"],
                                   "Beside": ["Beside", "Besides"], "Besides": ["Beside", "Besides"],
                                   "Ensure": ["Ensure", "Insure"], "Insure": ["Ensure", "Insure"],
                                   "Diary": ["Diary", "Dairy"], "Dairy": ["Diary", "Dairy"],
                                   "Sensitive": ["Sensitive", "Sensible"],
                                   "Sensible": ["Sensitive", "Sensible"],
                                   "Bare": ["Bare", "Bear"], "Bear": ["Bare", "Bear"],
                                   "Affect": ["Affect", "Effect"], "Effect": ["Affect", "Effect"],
                                   "Quite": ["Quite", "Quiet"], "Quiet": ["Quite", "Quiet"],
                                   "Alone": ["Alone", "Along"], "Along": ["Alone", "Along"],
                                   "Cereal": ["Cereal", "Serial"], "Serial": ["Cereal", "Serial"],
                                   "Stationary": ["Stationary", "Stationery"],
                                   "Stationery": ["Stationary", "Stationery"],
                                   "Conscience": ["Conscience", "Conscious"],
                                   "Conscious": ["Conscience", "Conscious"],
                                   "Storey": ["Storey", "Story"], "Story": ["Storey", "Story"],
                                   "Right": ["Right", "Wright"], "Wright": ["Right", "Wright"],
                                   "Patience": ["Patience", "Patients"],
                                   "Patients": ["Patience", "Patients"],
                                   "Compliment": ["Compliment", "Complement"],
                                   "Complement": ["Compliment", "Complement"],
                                   "Peace": ["Peace", "Piece"], "Piece": ["Peace", "Piece"],
                                   "Ate": ["Ate", "Eight"], "Eight": ["Ate", "Eight"],
                                   "Buy": ["Buy", "By"], "By": ["Buy", "By"],
                                   "Cell": ["Cell", "Sell"], "Sell": ["Cell", "Sell"],
                                   "Dew": ["Dew", "Do"], "Do": ["Dew", "Do"],
                                   "Fairy": ["Fairy", "Ferry"], "Ferry": ["Fairy", "Ferry"],
                                   "Flour": ["Flour", "Flower"], "Flower": ["Flour", "Flower"],
                                   "For": ["For", "Four"], "Four": ["For", "Four"],
                                   "Hear": ["Hear", "Here"], "Here": ["Hear", "Here"],
                                   "Hour": ["Hour", "Our"], "Our": ["Hour", "Our"],
                                   "Know": ["Know", "No"], "No": ["Know", "No"],
                                   "Knight": ["Knight", "Night"], "Night": ["Knight", "Night"],
                                   "Mail": ["Mail", "Males"], "Males": ["Mail", "Males"],
                                   "Marry": ["Marry", "Merry"], "Merry": ["Marry", "Merry"],
                                   "Meat": ["Meat", "Meet"], "Meet": ["Meat", "Meet"],
                                   "Pair": ["Pair", "Pear"], "Pear": ["Pair", "Pear"],
                                   "Rites": ["Rites", "Write"], "Write": ["Rites", "Write"],
                                   "Sight": ["Sight", "Site"], "Site": ["Sight", "Site"],
                                   "Son": ["Son", "Sun"], "Sun": ["Son", "Sun"],
                                   "Their": ["Their", "There"], "There": ["Their", "There"],
                                   "To": ["To", "Too"], "Too": ["To", "Too"],
                                   "One": ["One", "Won"], "Won": ["One", "Won"],
                                   "Wait": ["Wait", "Weight"], "Weight": ["Wait", "Weight"],
                                   "Wear": ["Wear", "Where"], "Where": ["Wear", "Where"]}

        self.words_level1 = ["Accept", "Except", "Principal", "Principle",
                             "Lose", "Loose", "Beside", "Besides",
                             "Ensure", "Insure", "Diary", "Dairy",
                             "Sensitive", "Sensible", "Bare", "Bear",
                             "Affect", "Effect", "Quite", "Quiet",
                             "Alone", "Along", "Cereal", "Serial",
                             "Stationary", "Stationery", "Conscience", "Conscious",
                             "Storey", "Story", "Right", "Wright",
                             "Patience", "Patients", "Compliment", "Complement",
                             "Peace", "Piece", "Ate", "Eight",
                             "Buy", "By", "Cell", "Sell",
                             "Dew", "Do", "Fairy", "Ferry",
                             "Flour", "Flower", "For", "Four",
                             "Hear", "Here", "Hour", "Our",
                             "Know", "No", "Knight", "Night",
                             "Mail", "Male", "Marry", "Merry",
                             "Meat", "Meet", "Pair", "Pear",
                             "Right", "Write", "Sight", "Site",
                             "Son", "Sun", "Their", "There",
                             "To", "Too", "One", "Won",
                             "Wait", "Weight", "Wear", "Where"]

        # Создаем окно, размер которого нельзя изменить
        self.move(600, 500)
        self.setFixedSize(400, 500)
        self.setWindowTitle('Сочный слух')

        # Создаем основные кнопки и убираем их
        self.btn_start = QPushButton("СТАРТ", self)
        self.btn_start.move(140, 200)
        self.btn_start.clicked.connect(self.start_button)
        self.btn_voice = QPushButton("ОЗВУЧИТЬ", self)
        self.btn_voice.move(6000, 6000)
        self.btn_voice.clicked.connect(self.voice_button)
        self.btn_stop = QPushButton("СТОП", self)
        self.btn_stop.move(6000, 6000)
        self.btn_stop.clicked.connect(self.stop_button)
        self.btn_next = QPushButton("ДАЛЕЕ", self)
        self.btn_next.move(6000, 6000)
        self.btn_next.clicked.connect(self.next_button)
        self.btn_back = QPushButton("НАЗАД", self)
        self.btn_back.move(6000, 6000)
        self.btn_back.clicked.connect(self.back_button)
        self.correct_answer = QLineEdit(self)
        self.correct_answer.move(6000, 6000)
        self.correct_answer.setEnabled(False)

        # Создаем кнопки выбора слова с одним из нескольких вариантов
        layout = QGridLayout()
        self.setLayout(layout)
        self.answer_options = []

        self.radiobutton = QRadioButton(" ")
        self.radiobutton.country = " "
        self.radiobutton.toggled.connect(self.choice_button)
        self.radiobutton.setCheckable(True)
        layout.addWidget(self.radiobutton, 0, 0)
        self.answer_options.append(self.radiobutton)
        self.radiobutton = QRadioButton(" ")
        self.radiobutton.country = " "
        self.radiobutton.toggled.connect(self.choice_button)
        self.radiobutton.setCheckable(True)
        layout.addWidget(self.radiobutton, 0, 1)
        self.answer_options.append(self.radiobutton)
        self.radiobutton = QRadioButton(" ")
        self.radiobutton.country = " "
        self.radiobutton.toggled.connect(self.choice_button)
        self.radiobutton.setCheckable(True)
        layout.addWidget(self.radiobutton, 0, 2)
        self.answer_options.append(self.radiobutton)

        # Убираем кнопки выбора
        for i in range(len(self.answer_options)):
            radiobutton = self.answer_options[i]
            radiobutton.hide()
        self.examination = -1
        self.number = None

        # Создаем кнопки выбора уровня и убираем их
        self.level_1 = QPushButton("1 уровень", self)
        self.level_1.move(6000, 6000)
        self.level_1.clicked.connect(self.levell_1)
        self.level_2 = QPushButton("2 уровень", self)
        self.level_2.move(6000, 6000)
        self.level_2.clicked.connect(self.levell_2)

        self.lel1 = 0
        self.lel2 = 0

        self.past_word = ""

    # Работа кнопки НАЗАД
    def back_button(self):
        # Обнуляем отметки кнопки выбора ответа
        for i in range(len(self.answer_options)):
            radiobutton = self.answer_options[i]
            radiobutton.setCheckable(False)
        self.lel1 = 0
        self.lel2 = 0

        # Убираем все кнопки выбора ответа и обуляем текст на кнопках
        for i in range(len(self.answer_options)):
            radiobutton = self.answer_options[i]
            radiobutton.hide()
            radiobutton.setText(" ")

        # Обнуляем окно с правильностью ответа
        self.correct_answer.setText("")
        # Убираем ненужные кнопки и достаем нужные
        self.btn_back.move(6000, 6000)
        self.level_1.move(80, 190)
        self.level_2.move(190, 190)
        self.btn_voice.move(6000, 6000)
        self.btn_stop.move(190, 380)
        self.btn_next.move(6000, 6000)
        self.correct_answer.move(6000, 6000)


    # работа кнопки СТАРТ
    def start_button(self):
        # Убираем кнопку старт и достаем снопки выбора уровня, так же кнопку стоп, если пользователь хочет
        # прекратить работу приложения
        self.btn_start.move(6000, 6000)
        self.level_1.move(80, 190)
        self.level_2.move(190, 190)
        self.btn_stop.move(190, 380)

    # Работа кнопки УРОВЕНЬ 1
    def levell_1(self):
        self.lel1 = 1

        # Убираем кнопки выбора уровня и достаем нужные кнопки
        self.level_1.move(6000, 6000)
        self.level_2.move(6000, 6000)
        self.btn_voice.move(140, 55)
        self.btn_stop.move(190, 380)
        self.btn_next.move(290, 380)
        self.btn_back.move(90, 380)
        self.correct_answer.move(120, 275)

    # Работа кнопки УРОВЕНЬ 2
    def levell_2(self):
        self.lel2 = 1

        # Убираем кнопки выбора уровня и достаем нужные кнопки
        self.level_1.move(6000, 6000)
        self.level_2.move(6000, 6000)
        self.btn_voice.move(140, 55)
        self.btn_stop.move(190, 380)
        self.btn_next.move(290, 380)
        self.btn_back.move(90, 380)
        self.correct_answer.move(120, 275)

    # Работа кнопки СТОП
    def stop_button(self):
        # Обнуляем отметки кнопки выбора ответа
        for i in range(len(self.answer_options)):
            radiobutton = self.answer_options[i]
            radiobutton.setCheckable(False)
        self.lel1 = 0
        self.lel2 = 0

        # Убираем все кнопки выбора ответа и обуляем текст на кнопках
        for i in range(len(self.answer_options)):
            radiobutton = self.answer_options[i]
            radiobutton.hide()
            radiobutton.setText(" ")

        # Обнуляем окно с правильностью ответа
        self.correct_answer.setText("")
        # Убираем ненужные кнопки и достаем нужные
        self.btn_back.move(6000, 6000)
        self.level_1.move(6000, 6000)
        self.level_2.move(6000, 6000)
        self.btn_start.move(140, 200)
        self.btn_voice.move(6000, 6000)
        self.btn_stop.move(6000, 6000)
        self.btn_next.move(6000, 6000)
        self.correct_answer.move(6000, 6000)

    # Работа кнопки ДАЛЕЕ
    def next_button(self):
        # Обнуляем окно с правильностью ответа
        self.correct_answer.setText("")
        # Обнуляем отметки кнопки выбора ответа, убираем слово которое озвучивалось раньшеб убираем кнопки
        for i in range(len(self.answer_options)):
            radiobutton = self.answer_options[i]
            radiobutton.setText(" ")
            radiobutton.hide()
            radiobutton.setCheckable(False)

        self.examination = 1
        self.number = None

    # Работа кнопок выбора слова
    def choice_button(self):
        # Создаем список с нажатием кнопок, смотрим какую кнопку нажали, какое слово выбрали
        self.radiobutton = self.sender()
        self.answer = self.radiobutton.text()
        # Проверяем на правильность выбранное слово
        if self.answer == self.word_answer:
            self.correct_answer.setText("Верно")
        else:
            self.correct_answer.setText("Неверно")

    # Работа кнопки ОЗВУЧИТЬ
    def voice_button(self):
        # Разрешаем кнопкам выбора ответа делать отметиныб
        for i in range(len(self.answer_options)):
            radiobutton = self.answer_options[i]
            radiobutton.setCheckable(True)
        # Проверяем какой выбрали уровень
        if self.lel1 == 1:
            # Достаем нужное количество кнопок
            for i in range(len(self.answer_options) - 1):
                radiobutton = self.answer_options[i]
                radiobutton.show()
            # Проверяем была ли нажата кнопка ДАЛЕЕ/СТОП
            if self.examination == 1 or self.examination == -1:
                # Создаем рандомное число, достаем слова, которые зависят от него
                self.examination = 0
                random_number = randint(0, len(self.words_level1) - 1)
                self.number = random_number
                self.word_answer = self.words_level1[random_number]

                # Проверяем равно ли прошедшее слово нынешнему
                if self.past_word == self.word_answer:
                    # Изменяем нынешнее слово, чтобы не было повторений, так же изменяем зависящие слова
                    self.number = random_number + 1
                    self.word_answer = self.words_level1[random_number + 1]
                    self.past_word = self.word_answer

            else:
                # Выбираем заново то же слово, чтобы можно было пролушать его снова
                self.word_answer = self.words_level1[self.number]
            list_of_options = self.word_choice_level1[self.word_answer]

            # К кнопкам выбора прикрепляем слова выбора
            for i in range(len(self.answer_options) - 1):
                radiobutton = self.answer_options[i]
                radiobutton.setText(list_of_options[i])

            # Переводим слово в аудио и сохраняем его
            mp3_fp = BytesIO()
            tts = gTTS(self.word_answer)
            tts.write_to_fp(mp3_fp)
            mixer.init()
            mixer.music.load(mp3_fp, "mp3")
            mixer.music.play()
        else:
            # Достаем нужное количество кнопок
            for i in range(len(self.answer_options)):
                radiobutton = self.answer_options[i]
                radiobutton.show()
            # Проверяем ыла ли нажата кнопка ДАЛЕЕ/СТОП
            if self.examination == 1 or self.examination == -1:
                # Создаем рандомное число, достаем слова, которые зависят от него
                self.examination = 0
                random_number = randint(0, len(self.words_level2) - 1)
                self.number = random_number
                self.word_answer = self.words_level2[random_number]
                # Проверяем равно ли прошедшее слово нынешнему
                if self.past_word == self.word_answer:
                    # Изменяем нынешнее слово, чтобы не было повторений, так же изменяем зависящие слова
                    self.number = random_number + 1
                    self.word_answer = self.words_level1[random_number + 1]
                    self.past_word = self.word_answer

            else:
                # Выбираем заново то же слово, чтобы можно было пролушать его снова
                self.word_answer = self.words_level2[self.number]
            list_of_options = self.word_choice_level2[self.word_answer]

            # К кнопкам выбора прикрепляем слова выбора
            for i in range(len(self.answer_options)):
                radiobutton = self.answer_options[i]
                radiobutton.setText(list_of_options[i])

            # Переводим слово в аудио и сохраняем его
            mp3_fp = BytesIO()
            tts = gTTS(self.word_answer)
            tts.write_to_fp(mp3_fp)
            mixer.init()
            mixer.music.load(mp3_fp, "mp3")
            mixer.music.play()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    app.exec_()