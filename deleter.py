from re import search
from docx import Document


def del_p(pattern, *doc_fps, prompt=True):
    if not pattern:
        return None

    stop = False
    for doc_fp in doc_fps:
        if stop:
            break
        doc = Document(doc_fp)
        for paragraph in doc.paragraphs:
            if search(pattern, paragraph.text):
                if prompt:
                    print('\n', paragraph.text, '\n')
                    print('Enter d to delete.', 'Enter s to stop.', 'Enter n to skip to the next document',
                          'Enter anything else to skip to the next paragraph.', sep='\n')
                    code = input().lower().strip()
                    if code == 'd':
                        p = paragraph._element
                        p.getparent().remove(p)
                        doc.save(doc_fp)
                    elif code == 's':
                        stop = True
                        break
                    elif code == 'n':
                        break

                else:
                    print('Deleting:', paragraph.text)
                    p = paragraph._element
                    p.getparent().remove(p)

        if prompt:
            print('All done!')
            del_p(input('Enter another pattern:\n'), *doc_fps)
        else:
            doc.save(doc_fp)
