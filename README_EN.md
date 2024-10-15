# netflix

Aps 5

If you are going to *develop* from this repository, go to the [development guide](README_DEV.md).

## Installing netflix:

Remember to follow these instructions from within your preferred virtual environment:

    conda create -n netflix python=3.11
    conda activate netflix

The first way is to clone the repository and do a local installation:

    git clone https://github.com/carloshernani-CH/netflix.git
    cd netflix
    pip install .

The second way is to install directly:

    pip install git+https://github.com/carloshernani-CH/netflix.git

To uninstall, use:

    pip uninstall netflix

## Usage

To find all implemented commands, run:

    netflix-cli --help
