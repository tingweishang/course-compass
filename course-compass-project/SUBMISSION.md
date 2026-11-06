# 作業繳交草稿

繳交標題：〔學校〕〔學號〕〔系級〕〔姓名〕 課程羅盤

## 1. 專案簡介
我設計「課程羅盤」，把課程資料整理成學習目標、核心觀念、例子與自我測驗，幫助自己掌握重點並找出尚未理解的地方。支援搜尋、分類、手機瀏覽與本機進度。第一門課依課堂講義改寫，另外兩門原創示範呈現跨科目延伸方式。

## 2. GitHub Repository
https://github.com/tingweishang/course-compass

狀態：Repository 已公開；目前 GitHub 連線寫入回傳 403，原始碼尚待上傳。

## 3. 網頁連結
https://course-compass-tingwei.jetbarn.chatgpt.site

## 4. AGENTS.md
本專案根目錄的 AGENTS.md，規定專案目的、目錄、資料欄位、視覺、來源處理、開發流程與驗收標準。

## 5. 規則如何幫助 AI 延伸
新增內容時，AI 先讀 AGENTS.md，使用 templates/course.json，從教材整理三個目標、三個附例子的觀念、常見誤解、練習和兩題有解析的測驗，再將資料加入 courses.json。共用模板自動呈現課程，不用每次重寫頁面。驗證腳本會檢查必要欄位、唯一 id 與答案索引；來源規則避免捏造教材。因此換一門課、換一次對話或換一個 AI，也能維持一致的整理方式。
