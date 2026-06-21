# Name: Hassan Abdurehman
# RN: 303-221002

"""
Task 1.1: Manual AneRBC dataset download and placement guide.

This script creates the expected raw-data folder for the AneRBC-I dataset.
The dataset is downloaded manually because large medical image files should
not be pushed to the Git repository.
"""

from pathlib import Path


def prepare_raw_data_directory(project_root: Path) -> Path:
    """
    Create the directory where the downloaded AneRBC-I dataset will be stored.

    Inputs:
        project_root (Path): Root directory of the coursework project.

    Outputs:
        Path: Location of the created AneRBC-I raw-data directory.

    Assumptions:
        The project contains a data/raw/ directory.
    """
    raw_data_path = project_root / "data" / "raw" / "AneRBC-I"
    raw_data_path.mkdir(parents=True, exist_ok=True)
    return raw_data_path


def main() -> None:
    """
    Prepare the raw-data folder and display manual placement instructions.

    Inputs:
        None.

    Outputs:
        None. Prints the expected dataset location to the terminal.

    Assumptions:
        The dataset archive is downloaded manually from the official source.
    """
    project_root = Path(__file__).resolve().parents[1]
    raw_data_path = prepare_raw_data_directory(project_root)

    print("\nAneRBC-I raw-data folder is ready.")
    print(f"Extract the downloaded dataset inside:\n{raw_data_path}")
    print("\nDo not rename, delete, or reorganize the original dataset files yet.")
    print("The next task will validate the files and inspect the actual labels.")


if __name__ == "__main__":
    main()