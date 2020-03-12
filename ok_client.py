import requests
import hashlib

class OkClient(object):
    def __init__(self, tag='test'):
        #https://apiok.ru/dev/methods/rest/search/search.tagContents
        self.tag= tag
        self.application_id='512000489878'
        self.application_key = 'CHJKHMJGDIHBABABA'
        self.application_secret_key = 'AF32B6A5CBC67C26CA9AA7F3'
        self.session_secret_key='b0d0aba5693ae0e6c100e4f31bdbe959'
        self.access_token='-s-a936ih54ABaAFj4dBdY6Co5cBB0eAI3cEbY5DnCcIc-BBh6ekXV5ll89B72ikh79BdafAhB8ma0hjn5bl90-jIi4'
        self.method=''
    def search(self):
        self.method='search.tagContents'
        sig = self.count_hash('application_key='+self.application_key+'format=jsonmethod=search.tagContentsquery='+self.tag+self.session_secret_key)


        result = requests.get('https://api.ok.ru/fb.do?application_key='+self.application_key+
                              '&format=json&method='+self.method+
                              '&query='+self.tag+
                              '&sig='+sig+
                              '&access_token='+self.access_token)
        print (result.headers)

        print(result.content)

    def count_hash(self,the_str,type='md5'):
        the_str_md5 = str(hashlib.md5(the_str.encode('utf-8')).hexdigest())
        print(the_str_md5)
        return the_str_md5
def main():
    ok = OkClient()
    ok.search()

if __name__ == '__main__':
    main()