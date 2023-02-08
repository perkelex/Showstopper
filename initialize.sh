if [ ! -d  .venv ]; then
    echo "Creating python virtual environment .venv"
    python -m venv .venv
fi

echo "Activating virtual environment"
source .venv/Scripts/activate

echo "Updating .venv pip"
python -m pip install -U pip wheel setuptools

echo "Installing project requirements in .venv"
pip install -r requirements.txt

echo "Initialization done!"