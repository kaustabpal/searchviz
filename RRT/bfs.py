from gridviz import searchviz
import time
import os
env = searchviz('Bredth First Search')

def next_state(env,i):
    if(i%4==0): # up
        if ( not (env.y == 0) and ([env.x,env.y-1] not in env.visited) and ([env.x,env.y-1] not in env.dead)):
            env.visited.append([(env.x+0),env.y-1])
    if(i%4==1): # right
        if (not (env.x == 9) and ([env.x+1, env.y] not in env.visited) and ([env.x+1, env.y] not in env.dead)):
            env.visited.append([(env.x+1), env.y])

    if(i%4==2): # down
        if (not (env.y == 9) and ([env.x, env.y+1] not in env.visited) and ([env.x+0, env.y+1] not in env.dead)):
            env.visited.append([(env.x+0), env.y+1])
    if(i%4==3): # left
        if ( not (env.x == 0) and ([env.x-1,env.y] not in env.visited) and ([env.x-1,env.y] not in env.dead)):
            env.visited.append([(env.x-1),env.y])
        env.dead.append([env.x,env.y])
        new_loc=env.visited.pop(0)
        env.x=new_loc[0]
        env.y=new_loc[1]
    if(env.visited==[]):
        env.done=True

done = env.step()
visited_x=[]
visited_y=[]
dead_x=[]
dead_y=[]
i=0
while not done:
    done = env.step()
    time.sleep(1/20)
    next_state(env,i)
    i=i+1
#os.system('ffmpeg -framerate 25 -i video/image%04d.jpg -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p bfs.mp4')
