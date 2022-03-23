import os
def cut_video(file_name,start_time,lasts_time,save_name):
    # file_time = ffmpeg.probe(file_name)['format']['duration']    # 视频总时长 秒
    command = 'ffmpeg.exe -y -i ' +  file_name + ' -ss ' + start_time + ' -t '+ lasts_time + \
              ' -acodec copy -vcodec copy -async 1 ' + save_name
    print("执行命令："+command)
    os.system(command)
def video2img(path_to_video,save_path = "datasets/AVA/frames"):
    video_name = path_to_video.split(".")[0].split("/")[-1]
    cur_dir = save_path+"/"+video_name
    if not os.path.exists(cur_dir):
        os.mkdir(cur_dir)
    command = "ffmpeg.exe -i "+path_to_video+" -r 30 -qscale:v 1 "+f'{cur_dir}/{video_name}_%06d.jpg'
    print("执行命令：" + command)
    os.system(command)
if __name__=="__main__":
    # _ = cut_video("ava_video/--205wugM18.mkv")
    for file in os.listdir("ava_video"):
        video_path = "ava_video/"+ file
        if not os.path.exists("ava_video_15min"):
            os.mkdir("ava_video_15min")
        save_path = "ava_video_15min/"+ file
        cut_video(video_path,start_time='00:15:00',lasts_time='00:15:01',save_name=save_path)
        video2img(path_to_video=save_path)
    print("done!!!!!!!")



