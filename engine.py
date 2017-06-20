import recsys.algorithm
from recsys.algorithm.factorize import SVD
import os.path

DATASET = '/tmp/movielens.zip'
RATINGS = './ml-1m/ratings.dat'

class Engine:
    def __init__(self, svd, *args, **kwargs):
        self.svd = svd

    def get_similarity(self, item1, item2):
        return self.svd.similarity(item1, item2)

    def get_similar(self, item):
        return self.svd.similar(item)

    def predict_rating(self, user, movie):
        MIN_RATING = 0.0
        MAX_RATING = 5.0
        return self.svd.predict(movie, user, MIN_RATING, MAX_RATING)

    def recommend_from_user(self, user):
        return self.svd.recommend(user, is_row=False)

    def recommend_from_item(self, item):
        return self.svd.recommend(item)

def load_data():
    if os.path.isfile(DATASET):
        svd = SVD(filename=DATASET)
    else:
        svd = SVD()
        svd.load_data(filename=RATINGS, sep='::', format={'col':0, 'row':1, 'value':2, 'ids': int})
        k = 100
        svd.compute(k=k,
                    min_values=10,
                    pre_normalize=None,
                    mean_center=True,
                    post_normalize=True,
                    savefile=DATASET)
    return svd

if __name__ == '__main__':
    svd = load_data()
    engine = Engine(svd)
