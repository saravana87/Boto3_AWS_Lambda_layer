import json
import boto3


# Bedrock client used to interact with APIs around models
# We are using amazon.titan-text-express-v1 to create text

bedrock = boto3.client(
 service_name='bedrock', 
 region_name='us-east-1'
)
 
# Bedrock Runtime client used to invoke and question the models
bedrock_runtime = boto3.client(
 service_name='bedrock-runtime', 
 region_name='us-east-1'
)

def handler(event, context):
        
     # Just shows an example of how to retrieve information about available models
     foundation_models = bedrock.list_foundation_models()
     print(foundation_models)
     prompt = "what is jurrassic park"
    
     # The payload to be provided to Bedrock 
     body = json.dumps(
  {
     "inputText": prompt,
     "textGenerationConfig": {
        "maxTokenCount": 100,
        "stopSequences": [],
        "temperature":0,
        "topP":1
       }
   } 
     )
     
     # The actual call to retrieve an answer from the model
     response = bedrock_runtime.invoke_model(
       body=body, 
       modelId="amazon.titan-text-express-v1", 
       accept='application/json', 
       contentType='application/json'
     )
    
     response_body = json.loads(response.get('body').read())
    
     # The response from the model now mapped to the answer
     #answer = response_body.get('completions')[0].get('data').get('text')
     
     return {
       'statusCode': 200,
       'headers': {
         'Access-Control-Allow-Headers': '*',
         'Access-Control-Allow-Origin': '*',
         'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
       },
         'body': json.dumps({ "Answer": response_body })
}
