library(tidyverse)
library(ggplot2)
library(ggthemes)

ggplot(
  data = DATA_SRP_PROJECT,
  mapping = aes(y = Chlorophyll_A)
) +
  geom_histogram() +
  labs(
    title = "Chlorophyll A concentration of Phytoplankton depending on the light colour",
    subtitle = "Measurements were taken after 7 days of growth",
    y = "Chlorophyll A concentration (g/L)"
  )

#Idk if i made something wrong but the result is not what i imagined AT ALL but anyway
# OR: by setting each color to 1, 2, 3, 4, 5, 6 or by usinf each person's data

ggplot(
  data = DATA_SRP_PROJECT,
  mapping = aes(x = Colour, y = Chlorophyll_A),
) +
  geom_point(aes(color = Colour, shape = Person)) +
  labs(
    title = "Chlorophyll A concentration of Phytoplankton depending on the light colour",
    subtitle = "Measurements were taken after 7 days of growth",
    x = "Light colour", y = "Chlorophyll A concentration (g/L)"
  )

# The result is definitely way better, I'm gonna try to improve it again:

DATA_SRP_PROJECT$Colour <- factor(
  DATA_SRP_PROJECT$Colour, levels = c("Dark", "Green", "Red", "Blue", "Sun", "White"))
ggplot(
  data = DATA_SRP_PROJECT,
  mapping = aes(x = Colour, y = Chlorophyll_A),
) +
  geom_point(aes(color = Colour, shape = Person), size = 3) +
  labs(
    title = "Growth of Phytoplankton depending on Light Colours",
    subtitle = "Measurements were taken after 7 days of growth",
    x = "Light colour", y = "Chlorophyll A concentration (g/L)"
  ) +
  scale_color_manual(
    values = c(
      "Dark" = "black", "Green" = "lightgreen", 
      "Red" = "red", "Blue" = "skyblue1",
      "Sun" = "yellow1", "White" = "lightyellow" )
  )

# Ill maybe try other things +
  ggsave(filename = "SRP_DATA.png")


# FINAL

DATA_SRP_GRAPH_Sheet1_$Colour <- factor(
  DATA_SRP_GRAPH_Sheet1_$Colour, levels = c("Initial", "Dark", "Green", "Red", "Blue", "Sun", "White"))
ggplot(
  data = DATA_SRP_GRAPH_Sheet1_,
  mapping = aes(x = Colour, y = Chlorophyll_A), # or x = Index
) +
  geom_point(aes(color = Colour, shape = Person), size = 3) +
  labs(
    title = "Growth of Phytoplankton depending on Light Colour",
    subtitle = "Measurements were taken after 6 days of growth (except for the initial measurement)",
    x = "Light Colour", y = "Chlorophyll A concentration (μg/L)"
  ) +
  scale_color_manual(
    values = c(
      "Initial" = "black",
      "Dark" = "slategray", "Green" = "chartreuse2", 
      "Red" = "coral2", "Blue" = "blue",
      "Sun" = "gold", "White" = "snow" )
  ) +
  ggsave(filename = "SRP_DATA.png")

# Or
DATA_SRP_GRAPH_Sheet1_$Colour <- factor(
  DATA_SRP_GRAPH_Sheet1_$Colour, levels = c("Initial", "Dark", "Green", "Red", "Blue", "Sun", "White"))
ggplot(
  data = DATA_SRP_GRAPH_Sheet1_,
  mapping = aes(x = Index, y = Chlorophyll_A),
) +
  geom_point(aes(color = Colour, shape = Person), size = 4) +
  labs(
    title = "Growth of Phytoplankton depending on Light Colour",
    subtitle = "Measurements were taken after 6 days of growth (except for the initial measurement)",
    x = "Index", y = "Chlorophyll A concentration (g/L)"
  ) +
  scale_color_manual(
    values = c(
      "Initial" = "black",
      "Dark" = "slategray", "Green" = "chartreuse2",  
      "Red" = "coral2", "Blue" = "blue",
      "Sun" = "gold", "White" = "snow" )
  ) +
  geom_smooth(method = "lm") +
  ggsave(filename = "SRP_DATA.png")

# Or:

Livre$Colour <- factor(
  Livre$Colour, levels = c("Initial", "Dark", "Green", "Red", "Blue", "Sun", "White"))
