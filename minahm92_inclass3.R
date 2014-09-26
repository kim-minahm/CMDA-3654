
getwd()
setwd("C:\\Users\\minahm\\Documents\\School\\Fall 2014\\CMDA 3654")

load("exampleData1.RData")

merge.income <- merge(medianincome,custdata)
norm.income <- merge.income$Income/merge.income$Median.Income
summary(norm.income)

merge.income$gp <- runif(dim(merge.income)[1])
head(merge.income$gp)

testSet <- subset(merge.income, merge.income$gp <= 0.3)
trainingSet <- subset(merge.income, merge.income$gp > 0.3)
