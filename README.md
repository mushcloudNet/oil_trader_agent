# 🛢️ Automated Oil Market Report

This repository generates a daily oil market report using Claude AI and web search data. The report includes the latest oil news, technical sentiment, and a combined outlook, then saves the result as a markdown file in `reports/`.

---

## 📁 File Structure

```
├── oil_report.py                          # Main Python script
├── prompt.txt                            # Prompt used by Claude AI
├── .github/
│   └── workflows/
│       └── oil_report.yml                 # GitHub Actions schedule and automation
└── reports/
    └── oil_report_YYYY-MM-DD.md           # Generated reports
```

---

## ⚙️ Setup Instructions

### 1. Install dependencies
If you run the script locally, install the required package:

```bash
pip install anthropic
```

### 2. Add your Anthropic API key
In your GitHub repo, go to **Settings → Secrets and variables → Actions** and add a new secret:

- Name: `ANTHROPIC_API_KEY`
- Value: your key from [console.anthropic.com](https://console.anthropic.com)

### 3. Configure the workflow schedule
Open `.github/workflows/oil_report.yml` and update the cron schedule as needed.

```yaml
- cron: '0 0 * * *'   # 00:00 UTC = 8:00 AM Philippine Time
```

Use [crontab.guru](https://crontab.guru) to convert your preferred local time to UTC.

**Common examples:**
| Time (PH, UTC+8) | Cron (UTC)       |
|------------------|------------------|
| 8:00 AM          | `0 0 * * *`      |
| 12:00 PM         | `0 4 * * *`      |
| 6:00 PM          | `0 10 * * *`     |
| 9:00 PM          | `0 13 * * *`     |

### 4. Run manually
From GitHub, go to **Actions → Daily Oil Market Report → Run workflow**.

To run locally:

```bash
python oil_report.py
```

---

## 🧠 How it works

- `oil_report.py` builds a prompt and sends it to the Anthropic Claude API.
- The prompt is defined in `prompt.txt` and requests:
  - oil market news from OilPrice.com and CNBC Oil
  - technical sentiment from Investing.com and TradingView
  - a combined summary and outlook
- The generated markdown is saved under `reports/oil_report_YYYY-MM-DD.md`.

---

## 📊 What the report includes

- Latest oil market news (prices, geopolitics, OPEC updates, supply/demand themes)
- Technical sentiment from Investing.com and TradingView
- Summary and outlook based on news and technical signals

Reports are saved in `reports/` as `oil_report_YYYY-MM-DD.md`.
