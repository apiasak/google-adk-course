from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="google_search_agent",
    model="gemini-2.5-flash",
    description="A search agent that uses Google's search API to find information on the web.",
    instruction="""
    คุณคือผู้ช่วยอัจฉริยะที่ช่วยค้นหาข้อมูลบนเว็บไซต์ต่างๆ ที่มีความสามารถในการตอบคำถามและให้ข้อมูลที่ถูกต้องและน่าเชื่อถือ
    คุณสามารถใช้เครื่องมือต่อไปนี้ ในการค้นหาข้อมูลก่อนตอบผู้ใช้
    - google_search
    """,
    tools=[google_search]
)
