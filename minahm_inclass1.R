# get and set working directory
getwd()
setwd("C:\\Users\\minahm\\Documents\\School\\Fall 2014\\CMDA 3654")

#read in the data file
data<-read.csv("cars1.csv")

#get dimensions of the data
dim(data)

#get the data at cell [2,2]
var1<-data[2,2]

#get the variable names in the data frame
names(data)

#output first column
data[1]

#output second column
data[2]

#move variable "speed" into SPEED and print
SPEED<-data$speed
SPEED

#output value from row 15
data[15,]
