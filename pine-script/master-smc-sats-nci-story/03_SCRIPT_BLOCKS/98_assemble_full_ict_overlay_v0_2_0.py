from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJECT = ROOT / 'pine-script' / 'master-smc-sats-nci-story'
ICT = PROJECT / '03_SCRIPT_BLOCKS' / '00_ict_validated_smc_source_full.pine'
OVERLAY = PROJECT / '03_SCRIPT_BLOCKS' / '20_nci_story_overlay_for_ict_v0_2_0.pine'
OUT = PROJECT / '03_CANDIDATES' / 'master-smc-sats-nci-story-v0.2.0-full-ict-overlay.pine'

def active_count(text, token):
    return sum(1 for line in text.splitlines() if line.strip().startswith(token))

def main():
    if not ICT.exists():
        raise RuntimeError('Missing restored ICT source')
    if not OVERLAY.exists():
        raise RuntimeError('Missing NCI overlay block')
    ict = ICT.read_text(encoding='utf-8')
    overlay = OVERLAY.read_text(encoding='utf-8')
    ict = ict.replace('indicator("ICT Validated SMC v1", "ICT-V", overlay=true, max_labels_count=500, max_lines_count=500, max_boxes_count=500)', 'indicator("Master SMC SATS NCI Story v0.2.0 Full ICT Overlay", "NCI_ICT_v020", overlay=true, max_labels_count=500, max_lines_count=500, max_boxes_count=500)', 1)
    header = '// MASTER SMC SATS NCI STORY v0.2.0 - FULL ICT OVERLAY\n'
    content = header + ict.rstrip() + '\n\n' + overlay.rstrip() + '\n'
    if active_count(content, '//@version') != 1:
        raise RuntimeError('Candidate must contain exactly one //@version')
    if active_count(content, 'indicator(') != 1:
        raise RuntimeError('Candidate must contain exactly one indicator()')
    for item in ['type OTEZone','type BPR','type IFVG','type BreakerBlock','showOTE','showBPR','showIFVG','nciOvlBullOTEInside','NCI ICT Overlay BUY Story']:
        if item not in content:
            raise RuntimeError('Missing ' + item)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(content, encoding='utf-8')
    print('Created', OUT.relative_to(ROOT), 'lines', len(content.splitlines()))

if __name__ == '__main__':
    main()
