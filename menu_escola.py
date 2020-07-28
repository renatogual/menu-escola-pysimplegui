import PySimpleGUI as sg

sg.theme('DarkAmber') # Tema da janela da interface gráfica

class MenuEscola():
    def __init__(self):
        self.notas = {} # Variavel que armazena os dados 
        # layout da janela principal
        layout = [
            [sg.Button('Inserir aluno e nota', size=(50,2))],
            [sg.Button('Alterar a nota de um aluno', size=(50,2))],
            [sg.Button('Consultar nota de um aluno específico', size=(50,2))],
            [sg.Button('Apagar um aluno da lista', size=(50,2))],
            [sg.Button('Mostrar a média da turma', size=(50,2))],
            [sg.Button('Exibir lista de alunos com suas notas', size=(50,2))],
            [sg.Button('Sair', size=(50,2))]
        ]
        # Instancia do objeto janela com o layout
        self.window = sg.Window('Menu de Notas', layout)


    def menu(self): # Menu do programa onde chama todas as outras funções
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Sair':
                break
            elif event == 'Inserir aluno e nota':
                self.inserir_aluno()
            elif event == 'Alterar a nota de um aluno':
                self.alterar_nota()
            elif event == 'Consultar nota de um aluno específico':
                self.consulta_nota()
            elif event == 'Apagar um aluno da lista':
                self.apagar_aluno()
            elif event == 'Mostrar a média da turma':
                self.media_turma()
            elif event == 'Exibir lista de alunos com suas notas':
                self.exibir_alunos()
        self.window.close()

    def inserir_aluno(self):
        nome = sg.popup_get_text('Nome')
        if self.notas.get(nome):
            sg.PopupError(f'Nome {nome} já existe')
        elif nome is None:
            pass
        else:
            nota = (sg.popup_get_text('Nota'))
            self.notas[nome] = int(nota)

    def alterar_nota(self):
        nome = sg.popup_get_text('Nome')
        if nome in self.notas.keys():
            nota = int(sg.popup_get_text('Nota'))
            self.notas[nome] = nota
        elif nome is None:
            pass
        else:
            sg.PopupError(f'Nome {nome} não existe na lista')

    def consulta_nota(self):
        nome = sg.popup_get_text('Nome')
        if nome in self.notas.keys():
            sg.Print(f'Nota de {nome}: ', self.notas[nome])
        elif nome is None:
            pass
        else:
            sg.PopupError(f'Nome {nome} não existe na lista')

    def apagar_aluno(self):
        nome = sg.popup_get_text('Nome')
        if nome in self.notas.keys():
            self.notas.pop(nome)
        elif nome is None:
            pass
        else:
            sg.PopupError(f'Nome {nome} não existe na lista')

    def media_turma(self):
        soma = 0
        for val in self.notas.values():
            soma += val
            media = soma / len(self.notas)   

        return sg.Popup(f'A média da turma é: {media}', title='Média')
        
    def exibir_alunos(self):
        for nome in self.notas.keys():
            sg.Print(nome, 'tirou a nota: ', self.notas[nome], no_titlebar=True)
            
        
# Roda o programa locamente no caso deste modulo ser importado para outro script
if __name__ == "__main__":
    Notas = MenuEscola()
    Notas.menu()





