import PySimpleGUI as sg
from math import *

sg.theme('Topanga')

# Window stuff
layout = [[sg.Text('A:'), sg.Input(key='-INA-', size=(10, 20), do_not_clear=True, enable_events=True),
           sg.Text('B:'), sg.Input(key='-INB-', size=(10, 20), do_not_clear=True, enable_events=True),
           sg.Text('C:'), sg.Input(key='-INC-', size=(10, 20), do_not_clear=True, enable_events=True),
           sg.Button('Continue'),
           sg.Text('        *** A > 0 *** ' '\n' ' *** Otherwise - error *** ')],
          [sg.Text('Result: '), sg.Button('Decide', key='-RESH-', bind_return_key=True, visible=False)],
          [sg.Text('Discriminant: '), sg.Text(key='-DIS-', size=(7, 1))],
          [sg.Text('Root №1 (b**2 + sqrt(D) / 2a): '), sg.Text(key='-XF-', size=(50, 1))],
          [sg.Text('Root №2 (b**2 - sqrt(D) / 2a): '), sg.Text(key='-XS-', size=(50, 1))],
          [sg.Button('Exit')]]

# Create the Window
width, height = 600, 200
window = sg.Window('Find the Discriminant and Its Roots', layout, size=(width, height))


# func for check input == float
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


# main loop and check events
while True:
    event, values = window.read()

    if event == 'Exit' or event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
        break
    # Check input == float and do button visible
    if event == 'Continue':
        j = float(2)
        if values['-INA-'] and isfloat(values['-INB-']) and isfloat(values['-INC-']):
            window['-RESH-'].Update(visible=True)

    if event == '-RESH-':
        dis = float(values['-INB-']) ** 2 - ((4 * float(values['-INA-'])) * float(values['-INC-']))
        window['-DIS-'].Update(str(dis))
        window['-RESH-'].Update(visible=False)
        if float(dis) >= 0:
            x_1 = (-float(values['-INB-']) + float(sqrt(dis))) / (2 * float(values['-INA-']))
            x_2 = (-float(values['-INB-']) - float(sqrt(dis))) / (2 * float(values['-INA-']))
            float(x_1)
            float(x_2)
            window['-XF-'].Update(float(x_1))
            window['-XS-'].Update(float(x_2))

        if float(dis) == 0:
            x = (-float(values['-INB-'])) / (2 * float(values['-INA-']))
            window['-XF-'].Update(float(x))

        elif float(dis) < 0:
            y = str('No Roots!')
            window['-XF-'].Update(y)
            window['-XS-'].Update(y)

window.close()
