Title: Visualizing Diabetes Risk with d3.js
Date: 2015-02-23 13:08
Category: blog
Tags: logistic regression, d3.js, data visualization
Author: Michael Moliterno
Summary: Visualizing Type 2 Diabetes Risk with a multivariate logistic regression using d3.js

### Predicting the Risk of Type 2 Diabetes
I recently revisited [an old Kaggle competition](https://www.kaggle.com/c/pf2012-diabetes) that challenged entrants to use electronic health records (EHR) from Practice Fusion's database to identify patients diagnosed with Type 2 Diabetes. Given a set of ~10,000 electronic health records, I developed a set of classifiers for Type 2 Diabetes (an article on this analysis will be posted shortly).  While my models were not as good as the winning models, I was happy with my results; I think would have placed in about the middle of the leaderboard if I had entered when the competition was active.

### Visualizing Classifiers
One of the challenges in using machine learning is communicating results to non-data-nerds.   Support Vector Machines (SVMs) and random forests are nearly impossible to visualize in high dimensions.  Decision trees are fairly easy so visualize, but not useful in many cases.  

As I was mulling over ideas for visualizations to build in d3.js, I came up with an idea for visualizing a multivariate logistic regression.  By keeping one variable on an axis (in this case BMI), and allowing other variables to be modified with sliders (e.g. age) and radio buttons (e.g. gender), we can see the shape of the logistic regression curve (which we can think of as a risk profile for Type 2 Diabetes).   


###Logistic Regression with d3.js
Check out the visualization I built below.  Some of the features that took a bit of time to build were:
* the brush on the bottom that allows you to zoom into a smaller range on the BMI axis
* the updating values on each axis (when the brush is created and moved)
* the values (and tracking ball/line) that follow your mouse on the screen
* and of course, the dynamic logistic regression that adjusts as input variables are updated

You can check out the source to the [d3 code on my github](https://github.com/michaelmoliterno/d3).

<iframe width="910" height="670" display="block" src="/images/diabetes_logistic_regressions_d3_small.html" style="-webkit-transform:scale(0.8,.8);-moz-transform-scale(0.8,.8);"></iframe>
