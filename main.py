import requests 

# ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmxlSEFpT2pFMU9EYzJORGs1TlRFc0lrMXZaR1ZzSWpwN0lrTm9ZWEpoWTNSbGNuTlFaWEpFWVhraU9qVXdNREF3TENKVmMyVnlTV1FpT2pNeU5qZ3NJbFZ1YVhGMVpVbGtJam9pTldSaVpUWmpZakV0WlRCbE1TMDBZVFV6TFRrd01qZ3RaVEF5T0RjME1EWmhORGhoSW4xOS41cGJDUzJqVTMzZVZWYUkyM2R0ZWEwcmtYTmx6TGZ3b0xxbnV3Z25xbmQ4

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'NWRiZTZjYjEtZTBlMS00YTUzLTkwMjgtZTAyODc0MDZhNDhhOjdkNTU2OWE5OTMxOTRlNDNhY2NkMWY0MTE3YTAxYmM1'

headers_auth = {'Authorization': 'Basic ' + KEY}

auth = requests.post(URL_AUTH, headers=headers_auth)

if auth.status_code == 200:
    token= auth.text
    while True:    
        word = input('Insert word to translate: ')
        if word:
            headers_translate = {
                'Authorization': 'Bearer ' + token
            }
            params = {
                'text': word,
                'srcLang': 1033,
                'dstLang': 1049
            }
            r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
            res = r.json()
            try:
                print(res['Translation']['Translation'])
            except:
                print("Не найдено варианта для перевода")
else:
    print('Error')


