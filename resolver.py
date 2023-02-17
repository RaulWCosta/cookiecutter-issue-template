from cookiecutter.main import cookiecutter
from pathlib import Path



def run():
    for template_folder in ["template", "template2"]:

        cookiecutter(
            template=str(Path("cookiecutter_resolver/" + template_folder)),
            output_dir=str(Path("cookiecutter_resolver/target/" + template_folder)),
            overwrite_if_exists=True,
            skip_if_file_exists=True,
            no_input=True,
        )

run()