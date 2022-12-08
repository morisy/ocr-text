"""
This is a hello world add-on for DocumentCloud.

It demonstrates how to write a add-on which can be activated from the
DocumentCloud add-on system and run using Github Actions.  It receives data
from DocumentCloud via the request dispatch and writes data back to
DocumentCloud using the standard API
"""

from documentcloud.addon import AddOn
import re


class OCRcheck(AddOn):
    """An example Add-On for DocumentCloud."""

    def main(self):
        """The main add-on functionality goes here."""
        # fetch your add-on specific data

        self.set_message("Evaluating the OCR quality for the given documents.")

        # add a hello note to the first page of each selected document
        for document in self.get_documents():
            quality_score = 0

            # Check if the text is empty or consists only of whitespace characters
            if not text.strip():
                # If the text is empty, return a quality score of 1
                self.set_message("No text in document! Score of 1")
                quality_score = 1

            # Use regular expressions to find common OCR errors in the text
            errors = re.findall(r'[^\w\s]', text)

            # If there are no errors, return a quality score of 5
            if not errors:
                 quality_score =  5

            # If there are errors, calculate the error rate by dividing the
            # number of errors by the length of the text
            error_rate = len(errors) / len(text)

            # Use regular expressions to find English words in the text
            words = re.findall(r'\b\w+\b', text)

            # Calculate the ratio of English words to total words
            word_ratio = len(words) / len(text)

            # Use regular expressions to find nonsense phrases in the text
            nonsense = re.findall(r'[^\w\s]+', text)

            # Calculate the ratio of nonsense phrases to total phrases
            nonsense_ratio = len(nonsense) / len(text)

            # Calculate the overall score by combining the error rate,
            # word ratio, and nonsense ratio
            score = error_rate + word_ratio + nonsense_ratio

            # If the score is less than 0.5, return a quality score of 4
            if score < 0.5:
                return 4

            # If the score is less than 0.75, return a quality score of 3
            if score < 0.75:
                return 3

            # If the score is less than 1.25, return a quality score of 2
            if score < 1.25:
                return 2

            # Otherwise, return a quality score of 1
            return 1
            document.annotations.create(f"Hello {name}!", 0)
            
            try:
                document.data[self.data.get("value")] = [str(results)]
                document.save()
            except:
                print("Saving the OCR Score did not work")

        with open("hello.txt", "w+") as file_:
            file_.write("Hello world!")
            self.upload_file(file_)

        self.set_message("Hello World end!")
        self.send_mail("Hello World!", "We finished!")


if __name__ == "__main__":
    HelloWorld().main()
