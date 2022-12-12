from flask import Flask
import aiohttp
import logging

logfile = 'social_network_activity.log'
logging.basicConfig(format='%(asctime)s %(message)s', filename=logfile,level=logging.DEBUG)

# load
app = Flask(__name__)

async def make_request(url, session):
    try:
        async with session.get(url) as response:
                if response:
                    response_json = await response.json()
                    return len(response_json)
        return "No data"
    except Exception as e:
        print(f'make_request Exception: {e}')
        logging.error(f'make_request: {e}')
        return "No data"



@app.route("/")
async def social_network_activity():

    twitter_url = 'https://takehome.io/twitter'
    facebook_url = 'https://takehome.io/facebook'
    instagram_url = 'https://takehome.io/instagram'
    try:

        async with aiohttp.ClientSession() as session:
            instagram_activity_level = await make_request(instagram_url,session) 
            facebook_activity_level = await make_request(facebook_url,session) 
            twitter_activity_level = await make_request(twitter_url,session)      

        json_response = {"instagram": instagram_activity_level, 
                        "facebook": facebook_activity_level, 
                        "twitter": twitter_activity_level}

        return json_response

    except Exception as e:
        print(f'social_network_activity Exception {e}')
        logging.error(f'social_network_activity: {e}')




