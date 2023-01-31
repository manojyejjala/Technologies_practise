import boto3
import functools as ft
import operator as op

client = boto3.client('s3')
# # # # response = client.list_bucket_analytics_configurations(
# # # #     Bucket='ex-bucket-srinivas',
# # # #     ContinuationToken='string',
# # # #     ExpectedBucketOwner='string'
# # # # )
# # # # print(client)
# # # # print(response)
# response = client.head_object(Bucket= "manoj93", Key= "example_2.json")
# data = response.read()
# print(response)
response =client.list_objects_v2(Bucket= "manoj93"''' )
for key in sorted(response['Contents'],
 key=lambda obj: obj['LastModified'], reverse=True):
    print(key)
# # import boto3
    
# # bucket_name = "ex-bucket-srinivas"
# # prefix = "/"
    
# # get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))

# # s3 = boto3.client('s3')
# # objs = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix, Delimiter='/' ['Contents'])
# # last_added = [obj['Key'] for obj in sorted(objs, key=get_last_modified)][0]
# import boto3
# def list_s3_files_in_folder_using_client():
#     """
#     This function will list down all files in a folder from S3 bucket
#     :return: None
#     """
#     s3_client = boto3.client("s3")
#     bucket_name = "testbucket-frompython-2"
#     response = s3_client.list_objects_v2(Bucket='ex-bucket-srinivas', Prefix="images")
#     files = response.get("Contents")
#     for file in files:
#         print(f"file_name: {file['Key']}, size: {file['Size']}")