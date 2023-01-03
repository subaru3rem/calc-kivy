from kivy import app
from kivy.uix import label as l, button as b, boxlayout as box, gridlayout as grid
import calc as c
import re

class MyApp(app.App):
    list = []
    def build(self):
        self.layout = box.BoxLayout(orientation='vertical')
        self.widget()
        return self.layout
    def adicionar(self, widgets):
        for i in widgets: self.layout.add_widget(i)
    def widget(self):
      self.resultado = '0'
      self.hello = l.Label(text=self.resultado, size_hint=(1,.3))
      click = grid.GridLayout(cols=4, size_hint=(1,.7))
      for i in self.teclado(): click.add_widget(i)
      self.adicionar([self.hello, click])
    def teclado(self):
        um = b.Button(text='1')
        um.bind(on_press=lambda a:self.add(1))
        dois = b.Button(text='2')
        dois.bind(on_press=lambda a:self.add(2))
        tres = b.Button(text='3')
        tres.bind(on_press=lambda a:self.add(3))
        soma = b.Button(text='+')
        soma.bind(on_press=lambda a:self.add('+'))
        quatro = b.Button(text='4')
        quatro.bind(on_press=lambda a:self.add(4))
        cinco = b.Button(text='5')
        cinco.bind(on_press=lambda a:self.add(5))
        seis = b.Button(text='6')
        seis.bind(on_press=lambda a:self.add(6))
        sete = b.Button(text='7')
        sete.bind(on_press=lambda a:self.add(7))
        oito = b.Button(text='8')
        oito.bind(on_press=lambda a:self.add(8))
        nove = b.Button(text='9')
        nove.bind(on_press=lambda a:self.add(9))
        zero = b.Button(text='0')
        zero.bind(on_press=lambda a:self.add(0))
        subtracao = b.Button(text='-')
        subtracao.bind(on_press=lambda a:self.add('-'))
        multiplicacao = b.Button(text='*')
        multiplicacao.bind(on_press=lambda a:self.add('*'))
        divisao = b.Button(text='/')
        divisao.bind(on_press=lambda a:self.add('/'))
        zero = b.Button(text='0')
        zero.bind(on_press=lambda a:self.add(0))
        igual = b.Button(text='=')
        igual.bind(on_press=lambda a:self.result())
        backspace = b.Button(text="x")
        backspace.bind(on_press=lambda a: self.backspace())
        clean = b.Button(text='c')
        clean.bind(on_press=lambda a: self.clean())
        virgula = b.Button(text=',')
        virgula.bind(on_press=lambda a: self.add())
        return []
    def add(self, value):
        self.layout.remove_widget(self.hello)
        if type(value)==str:
            self.list.insert(0,self.resultado)
            self.list.insert(1,value)
            self.resultado ='0'
        else:
            self.resultado = str(value) if self.resultado == '0' else self.resultado+str(value)
        self.reload()
    def result(self):
        self.layout.remove_widget(self.hello)
        self.list.insert(2,self.resultado)
        self.resultado = c.Calc(int(self.list[0]),self.list[1],int(self.list[2]))
        self.reload()
    def reload(self):
        self.hello = l.Label(text=str(self.resultado), size_hint=(1,.3))
        self.layout.add_widget(self.hello, 1)
    def backspace(self):
        self.layout.remove_widget(self.hello)
        string = ''
        for i in self.resultado[:-1]:
            string+= i
        self.resultado = string
        self.reload()
    def clean(self):
        self.layout.remove_widget(self.hello)
        self.resultado = '0'
        self.list.clear()
        self.reload()
if __name__ == '__main__':
    MyApp().run()