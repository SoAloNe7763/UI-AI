from aift import setting
from aift.multimodal import textqa
 
setting.set_api_key('Li1PLpPipwxF3k0LHgr1hcMnJSVgiVGI')

result = textqa.generate('คิดโจทย์คณิตศาสตร์ให้หน่อย')
print(result)
print(result['content'])