data(iris)
head(iris)
names(iris)
summary(iris)
sLength <- iris$Sepal.Length
pLength <- iris$Petal.Length
swidth <- iris$Sepal.Width
pwidth <- iris$Petal.Width
scaled_sLength <- scale(sLength)
scaled_pLength <- scale(pLength)
scaled_sWidth <- scale(swidth)
scaled_pWidth <- scale(pwidth)

sLength_dist <- dist(scaled_sLength, method="euclidean")
pLength_dist <- dist(scaled_pLength, method="euclidean")
sWidth_dist <- dist(scaled_sWidth, method="euclidean")
pWidth_dist <- dist(scaled_pWidth, method="euclidean")

clust_sLength <- hclust(sLength_dist, method="ward.D")
clust_pLength <- hclust(pLength_dist, method="complete")
clust_sWidth <- hclust(sWidth_dist, method="complete")
clust_pWidth <- hclust(pWidth_dist, method="complete")

plot(clust_sLength, labels=iris$Species)
rect.hclust(clust_sLength, k=3)
groups <- cutree(clust_sLength, k = 3)
print(groups)

plot(clust_pLength, labels=iris$Species)
rect.hclust(clust_pLength, k=3)
groups <- cutree(clust_pLength, k = 3)
print(groups)

plot(clust_sWidth, labels=iris$Species)
rect.hclust(clust_sWidth, k=3)
groups <- cutree(clust_sWidth, k = 3)
print(groups)

plot(clust_pWidth, labels=iris$Species)
rect.hclust(clust_pWidth, k=3)
groups <- cutree(clust_pWidth, k = 3)
print(groups)