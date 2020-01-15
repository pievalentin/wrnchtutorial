# Run the following command 
# !pip install requests 
import requests     
import json
import time

LOGIN_URL = 'https://api.wrnch.ai/v1/login'
JOBS_URL = 'https://api.wrnch.ai/v1/jobs'
API_KEY = 'aaaaaabbbbbbbbbccccccccddddddd' # Go to https://devportal.wrnch.ai/licenses, click on the key icon to find your cloud API key

resp_auth = requests.post(LOGIN_URL,data={'api_key':API_KEY})
print(resp_auth.text)
# the jwt token is valid for an hour
JWT_TOKEN = json.loads(resp_auth.text)['access_token']

# {"access_token": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
#                   bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
#                   ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"}


with open('img/test-image.jpg', 'rb') as f:
  resp_sub_job = requests.post(JOBS_URL,
                              headers={'Authorization':f'Bearer {JWT_TOKEN}'},
                              files={'media':f},
                              data={'work_type':'json'}
                              )

job_id = json.loads(resp_sub_job.text)['job_id']
print('Status code:',resp_sub_job.status_code)  # Status code: 202
print('Response:',resp_sub_job.text)            # Response: {"job_id": "f1cdaa7f-4823-49e1-9a26-382058278e35"}

# wait a few seconds to retrieve the result
# you could check the job status in this link https://devportal.wrnch.ai/jobs OR using following command

GET_JOB_STATUS_URL = 'https://api.wrnch.ai/v1/status' + '/' + job_id
response = requests.get(GET_JOB_STATUS_URL, headers={'Authorization':f'Bearer {JWT_TOKEN}'})
print('Job status:', response.text)

time.sleep(3)

GET_JOB_URL = JOBS_URL + '/' + job_id
print(GET_JOB_URL)
resp_get_job = requests.get(GET_JOB_URL,headers={'Authorization':f'Bearer {JWT_TOKEN}'})
print('Status code:',resp_get_job.status_code)
print('\nResponse:',resp_get_job.text)

# https://api.wrnch.ai/v1/jobs/1cc5c026-1ac8-483b-8ff5-83ec09fa425e
# Status code: 200

# Response: {"file_info":{"joint_definitions":{"hands":"hand21","head":"wrFace20","pose2d":"j25","pose3d_ik":"extended",
# "pose3d_raw":"j25"}},"frames":[{"frame_time":0,"height":614,"persons":[{"id":0,"pose2d":{"bbox":{"height":0.9895586371421814,
# "minX":0.2897970974445343,"minY":0.039630815386772156,"width":0.5532262325286865},"is_main":true,"joints":[0.37112537026405334,
# 0.7902586460113525,0.5703703165054321,0.7099169492721558,0.3749939203262329,0.6030898690223694,0.5311734676361084,0.5763961672782898,
# 0.7657291889190674,0.5610739588737488,0.6757756471633911,0.866474986076355,0.45308369398117065,0.5897430181503296,0.5196003913879395,
# 0.2996460795402527,0.5196273922920227,0.29780837893486023,0.5455899834632874,0.13356269896030426,0.5350296497344971,0.5954576730728149,
# 0.3633612096309662,0.46940380334854126,0.42190080881118774,0.28249606490135193,0.6172999143600464,0.31679609417915344,0.6875200271606445,
# 0.4581219255924225,0.7735621333122253,0.4886617064476013,0.5779774188995361,0.13753801584243774,0.5470162034034729,0.1220940351486206,
# 0.49219584465026855,0.14887282252311707,0.5975579619407654,0.12972120940685272,-0.00390625,-0.0038171824999153614,0.39449259638786316,
# 0.908473789691925,0.7969211339950562,0.9467262029647827,0.335899293422699,0.7709774374961853,0.6288465857505798,0.9007530212402344],
# "scores":[0.8040049076080322,0.9206298589706421,0.6534831523895264,0.6234648823738098,0.8405327200889587,0.895474910736084,
# 0.6384739875793457,0.8672735691070557,0.8769335746765137,0.9407069087028503,0.8741081357002258,0.9001782536506653,0.8620328903198242,
# 0.8725142478942871,0.791862428188324,0.8561787605285645,0.9511832594871521,0.961635947227478,0.9231566190719604,0.9373281002044678,
# 0.0,0.8867651224136353,0.9401049017906189,0.8837882280349731,0.8658027648925781]}}],"width":600}]}

cloud_pose_estimation = json.loads(resp_get_job.text)
cloud_xLWRIST = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][30]
cloud_xLKNEE = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][8]

print(cloud_xLWRIST)    # 0.7735621333122253
print(cloud_xLKNEE)     # 0.7657291889190674