import pytesseract
import os
from PIL import Image
from textblob import TextBlob
from googletrans import Translator
import matplotlib.pyplot as plt
from textblob.sentiments import NaiveBayesAnalyzer


def main():
    
    comment_count, comments_sentiments = sentimetal_analysis(process_images('comments/'))
    gen_chart(comment_count, comments_sentiments)


def process_images(path_file):
    comments = []

    for file in os.listdir(path_file):
        file_path = os.path.join(path_file, file)

        if os.path.isfile(file_path):
            image = Image.open(file_path)
            image_text = translate_text(pytesseract.image_to_string(image))

            comments.append(image_text)

    return comments


def translate_text(text):
    translator = Translator()
    source_language = translator.detect(text).lang
    translated_text = translator.translate(text, src=source_language, dest="en")

    return translated_text.text


def sentimetal_analysis(comments):
    comments_sentiment = []
    positives_comments = 0
    negatives_comments = 0

    for comment in comments:
        blob = TextBlob(comment, analyzer=NaiveBayesAnalyzer())

        if blob.sentiment.classification == "pos":
            comments_sentiment.append(round(blob.sentiment.p_pos, 2))
            positives_comments += 1
        else:
            comments_sentiment.append(round(blob.sentiment.p_pos, 2))
            negatives_comments += 1

    total_comments = negatives_comments + positives_comments
    comment_count = [positives_comments, negatives_comments, total_comments]
    return comment_count, comments_sentiment


def gen_chart(comment_count, comments_sentiments) -> None:
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))

    types = ["Positives", "Negatives", "total"]
    bar_colors = ["tab:green", "tab:red", "tab:orange"]
    bar_labels = [
        f"Positives: {comment_count[0]}",
        f"Negatives: {comment_count[1]}",
        f"total: {comment_count[2]}",
    ]

    ax[0].bar(types, comment_count, label=bar_labels, color=bar_colors)
    ax[0].set_ylabel("comments")
    ax[0].set_title("Movie Classification Based on Comments")
    ax[0].legend(title="info")


    list_range = len(comments_sentiments) + 1
    quantity_of_coments = list(range(1, list_range))
    average = (sum(comments_sentiments) / len(comments_sentiments)) * 10

    ax[1].plot(quantity_of_coments, comments_sentiments)
    ax[1].set_xlabel(f"comments   -   Average: {average:.2f}")
    ax[1].set_ylabel("sentimental")
    ax[1].set_title("Analisys of Sentimentals")

    plt.tight_layout()

    plt.show()



if __name__ == "__main__":
    main()
