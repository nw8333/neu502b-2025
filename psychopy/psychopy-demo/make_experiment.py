from sys import argv
import numpy as np
import pandas as pd

subject = int(argv[1])

stimuli = ['Sam', 'Kirsten', 'Ari']
onsets = [4.0, 8.0, 10.0]

np.random.seed(subject)
trial_order = np.random.permutation(stimuli)

exp_df = {'stimuli': trial_order, 'onsets': onsets}
exp_df = pd.DataFrame(exp_df)
exp_df.to_csv(f'trials_subject-{subject}.csv', index=False)
