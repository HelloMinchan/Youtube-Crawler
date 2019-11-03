class VedioInfo:
    # 멤버변수
    title = ''
    views = ''
    dates = ''
    link = ''
    img = ''
    # 생성자
    def __init__(self, title, views, dates, link, img):
        self.title = title
        self.views = views
        self.dates = dates
        self.link = link
        self.img = img