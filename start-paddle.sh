#Run paddle
#以后台服务方式运行
#docker run -d -p 2202:22 -p 8888:8888 paddledev/paddle
#连接方式:ssh -p 2202 root@localhost
#以交互方式运行
docker run -it -v /work/project/deepmind:/app paddledev-local  /bin/bash
#AIX，检查Linux是否支持AIX
#if cat /proc/cpuinfo | grep -i avx; then echo Yes; else echo No; fi
#如果输出NO，不支持，就需要选择使用no-AVX的镜像

###############运行AI训练程序#########################
#docker run -it -v $PWD:/work paddle /work/a.py

#如果使用GPU，使用以下命令进行训练
#nvidia-docker run -it -v $PWD:/work paddle /work/a.py

