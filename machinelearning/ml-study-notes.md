# ML study notes

## 모두를 위한 머신러닝/딥러닝 강의
- [Lecture](http://hunkim.github.io/ml/)
- [Code](https://github.com/AWEEKJ/ML-study)


### Lecture 1: Machine Learning Basics

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

### Lecture 2: Linear Regression

- 이미 존재하는 데이터(training data set)로 Regression model을 학습시킴(training)
- 세상의 많은 현상들이 리니어한 모델로 설명할 수 있다! 
- (Linear) Hypothesis: H(x) = Wx+b
- Which hypothesis is better? => Cost Function(Loss Function)
- cost(W, b) = average of (H(x)-y)^2
- Goal: Minimize cost(W, b)

### Lecture 3: How to minimize cost

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

### Lecture 4: Multi-variable linear regression

#### Multi-variable/feature

- represent as matrix
- H(X) = W* X
- H(X) = W transpose * X