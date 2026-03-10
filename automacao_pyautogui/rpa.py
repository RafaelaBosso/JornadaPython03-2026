# Automação para preencher formulário em https://rpaexercise.aisingapore.org/login

import pandas
import pyautogui
pyautogui.PAUSE = 0.3

#mostrar a tabela
tabela = pandas.read_csv('datatable.csv')
print(tabela)

# Abrir o navegador


pyautogui.press('win')
pyautogui.write('firefox')
pyautogui.press('enter')

pyautogui.sleep(3) # Esperar o navegador carregar

# Acessar o site

pyautogui.write('https://rpaexercise.aisingapore.org/login', interval=0.05)
pyautogui.press('enter')

pyautogui.sleep(3) # Esperar o site carregar

# Fazer login

pyautogui.moveTo(852, 344)
pyautogui.click()
pyautogui.write('jane007', interval=0.05)
pyautogui.press('tab')
pyautogui.write('TheBestHR123', interval=0.05)
pyautogui.press('enter')

pyautogui.sleep(3) # Esperar o login ser processado

# Inserir todas as informações de um cadastro

# Pyautogui.write – Comando para escrever
# Str – É um comando para transformar em string (texto)
# .loc – É um comando para buscar uma informação, nesse caso dentro da nossa tabela. 
# Então vamos buscar uma informação na linha x (dependendo de quantas vezes estamos repetindo) na coluna “codigo

x = 0

for linha in tabela.index:
    pyautogui.moveTo(941,265) 
    pyautogui.click()
    for clicks in range(2):
        pyautogui.press('tab')
    
    # Preenche "Job Title"
    pyautogui.write(str(tabela.loc[linha, 'jobTitle']), interval=0.05)
    pyautogui.press('tab')

    # Preenche "Job Description"
    pyautogui.write(str(tabela.loc[linha, 'jobDescription']), interval=0.05)
    pyautogui.press('tab')

    # Preenche "Hiring Department"
    pyautogui.press('space')  # Pressiona espaço para abrir o dropdown de departamentos
    if (tabela.loc[linha, 'hiringDepartment']) == 'Bussiness Development':
        pyautogui.press('down')
        pyautogui.press('enter')
    elif (tabela.loc[linha, 'hiringDepartment']) == 'Engineering':
        for clicks in range(2):
            pyautogui.press('down')
        pyautogui.press('enter')
    elif (tabela.loc[linha, 'hiringDepartment']) == 'Finance':
        for clicks in range(3):
            pyautogui.press('down')
        pyautogui.press('enter')
    elif (tabela.loc[linha, 'hiringDepartment']) == 'Human Resource':
        for clicks in range(4):
            pyautogui.press('down')
        pyautogui.press('enter')
    else:
        for clicks in range(5):
            pyautogui.press('down')
        pyautogui.press('enter')
    pyautogui.press('tab')

    # Preenche "Education Level"
    # Bug
    pyautogui.press('space')  # Pressiona espaço para abrir o dropdown de departamentos
    if (tabela.loc[linha, 'educationLevel']) == 'Diploma':
        pyautogui.press('down')
        pyautogui.press('enter')
    else:
        for clicks in range(2):
            pyautogui.press('down')
        pyautogui.press('enter')
    pyautogui.press('tab')

    # Preenche "Posting Start Date"
    # Bug 
    pyautogui.write((tabela.loc[linha, 'postingStartDate']), interval=0.05)
    for clicks in range(2):
        pyautogui.press('tab')

    # Preenche "Posting End Date"
    # Bug
    pyautogui.write((tabela.loc[linha, 'postingEndDate']), interval=0.05)
    for clicks in range(2):
        pyautogui.press('tab')

 
    # Preenche "Remote"
    if tabela.loc[linha, 'remote'] == 'Yes':
        pyautogui.press('enter')  # Pressiona espaço para marcar a checkbox
    else:
        pyautogui.press('down')  # Pressiona espaço para marcar a checkbox
        pyautogui.press('enter')
    pyautogui.press('tab')

    # Preenche "Job Type"
    # Bug
    job = (str(tabela.loc[linha, 'jobType']))
    i=0
    if job in ['Full-time', 'Full-time/Permanent', 'Full-time/Temp']:
        pyautogui.press('space')
        for clicks in range(2):
            pyautogui.press('tab')
    else:
        pyautogui.press('tab')
        pyautogui.press('space')
        pyautogui.press('tab')
    
    if job in ['Temp', 'Full-time/Temp', 'Part-time/Temp']:
        pyautogui.press('space')
        pyautogui.press('tab')
    elif job in ['Full-time', 'Part-Time']:
        pyautogui.press('tab')
    else:
        pyautogui.press('tab')
        pyautogui.press('space')
    
    # Enviar as informações para o sistema
    for clicks in range(2):
            pyautogui.press('tab')
    pyautogui.press('space')
    
    x+=1

    pyautogui.sleep(3.5) # Esperar o cadastro ser processado

pyautogui.alert('Processo finalizado!')
