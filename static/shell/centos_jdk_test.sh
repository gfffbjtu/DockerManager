#!bin/sh

# 参数1：java项目git地址 参数2：镜像名称 参数3：网络名称 参数4：IP地址

#进入工作文件夹
cd ~/workspace

#解析获取项目名称
git_address=$1
# git_address="https://github.com/gfffbjtu/SpringBootTest.git"
arr=(${git_address//// })
git_name=${arr[-1]}
arr=(${git_name//./ })
project_name=${arr[0]}

# 判断目标目录是否已经存在
if [ -d "$project_name" ]
then
rm -rf  $project_name
fi

#打包构建项目
git clone $git_address
cd $project_name
mvn clean package
cp target/$project_name*.jar ../
cd ..

#获取jar包完整名称
jar_name=$(ls | grep jar | grep $project_name)

#构建镜像
echo "FROM adoptopenjdk/openjdk8">Dockerfile
echo "COPY $jar_name /home/work/webapps/">>Dockerfile
echo "WORKDIR /home/work/webapps">>Dockerfile
echo "RUN nohup java -jar $jar_name >nohup.out &">>Dockerfile
echo "ENTRYPOINT [\"nohup\",\"java\",\"-jar\",\"$jar_name\",\">nohup.out\",\"&\"]">>Dockerfile

# 构建镜像
docker build -t $2 .

# 指定网络和ip启动镜像，判断如果没输入参数或者输入部分参数如何启动
if [ -z "$4" ]
then
   docker run -p 8081:8080 -dit $2
   exit
else
   docker run -dit -p 8081:8080 --net $3 --ip $4 $2
fi