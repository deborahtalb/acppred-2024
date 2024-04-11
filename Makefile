setup:
	mamba env create --file environment.yml || mamba env update --file environment.yml

dirs: 
	mkdir -p data/models


preprocess:
	echo "Running data preprocessing"
	acppred-preprocess data/raw data/processed

train: dirs #nesse caso dirs é uma depedência do train 
	echo "Running model training"
	acppred-train data/processed/ data/models/model.pickle

all: preprocess train 

test: 
	pytest 
