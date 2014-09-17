
getwd()
setwd("C:\\Users\\minahm\\Documents\\School\\Fall 2014\\CMDA 3654")

load('phsample.RData')
#The data is an anonymized dataset of a person/household containing the information
#Age, Employment class, Education Level, Sex of Worker

#Selects a subset that is self-described fulltime
#working 40 hours a week atleast
#20 to 50 years of age
#income between $1000 nd $250000
psub = subset(dpus,with(dpus,(PINCP>1000)&(ESR==1)&
                          (PINCP<=250000)&(PERNP>1000)&(PERNP<=250000)&
                          (WKHP>=40)&(AGEP>=20)&(AGEP<=50)&
                          (PWGTP1>0)&(COW %in% (1:7))&(SCHL %in% (1:24))))
#Reencodes sex from 1/2 to M/F
psub$SEX = as.factor(ifelse(psub$SEX==1,'M','F'))
#Sets reference of sex to M, so when graphing M and F are differentiated
psub$SEX = relevel(psub$SEX,'M')
cowmap <- c("Employee of a private for-profit",
            "Private not-for-profit employee",
            "Local government employee",
            "State government employee",
            "Federal government employee",
            "Self-employed not incorporated",
            "Self-employed incorporated")
#Refactors class of worker so it can be better accessed 
psub$COW = as.factor(cowmap[psub$COW])
psub$COW = relevel(psub$COW,cowmap[1])
#education is reencoded to be more readable
schlmap = c(
  rep("no high school diploma",15),
  "Regular high school diploma",
  "GED or alternative credential",
  "some college credit, no degree",
  "some college credit, no degree",
  "Associate's degree",
  "Bachelor's degree",
  "Master's degree",
  "Professional degree",
  "Doctorate degree")
psub$SCHL = as.factor(schlmap[psub$SCHL])
psub$SCHL = relevel(psub$SCHL,schlmap[1])
#gets subset of data for training purposes 
dtrain = subset(psub,ORIGRANDGROUP >= 500)
#Data subset used for testing
dtest = subset(psub,ORIGRANDGROUP < 500)
summary(dtrain$COW)

project = read.csv("Cars93.csv")
project
