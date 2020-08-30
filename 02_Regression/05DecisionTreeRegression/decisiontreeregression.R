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


# Fitting  Regression Model to the dataset
#install.packages('rpart')
library(rpart)
regressor = rpart(formula = Salary ~ .,
                  data = dataset,
                  control = rpart.control(minsplit = 1))

# Predicting a new result with  Regression
y_pred = predict(regressor, data.frame(Level = 6.5))



# Visulaising the  Decision Tree Regression Model results
# install.package('ggplot2')
library(ggplot2)
ggplot() + 
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = 'red') + 
  geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)),
            color = 'blue') + 
  ggtitle('Truth or Bluff (Decision Tree Regression)')  + 
  xlab('Level') + 
  ylab('Salary')

# Visulaising the  Decision Tree Regression Model results (for higher resoultion and smoother curve)
# install.package('ggplot2')
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.01)
ggplot() + 
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = 'red') + 
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid))),
            color = 'blue') + 
  ggtitle('Truth or Bluff (Decision Tree Regression)')  + 
  xlab('Level') + 
  ylab('Salary')


