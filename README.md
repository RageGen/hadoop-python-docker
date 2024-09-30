# Hadoop - Python HDFS Docker Container

This repository contains a Dockerfile to set up a single-node Hadoop HDFS container using Docker. The container allows you to run a NameNode and a DataNode, exposing the HDFS web UI on port `9870`. Additionally, you can use the provided Python script to upload and read files from HDFS.

## Prerequisites

- Docker Desktop installed on your computer


## Installing Docker Desktop

Follow these steps to install Docker Desktop on your machine:

### Windows

1. Download Docker Desktop for Windows from [Docker Hub](https://www.docker.com/products/docker-desktop).
2. Run the installer and follow the on-screen instructions.
3. After installation, launch Docker Desktop, and ensure it is running.

### Linux

1. Install Docker by following the instructions on the [Docker documentation](https://docs.docker.com/engine/install/).

### Build and Run the Hadoop - Python HDFS Container

#### Clone the repository

```bash
git clone https://github.com/ragegen/hadoop-python-docker.git
cd hadoop-python-docker
```

#### Build the Docker image

```bash
docker build -t hadoop-python .
```

#### Run the Docker container

```bash
docker run -d --name hadoop-python -p 9870:9870 hadoop-python
```

- The ```-d``` flag runs the container in detached mode.

- The ```--name``` flag assigns a name (hadoop-python) to the container.

- The ```-p 9870:9870``` flag maps port 9870 from the container to 9870 on the host machine, making the HDFS web UI accessible at ```http://localhost:9870```.

### Running the Test Script

#### Create a Sample File

```bash
docker exec -it hadoop-python bash -c 'echo "Hello, HDFS! This is a test file." > /example.txt'

```

####  Execute the Script Inside the Container

```bash
docker exec -it hadoop-python python3 script.py
```

#### Expected Output

```
Uploading example.txt to /user/hadoop/example.txt in HDFS...
Upload completed successfully.

Reading the contents of /user/hadoop/example.txt from HDFS:
File content:
Hello, HDFS! This is a test file.
```

#### Verify the File in the HDFS UI

Navigate to ```http://localhost:9870``` in your browser and browse to ```/user/hadoop/```. You should see ```example.txt``` listed in the directory.

### Cleanup

#### To stop and remove the running container

```bash
docker stop hadoop-python
docker rm hadoop-python
```

#### To remove the Docker image

```bash
docker rmi hadoop-python
```

### License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License - see the LICENSE file for details.