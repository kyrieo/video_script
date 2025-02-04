from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import QianfanChatEndpoint
from langchain_community.utilities import WikipediaAPIWrapper

def generate_script(subject,video_length,creativity,api_key,secret_key):
    title_template = ChatPromptTemplate.from_messages(
        [
            ("human","请为{subject}这个主题的视频想一个吸引人的标题")
         ]
    )
    script_template = ChatPromptTemplate.from_messages(
        [
            ("human",
            """你是一位短视频频道的博主。根据以下标题和相关信息，为短视频频道写一个视频脚本。
             视频标题：{title}，视频时长：{duration}分钟，生成的脚本的长度尽量遵循视频时长的要求。
             要求开头抓住限球，中间提供干货内容，结尾有惊喜，脚本格式也请按照【开头、中间，结尾】分隔。
             整体内容的表达方式要尽量轻松有趣，吸引年轻人。
             脚本内容可以结合以下维基百科搜索出的信息，但仅作为参考，只结合相关的即可，对不相关的进行忽略：
             """)
        ]
    )
    qianfan_chat = QianfanChatEndpoint(
        model="ERNIE-3.5-8K",
        temperature=creativity,
        api_key=api_key,
        secret_key=secret_key,
    )
    title_chain = title_template | qianfan_chat
    script_chain = script_template | qianfan_chat
    title = title_chain.invoke({"subject":subject}).content
    # search = WikipediaAPIWrapper(lang="zh")
    # search_result = search.run(subject)
    script = script_chain.invoke({"title":title,"duration":video_length,"wikipedia_search":"search_result"}).content
    return title,script
# print(generate_script("玉龙雪山",1,0.7,"KqqbeEq6uyKNM0FgnVapwCGM","S40RS2tFfbfmmRh9M19BoVLhmoAySbWo"))