# **AVA2.2数据集使用教程**

1, 运行ava_download下的geturl.py,会在同级目录下生成下载链接test_url.txt和trainval_url.txt
    
2, 复制链接，使用迅雷批量下载，将所有视频文件放入ava_video下
    
3, 运行video2img.py。

    1, 会在同级目录创建ava_video_15min文件夹，并将ava_video下所有视频截取15min-30min片段放入其中

    2, 将ava_video_15min文件夹下的15min视频划分为帧，保存在datasets/AVA/frames文件夹下
    
4, 下载train.csv和val.csv,放在datasets/AVA/frame_lists文件夹下。
    [[train.csv下载地址]](https://dl.fbaipublicfiles.com/video-long-term-feature-banks/data/ava/frame_lists/train.csv)
    [[val.csv下载地址]](https://dl.fbaipublicfiles.com/video-long-term-feature-banks/data/ava/frame_lists/val.csv)

进入上述网址后右键另存即可。
    
5, 解压datasets/AVA/ava_v2.2.zip压缩包到同级文件夹下:
    [[ava_v2.2.zip下载地址]](https://s3.amazonaws.com/ava-dataset/annotations/ava_v2.2.zip)
    
6, 运行build_dataset.py,即可生成Dataloader用于训练
    
# **需求工具**

ffmpeg,用于剪辑视频。

[[ffmpeg官方地址]](https://www.ffmpeg.org/)

在官网下载win64压缩包，解压并配置环境变量

