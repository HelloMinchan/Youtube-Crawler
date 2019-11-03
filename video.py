class VedioInfo:
    '''
    멤버변수 : 제목, 조회수, 게시일, 링크, 썸네일, 검색어
    '''
    title = ''
    views = ''
    dates = ''
    link = ''
    img = ''
    keyword = ''
    '''
    생성자
    '''
    def __init__(self, title, views, dates, link, img, keyword):
        self.title = title
        self.views = views
        self.dates = dates
        self.link = link
        self.img = img
        self.keyword = keyword