ggplot(
  data = Livre,
  mapping = aes(x = Colour, y = Chlorophyll_A), # or x = Index
) +
  geom_point(aes(color = Colour, shape = Person), size = 3) +
  labs(
    title = "Growth of Phytoplankton depending on Light Colour",
    subtitle = "Measurements were taken after 6 days of growth (except for the initial measurement)",
    x = "Light Colour", y = "Chlorophyll A concentration (μg/L)"
  ) +
  scale_color_manual(
    values = c(
      "Initial" = "black",
      "Dark" = "slategray", "Green" = "chartreuse2", 
      "Red" = "coral2", "Blue" = "blue",
      "Sun" = "gold", "White" = "snow" )
  )

# or again average:
AVERAGE_SRP_DATA_1_$Colour <- factor(
  AVERAGE_SRP_DATA_1_$Colour, levels = c("Initial", "Dark", "Green", "Red", "Blue", "Sun", "White"))
ggplot(
  data = AVERAGE_SRP_DATA_1_,
  mapping = aes(x = Colour, y = Chlorophyll_A), # or x = Index
) +
  geom_point(aes(color = Colour), size = 3) +
  labs(
    title = "Growth of Phytoplankton depending on Light Colour",
    subtitle = "Measurements were taken after 6 days of growth (except for the initial measurement)",
    x = "Light Colour", y = "Chlorophyll A concentration (μg/L)"
  ) +
  scale_color_manual(
    values = c(
      "Initial" = "black",
      "Dark" = "slategray", "Green" = "chartreuse2", 
      "Red" = "coral2", "Blue" = "blue",
      "Sun" = "gold", "White" = "snow" )
  )




# FINAL CODES:
# library(tidyverse)
# library(ggplot2)
# library(ggthemes)

SRP_DATA_FINAL$Colour <- factor(
  SRP_DATA_FINAL$Colour, levels = c("Initial", "Dark", "Green", "Red", "Blue", "Sun", "White"))
ggplot(
  data = SRP_DATA_FINAL,
  mapping = aes(x = Colour, y = Chlorophyll_A), # or x = Index
) +
  geom_point(aes(color = Colour, shape = Person), size = 3) +
  labs(
    title = "Growth of Phytoplankton depending on Light Colour",
    subtitle = "Measurements were taken after 6 days of growth (except for the initial measurement)",
    x = "Light Colour", y = "Chlorophyll A concentration (μg/L)"
  ) +
  scale_color_manual(
    values = c(
      "Initial" = "black",
      "Dark" = "slategray", "Green" = "chartreuse2", 
      "Red" = "coral2", "Blue" = "blue",
      "Sun" = "gold", "White" = "snow" )
  )

# AVERAGE:

SRP_DATA_AVERAGE_Feuil1_$Colour <- factor(
  SRP_DATA_AVERAGE_Feuil1_$Colour, levels = c("Initial", "Dark", "Green", "Red", "Blue", "Sun", "White"))
ggplot(
  data = SRP_DATA_AVERAGE_Feuil1_,
  mapping = aes(x = Colour, y = Chlorophyll_A), # or x = Index
) +
  geom_point(aes(color = Colour), size = 5) +
  labs(
    title = "Growth of Phytoplankton depending on Light Colour",
    subtitle = "Measurements were taken after 6 days of growth (except for the initial measurement)",
    x = "Light Colour", y = "Average Chlorophyll A concentration (μg/L)"
  ) +
  scale_color_manual(
    values = c(
      "Initial" = "black",
      "Dark" = "slategray", "Green" = "chartreuse2", 
      "Red" = "coral2", "Blue" = "blue",
      "Sun" = "gold", "White" = "snow" )
  )

# AVERAGE WITHOUT OUTLIER

SRP_DATA_OUTLIERS_Feuil1_$Colour <- factor(
  SRP_DATA_OUTLIERS_Feuil1_$Colour, levels = c("Dark", "Green", "Red", "Blue", "Sun", "White"))
ggplot(
  data = SRP_DATA_OUTLIERS_Feuil1_,
  mapping = aes(x = Colour, y = Chlorophyll_A), # or x = Index
) +
  geom_point(aes(color = Colour), size = 5) +
  labs(
    title = "Growth of Phytoplankton depending on Light Colour",
    subtitle = "Measurements were taken after 6 days of growth (except for the initial measurement)",
    x = "Light Colour", y = " Average Chlorophyll A concentration (μg/L)"
  ) +
  scale_color_manual(
    values = c(
      "Dark" = "slategray", "Green" = "chartreuse2", 
      "Red" = "coral2", "Blue" = "blue",
      "Sun" = "gold", "White" = "snow" )
  )

