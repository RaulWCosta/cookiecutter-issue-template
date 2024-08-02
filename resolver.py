from cookiecutter.main import cookiecutter
from pathlib import Path



def run():
    for template_folder in ["template", "template2"]:

        cookiecutter(
            template=str(Path(template_folder)),
            output_dir=str(Path("target/" + template_folder)),
            overwrite_if_exists=True,
            skip_if_file_exists=True,
            no_input=True,
        )
if __name__ == "__main__":
    run()
