# 🚀 Hướng dẫn Enable GitHub Pages

## Bước 1: Truy cập GitHub Repository Settings

1. Truy cập repository: `https://github.com/taipm/python_book`
2. Click tab **"Settings"** (ở góc phải trên)
3. Scroll xuống phần **"Pages"** ở sidebar bên trái

## Bước 2: Configure GitHub Pages

### Option 1: Deploy from docs/ folder (Recommended)
1. Trong **"Source"** section:
   - Chọn **"Deploy from a branch"**
   - **Branch**: `main`
   - **Folder**: `/docs`
2. Click **"Save"**

### Option 2: GitHub Actions (Advanced)
1. Trong **"Source"** section:
   - Chọn **"GitHub Actions"**
2. GitHub sẽ tự động detect Jekyll và suggest workflow
3. File workflow đã được tạo sẵn tại `.github/workflows/pages.yml`

## Bước 3: Verify Deployment

Sau khi enable, GitHub sẽ:
1. **Build** trang web từ docs/ folder
2. **Deploy** lên `https://taipm.github.io/python_book`
3. Quá trình này mất **2-5 phút**

## Bước 4: Check Website

1. Đợi deployment hoàn tất (check Actions tab)
2. Truy cập: `https://taipm.github.io/python_book`
3. Xem trang web đã hoạt động chưa

## 📋 Checklist

- [ ] Repository settings → Pages
- [ ] Source: Deploy from branch (main, /docs)
- [ ] Save settings
- [ ] Wait for deployment (2-5 minutes)
- [ ] Test website: `https://taipm.github.io/python_book`

## 🔧 Troubleshooting

### Website không load:
- Check Actions tab xem có lỗi build không
- Verify file `docs/_config.yml` syntax đúng
- Ensure `docs/index.md` tồn tại

### Jekyll build errors:
- Check `docs/Gemfile` dependencies
- Review Jekyll theme compatibility
- Check markdown syntax trong docs files

### 404 Not Found:
- Verify repository name đúng
- Check branch name (phải là `main`)
- Ensure folder path `/docs` đúng

## 📞 Support

Nếu gặp vấn đề:
1. Check GitHub Actions logs
2. Review GitHub Pages documentation
3. Create issue tại repository

---

**Sau khi enable thành công, website sẽ available tại:**
## 🌐 https://taipm.github.io/python_book

**Auto-deployment:** Mỗi khi push code mới, website sẽ tự động update!
