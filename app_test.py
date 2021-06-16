from pipelines import pipeline

nlp = pipeline("question-generation")

print(nlp("42 is the answer to life, the universe and everything."))
