# dh-401-rhythm-generation-group-2

Our work is located inside the 'final_notebook.ipynb' Jupyter Notebook.

Our outputs are located inside Dataframes saved as csv files: 'random_songs.csv' for the random model and 'markov_songs.csv' for the generation model. We have then converted these outputs into 500 midi files for each model: these are located in the folder "./random_rhythms" for the random model and "./generated_rhythms" for the Markov model.

./abc contains copies of the abc files of the original dataset 

The other csv files correspond to the training data, test data... according to their names. The reason we have some files named "\*_all.csv" is due to 1 or 2 pieces in the original csv files containing empty bars. These pieces caused bugs in the metric evaluation, and thus we removed them to create the "\*_all.csv" files used in parts of the evaluation.
