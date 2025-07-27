import streamlit as st # Streamlit 라이브러리 임포트
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled # YouTube 자막 API 관련 임포트
from urllib.parse import urlparse, parse_qs # URL 파싱을 위해 임포트

# # 웹 페이지의 제목 설정
# st.set_page_config(page_title="유튜브 자막 추출기", layout="centered")
# st.title("🎬 유튜브 자막 추출기")
# st.markdown("영상 URL을 입력하고 자막을 가져오세요.")

# # 사용자로부터 유튜브 URL을 입력받는 텍스트 입력창
# youtube_url_input = st.text_input("유튜브 영상 주소를 입력하세요 (예: https://www.youtube.com/watch?v=VIDEO_ID)", "")

# # 자막 가져오기 버튼
# if st.button("자막 가져오기"):
#     if youtube_url_input:
#         video_id = None
#         try:
#             # YouTube URL에서 비디오 ID 추출
#             parsed_url = urlparse(youtube_url_input)
#             if parsed_url.hostname in ('www.youtube.com', 'youtube.com'):
#                 query_params = parse_qs(parsed_url.query)
#                 video_id = query_params.get('v', [None])[0]
#             elif parsed_url.hostname == 'youtu.be':
#                 video_id = parsed_url.path[1:] # /video_id 형태에서 ID만 추출

#             if video_id:
#                 with st.spinner("자막을 가져오는 중... 잠시만 기다려주세요."):
#                     # YouTubeTranscriptApi.get_transcript를 사용하여 자막을 가져옵니다.
#                     # 영어(en)를 우선 시도하고, 없으면 한국어(ko)를 시도합니다.
#                     transcript_data = YouTubeTranscriptApi.get_transcript(
#                         video_id,
#                         languages=['en', 'ko'] # 영어, 한국어 순으로 시도
#                     )

#                 # 자막 데이터를 텍스트로 합치기
#                 transcript_text = "\n".join([item['text'] for item in transcript_data])

#                 st.subheader(f"영상 ID: `{video_id}` 자막")
#                 st.info("아래 텍스트 박스에서 자막을 확인할 수 있습니다.")
#                 # 텍스트 에어리어에 자막 표시 (높이 조절 가능)
#                 st.text_area("영상 자막", transcript_text, height=400)

#             else:
#                 st.error("❌ 유효한 유튜브 비디오 ID를 찾을 수 없습니다. URL을 확인해주세요.")

#         # youtube-transcript-api에서 발생하는 특정 예외 처리
#         except NoTranscriptFound:
#             st.warning("⚠️ 해당 영상에 요청된 언어(영어, 한국어)의 자막을 찾을 수 없거나, 자막이 없습니다.")
#         except TranscriptsDisabled:
#             st.warning("⚠️ 해당 영상의 자막이 비활성화되어 있습니다.")
#         except Exception as e:
#             st.error(f"❌ 자막을 가져오는 중 알 수 없는 오류가 발생했습니다: {e}")
#             st.info("URL이 올바른지, 영상이 비공개/삭제되었는지, 또는 자막을 제공하지 않는 영상인지 확인해보세요.")
#     else:
#         st.warning("☝️ 유튜브 영상 주소를 입력해주세요.")

# st.markdown("---")

