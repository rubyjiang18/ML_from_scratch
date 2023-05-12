# 3 Tips to help you solve ML problems in the real world

Summarized from a LinkedIn post from Pau Labarta Bajo.

## Context
Online courses and Kaggle-style competitions are great resources to learn fundamentals of ML. Hoever, the daily job of a MLE requires an **additional layer of skilss** that you won't master there.

## Tip 1
Understand the business problem first, then frame it as an ML problem. Otherwise, you will end up building a great ML model in a Jupyter Notebook, that does NOT move the business metric it was intended to move. My advice? Ask 3 questions:
**Question 1**: What is the business metric we want to improve? It is crucial you talk with all relevant stakeholders at the beginning of the project. They have more business context than you and can help you understand what is the target you need to shoot at.\
**Question 2**: Is there any solution currently working to solve this, like some rule-based heuristics? If there is one, this is the benchmark you have to beat in order to have a business impact. Otherwise, you can have a quick win by implementing a non-ML solution.\
**Question 3**: Will the model be used as a black box or as a tool to assist humans to make better decisions? Creating blaxk-box solutions is easier than explainable ones. If you work in healthcare, for example, you need explainability. If you work in trading, you don't.\
If you can answer these 3 questions above it means you know ****WHAT**** is the Machine Learning problem you need to solve.

## Tip 2
Focus on getting more and better data. In Kaggle competitions you are given the data. In fact, all participants use the same data and compete against each other on who has the better model. The focus is on models, not on data. In reality, the opposite happens. But how do you get more and better data? IMHO there are 2 skilss you do not learn in online courses.
**Skill 1**: You need to talk (a lot) with the data engineering guys. They know where each bit of data is. They can help you fetch it and use it to generate useful features for your models. Also, they can build pipelines to add 3rd party data that can help you.\
**Skill 2**: The most universal language to access data is SQL, so you need to be fluent in it. This is especially true if you work in a less data-evolved environemnt, like a startup. Knowing SQL lets you quickly build the training data.\

Machine Learning models are a good combination of software (e.g. from a simple logistic regression all the way to a colossal Transformer) and DATA (capital letters, yes). Data is what makes projects successful or not, not models.

## Tip 3
Structure well you code. Jupyter notebooks are great for quickly prototyping and testing ideas. Pthon is a language designed for fast iterations, and Jupyter notebooks are the perfect match. However, notebooks quickly get crowded and unmanageable.\
My advice: It is best practice to structure your Python code as a package and avoid code duplication. Python Poetry is my favorite tool. With just 3 commands you can generate most of the scaffolding you need.\

That's a wrap! The job of professional MLE is more complex than what you will learn in any online course. I hope these 3 tips make your life easier and help you become even better at what you love.