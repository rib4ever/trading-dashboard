# AI Trade Supervisor

## Purpose

AI Trade Supervisor reviews Ravi's trades using:

- Raw Journal Story written in simple words.
- Structured trade fields from Notion.
- Synced screenshot records from Trade Screenshots.
- Google Drive screenshot files.

The AI checks whether the journal story matches the screenshot evidence and writes back structured feedback.

## Notion Fields Added to Trades

```text
Raw Journal Story
AI Review Status
AI Reality Check
AI Mistake Diagnosis
AI Future Rules
AI Review Confidence
AI Reviewed Time
```

## AI Review Status Values

```text
Not Requested
Ready for AI Review
AI Review Complete
Needs More Screenshots
AI Review Error
```

## User Flow

```text
1. Write simple notes in Raw Journal Story.
2. Upload and sync screenshots using Screenshot Sync.
3. Set AI Review Status to Ready for AI Review.
4. AI Review workflow processes the trade.
5. AI writes structured review outputs into Notion.
```

## AI Review Output Fields

```text
AI Review: summary
AI Reality Check: journal story vs screenshot evidence
AI Mistake Diagnosis: main mistakes and weaknesses
AI Future Rules: rules to avoid repeating mistakes
AI Review Confidence: 0.0 to 1.0
AI Reviewed Time: timestamp
```

## Evidence Rules

The AI should not invent chart facts. If screenshots are missing, unclear, or insufficient, it should mark:

```text
AI Review Status = Needs More Screenshots
```

## GitHub Files Added

```text
config/ai_trade_review_prompt.md
src/services/ai_trade_review_service.py
scripts/run_ai_trade_review.py
```

## Required Extra Secret

```text
OPENAI_API_KEY
```

Optional model override:

```text
OPENAI_TRADE_REVIEW_MODEL
```

Default model in code:

```text
gpt-4.1-mini
```

## Planned Workflow File

```text
.github/workflows/ravi_ai_trade_review.yml
```

The workflow should run manually and optionally every 60 minutes.
