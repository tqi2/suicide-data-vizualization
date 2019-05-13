#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 04:11:35 2019

@author: tianqiluke
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
df = pd.read_csv("../input/master.csv")

#histo
plt.hist(df.suicides_no, bins=100, density=True)
plt.title("Suicides Number Distribution for 31 Years")
plt.xlabel("Suicides Number")

#bar
plt.figure(figsize=(10,5))
sns.barplot(x = "age", y = "suicides/100k pop", hue = "sex",data = first_obs.groupby(["age","sex"]).sum().reset_index()).set_title("Age vs Suicides")
plt.xticks(rotation = 90)

#heatmap
sns.jointplot("Suicides100kPop", "SuicidesNo", data=data[data['Country']=='Russian Federation'], kind="kde",space=10,color='g')
# plt.title("Heat Map of Suicides Number on Population",loc="right",pad=10)
plt.show()