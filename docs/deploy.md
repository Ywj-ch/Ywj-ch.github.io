# 部署流程

本文档介绍如何将博客部署到 GitHub Pages。

---

## 前提条件

1. 已安装 Node.js 和 npm
2. 已安装 Git
3. 已有 GitHub 账号
4. 已创建 GitHub Pages 仓库（`Ywj-ch/Ywj-ch.github.io`）

---

## 部署方式

### 方式一：一键部署（推荐）⭐

```bash
hexo deploy
# 或
npm run deploy
```

Hexo 会自动：
1. 生成静态文件
2. 提交到 `_deploy_git` 目录
3. 推送到 GitHub Pages 仓库

---

### 方式二：手动部署

#### 步骤 1：生成静态文件

```bash
hexo generate
# 或
npm run build
```

生成的网站在 `public/` 目录。

#### 步骤 2：进入 public 目录

```bash
cd public
```

#### 步骤 3：提交到 GitHub

```bash
git add .
git commit -m "deploy: 更新博客内容"
git push
```

---

## 配置说明

部署配置在 `_config.yml`：

```yaml
deploy:
  type: git
  repo: git@github.com:Ywj-ch/Ywj-ch.github.io.git
  branch: main
```

| 配置项 | 说明 | 当前值 |
|--------|------|--------|
| `type` | 部署方式 | `git` |
| `repo` | GitHub 仓库地址 | `git@github.com:Ywj-ch/Ywj-ch.github.io.git` |
| `branch` | 部署分支 | `main` |

---

## 首次部署

如果是第一次部署，需要先初始化部署目录：

```bash
# 删除可能存在的部署目录
rm -rf .deploy_git

# 执行部署（会自动初始化）
hexo deploy
```

---

## 验证部署

1. 访问 https://Ywj-ch.github.io/
2. 检查文章和图片是否正常显示
3. 如有问题，检查 GitHub Pages 设置

---

## 自定义域名

如果使用自定义域名（如 `chippanda.top`）：

1. 在 GitHub Pages 仓库根目录创建 `CNAME` 文件
2. 内容填写域名：`chippanda.top`
3. 在 DNS 服务商处配置 CNAME 记录

---

## 常见问题

### Q1: 部署后图片不显示？
- 检查图片路径是否正确（应该是 `/images/年份/文章名/xxx.png`）
- 检查图片是否在 `source/images/` 目录下
- 运行 `hexo clean && hexo generate` 重新生成

### Q2: 部署失败？
- 检查 SSH key 是否已添加到 GitHub
- 检查仓库地址是否正确
- 检查是否有推送权限

### Q3: 如何回滚？
```bash
# 查看之前的提交
git log

# 回滚到指定版本
git reset --hard <commit-hash>
git push -f
```

---

**最后更新**：2026-03-01
