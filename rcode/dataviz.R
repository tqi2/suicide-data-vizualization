library(tidyverse) 
library(ggalt) 
library(countrycode) 
library(rworldmap) 
library(gridExtra) 
library(broom) 

theme_set(theme_light())
ggplot(demographic_most, aes(x = age, y = suicides_per_100k, col = sex)) + 
  geom_jitter(alpha = 0.5) + 
  labs(title = "5% Most At-Risk Instances in History", 
       subtitle = "Instances by Decade, Age, & Sex",
       x = "Age", 
       y = "Suicides per 100k", 
       col = "Sex") + 
  facet_wrap(~ time) + 
  scale_y_continuous(breaks = seq(50, 300, 10))