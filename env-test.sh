#Env test
#Is linux support AVX
#AIX，检查Linux是否支持AIX
if cat /proc/cpuinfo | grep -i avx; then echo Yes; else echo No; fi
#如果输出NO，不支持，就需要选择使用no-AVX的镜像