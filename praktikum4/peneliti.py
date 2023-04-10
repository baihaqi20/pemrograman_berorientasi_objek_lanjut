class Researcher:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.journal = Journal()

    def submit_article(self, article):
        self.journal.add_article(article)
        print(f"{self.name} has submitted an article to {self.journal.name}.")

class Journal:
    def __init__(self, name="Journal of Science"):
        self.name = name
        self.articles = []

    def add_article(self, article):
        self.articles.append(article)
        print(f"{article.title} has been added to {self.name}.")

    def print_articles(self):
        for article in self.articles:
            print(article.title)

class Article:
    def __init__(self, title, authors, abstract):
        self.title = title
        self.authors = authors
        self.abstract = abstract
# membuat objek Researcher
researcher1 = Researcher("Muhammad baihaqi", "mbaihaqi@gmail.com")

# membuat objek Article
article1 = Article("The Impact of Technology on Society", "Muhammad Baihaqi", "This article discusses the positive and negative effects of technology on society.")

# peneliti menyerahkan artikel ke jurnal
researcher1.submit_article(article1)

# mencetak semua artikel pada jurnal
researcher1.journal.print_articles()