# maybe add an outline to the white point

# Another one

SRP_DATA_OUTLIERS_Feuil1_2_$Colour <- factor(
  SRP_DATA_OUTLIERS_Feuil1_2_$Colour, levels = c("Dark", "Green", "Red", "Blue", "Sun", "White"))
ggplot(
  data = SRP_DATA_OUTLIERS_Feuil1_2_,
  mapping = aes(x = Colour, y = Chlorophyll_A), # or x = Index
) +
  geom_point(aes(color = Colour), size = 5) +
  labs(
    title = "Growth of Phytoplankton depending on Light Colour",
    subtitle = "Measurements were taken after 6 days of growth (except for the initial measurement)",
    x = "Light Colour", y = " Average Chlorophyll A concentration (μg/L)"
  ) +
  scale_color_manual(
    values = c(
      "Dark" = "slategray", "Green" = "chartreuse2", 
      "Red" = "coral2", "Blue" = "blue",
      "Sun" = "gold", "White" = "snow" )
  ) 



# test

p1 <- SRP_DATA_OUTLIERS_Feuil1_2_$Colour <- factor(
  SRP_DATA_OUTLIERS_Feuil1_2_$Colour, levels = c("Dark", "Green", "Red", "Blue", "Sun", "White"))
ggplot(
  data = SRP_DATA_OUTLIERS_Feuil1_2_,
  mapping = aes(x = Colour, y = Chlorophyll_A), # or x = Index
) +
  geom_point(aes(color = Colour), size = 5) +
  labs(
    title = "Growth of Phytoplankton depending on Light Colour",
    subtitle = "Measurements were taken after 6 days of growth (except for the initial measurement)",
    x = "Light Colour", y = " Average Chlorophyll A concentration (μg/L)"
  ) +
  scale_color_manual(
    values = c(
      "Dark" = "slategray", "Green" = "chartreuse2", 
      "Red" = "coral2", "Blue" = "blue",
      "Sun" = "gold", "White" = "snow" )
  ) 

p2 <- SRP_DATA_FINAL$Colour <- factor(
  SRP_DATA_FINAL$Colour, levels = c("Initial", "Dark", "Green", "Red", "Blue", "Sun", "White"))
ggplot(
  data = SRP_DATA_FINAL,
  mapping = aes(x = Colour, y = Chlorophyll_A), # or x = Index
) +
  geom_point(aes(color = Colour, shape = Person), size = 3) +
  labs(
    title = "Growth of Phytoplankton depending on Light Colour",
    subtitle = "Measurements were taken after 6 days of growth (except for the initial measurement)",
    x = "Light Colour", y = "Chlorophyll A concentration (μg/L)"
  ) +
  scale_color_manual(
    values = c(
      "Initial" = "black",
      "Dark" = "slategray", "Green" = "chartreuse2", 
      "Red" = "coral2", "Blue" = "blue",
      "Sun" = "gold", "White" = "snow" )
  )
  
p1 + p2

#or
SRP_DATA_FINAL_GRAPH_Feuil1_$Colour <- factor(
  SRP_DATA_FINAL_GRAPH_Feuil1_$Colour, levels = c("Initial", "Dark", "Green", "Red", "Blue", "Sun", "White"))
ggplot(
  data = SRP_DATA_FINAL_GRAPH_Feuil1_,
  mapping = aes(x = Colour, y = Chlorophyll_A), # or x = Index
) +
  geom_point(aes(color = Colour, shape = Person), size = 5) +
  labs(
    title = "Growth of Phytoplankton depending on Light Colour",
    subtitle = "Measurements were taken after 6 days of growth (except for the initial measurement)",
    x = "Light Colour", y = "Chlorophyll A concentration (μg/L)"
  ) +
  scale_color_manual(
    values = c(
      "Initial" = "black",
      "Dark" = "slategray", "Green" = "chartreuse2", 
      "Red" = "coral2", "Blue" = "blue",
      "Sun" = "gold", "White" = "snow" )
  )