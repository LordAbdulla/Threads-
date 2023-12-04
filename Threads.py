import requests
import re

def getUserId(username):
    url = f"https://www.threads.net/@{username}"
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "ko,en;q=0.9,ko-KR;q=0.8,ja;q=0.7",
        "pragma": "no-cache",
        "referer": "https://www.instagram.com/",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "cross-site",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
    }

    response = requests.get(url, headers=headers)
    text = response.text
    text = text.replace(" ", "")
    text = text.replace("\n", "")

    user_id = re.search(r'"props":{"user_id":"(\d+)"},', text)
    
    if user_id:
        return user_id.group(1)
    else:
        return None

def getUserInfo(username):
    user_id = getUserId(username)
    
    if not user_id:
        return "User ID not found"
    
    headers = {
        'authority': 'www.threads.net',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.threads.net',
        'referer': f'https://www.threads.net/@{username}',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
        'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-platform-version': '"11.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO KG6k) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
        'viewport-width': '400',
        'x-asbd-id': '129477',
        'x-fb-friendly-name': 'BarcelonaProfileRootQuery',
        'x-fb-lsd': 'WXO1JfwAaW5E7xXnLqoiJg',
        'x-ig-app-id': '1412234116260832',
    }

    data = {
        'av': '0',
        '__user': '0',
        '__a': '1',
        '__req': '1',
        '__hs': '19544.HYP:barcelona_web_pkg.2.1..0.0',
        'dpr': '1',
        '__ccg': 'GOOD',
        '__rev': '1007796774',
        '__s': 'bpvlhe:sf2fz0:48dtbr',
        '__hsi': '7252771177007524518',
        '__dyn': '7xeUmwlEnwn8K2WnFw9-2i5U4e0yoW3q32360CEbo1nEhw2nVE4W0om78b87C0yE465o-cw5Mx62G3i0Bo7O2l0Fwqo31wnEfovwRwlE-U2zxe2Gew9O22362W2K0zK5o4q0GpovU1aUbodEGdwtU2ewbS1LwTwNwLw8O1pwr82gxC',
        '__csr': 'nNqHt5rCg016kEuw-g467403FW3N0aSaDxPa2s8EqfIN6EuN0C8x27on7oBQfoO1DmucBz582u2Xz5Ceudguxko0FEb85g8z22wH1Y0xo5d0gQcg3uChayAEukbD16089w88238az0h0',
        '__comet_req': '29',
        'lsd': 'WXO1JfwAaW5E7xXnLqoiJg',
        'jazoest': '21924',
        '__spin_r': '1007796774',
        '__spin_b': 'trunk',
        '__spin_t': '1688667381',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'BarcelonaProfileRootQuery',
        'variables': f'{{"userID":"{user_id}"}}',
        'server_timestamps': 'true',
        'doc_id': '23996318473300828',
    }

    response = requests.post('https://www.threads.net/api/graphql', headers=headers, data=data)
    
    return response.text


username = "null"
info = getUserInfo(username)
print(info)
