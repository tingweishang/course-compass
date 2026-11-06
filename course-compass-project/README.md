# 課程羅盤 Course Compass

把課程資料整理為學習目標、核心觀念、具體例子與自我測驗的繁體中文網站。

網站：https://course-compass-tingwei.jetbarn.chatgpt.site

GitHub：https://github.com/tingweishang/course-compass

## 功能
課程搜尋與分類、共用課程頁面、兩題測驗與解析、瀏覽器本機完成標記、手機版版面。沒有後端、帳號、上傳功能或自動 AI 摘要服務。

## 本機啟動
需要 Python 3，無需安裝套件：

```sh
python3 scripts/validate.py
python3 -m http.server 8000 --directory dist
```

在瀏覽器開啟 `http://localhost:8000`。不要直接雙擊 index.html，因為內容透過 fetch 載入。

## 新增一門課
先讀 AGENTS.md。複製 templates/course.json，完全替換內容，再加入 dist/data/courses.json 的陣列。id 使用唯一英文 kebab-case。驗證後，列表、分類和 `#course/id` 會使用同一模板產生，不需新增 HTML。詳見 AGENTS.md 的欄位規則與驗收流程。

給 AI 的範例指令：
> 請先讀 AGENTS.md，依照我提供的講義新增課程。遵守模板，保留來源頁碼，缺資料標記待確認。執行驗證並檢查頁面與測驗。

## 內容來源
「換你當老闆」依使用者提供的講義第 11–24 頁改寫；不包含原始完整講義。「學會如何學習」「Python 迴圈入門」為原創示範，非使用者實際修課紀錄。預估閱讀時間不是學習成效保證。

## 發布到 GitHub Pages
1. 在自己的 GitHub 建立名為 course-compass 的公開 Repository。
2. 將本專案完整上傳，包含 AGENTS.md、dist、templates、scripts 與 .github。
3. 到 Settings → Pages → Source 選擇 GitHub Actions。
4. 推送 main 或手動執行 Validate and deploy Pages。
5. 成功後使用 workflow 顯示的實際網站網址。資源使用相對路徑，支援 Repository 子路徑。

## 資料與驗證
進度使用 localStorage，不跨裝置同步。課程資料一律轉義為純文字。不要提交原始完整教材、個資、憑證或 API 金鑰。使用 scripts/validate.py 驗證結構與答案索引；人工核對來源與教學正確性。GitHub workflow 會在部署前執行同一驗證。
