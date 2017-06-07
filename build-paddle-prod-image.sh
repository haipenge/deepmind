#构建paddle生产镜像
docker run -v $(pwd):/paddle -e "WITH_GPU=OFF" -e "WITH_AVX=OFF" -e "WITH_TEST=ON" paddle:dev
docker build -t paddle:prod -f build/Dockerfile ./build

#运行单元测试
#docker run -it -v $(pwd):/paddle paddle:dev bash -c "cd /paddle/build && ctest"