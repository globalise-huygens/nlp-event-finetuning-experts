import pandas as pd
from get_data_selection import get_filepath_list
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

filepaths = get_filepath_list('../checking_output_40_epochs')

all_predictions = []
for filepath in filepaths:
    df = pd.read_csv(filepath,  sep='\t')
    predictions = df['prediction'].tolist()
    for prediction in predictions:
        all_predictions.append(prediction)

counted = Counter(all_predictions)
print(counted)

frequencies = list(counted.values())[1:] # take out None class
frequencies.sort()

frequencies_divided_by_5 = []
for item in frequencies:
    frequencies_divided_by_5.append(item/5)


print(frequencies_divided_by_5)
#y = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]

plt.plot(frequencies_divided_by_5, 'o-r')
plt.show()

counted_frequencies = Counter(frequencies)
print(counted_frequencies)

# create staafdiagram om klasses te vergelijken
data_20_epochs = {'Transportation': (139, 66), 'Translocation': (137, 295), 'HavingInPossession': (127, 11.4), 'Arriving': (127, 148.2), 'BeingAtAPlace': (112, 72.2),
        'Leaving': (111, 94), 'Getting': (91, 46.2), 'Enslaving': (77, 1), 'Communication': (62, 125), 'TakingUnderControl': (55, 11.8),
        'Giving': (53, 8.8), 'Request': (48, 29.8), 'Trade': (42, 1.2)}


data_30_epochs = {'Transportation': (139, 106.8), 'Translocation': (137, 195.2), 'HavingInPossession': (127, 20.4), 'Arriving': (127, 131.6), 'BeingAtAPlace': (112, 241),
        'Leaving': (111, 127), 'Getting': (91, 59.2), 'Enslaving': (77, 5.2), 'Communication': (62, 180.4), 'TakingUnderControl': (55, 31.2),
        'Giving': (53, 59.8), 'Request': (48, 72.4), 'Trade': (42, 3.4)}

data_40_epochs = {'Transportation': (139, 107.6), 'Translocation': (137, 175), 'HavingInPossession': (127, 19.6), 'Arriving': (127, 132.2), 'BeingAtAPlace': (112, 215.4),
        'Leaving': (111, 124), 'Getting': (91, 65.4), 'Enslaving': (77, 3), 'Communication': (62, 129.4), 'TakingUnderControl': (55, 26.6),
        'Giving': (53, 83.8), 'Request': (48, 64.6), 'Trade': (42, 7)}

import matplotlib.pyplot as plt
import numpy as np

categories = data_30_epochs.keys()
humanannotated = []
predicted = []
for value in data_40_epochs.values():
    humanannotated.append(value[0])
    predicted.append(value[1])

values = {'Gold' : humanannotated, 'Predicted': predicted}

x = np.arange(len(categories))  # the label locations
width = 0.3  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in values.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Amount of labels')
ax.set_title('Amount of labels in gold data compared to predictions')
ax.set_xticks(x + width, categories)
ax.legend(loc='upper left', ncols=2)
ax.set_ylim(0, 350)

ax.tick_params(axis='x', which='major', labelsize=7)


plt.show()
