# GitHub Pages Setup — One-Time Steps

Run these commands once from your local machine inside the "DFIR watchtower" folder
(the folder you've connected to Claude — wherever it lives on your Mac).

---

## Step 1 — Initialize the git repo and push to GitHub

Open Terminal, navigate to the DFIR Watchtower folder, then run:

```bash
git init
git add index.html watchtower_digest_*.html README.md watchtower.py build_full_digest.py
git commit -m "Initial Watchtower setup"
git branch -M main
git remote add origin https://github.com/forensicfellowship/DFIR_Watchtower.git
git push -u origin main
```

If prompted for credentials, use your GitHub username and a **Personal Access Token** (not your password).
Generate one at: GitHub → Settings → Developer Settings → Personal Access Tokens → Tokens (classic)
Scopes needed: `repo`

---

## Step 2 — Enable GitHub Pages

1. Go to https://github.com/forensicfellowship/DFIR_Watchtower/settings/pages
2. Under **Source**, select **Deploy from a branch**
3. Branch: `main` | Folder: `/ (root)`
4. Click **Save**

GitHub Pages will publish within ~60 seconds.
Live URL: **https://forensicfellowship.github.io/DFIR_Watchtower/**

---

## Step 3 — Create the Blogger page

1. Go to your Blogger dashboard → **Pages** → **New Page**
2. Title it: `DFIR Watchtower`
3. Click the **HTML view** button (top-right of the editor)
4. Paste the contents of `blogger_page_embed.html`
5. Click **Publish**
6. In Blogger → **Layout** → add the page to your navigation links

---

## Step 4 — Weekly auto-publish (after each Monday run)

After the scheduled Watchtower task runs and saves a new `index.html`, push it:

```bash
cd /path/to/your/DFIR\ watchtower/
git add index.html watchtower_digest_$(date +%Y-%m-%d).html
git commit -m "Watchtower update $(date +%Y-%m-%d)"
git push
```

Or set up a Git credential helper so this runs without prompts:
```bash
git config --global credential.helper osxkeychain   # macOS
```

---

## Verify it's working

- Digest URL: https://forensicfellowship.github.io/DFIR_Watchtower/
- Blogger page: https://www.forensicfellowship.com/p/dfir-watchtower.html (after publishing)
