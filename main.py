from fbmscraper import *
import configparser

if __name__ == '__main__':
    
    fbchat._state.FB_DTSG_REGEX = re.compile(r'"name":"fb_dtsg","value":"(.*?)"')
    config = configparser.ConfigParser()
    config.read('config.ini')
    email = config.get('Credentials','email')
    password = config.get('Credentials','password')
    user_agent = config.get('Credentials','user_agent')
    thread_id = config.get('Thread', 'id')
    outpath = config.get('Download', 'path')

    client = Client(email, password, user_agent = user_agent)
    
    fbm_scraper(client, thread_id, outpath, gif = False)
