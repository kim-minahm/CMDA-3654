#Minahm Kim
#9/2/2014
#CMDA 3654 12:25 TR
#Homework 1

getwd()
setwd("C:\\Users\\minahm\\Documents\\school\\Fall 2014\\CMDA 3654")

#Problem 2
#data has the assigned names as variables
data<-read.table("prices.txt",col.names=c("PRICE","SQFT","AGE","NE"),header=T)
#data1 has the variable names assigned as the first entry, and the variable anmes are just v1 v2 v3 v4
data1<-read.table("prices.txt",header=F)

#7 like col.names, row.names will assign a variable name to each row

table<-read.table("data.txt", col.names=c("A","B","C"),header = F)
table

#Problem 2
problem<-cbind(c(1,0,0,0),c(0,1,0,0),c(0,0,1,0),c(0,0,0,1))
problem<-problem*diag(4)
problem[4,4]
t(problem)
solve(problem)

#Problem 3
fpe <- read.table("http://data.princeton.edu/wws509/datasets/effort.dat")
#print out data sets with only 0 effort
fpe[fpe$effort==0,]
names(fpe)
row.names(fpe)
#head is a function that prints the beginning of a data structer. Default length is 6, it can be set as a parameter
#head(fpe,1)
write.table(fpe,"fpe.txt")
write.table(fpe,"fpe.csv")
