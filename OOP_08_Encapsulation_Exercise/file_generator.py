import os


def get_filepath(filename):
    return f"{work_dir}/{filename}"


def create_file(args):
    filename = args[0]
    with open(get_filepath(filename), 'w') as f:
        f.write(f"class {filename}:\n"
                f"  def __init__(self):"
                f"      pass"
                )
        print('File created/truncated')


def delete_file(args):
    filename = args[0]
    try:
        os.remove(get_filepath(filename))
        print('File deleted')
    except FileNotFoundError:
        print('An error occurred')


def add_content(args):
    filename, content = args
    try:
        with open(get_filepath(filename), 'a') as file:
            file.write(content + '\n')

    except FileNotFoundError:
        print('An error occurred')


def replace_content(args):  # Replace-EN01_Wild_Cat_Zoo_INES.txt-^-&
    filename, old_str, new_str = args
    try:
        with open(get_filepath(filename), 'r+') as file:
            text = file.read()
            text = text.replace(old_str, new_str)
            file.seek(0)
            # file.truncate()  # only if opened 'w+'
            file.write(text)

    except FileNotFoundError:
        print('An error occurred')


mapper = {
    'add': add_content,
    'replace': replace_content,
    'create': create_file,
    'delete': delete_file,
}

work_dir = input('Enter working directory: ').lower()
command = input().split(' ')
while command[0] != "End":
    command, *rest_as_list = command
    mapper[command.lower()](rest_as_list)
    command = input().split(' ')
