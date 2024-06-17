sc create --name temp  --image "harbor.smoa.cc/public/xsemseg:v1.4" --gpu 2 --cmd "source /dataset/vsitongwu/.bashrc && cd /dataset/vsitongwu/LJC/temp && conda activate animate && python train.py" --arch ampere --debug


sc create --name test  --image "harbor.smoa.cc/public/xsemseg:v1.4" --gpu 2 --cmd "source /dataset/vsitongwu/.bashrc && cd /dataset/vsitongwu/LJC/temp && conda activate animate && python get_map.py" --arch ampere --debug


Get map.
63.91% = aeroplane AP   ||      score_threhold=0.5 : F1=0.64 ; Recall=56.59% ; Precision=72.38%
64.69% = bicycle AP     ||      score_threhold=0.5 : F1=0.63 ; Recall=56.81% ; Precision=71.39%
49.05% = bird AP        ||      score_threhold=0.5 : F1=0.52 ; Recall=40.17% ; Precision=72.12%
29.00% = boat AP        ||      score_threhold=0.5 : F1=0.25 ; Recall=15.74% ; Precision=67.01%
17.28% = bottle AP      ||      score_threhold=0.5 : F1=0.14 ; Recall=8.32% ; Precision=54.05%
65.02% = bus AP         ||      score_threhold=0.5 : F1=0.63 ; Recall=53.82% ; Precision=75.86%
71.77% = car AP         ||      score_threhold=0.5 : F1=0.69 ; Recall=59.36% ; Precision=82.75%
68.83% = cat AP         ||      score_threhold=0.5 : F1=0.67 ; Recall=62.77% ; Precision=72.27%
24.78% = chair AP       ||      score_threhold=0.5 : F1=0.23 ; Recall=14.47% ; Precision=55.30%
45.55% = cow AP         ||      score_threhold=0.5 : F1=0.50 ; Recall=51.50% ; Precision=48.21%
51.43% = diningtable AP ||      score_threhold=0.5 : F1=0.56 ; Recall=48.74% ; Precision=65.40%
64.73% = dog AP         ||      score_threhold=0.5 : F1=0.62 ; Recall=53.22% ; Precision=75.62%
72.96% = horse AP       ||      score_threhold=0.5 : F1=0.70 ; Recall=66.10% ; Precision=73.63%
65.87% = motorbike AP   ||      score_threhold=0.5 : F1=0.65 ; Recall=64.19% ; Precision=64.97%
60.41% = person AP      ||      score_threhold=0.5 : F1=0.56 ; Recall=41.92% ; Precision=82.53%
40.56% = sheep AP       ||      score_threhold=0.5 : F1=0.43 ; Recall=34.42% ; Precision=56.95%
54.73% = sofa AP        ||      score_threhold=0.5 : F1=0.54 ; Recall=41.60% ; Precision=76.26%
69.94% = train AP       ||      score_threhold=0.5 : F1=0.67 ; Recall=64.52% ; Precision=69.83%
59.97% = tvmonitor AP   ||      score_threhold=0.5 : F1=0.60 ; Recall=51.07% ; Precision=73.68%
mAP = 54.76%
Get map done.
其实这次类别标签少写了一个


test-dataset/VOCdevkit/VOC2007/JPEGImages/000001.jpg

50+50 epoch
Epoch:100/100
Total Loss: 2.653 || Val Loss: 4.004 
其实到70多的时候 Val Loss就趋于4 平稳不动了，但是Total Loss还在下降 怀疑过拟合的问题
Get map.
70.37% = aeroplane AP   ||      score_threhold=0.5 : F1=0.69 ; Recall=56.82% ; Precision=87.11%
71.73% = bicycle AP     ||      score_threhold=0.5 : F1=0.69 ; Recall=62.65% ; Precision=77.03%
54.38% = bird AP        ||      score_threhold=0.5 : F1=0.56 ; Recall=43.30% ; Precision=77.75%
40.84% = boat AP        ||      score_threhold=0.5 : F1=0.41 ; Recall=28.57% ; Precision=71.95%
21.93% = bottle AP      ||      score_threhold=0.5 : F1=0.19 ; Recall=11.23% ; Precision=72.97%
70.43% = bus AP         ||      score_threhold=0.5 : F1=0.69 ; Recall=62.08% ; Precision=78.08%
76.13% = car AP         ||      score_threhold=0.5 : F1=0.74 ; Recall=65.61% ; Precision=84.84%
74.49% = cat AP         ||      score_threhold=0.5 : F1=0.72 ; Recall=66.06% ; Precision=79.91%
30.57% = chair AP       ||      score_threhold=0.5 : F1=0.34 ; Recall=24.61% ; Precision=53.38%
53.49% = cow AP         ||      score_threhold=0.5 : F1=0.53 ; Recall=47.96% ; Precision=58.09%
58.11% = diningtable AP ||      score_threhold=0.5 : F1=0.61 ; Recall=55.35% ; Precision=67.95%
72.66% = dog AP         ||      score_threhold=0.5 : F1=0.69 ; Recall=62.87% ; Precision=76.26%
78.11% = horse AP       ||      score_threhold=0.5 : F1=0.75 ; Recall=70.27% ; Precision=79.78%
72.82% = motorbike AP   ||      score_threhold=0.5 : F1=0.71 ; Recall=65.79% ; Precision=76.58%
65.38% = person AP      ||      score_threhold=0.5 : F1=0.62 ; Recall=50.82% ; Precision=79.55%
0.00% = pottedplant AP  ||      score_threhold=0.5 : F1=0.00 ; Recall=0.00% ; Precision=0.00%
3.30% = sheep AP        ||      score_threhold=0.5 : F1=0.12 ; Recall=10.84% ; Precision=14.04%
4.11% = sofa AP         ||      score_threhold=0.5 : F1=0.15 ; Recall=14.33% ; Precision=16.72%
10.96% = train AP       ||      score_threhold=0.5 : F1=0.26 ; Recall=23.50% ; Precision=30.27%
20.34% = tvmonitor AP   ||      score_threhold=0.5 : F1=0.28 ; Recall=16.95% ; Precision=73.15%
mAP = 47.51%
Get map done.