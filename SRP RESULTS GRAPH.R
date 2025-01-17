# FINAL PLOTS:

# The goal of this code is two create two plots to visualize the data 
# collected about the growth of phytoplankton under different light colours.

# Import statements:
library(tidyverse)
library(ggplot2)
library(ggthemes)

# FIRST PLOT:

SRP_DATA_FINAL$Colour <- factor(
  SRP_DATA_FINAL$Colour, levels = c("Initial", "Dark", "Green", "Red", "Blue","Sun", "White"))
ggplot(
  data = SRP_DATA_FINAL,
  mapping = aes(x = Colour, y = Chlorophyll_A), # or x = Index
) +
  geom_point(aes(color = Colour, shape = Person), size = 3) +
  labs(
    title = "Growth of Phytoplankton depending on Light Colour",
    subtitle = "Measurements were taken after 6 days of growth (except for the \
    initial measurement)",
    x = "Light Colour", y = "Chlorophyll A concentration (μg/L)"
  ) +
  scale_color_manual(
    values = c(
      "Initial" = "black",
      "Dark" = "slategray", "Green" = "chartreuse2", 
      "Red" = "coral2", "Blue" = "blue",
      "Sun" = "gold", "White" = "snow" )
  )

# SECOND PLOT:

SRP_DATA_AVERAGE_Feuil1_$Colour <- factor(
  SRP_DATA_AVERAGE_Feuil1_$Colour, levels = c("Initial", "Dark", "Green", "Red", "Blue", "Sun", "White"))
ggplot(
  data = SRP_DATA_AVERAGE_Feuil1_,
  mapping = aes(x = Colour, y = Chlorophyll_A), # or x = Index
) +
  geom_point(aes(color = Colour), size = 5) +
  labs(
    title = "Growth of Phytoplankton depending on Light Colour",
    subtitle = "Measurements were taken after 6 days of growth (except for the \
    initial measurement)",
    x = "Light Colour", y = "Average Chlorophyll A concentration (μg/L)"
  ) +
  scale_color_manual(
    values = c(
      "Initial" = "black",
      "Dark" = "slategray", "Green" = "chartreuse2", 
      "Red" = "coral2", "Blue" = "blue",
      "Sun" = "gold", "White" = "snow" )
  )
