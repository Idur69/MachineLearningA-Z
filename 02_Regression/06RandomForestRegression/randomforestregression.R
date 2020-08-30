# Polynomial Regressio template

# Importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

# Encoding the categorical data
#dataset$State = factor(dataset$State,
#                      levels = c('New York','California', 'Florida'),
#                      labels = c(1,2,3))

# Spliting the dataset into the Training set and Test set
# install.packages('çaTools')
#library(caTools)
#set.seed(123)
#split = sample.split(dataset$Profit, SplitRatio = 0.8)
#training_set = subset(dataset, split == TRUE)
#test_set = subset(dataset, split == FALSE)

# Feature Scaling
#training_set = scaler(training_set)
#test_set = scaler(test_set)


# Fitting Random Forest   Regression Model to the dataset
#install.packages('randomForest')
library(randomForest)
set.seed(1234)
regressor = randomForest(x = dataset[1],
                         y = dataset$Salary,
                         ntree = 500)

# Predicting a new result with  Regression



# Visulaising the Radom Forest Regression Model results (for higher resoultion and smoother curve)
# install.package('ggplot2')
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.01)
ggplot() + 
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = 'red') + 
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid))),
            color = 'blue') + 
  ggtitle('Truth or Bluff (Random Forest  Regression)')  + 
  xlab('Level') + 
  ylab('Salary')


