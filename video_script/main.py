import streamlit as st
import altair as alt
from utils import generate_script

st.title(":clapper: 视频脚本生成器")
with st.sidebar:
    ak = st.text_input("请输入千帆模型的api_key",type="password")
    sk = st.text_input("请输入千帆模型的secret_key",type="password")
    st.markdown("[获取千帆模型的api_key和secret_key](https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application/v1)")
subject = st.text_input(":dart: 请输入视频的主题")
video_time = st.number_input(" 请输入视频的大致时长（单位：分钟）",min_value=0.1,step=0.1)
creativity = st.slider("请输入视频脚本的创造力（数字越小越严谨，数字越大越多样）",min_value=0.0,max_value=1.0,value=0.1,step=0.01)
submit = st.button(":star: 生成脚本")
if submit and not ak:
    st.info("请输入千帆模型的api_key")
    st.stop()
if submit and not sk:
    st.info("请输入千帆模型的secret_key")
    st.stop()
if submit and not subject:
    st.info("请输入视频的主题")
    st.stop()
if submit and not video_time>=0.1:
    st.info("视频长度输入有误")
    st.stop()
if submit:
    with st.spinner(("AI正在思考，请稍等...")):
        title,script = generate_script(subject,video_time,creativity,ak,sk)
    st.success("视频脚本已经生成！")
    st.subheader(":fire: 标题：")
    st.write(title)
    st.subheader(":open_book: 脚本内容：")
    st.write(script)