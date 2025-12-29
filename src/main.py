from dataclasses import field
import flet as ft


@ft.control
class CalcButton(ft.FilledButton):
    expand: int = field(default_factory=lambda: 1)


@ft.control
class DigitButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.WHITE_24
    color: ft.Colors = ft.Colors.WHITE


@ft.control
class ActionButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.ORANGE
    color: ft.Colors = ft.Colors.WHITE


@ft.control
class ExtraActionButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.BLUE_GREY_100
    color: ft.Colors = ft.Colors.BLACK


@ft.control
class CalculatorApp(ft.Container):
    def init(self):
        self.reset()
        self.width = 350
        self.bgcolor = ft.Colors.BLACK
        self.border_radius = ft.BorderRadius.all(20)
        self.padding = 20
        self.resultado = ft.Text(value="0", color=ft.Colors.WHITE, size=20)
        self.content = ft.Column(
            controls=[
                ft.Row(controls=[self.resultado],
                       alignment=ft.MainAxisAlignment.END),
                ft.Row(controls=[
                    ExtraActionButton(
                        content='AC', on_click=self.button_clicked),
                    ExtraActionButton(
                        content='+/-', on_click=self.button_clicked),
                    ExtraActionButton(
                        content='%', on_click=self.button_clicked),
                    ActionButton(content='/', on_click=self.button_clicked)
                ]
                ),
                ft.Row(controls=[
                    DigitButton(content='7', on_click=self.button_clicked),
                    DigitButton(content='8', on_click=self.button_clicked),
                    DigitButton(content='9', on_click=self.button_clicked),
                    ActionButton(content='*', on_click=self.button_clicked)
                ]
                ),
                ft.Row(controls=[
                    DigitButton(content='4', on_click=self.button_clicked),
                    DigitButton(content='5', on_click=self.button_clicked),
                    DigitButton(content='6', on_click=self.button_clicked),
                    ActionButton(content='-', on_click=self.button_clicked)
                ]
                ),
                ft.Row(controls=[
                    DigitButton(content='1', on_click=self.button_clicked),
                    DigitButton(content='2', on_click=self.button_clicked),
                    DigitButton(content='3', on_click=self.button_clicked),
                    ActionButton(content='+', on_click=self.button_clicked)
                ]
                ),
                ft.Row(controls=[
                    DigitButton(content='0', expand=2,
                                on_click=self.button_clicked),
                    DigitButton(content='.', on_click=self.button_clicked),
                    ActionButton(content='=', on_click=self.button_clicked)
                ]
                )
            ]
        )

    def button_clicked(self, e):
        data = e.control.content
        print(f'Button clicked with data = {data}')
        if self. resultado.value == 'Error' or data == 'AC':
            self.resultado.value = 0
            self.reset()
        elif data in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'):
            if self.resultado.value == '0' or self.new_operand:
                self.resultado.value = data
                self.new_operand = False
            else:
                self.resultado.value = self.resultado.value + data

        elif data in ('+', '-', '*', '/'):
            self.resultado.value = self.calculate(
                self.operand1, float(self.resultado.value), self.operator)
            self.operator = data
            if self.resultado.value == "Error":
                self.operand1 = "0"
            else:
                self.operand1 = float(self.resultado.value)
            self.new_operand = True

        elif data in ("="):
            self.resultado.value = self.calculate(
                self.operand1, float(self.resultado.value), self.operator)
            self.reset()

        elif data in ("%"):
            self.resultado.value = float(self.resultado.value) / 100
            self.reset()

        elif data in ("+/-"):
            if float(self.resultado.value) > 0:
                self.resultado.value = "-" + str(self.resultado.value)

            elif float(self.resultado.value) < 0:
                self.resultado.value = str(self.format_number(
                    abs(float(self.resultado.value))))

        self.update()

    def format_number(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

    def calculate(self, operand1, operand2, operator):
        if operator == '+':
            return self.format_number(operand1 + operand2)
        elif operator == '-':
            return self.format_number(operand1 - operand2)
        elif operator == '*':
            return self.format_number(operand1 * operand2)
        elif operator == '/':
            if operand2 == 0:
                return 'Error'
            else:
                return self.format_number(operand1 / operand2)

    def reset(self):
        self.operator = '+'
        self.operand1 = 0
        self.new_operand = True


def main(page: ft.Page):
    page.title = 'Calculadora'
    page.window.width = 385
    page.window.height = 335
    calc_1 = CalculatorApp()
    page.add(calc_1)


if __name__ == '__main__':
    ft.app(target=main)
