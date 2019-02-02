#CBC Recommendation System Dataset

This dataset contains user sessions collected from activity on the CBC website.

Each row represents an instance of a user reading a piece of online content,
identified by its ID and position within the user's read sequence.

##Columns

###sessionId

Anonymized user IDs, e.g. `user-0000001`, `user-242718`

###contentId

Internal ID uniquely identifying the CBC content. These have not been anonymized, and in
fact, the article content can be accessed using the following URL format:
`https://www.cbc.ca/json/cmlink/{contentId}`

###eventId

Zero-indexed ID identifying the content's position in the user's read sequence. For example,
and event ID of `2` implies that it's the 3rd article the user has read.

##Files

###train.csv

This is the main file for training, containing all the user read events over a period of time.

###test.csv

This is a file for evaluating your model's performance. It's in the same format as the
training file.

Notes:

- The test events are taken from a time period **after** the training period -- there is no overlap.

- Many of the users in the testing file also appear in the training file, but some do not.

- Some of the content in the test set was published after the end of the training period,
  and thus does not appear in the training set.
