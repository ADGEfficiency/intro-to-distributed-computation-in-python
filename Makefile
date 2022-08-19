setup:
	pip install -U pip
	pip install -r requirements-coiled.txt

mermaid:
	mmdc -i ./assets/scaling.mmd -o ./assets/scaling.svg

dev:
	pip install -q jupyterlab-vim jupyterlab-spellchecker
