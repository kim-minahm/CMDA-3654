getwd()
#setwd("C:\\Users\\minahm\\Documents\\school\\CMDA")
data<-read.table("prices.txt",col.names=c("PRICE","SQFT","AGE","NE"),header=T)
data

#like col.names, row.names will assign a variable name to each row


table<-read.table("data.txt", col.names=c("A","B","C"),header = F)
table
