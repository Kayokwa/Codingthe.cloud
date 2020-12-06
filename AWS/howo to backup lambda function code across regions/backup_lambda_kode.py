"""
Video title: How to back up all lambda function code (deployment packages) across AWS account regions 
URL: https://youtu.be/_S2JSnwnUL4

"""


#import modules
import boto3
import requests

regions = ['us-west-1', 'us-west-2']

for region in regions:
    client = boto3.client('lambda', region_name=region)

    # get a list of functions
    list_of_functions = client.list_functions(FunctionVersion='ALL', MaxItems=123)

    function_names = [function_['FunctionName'] for function_ in list_of_functions['Functions']]

    for function_name in function_names:
        lambda_func = client.get_function(FunctionName=function_name)

        #write to disk
        my_func_code = requests.get(lambda_func['Code']['Location'])
        open(function_name + '.zip', 'wb').write(my_func_code.content)
