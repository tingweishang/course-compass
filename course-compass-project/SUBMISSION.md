# 作業繳交

繳交標題：政大 115356040 資管碩一 商庭維 
主題：課程羅盤

## 1. 專案簡介
根據這次作業的要求，我設計了「課程羅盤」這個網頁，能將課程資料整理成學習目標、核心觀念、例子與自我測驗，來幫助我掌握重點並找出尚未理解的地方。支援搜尋、分類、手機瀏覽與本機進度。

## 2. GitHub Repository
https://github.com/tingweishang/course-compass

## 3. 網頁連結
https://course-compass-tingwei.jetbarn.chatgpt.site

## 4. AGENTS.md
規定專案目的、目錄、資料欄位、視覺、來源處理、開發流程與驗收標準。

## 5. 規則如何幫助AI延伸
新增內容時，AI先讀AGENTS.md，使用templates/course.json，從教材整理三個目標、三個附例子的觀念、常見誤解、練習和兩題有解析的測驗，再將資料加入courses.json，並使用共用模板自動呈現課程，不用每次重寫頁面，驗證腳本會檢查必要欄位、唯一id與答案索引，因此換一門課、換一次對話或換一個AI，也能維持一致的整理方式。
