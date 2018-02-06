

STATUS_TEXT = """A  .gitignore
 M command_spike.py
 M easygit.py
?? .easygit.py.swp
?? concepto.txt
?? git_status_output.log
?? spec.py
"""

with context('given a git status text'):
    with context('with modified files and unstagges files'):
        with it('separate the filenames in two lists'):
            split_git_text(REPO_STATUS_TEXT)
