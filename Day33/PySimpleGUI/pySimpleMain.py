import PySimpleGUI as pysimple

pysimple.theme('BluePurple')
# All the stuff inside your window
layout = [
    [pysimple.Text("Donkey Gabrage")],
    [pysimple.Text("Donkey Garbage two"), pysimple.InputText()],
    [pysimple.Text("Donkey Garbage two"), pysimple.InputText(), pysimple.Checkbox("True"),  pysimple.Checkbox("false")],
    [pysimple.OK(), pysimple.Canvas()]
]

window = pysimple.Window('donkey', layout)

while True:
    event, values = window.read()
    if event in (pysimple.WINDOW_CLOSED, 'Cancel'):
        break

window.close()
