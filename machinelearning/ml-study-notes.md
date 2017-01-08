# ML study notes

## 모두를 위한 머신러닝/딥러닝 강의
- [Lecture](http://hunkim.github.io/ml/)
- [Code](https://github.com/AWEEKJ/ML-study)


### [Lecture 1: Machine Learning Basics](http://hunkim.github.io/ml/lec1.pdf)

- What is ML?
- What is learning?
  - supervised
  - unsupervised
- What is regression?
- What is classification?

#### Machine Learning

- explicit programming(ex. a일 때는 b를 하라) 의 한계
- ML: "Field of study that gives computers the ability to learn without being explicitly programmed" by Arthur Samuel

#### Supervised/Unsupervised learning

- Supervised learning:
  - 레이블이 정해져 있는 데이터(training set)으로 학습
- Unsupervised learning:
  - un-labeled data
  - ex. 구글 뉴스 그룹핑, 단어의 분류 Word clustering

#### Supervised Learning

- Most common problem type in ML
- 이미 트레이닝 셋이 있음, 새로운 셋을 트레이닝 데이타 셋을 기반으로 분류

#### Types of supervised learning

1. Predicting final exam score based on time spent => **regression**
2. Pass/non-pass based on time spent => **binary classification**
3. Letter grade (A, B, C, D and F) based on time spent => **multi-label classification**



### [Lecture 2: Linear Regression](http://hunkim.github.io/ml/lec2.pdf)

- 이미 존재하는 데이터(training data set)로 Regression model을 학습시킴(training)
- 세상의 많은 현상들이 리니어한 모델로 설명할 수 있다! 
- (Linear) Hypothesis: H(x) = Wx+b
- Which hypothesis is better? => Cost Function(Loss Function)
- cost(W, b) = average of (H(x)-y)^2
- Goal: Minimize cost(W, b)

### [Lecture 3: How to minimize cost](http://hunkim.github.io/ml/lec3.pdf)

#### Simplified Hypothesis

#### Gradient descent algorithm

- 경사를 따라 내려가는 알고리즘
- Minimize cost function
- Gradient descent is used many minimization problems
- For a given cost function, cost(W, b), it will find W, b to minimize cost
- It can be applied to more general function: cost(W1, W2, ...)

#### How it works? How would you find thd lowest point?

- Start with initial guesses
  - Start at (0,0) (or any other value) *아무 점에서 시작한다.*
  - Keeping changing W and b a little bit to try and reduce cost(W, b) 
- Each time you change the parameters, you select the gradient which reduces cost(W, b) the most possible
- Repeat
- Do so until you converge to a local minimum
- Has an interesting property
  - Where you start can determine which minimum you end up
- 기울기는 미분해서 구한다. 기울기 < 0 이면 W를 크게, 기울기 > 0 이면 W를 작게 만든다.
- cost(W, b)를 설계할 때 그 모양이 Convex function인지를 확인하라.
- Convex function: 밥그릇 모양. Gradient descent algorithm을 사용할 때, 초기값으로 무엇을 주더라도 같은 결과가 나온다.



### [Lecture 4: Multi-variable linear regression](http://hunkim.github.io/ml/lec4.pdf)

#### Multi-variable/feature

- represent as matrix
- H(X) = W* X
- H(X) = W transpose * X



### [Lecture 5-1: Logistic (regression) classification](http://hunkim.github.io/ml/lec5.pdf) 

#### (Binary) Classification Application

- Spam Detection: Spam(1) or Ham(0)
- Facebook feed: show(1) or hide(0)
- Credit Card Fraudulent Transaction detection: legitimate(0) / fraud(1)

#### Example Model: Pass(1)/Fail(0) based on study hours

- Linear Regression?
- We know Y is 0 or 1
- Hypothesis can give values large than 1 or less than 0
- => Use Sigmate Fuction!

#### Sigmoid Function

-  Curved in two directions, like the letter "S"



### [Lecture 5-2: Logistic (regression) classification - cost function & gradient decent](http://hunkim.github.io/ml/lec5.pdf)



- 어디서 시작하느냐에 따라서 최저점이 달라질 수 있다 -> Local Minimum
- Global Minimum을 찾아야 한다!

#### New cost function for logistic!



### [Lecture 6-1: Softax classification - Multinomial classification](http://hunkim.github.io/ml/lec6.pdf) 



### [Lecture 6-2: Softmax classification - Cross entry cost function & gradient decent](http://hunkim.github.io/ml/lec6.pdf)



- Cross entropy cost function
- Logistic cost vs cross entropy




### [Lecture 7-1: Application & Tips - Learning rate, data preprocessing, overfitting](http://hunkim.github.io/ml/lec7.pdf)

#### Learning Rate

- Large learning rate: overshooting
- Small learning rate: takes too long, stops at local minimum
- Try several learning rates
  - Observe the cost function
  - Check it goes down in a reasonable rate

#### Date preprocessing for gradient descent

- Original data -> Zero-centered data -> Normalized data

#### Overfitting

- 학습 데이터에 너무 잘 맞는(overfitting) 모델. 실제 데이터나 테스트 데이터를 적용하면 잘 안맞는 경우가 발생.
- Solutions for overfitting
  - More training data
  - Reduce the number of features
  - Regularization

##### Regularization

- Let's not have too big numbers in the weight



### [Lecture 7-2: Application & Tips - Learning and test data sets](http://hunkim.github.io/ml/lec7.pdf)

- Training sets -> Validation sets -> Test sets
- Online learning

#### Accuracy

- How many of your predictions are correct?
- 95~99%