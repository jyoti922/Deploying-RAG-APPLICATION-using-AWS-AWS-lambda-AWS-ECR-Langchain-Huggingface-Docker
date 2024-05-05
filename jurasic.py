# import boto3
# import json
# import base64
# import os
# print("impotred successfully...")

# prompt="""

# provide me one 4k hd image of person who is standing over the mount everest peak.

# """

# prompt_template=[{"text":prompt,"weight":1}]

# bedrock=boto3.client(service_name="bedrock-runtime")

# payload={
#     "text_prompts":prompt_template,
#     "cfg_scale":10,
#     "seed":0,
#     "steps":50,
#     "width":512,
#     "height":512
    
# }
# body=json.dumps(payload)
# model_id="stability.stable-diffusion-xl-v0"

# response=bedrock.invoke_model(
#     body=body,
#     modelId=model_id,
#     accept="application/json",
#     contentType="application/json"
    
# )

# response_body=json.loads(response.get("body").read())
# print(response_body)

# artifacts=response_body.get("artifacts")[0]
# image_encoded=artifacts.get("base64").encode('utf-8')
# image_bytes=base64.b64decode(image_encoded)


# output_dir="output"
# os.makedirs(output_dir,exist_ok=True)
# file_name=f"{output_dir}/generated-img.png"
# with open(file_name, "wb") as f:
#         f.write(image_bytes)

import os
import json
import sys
import boto3

print("impotred successfully...")

prompt="""

        you are a cricket expert now just tell me when RCB will win the IPL?
"""

bedrock=boto3.client(service_name="bedrock-runtime")

payload={
    
    "prompt": "[INST]"+prompt+"[/INST]",
    "max_gen_len": 512,
    "temperature": 0.3,
    "top_p":0.9
}

body=json.dumps(payload)
model_id="meta.llama2-70b-chat-v1"


response=bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

response_body=json.loads(response.get("body").read())
response_text=response_body["generation"]
print(response_text)
