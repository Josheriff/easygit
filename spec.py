
SPANISH_STATUS_TEXT = """
M  easygit.py
 M spec.py
?? lololo.py

"""



ENGLISH_STATUS_TEXT = """
A  easygit.py
 M spec.py
?? lololo.py
"""

with context('given a git status text'):
    with context('with modified files and unstagges files'):
        with it('separate the filenames in two lists'):
            scrapper = Scrapper()

            sut = scrapper.git_text(REPO_STATUS_TEXT)

            expected_result = {'to_be_added_in_commit': ['spec.py'], 'added_in_commit': ['easygit.py'],'new_file_to_be_added':['lololo.py']}
            expect(expected_result).to(equal(result))
