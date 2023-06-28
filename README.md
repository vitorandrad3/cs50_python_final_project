 # Object Evaluation Based on Comment Sentiments
    #### Video Demo:  <URL HERE>
    
    #### Description:

    This is my final project for CS50 Python: an algorithm that reads comments from screenshots, using the pytesseract library (OCR) and assigns a sentiment value to them using the TextBlob library. The data is organized and presented in two graphs for easier analysis.

    The main idea of this program is to enable comment analysis and organize the information for various purposes, such as determining whether a particular product is well-received by the public based on the comments. As an example, comments obtained from the "IMDb" website about the movie "Spider-Man: Across the Spider-Verse" are being analyzed.

    The comments' images are located in the "comments" folder.

    In the main file "project.py", there are four functions, excluding the Main function. Each of them is responsible for a specific functionality of the project. The file is organized this way to modularize the functionalities, allowing scalability, easier code maintenance, and better understanding. It also enables the creation of unit tests.

    The first function, "process_images(path_file)", handles the processing of comment images. It accesses the directory where the images are located, processes each image by converting it into text, and stores them in a list, which is returned at the end of the process. It's important to note that the function expects the file path as an argument and relies on the "translate_text()" function, which will be explained in the next paragraph.

    The second function, "translate_text(text)", is responsible for translating the text using the googletrans library if it is not in English. This function is essential because during the program development, I noticed that the TextBlob library performs better in sentiment analysis when the text is in English. With this function, the program's applicability expands, as it can process texts in various languages.

    The third function, "sentiment_analysis(comments)", assigns sentiment to the texts and counts the negative and positive comments. It utilizes the TextBlob library with the "Analyzer = NaiveBayesAnalyzer()" parameter in its constructor. This allows for more accurate classification of the text, as it uses an NLTK classifier trained on a movie reviews corpus. It returns the comment counts (positive and negative) and the sentiment values.
    It's important to highlight that this function expects a list of strings as a parameter, so it does not depend on the "process_images()" function. Therefore, this program can consume, for example, an API containing product comments and process that data. The functionality of reading text from images is just an additional detail in the project.

    The fourth and final function, "gen_chart(comment_count, comments_sentiments)", expects the comment counts (positive, negative and total) and the sentiment values as arguments. It generates two charts that provide information such as the average sentiment of comments and the total number of analyzed comments.

    ##Features:

    - Reading comments from image format using OCR (Optical Character Recognition).
    - Translation of comments to the desired language.
    - Sentiment analysis of comments using the "TextBlob" library.
    - Generation of graphs for result visualization.
    - Display of the count of positive, negative, and total comments in a bar chart.
    - Variation of sentiment values over comments displayed in a line chart.
    - Calculation of the average sentiment value and display on the line chart.
    
    ##Prerequisites:

    Python 3.x
    Required libraries: pytesseract, PIL, textblob, googletrans, matplotlib

    