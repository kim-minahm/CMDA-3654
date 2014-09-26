getwd()
setwd("C:\\Users\\minahm\\Documents\\School\\Fall 2014\\CMDA 3654")

project = read.csv("Cars93.csv")
project

#2a get numeric variables
numeric <- sapply(project, is.numeric)
summary(project[,numeric])

#2b get factor variables
factors <- sapply(project, is.factor)
project[,factors]
#3 get summaries of numeric values
summary(project[,numeric])

library(ggplot2)
library(hexbin)

#Shows the correlation between engine size and power output
ggplot(data=project, aes(x=project$EngineSize, y=project$Horsepower, group=1)) +geom_point() +
  ylim(0, max(project$Horsepower)) +
  xlab("Engine Size") + ylab("Horsepower") +
  ggtitle("Power/Displacement")

#Shows where most motor's power ratio is (120 hp/~3L)
ggplot(data=project, aes(x=project$EngineSize, y=project$Horsepower, group=1)) + stat_binhex() +geom_point() +
  ylim(0, max(project$Horsepower)) +
  xlab("Engine Size") + ylab("Horsepower") +
  ggtitle("Power/Displacement")

#Shows the relationship between weight and city fueleconomy
ggplot(data=project, aes(x=project$Weight, y=project$MPG.city, group=1)) + stat_binhex() +geom_point() +
  ylim(0, max(project$MPG.city)) +
  xlab("Weight") + ylab("City MPG") +
  ggtitle("CityMPG/weight")

write.table(project, file="TransformedData.RData")
