from os.path import join
from jinja2 import Environment, PackageLoader, select_autoescape
import json

PROJECTS_PER_ROW = 4
README_SAVE_PATH = "../../ljdyer"


# ====================
def main():

    env = Environment(
        loader=PackageLoader("main"),
        autoescape=select_autoescape()
    )
    template = env.get_template('readme_template.md')

    project_info = load_json('project_info.json')
    rows = []
    while project_info:
        this_row = project_info[0:PROJECTS_PER_ROW]
        rows.append(this_row)
        project_info = project_info[PROJECTS_PER_ROW:]

    readme_md = (template.render(rows=rows))
    save_text_to_file(readme_md, join(README_SAVE_PATH, 'README.md'))


# ====================
def load_json(JSON_PATH):

    with open(JSON_PATH, 'r') as file:
        content = json.load(file)
    return content


# ====================
def save_text_to_file(text: str, file_path: str):

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)


# ====================
if __name__ == "__main__":

    main()