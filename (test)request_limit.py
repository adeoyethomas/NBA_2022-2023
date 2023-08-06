# Used this file to help grab the remaining request limits that I have on my API
header_response_text = {'Date': 'Fri, 10 Jun 2022 13:14:57 GMT',
                        'Content-Type': 'application/json',
                        'Transfer-Encoding': 'chunked',
                        'Connection': 'keep-alive',
                        'X-Request-ID': '3a5198b5-353d-45a7-aa6c-177df2d36926, 3a5198b5-353d-45a7-aa6c-177df2d36926',
                        'Strict-Transport-Security': 'max-age=31536000',
                        'Vary': 'Accept-Encoding',
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': 'GET, OPTIONS',
                        'Access-Control-Allow-Headers': 'x-rapidapi-key, x-apisports-key, x-rapidapi-host',
                        'X-RateLimit-Limit': '10',
                        'X-RateLimit-Remaining': '9',
                        'x-ratelimit-requests-limit': '100',
                        'x-ratelimit-requests-remaining': '97',
                        'Content-Encoding': 'gzip'}

daily_calls_remaining = header_response_text['x-ratelimit-requests-remaining']
perMinute_calls_remaining = header_response_text['X-RateLimit-Remaining']

print('Daily calls remaining = ' + daily_calls_remaining)
print('Calls left per minute = ' + perMinute_calls_remaining)
