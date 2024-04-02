#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QHBoxLayout,QRadioButton,QPushButton,QGroupBox,QButtonGroup
from random import shuffle

class Question():
    def __init__(self, quest, right_answer, wrong1, wrong2, wrong3):
        self.quest = quest
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
list_question = list()
list_question.append(Question('Что нужно предложить гостю,если тот пришел к вам в гости в Ирландии', 'Предложить чай,кофе', 'Поприветствовать', 'Не впускать в дом', 'Спросить что надо?'))
list_question.append(Question('Из-за чего левая рука в Арабских Эмиратах считается грязной?', 'Левой рукой принято выполнять ритуалы личной гигиены', 'Через неё нельзя здороваться', 'Левая рука считается не гостеприимной', 'Левой рукой нельзя приветствовать '))
list_question.append(Question('Что нужно сделать,когда ты пришел в гости,в другой дом в Канаде?', 'Снять обувь', 'Просто чувствовать себя как дома', 'Купить много подарков', 'Пройти не снимая обувь в чужом доме'))
list_question.append(Question('Какой рукой надо есть в Китае?', 'Только правой', 'Только левой', 'Левой и правой', 'Есть как захочется'))
list_question.append(Question('Что в Бразилии считается символом процветания?', 'Чечевица', 'Тако', 'Пицца', 'Любой фрукт'))
list_question.append(Question('Как назывался род первых правителей России?', 'Рюриковичи', 'Романовы', 'Комунисты', 'Короли'))
list_question.append(Question('Кто первый доказал,что Земля имеет форму шара?', 'Аристотель', 'Пифагор', 'Кристофор Колумб', 'Фернан Магеллан'))
list_question.append(Question('Из какой страны был Пифагор?', 'Греция', 'Османска Империя', 'Франция','Англия'))
list_question.append(Question('Что принято сделать в Японии,если ты зашел в ресторан?', 'Снять обувь у порога', 'Не снимать обувь', 'Сделать подарок шеф-повару', 'Рассказать стишок'))
list_question.append(Question('Что нельзя делать при разговоре с немцем?', 'Держать руки в карманах', 'Перебивать его', 'Не говорить о плохом', 'Пытаться понять его'))


app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('Memory Card')
my_win.resize(400,200)

#Создание виджетов
question = QLabel('')
button = QPushButton('Ответить')

#Группа с переключателями
RadioGroupBox = QGroupBox('Варианты ответов')
btn_1 = QRadioButton('')
btn_2 = QRadioButton('')
btn_3 = QRadioButton('')
btn_4 = QRadioButton('')

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_1)
RadioGroup.addButton(btn_2)
RadioGroup.addButton(btn_3)
RadioGroup.addButton(btn_4)

#Группа с результатами 
AnswerGroupBox = QGroupBox('Результат теста')
result = QLabel('Правильно/Неправильно')
otwet = QLabel('Правильный овтет')

line_res = QVBoxLayout()
line_res.addWidget(result, alignment = Qt.AlignLeft)
line_res.addWidget(otwet, alignment = Qt.AlignHCenter| Qt.AlignVCenter)
AnswerGroupBox.setLayout(line_res)

#Макет(Направляющие линии
line_win = QVBoxLayout()
line_q = QHBoxLayout()
line_answer = QHBoxLayout()
line_g = QHBoxLayout()

line_q.addWidget(question, alignment = Qt.AlignHCenter|Qt.AlignVCenter)
line_g.addWidget(RadioGroupBox)
line_g.addWidget(AnswerGroupBox)

line_answer.addStretch(1)
line_answer.addWidget(button, stretch = 2) 
line_answer.addStretch(1)

#Линии для переключателей
gline_g = QHBoxLayout()
vline_g1 = QVBoxLayout()
vline_g2 = QVBoxLayout()

vline_g1.addWidget(btn_1)
vline_g1.addWidget(btn_2)
vline_g2.addWidget(btn_3)
vline_g2.addWidget(btn_4)

gline_g.addLayout(vline_g1)
gline_g.addLayout(vline_g2)

RadioGroupBox.setLayout(gline_g)

line_win.addLayout(line_q, stretch = 2)
line_win.addLayout(line_g, stretch = 8)

line_win.addStretch(1)
line_win.addLayout(line_answer, stretch = 2)
line_win.addStretch(1)



AnswerGroupBox.hide()
def show_result():
    RadioGroupBox.hide()
    AnswerGroupBox.show()
    button.setText('Следущий вопрос')

def show_question():
    RadioGroupBox.show()
    AnswerGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False) #Снять огранечение выбора
    btn_1.setChecked(False)
    btn_2.setChecked(False)
    btn_3.setChecked(False)
    btn_4.setChecked(False)
    RadioGroup.setExclusive(True) #Вернуть огранеченеие выбора

def click_ok():
    if button.text() == 'Ответить':
        chek_answer()
    else:
        next_question()

answers = [btn_1, btn_2, btn_3, btn_4]
def ask(q:Question):
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.quest)
    otwet.setText(q.right_answer)
    show_question()

def chek_answer():
    print('Статистика \n-Всего вопросов:', my_win.total, '\n-Правильных ответов:', my_win.score)
    print('Рейтинг:', str(my_win.score/my_win.total*100)+'%')
    if answers[0]. isChecked():
        result.setText('Правильно')
        my_win.score += 1
        show_result()
    elif answers[1]. isChecked() or answers[2]. isChecked() or answers[3]. isChecked():
        result.setText('Неправильно')
        show_result()

my_win.shet = -1    #Номер текущего вопроса?
def next_question():
    print('Статистика \n-Всего вопросов:', my_win.total, '\n-Правильных ответов:', my_win.score)
    my_win.total += 1
    my_win.shet += 1
    if my_win.shet == len(list_question):
        my_win.shet = 0
    q = list_question[my_win.shet] #Взяли вопрос
    ask(q)  #Задали вопрос

my_win.total = 0 #Количесвто всех вопросов
my_win.score = 0 #Количество верных ответов
next_question()

button.clicked.connect(click_ok)
my_win.setLayout(line_win)
my_win.show()
app.exec_()
