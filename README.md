# Expers

Today's educational systems need an efficient tool to perform an assessment learning. 

Expers is aimed to improve and make self-directed learning processes effective. 

Learners have access to learning materials from a wide variety of sources, and these materials are not often accompanied by questions, So preparing a set of questions for assessment can be time-consuming while getting questions from external sources relevant to content studied by learners is really hard. 

Expers is a mobile app that makes this process simple by using Automatic Question Generation for generating a right set of questions from content by using NLP(Natural language processing).
        
A learner can take pictures of the material, select a document or search online for the topic from the app then it will generate a set of questions. The Application will generate questions in a way that is mindful of the context in which the generated questions are effective and pedagogically-useful questions. The Application will use deep learning for extracting the text from the pictures taken by the learner by using optical character recognition. Learners can see their overall performance and can review their answers next to the exact answers in the application.

 	Automatic question generation (QG) is a very important yet challenging problem in NLP.

# Installation
```
pip install --upgrade pip

pip install -U transformers==3.0.0

python -m nltk.downloader punkt

pip install torchvision 
```
Run QuestionGenration Notebook
