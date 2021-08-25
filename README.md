# ACM Research Coding Challenge (Fall 2021)

##Coding Language Utilized
___

I utilized Python to create this program as well as the TextBlob API that was imported into the project.

##My estimation
___

After skimming through the text file,I saw that lines 1-21 were negative due to strong words such as "furious", "murder," and "bleed." However, from lines 25-53, 
it is seen that the text changes its tone positively due to strong words such as "excellent," "pleasing," and "perfect." Though this may not be an ideal indicator,
I assumed that the overall sentiment score would barely be around 0, specifically in between 0.05 to 0.15 since the text had more "positive lines" than "negative lines." 

## What I did
___

When I first opened the project, I skimmed through the **input.txt** file in order to understand the overall emotion of the text.
I surfed throughout the web to find any sentimental analysis APIs that were compatible with Python and managed to find a website that
compared and contrasted the different sentimental analysis APIs that existed such as **TextBlob**, **VADER**, and **Flair**. Prior to my surfing around the web,
I opened the given file **input.txt** and created a new file called **sentimentAnalysisPerSentence.txt** in order to 
log in data regarding each and every sentence. Conveniently enough, **TextBlob** had the necessary methods to get across what I intended to, although
the other APIs provided more information regarding the overall story. In order to get the project going, I separated the files into lines and logged it into
the **sentimentAnalysisPerSentence.txt** while specifying the polarity as well as subjectivity of each sentence in the **input.txt** file. After logging in all the sentences, I then 
proceeded to open the file as it is and analyzed the sentiment as well as polarity for the entire essay.

## So what does that mean?
___

After running it through the TextBlob API, the polarity serves as a measure of "positive" and "negative" sentiments. The closer the polarity is to "+1," the higher the positive sentiment in 
the text. That said, the closer the polarity is to "-1," the closer it is to a negative sentiment. Additionally, the "subjectivity" part of the TextBlob serves to indicate the subjectivity/objectivity 
of the text. The closer the number is to 0, the higher the objectivity. In an opposite manner, the closer the number is to 1, the higher the subjectivity in the text.

## What does TextBlob say about the text?

TextBlob states that the entirety of the text has a polarity of 0.21353 and a subjectivity of 0.59540. Though the polarity was higher than I anticipated, it doesn't seem too high since there were more
statements that were more positive than negative. Additionally, the subjectivity seems to be lower than what I would anticipate, it is still near 60%, which makes sense as this is a story. When I analyzed only the sentences,
it was found that majority of the sentences on their own without any context tend to be neutral, though there were certain sentences that were outliers, which created the polarity and subjectivity that it has right now.

## Resources Utilized 
___
Open and write files: https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/

VADER API: https://www.geeksforgeeks.org/python-sentiment-analysis-using-vader/

TextBlob API: https://textblob.readthedocs.io/en/dev/quickstart.html#create-a-textblob

Flair API: https://github.com/flairNLP/flair

Sentiment Analysis Recommendations: https://neptune.ai/blog/sentiment-analysis-python-textblob-vs-vader-vs-flair

## [](https://github.com/ACM-Research/Coding-Challenge-F21#no-collaboration-policy)No Collaboration Policy

**You may not collaborate with anyone on this challenge.**  You  _are_  allowed to use Internet documentation. If you  _do_  use existing code (either from Github, Stack Overflow, or other sources),  **please cite your sources in the README**.

## [](https://github.com/ACM-Research/Coding-Challenge-F21#submission-procedure)Submission Procedure

Please follow the below instructions on how to submit your answers.

1.  Create a  **public**  fork of this repo and name it  `ACM-Research-Coding-Challenge-F21`. To fork this repo, click the button on the top right and click the "Fork" button.

2.  Clone the fork of the repo to your computer using  `git clone [the URL of your clone]`. You may need to install Git for this (Google it).

3.  Complete the Challenge based on the instructions below.

4.  Submit your solution by filling out this [form](https://acmutd.typeform.com/to/zF1IcBGR).

## Assessment Criteria 

Submissions will be evaluated holistically and based on a combination of effort, validity of approach, analysis, adherence to the prompt, use of outside resources (encouraged), promptness of your submission, and other factors. Your approach and explanation (detailed below) is the most weighted criteria, and partial solutions are accepted. 

## [](https://github.com/ACM-Research/Coding-Challenge-S21#question-one)Question One

[Sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) is a natural language processing technique that computes a sentiment score for a body of text. This sentiment score can quantify how positive, negative, or neutral the text is. The following dataset in  `input.txt`  contains a relatively large body of text.

**Determine an overall sentiment score of the text in this file, explain what this score means, and contrast this score with what you expected.**  If your solution also provides different metrics about the text (magnitude, individual sentence score, etc.), feel free to add it to your explanation.   

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library/API you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible as submissions are evaluated on a rolling basis.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

