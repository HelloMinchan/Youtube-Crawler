# --------모듈--------
import pymysql as my

class DBHelper:
    '''
    멤버변수 : 커넥션
    '''
    conn = None
    '''
    생성자
    '''
    def __init__(self):
        self.db_init()
    '''
    멤버 함수 : 연결, 해제, 검색어 가져오기, 데이터 삽입
    '''
    def db_init(self):
        self.conn = my.connect(
                        host='localhost',
                        user='root',
                        password='1234',
                        db='youtube_db',
                        charset='utf8',
                        cursorclass=my.cursors.DictCursor)

    def db_free(self):
        if self.conn:
            self.conn.close()
    
    def db_selectKeyword(self):
        rows = None
        with self.conn.cursor() as cursor:
            sql = "select * from info_tb;"
            cursor.execute(sql)
            rows = cursor.fetchall()
        return rows

    def db_insertCrawlingData(self, title, views, dates, link, img, keyword):
        with self.conn.cursor() as cursor:
            sql = '''
            insert into `data_tb`
            (title, views, dates, link, img, keyword) 
            values( %s,%s,%s,%s,%s,%s )
            '''
            cursor.execute(sql, (title, views, dates, link, img, keyword))
        self.conn.commit()

# --------테스트 코드--------
# 단독으로 수행시에만 작동
if __name__=='__main__':
    db = DBHelper()
    print(db.db_selectKeyword())
    db.db_insertCrawlingData('1','2','3','4','5','6')
    db.db_free()