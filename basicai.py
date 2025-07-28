from aift import setting
from aift.multimodal import vqa
 
setting.set_api_key('Li1PLpPipwxF3k0LHgr1hcMnJSVgiVGI')

result = vqa.generate('sea.jpg', 'ที่นี่คือที่ไหน')
print(result)