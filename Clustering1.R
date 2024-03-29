#Clustering for protein data
setwd('C:/Users/mkim/Downloads')
protein <- read.table('protein.txt', header=T, sep='\t')

#Always examine data first
names(protein)
head(protein)
summary(protein)

#Scale variables if they are not in the same
#unit of measurement (make them have mean 0 and std =1)

#features we will use to determine distances and clusters
features <- protein[,2:10]
#scale them
scaled_features <- scale(features)
#notice the new mean for each feature
summary(scaled_features)

#retain the means and std devs for each initial feature
#to be able to unscale later
#they are returned as attributes of the
#result returned by the scale() function
?scale
means <- attr(scaled_feaz
stdv <- attr(scaled_features, "scaled:scale")
print(stdv)

#Distance matrix calculation
#Use Euclidean distance
distance <- dist(scaled_features, method = "euclidean")
#this matrix contains the distance between each 2 countries
#using their coordinates in therms of the 10 food groups (features)
print(distance)

#Create hierarchical clusters
#use the distance matrix created
?hclust
hier_cl <- hclust(distance, method="ward.D")

#Plot dendogram
plot(hier_cl, labels=protein$Country)

#Separate 5 groups/clusters
rect.hclust(hier_cl, k=5)
groups <- cutree(hier_cl, k = 5)
print(groups) #each country to what group
#data wrangling to subselect the groups 
#and assign original data to each

