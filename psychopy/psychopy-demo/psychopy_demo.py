from sys import argv
from time import time
import pandas as pd
from psychopy import core, event, logging, visual

subject = int(argv[1])
print(f"Running subject {subject}")

trials = pd.read_csv(f'trials_subject-{subject}.csv').to_numpy()

run_clock = core.Clock()

logging.setDefaultClock(run_clock)
log = logging.LogFile(f=f'log_subject-{subject}.txt', level=logging.INFO, filemode='w')

start_message = "LFGGG!!!"
logging.exp(start_message)

win = visual.Window([1280, 720], screen=1, fullscr=True, color=0, name='Window')

instructions = visual.TextStim(win, pos=(0, 0), text='Send me a trigger!')
instructions.draw()
win.flip()

wait = True
while wait:
	keys = event.getKeys()
	if 'equal' in keys:
		wait = False

run_start = time()
run_clock.reset()
logging.info('Got first trigger!')

fixation = visual.TextStim(win, pos=(0, 0), text='+')
fixation.draw()
win.flip()

stimulus_duration = 1.5

for stimulus_text, onset in trials:

	stimulus = visual.TextStim(win, pos=(0, 0), text=stimulus_text)

	while time() - run_start < onset:
		fixation.draw()
		win.flip()
    
	while time() - run_start < onset + stimulus_duration:
		stimulus.draw()
		win.flip()
	
win.close()
core.quit()

