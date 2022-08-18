setup:
	pip install -r requirements.txt

mermaid:
	mmdc -i ./assets/scaling.mmd -o ./assets/scaling.svg

dev:
	pip install -q jupyterlab-vim jupyterlab-spellchecker

conda:
	conda create -n coiled -c conda-forge python=3.9 
	conda activate coiled; pip install "prefect[aws]" coiled-runtime "dask[complete]" requests
	conda activate coiled; conda export env >> environment.yml
