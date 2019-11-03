# --------모듈--------
from selenium import webdriver as wd
from video import VedioInfo as vi
import time

# --------함수--------
# 공유 버튼 클릭후 링크값 반환
def get_link():
    driver.find_element_by_xpath('/html/body/ytm-app/div[2]/ytm-watch/ytm-single-column-watch-next-results-renderer/ytm-item-section-renderer[1]/lazy-list/ytm-slim-video-metadata-renderer/div[2]/c3-material-button[3]').click()
    driver.implicitly_wait(delay)
    return driver.find_element_by_xpath('/html/body/div[5]/c3-dialog/div[2]/a').text
def get_img_link():
    video_id = driver.find_element_by_xpath('/html/body/div[5]/c3-dialog/div[2]/a').text[-11:]
    img_link = 'https://img.youtube.com/vi/'+video_id+'/0.jpg'
    return img_link

# --------사전 정보--------
main_url_desktop = 'https://www.youtube.com/'
main_url_mobile = 'https://m.youtube.com/?persist_app=1&app=m'
# 검색어 (원하는 재생목록 이름,""검색 명령어 붙이기)
keyword = '"2019 Worlds Championship 게임하이라이트"'
# 재생목록 개수 (사용자가 삭제한 동영상이 있는지 꼭 확인후 명시된 개수에서 빼기)
video_nums = 113
# 암묵적 대기 시간
delay = 10
# 비디오 정보 담는 리스트 (VidoeInfo 리스트)
video_list = []

# --------드라이버 로드--------
driver = wd.Chrome(executable_path='chromedriver.exe')

# --------사이트 접속--------
driver.get(main_url_mobile)
driver.implicitly_wait(delay)

# --------검색 버튼 클릭--------
driver.find_element_by_xpath('//*[@id="header-bar"]/header/div/button').click()

# --------검색어 입력--------
driver.find_element_by_xpath('//*[@id="header-bar"]/header/ytm-searchbox/form/div/input').send_keys(keyword)

# --------검색 버튼 클릭--------
driver.find_element_by_xpath('/html/body/ytm-app/ytm-mobile-topbar-renderer/header/ytm-searchbox/form/button[2]').click()
driver.implicitly_wait(delay)

# --------검색 내역 클릭--------
driver.find_element_by_xpath('/html/body/ytm-app/div[3]/ytm-search/ytm-section-list-renderer/lazy-list/ytm-item-section-renderer/lazy-list/ytm-compact-playlist-renderer/div/div/a/h4').click()
driver.implicitly_wait(delay)
'''
# --------데이터(썸네일) 추출--------
soup = bs(driver.page_source, 'lxml');
playlist = soup.find('ytm-playlist-video-renderer', {'class':'item'})
print(playlist)

'''
# --------재생목록 실행--------
driver.find_element_by_xpath('/html/body/ytm-app/div[1]/ytm-browse/ytm-single-column-browse-results-renderer/div/div/ytm-section-list-renderer/lazy-list/ytm-item-section-renderer/lazy-list/ytm-playlist-video-list-renderer/ytm-playlist-video-renderer[1]/div/div/a/h4/span').click()
driver.implicitly_wait(delay)


# --------데이터(제목, 조회수, 게시일, 링크, 썸네일) 추출--------
for page in range(video_nums):
    
    # --------정보 펼치기--------
    driver.find_element_by_xpath('/html/body/ytm-app/div[2]/ytm-watch/ytm-single-column-watch-next-results-renderer/ytm-item-section-renderer[1]/lazy-list/ytm-slim-video-metadata-renderer/button/div/c3-icon').click()
    time.sleep(2)
    obj = vi(
        driver.find_element_by_xpath('/html/body/ytm-app/div[2]/ytm-watch/ytm-single-column-watch-next-results-renderer/ytm-item-section-renderer[1]/lazy-list/ytm-slim-video-metadata-renderer/button/div/div/h2').text,
        driver.find_element_by_xpath('/html/body/ytm-app/div[2]/ytm-watch/ytm-single-column-watch-next-results-renderer/ytm-item-section-renderer[1]/lazy-list/ytm-slim-video-metadata-renderer/button/div/div/div/span').text,
        driver.find_element_by_xpath('/html/body/ytm-app/div[2]/ytm-watch/ytm-single-column-watch-next-results-renderer/ytm-item-section-renderer[1]/lazy-list/ytm-slim-video-metadata-renderer/div[3]/div[1]').text,
        get_link(),
        get_img_link()
    )
    video_list.append(obj)

    # --------공유 화면 취소--------
    driver.find_element_by_xpath('/html/body/div[5]/c3-dialog/div[3]/c3-material-button/button').click()
    time.sleep(2)

    if page != (video_nums-1):
        driver.find_element_by_xpath('/html/body/ytm-app/div[2]/ytm-watch/ytm-single-column-watch-next-results-renderer/ytm-playlist/div/ytm-playlist-controls/div[1]/c3-material-button[2]/button').click()
        time.sleep(2)

for i in range(video_nums):
    print(video_list[i].title)
    print(video_list[i].views)
    print(video_list[i].dates)
    print(video_list[i].link)
    print(video_list[i].img)
    print()