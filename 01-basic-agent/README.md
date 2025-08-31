# Basic Agent with Google Search

โปรเจคนี้เป็นตัวอย่างการสร้าง Agent พื้นฐานโดยใช้ `google-adk` library.

## โครงสร้างโปรเจค

-   `google_search_agent/`: โฟลเดอร์ที่เก็บโค้ดของ agent
    -   `__init__.py`: ทำให้ `google_search_agent` เป็น Python package
    -   `agent.py`: โค้ดหลักของ agent ที่มีการเรียกใช้ `google_search` tool
    -   `.env`: ไฟล์สำหรับเก็บค่า `GOOGLE_API_KEY`

## การทำงาน

Agent นี้ชื่อ `google_search_agent` ถูกสร้างขึ้นโดยใช้ `gemini-2.5-flash` model.
Agent มีหน้าที่ในการช่วยค้นหาข้อมูลบนเว็บไซต์โดยใช้ `google_search` tool.

## วิธีการใช้งาน

1.  ติดตั้ง dependencies:
    ```bash
    # Create
    python -m venv .venv
    # Activate (each new terminal)
    # macOS/Linux: source .venv/bin/activate
    # Windows CMD: .venv\Scripts\activate.bat
    # Windows PowerShell: .venv\Scripts\Activate.ps1
    ```
    ติดตั้ง Google ADK
    ```bash
    pip install google-adk
    ```
2.  ตั้งค่า `GOOGLE_API_KEY` ในไฟล์ `.env`
3.  รัน agent:
    ```bash
    adk web
    ```
