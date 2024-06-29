class Control:
    def __init__(self, view):
        self.view = view
        self.connectSignals()
        
    def calculate(self):
        num1 = float(self.view.le1.text())
        num2 = float(self.view.le2.text())
        operator =self.view.cb.currentText()
        
        if operator =='+':
            return f'{num1} + {num2} = {self.sum(num1, num2)}'
        
        else:
            return "Calculation Error"
        
    def connectSignals(self):       # btn1을 클릭하면 calculate 결과가 화면에 표시되도록 수정
        self.view.btn1.clicked.connect(lambda: self.view.setDisplay(self.calculate()))
        self.view.btn2.clicked.connect(self.view.clearMessage)
        
    def sum(self, a, b):        # 예외 처리 제거 : 향후 calculate 함수에서 처리하도록 구현 예정
        return a+b
    
    def sub(self, a, b):        # 뺄셈 함수 추가
        return a-b
    
    def mul(self, a, b):        # 곱셈 함수 추가
        return a*b
    
    def div(self, a, b):        # 나눗셈 함수 추가
        if (b==0):
            return 0
        else:
            return a/b
    
    def pow(self, a, b):        # 제곱 연산 함수 추가
        return pow(a, b)