from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
PROJECT = ROOT / 'pine-script' / 'master-smc-sats-nci-story'
BASE = PROJECT / '03_CANDIDATES' / 'master-smc-sats-nci-story-v0.1.4.pine'
BLOCK = PROJECT / '03_SCRIPT_BLOCKS' / '12_smart_validation_v0_1_6_clean.pine'
OUT = PROJECT / '03_CANDIDATES' / 'master-smc-sats-nci-story-v0.1.6.pine'
base = BASE.read_text(encoding='utf-8')
block = BLOCK.read_text(encoding='utf-8')
content = '// MASTER SMC + SATS + NCI STORY CANDIDATE v0.1.6\n// Base: v0.1.4 plus clean smart validation.\n' + base.rstrip() + '\n\n' + block.rstrip() + '\n'
checks = ['v0.1.6','nciV16BuySignal','nciV16SellSignal','NCI v0.1.6 Smart BUY','NCI v0.1.6 Smart SELL']
for x in checks:
    if x not in content:
        raise RuntimeError('missing ' + x)
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(content, encoding='utf-8')
print('Created', OUT.relative_to(ROOT))
