from hdfs import InsecureClient

hdfs_url = 'http://localhost:9870'  
client = InsecureClient(hdfs_url, user='hadoop')  

local_file_path = 'example.txt'  
hdfs_file_path = '/user/hadoop/example.txt'  

print(f"Uploading {local_file_path} to {hdfs_file_path} in HDFS...")
client.upload(hdfs_file_path, local_file_path, overwrite=True)
print("Upload completed successfully.")

print(f"\nReading the contents of {hdfs_file_path} from HDFS:")
with client.read(hdfs_file_path, encoding='utf-8') as reader:
    file_content = reader.read()
    print("File content:\n" + file_content)
