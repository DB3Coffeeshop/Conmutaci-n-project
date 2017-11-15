class Article:

    def __init__(self, id_article, category_first, category_second, name_article, stock):
        self.id_article = id_article
        self.category_first = category_first
        self.category_second = category_second
        self.name_article = name_article
        self.stock = stock


    def __str__(self):
        return "%d, '%s', '%s', '%s', %d" % (self.id_article, self.category_first, self.category_second, self.name_article, self.stock)