class Comment:

    all_comments = []

    def __init__(self,post_id,title,review):
        self.movie_id = movie_id
        self.title = title
        self.review = review


    def save_review(self):
        Comment.all_comments.append(self)


    @classmethod
    def clear_reviews(cls):
        Comment.all_comments.clear()