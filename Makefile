setup:
	mamba env create --file environment.yml || mamba env update --file environment.yml

dirs: 
	mkdir -p data/models


preprocess:
	echo "Running data preprocessing"
	python acppred/preprocess.py

train: dirs #nesse caso dirs é uma depedência do train 
	echo "Running model training"
	python acppred/train.py

all: preprocess train 

test: 
	pytest 
