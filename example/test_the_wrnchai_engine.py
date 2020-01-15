import json
import pprint

def json_r(filename):
   with open(filename) as f_in:
       return(json.load(f_in))

pose_estimation = json_r('test-image-processed.json')

# the first 300 char of pose_estimation['frames']
print(str(pose_estimation['frames'])[:300])

# [{'height': 819, 'width': 800, 'persons': [{'id': 0, 'head_pose': {'bbox': {'height': 0.15750916302204132, 'minX': 0.4650000035762787, 'width': 0.16124999523162842,
# 'minY': 0.05494505539536476}, 'landmarks': [0.5701904296875, 0.20753204822540283, 0.5002734661102295, 0.1503119319677353, 0.52987790107


man_pose = pose_estimation['frames'][0]['persons'][0]
print(man_pose.keys())      # dict_keys(['id', 'hand_pose', 'pose2d', 'head_pose'])


# Lets print the 10 first joint coordinates
pprint.pprint(man_pose['pose2d']['joints'][0:10])

# [0.3711889684200287,
#  0.7936080694198608,
#  0.5704107880592346,
#  0.7095877528190613,
#  0.3788127601146698,
#  0.6029024720191956,
#  0.5351067781448364,
#  0.5762162208557129,
#  0.7694329023361206,
#  0.5570101141929626]


# There are 25 joints and the joints json hold 50 values (25 pairs of coordinates).
# ex. Joint 0 coordinates, (x,y) = (man_pose['pose2d']['joints'][0],man_pose['pose2d']['joints'][1])
#     Joint n coordinates, (x,y) = (man_pose['pose2d']['joints'][2n],man_pose['pose2d']['joints'][2n+1])

print(len(man_pose['pose2d']['joints']))    # 50

xLWRIST = man_pose['pose2d']['joints'][30]
xLKNEE = man_pose['pose2d']['joints'][8]

print(xLWRIST)      # 0.7735595107078552
print(xLKNEE)       # 0.7694329023361206
