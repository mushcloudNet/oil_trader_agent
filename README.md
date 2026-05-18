# 🛢️ Automated Oil Market Report

Automatically fetches daily oil news and technical sentiment (from OilPrice.com, CNBC Oil, Investing.com, and Barchart) using Claude AI, then saves the report as a markdown file in this repo.

---

## 📁 File Structure

```
├── oil_report.py                          # Main script
├── .github/
│   └── workflows/
│       └── oil_report.yml                 # GitHub Actions schedule
└── reports/
    └── oil_report_YYYY-MM-DD.md           # Daily reports saved here
```

---

## ⚙️ Setup Instructions

### 1. Create a GitHub Repository
- Go to [github.com](https://github.com) and create a new repository.
- Upload `oil_report.py` and `.github/workflows/oil_report.yml` to it.

### 2. Add Your Anthropic API Key
- In your repo, go to **Settings → Secrets and variables → Actions**
- Click **New repository secret**
- Name: `ANTHROPIC_API_KEY`
- Value: your key from [console.anthropic.com](https://console.anthropic.com)

### 3. Set Your Preferred Time
Edit the cron line in `.github/workflows/oil_report.yml`:

```yaml
- cron: '0 0 * * *'   # 00:00 UTC = 8:00 AM Philippine Time
```

Use [crontab.guru](https://crontab.guru) to generate your preferred schedule.

**Common examples:**
| Time (PH, UTC+8) | Cron (UTC)       |
|------------------|------------------|
| 8:00 AM          | `0 0 * * *`      |
| 12:00 PM (noon)  | `0 4 * * *`      |
| 6:00 PM          | `0 10 * * *`     |
| 9:00 PM          | `0 13 * * *`     |

### 4. Run Manually (Optional)
Go to **Actions → Daily Oil Market Report → Run workflow** to trigger it anytime.

---

## 📊 What the Report Includes
- Latest oil market news (prices, geopolitics, OPEC, supply/demand)
- Technical sentiment from Investing.com (Buy/Sell signals per timeframe)
- Combined outlook summary

Reports are saved in the `reports/` folder as `oil_report_YYYY-MM-DD.md`.
