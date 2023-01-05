# CUDA_VISIBLE_DEVICES=0,1,2,3,4,5 ARCH=resnet50 python main.py --gpus 6 --lr 0.001 --data-path ../data/imagenet --pretrained
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 ARCH=resnet18 python main.py --gpus 8 --data-path ../data/imagenet-c

