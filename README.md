# Django HomeWork - TODO、AJAX、JSON

這是一個 Django 作業專案，主要功能是建立一個待辦事項應用。使用者可以新增、編輯和刪除待辦事項，並且可以標記待辦事項為已完成或未完成。除了待辦事項功能，還包括了用戶註冊頁面和景點展示頁面。

## 功能

- **新增待辦事項**: 使用者可以添加新的待辦事項到列表中。
- **顯示待辦事項列表**: 列出所有待辦事項，並顯示其狀態（已完成/未完成）。
- **編輯待辦事項狀態**: 可以標記待辦事項為已完成或未完成。
- **刪除待辦事項**: 可以刪除不再需要的待辦事項。
- **註冊頁面**: 使用者可以通過註冊頁面創建新帳戶。
- **景點展示**: 顯示旅遊景點的信息。

## 安裝與運行

1. **克隆專案**

    ```bash
    git clone https://github.com/lf2net679/DjangoHomeWork.git
    ```

2. **建立虛擬環境並安裝依賴**

    ```bash
    python -m venv env
    source env/bin/activate  # 在 Windows 上使用 `env\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **應用資料庫遷移**

    ```bash
    python manage.py migrate
    ```

4. **啟動開發伺服器**

    ```bash
    python manage.py runserver
    ```

5. **在瀏覽器中訪問**

    打開你的瀏覽器並訪問 [http://127.0.0.1:8000/](http://127.0.0.1:8000/) 訪問首頁內的應用。

## 文件結構

- `todo/`: Django 應用目錄，包含待辦事項應用的所有相關文件。
- `migrations/`: 存放資料庫遷移文件。
- `static/`: 存放靜態文件（CSS、JS、圖片等）。
- `templates/`: 存放 HTML 模板。
  - `todo/`: 存放待辦事項應用的模板。
  - `index.html`: 顯示待辦事項列表的頁面。
- `models.py`: 定義數據模型。
- `views.py`: 定義視圖函數。
- `urls.py`: 定義 URL 路由。
- `manage.py`: Django 的命令行工具。
- `requirements.txt`: 專案所需的 Python 庫。

## 新增頁面

- [Go to TODO清單 homework](http://127.0.0.1:8000/todo/) - 訪問待辦事項清單頁面。
- [Go to 註冊頁面 homework](http://127.0.0.1:8000/register/) - 訪問用戶註冊頁面。
- [Go to 旅遊景點 homework](http://127.0.0.1:8000/travel/) - 訪問旅遊景點展示頁面。
