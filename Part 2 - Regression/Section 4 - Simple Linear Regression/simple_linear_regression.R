# Data preprocessing
dataset = read.csv('Salary_Data.csv')
#dataset = dataset[, 2:3]

# Splitting the data into the training and test data sets
#install.packages('caTools')
set.seed(123)
split = sample.split(dataset$YearsExperience, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature scaling
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])