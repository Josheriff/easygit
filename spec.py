REPO_STATUS_TEXT = """En la rama master
Su rama está delante de «origin/master» para 1 commit.
  (use "git push" to publish your local commits)
Cambios no preparados para el commit:
  (use «git add <archivo>...» para actualizar lo que se confirmará)
  (use «git checkout -- <archivo>...» para descartar cambios en el directorio de trabajo)

	modificado:    command_spike.py
	modificado:    easygit.py

Archivos sin seguimiento:
  (use «git add <archivo>...» para incluir en lo que se ha de confirmar)

	.vscode/
	concepto.txt
	git_status_output.log
	spec.py

no hay cambios agregados al commit (use «git add» o «git commit -a»)
"""

##### FUNCTIONS
def split_git_text(text):
    first_double_enter = text.find('\n\n')
    second_double_enter = text.find('\n\n',first_double_enter+3)

    first_position = first_double_enter + 18 #18 spaces between jump and firs letter
    def word(position):
        last_position = text.find('\n',position)
        print(text[position:last_position])
        second_first_position = last_position

        if second_first_position < second_double_enter:
            word(second_first_position)

    word(first_position)


#### END OF FUNCTIONS



with context('given a git status text'):
    with context('with modified files and unstagges files'):
        with it('separate the filenames in two lists'):
            split_git_text(REPO_STATUS_TEXT)
