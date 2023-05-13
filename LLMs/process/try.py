# Import the library
import jsonlines

# Create a list of reviews
reviews = [
    "Rate this review on a scale from 1 to 5. Output only the integer rating : Always busy, wait times are terrible.",
    "Rate this review on a scale from 1 to 5. Output only the integer rating : Very unorganized and bad customer support",
    "Rate this review on a scale from 1 to 5. Output only the integer rating : This airport is one of the worst airports ever. TSA line makes you want to pull your hair out. The people checking IDs and Tickets make the process so long and the attitudes are so nasty. It's like they are upset they filled out a application and got the JOB.  It could be better handled so the process can be seamless. The TSA line is completely messy."
]

# Open a new jsonl file for writing
with jsonlines.open("reviews.jsonl", mode="w") as writer:
    # Loop through the reviews list
    for review in reviews:
        # Write each review as a separate line in the file
        writer.write(review)