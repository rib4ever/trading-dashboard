# Patch 11 — Settings Usage Report

Generated from:

```text
pine-script/master-smc-sats/03_MASTER_CANDIDATES/master-smc-sats-ravi-custom-01-v1.6-theme-engine-candidate.pine
```

Total input variables found: **167**

## Interpretation

- Downstream refs = how many times the input variable appears after its declaration.
- A value of 0 means the setting may be disconnected or only used indirectly through generated replacement logic. Review manually before deleting.
- This audit does not change trading logic.

## Inputs by group

### UNKNOWN

| Variable | Type | Downstream refs | Line |
|---|---:|---:|---:|
| `themePreset` | `string` | 12 | 74 |
| `themeIntensity` | `string` | 2 | 97 |
| `masterPreset` | `string` | 10 | 263 |
| `entryWorkflowMode` | `string` | 7 | 1552 |

### GRP_THEME

| Variable | Type | Downstream refs | Line |
|---|---:|---:|---:|
| `themeZoneTransparency` | `int` | 4 | 103 |
| `themePanelTransparency` | `int` | 2 | 104 |
| `manualBullColor` | `color` | 1 | 106 |
| `manualBearColor` | `color` | 1 | 107 |
| `manualNeutColor` | `color` | 1 | 108 |
| `manualSlColor` | `color` | 1 | 109 |
| `manualTpColor` | `color` | 1 | 110 |

### GRP_MASTER

| Variable | Type | Downstream refs | Line |
|---|---:|---:|---:|
| `manualMinTqi` | `float` | 2 | 278 |
| `manualUltraTqi` | `float` | 2 | 279 |
| `manualMinEr` | `float` | 2 | 280 |
| `manualKillzoneOnly` | `bool` | 2 | 281 |
| `manualSweepReq` | `bool` | 1 | 282 |
| `manualBlockLowVol` | `bool` | 1 | 283 |
| `manualBlockLowAtr` | `bool` | 1 | 284 |
| `manualSatsLookback` | `int` | 2 | 285 |
| `setupSweepLookback` | `int` | 2 | 288 |
| `setupCooldownBars` | `int` | 2 | 289 |
| `showCounterTrendSetups` | `bool` | 2 | 290 |
| `enableOpportunityMode` | `bool` | 2 | 291 |
| `setupRequiresQuality` | `bool` | 1 | 292 |
| `setupMinTqi` | `float` | 1 | 293 |
| `setupMinEr` | `float` | 1 | 294 |
| `opportunityMinTqi` | `float` | 1 | 295 |
| `opportunityMinEr` | `float` | 1 | 296 |
| `opportunityUsesKZ` | `bool` | 1 | 297 |
| `opportunityUsesVolume` | `bool` | 1 | 298 |
| `zoneRequirement` | `string` | 2 | 300 |
| `requireHtfPoiContext` | `bool` | 2 | 303 |
| `htfPoiMode` | `string` | 2 | 304 |
| `htfPoiType` | `string` | 4 | 305 |
| `htfPoiOverridesBias` | `bool` | 2 | 306 |
| `requireExecutionZone` | `bool` | 2 | 307 |
| `requireLiquidityConfirmation` | `bool` | 2 | 308 |
| `allowLondon` | `bool` | 1 | 923 |
| `allowNyAm` | `bool` | 1 | 924 |
| `allowNyPm` | `bool` | 1 | 925 |
| `allowAsian` | `bool` | 1 | 926 |
| `allowLunch` | `bool` | 1 | 927 |
| `allowNoKz` | `bool` | 2 | 928 |

### GRP_SMC

| Variable | Type | Downstream refs | Line |
|---|---:|---:|---:|
| `tf1Enabled` | `bool` | 2 | 377 |
| `tf1` | `timeframe` | 6 | 378 |
| `tf1Weight` | `int` | 1 | 379 |
| `tf2Enabled` | `bool` | 2 | 381 |
| `tf2` | `timeframe` | 6 | 382 |
| `tf2Weight` | `int` | 1 | 383 |
| `tf3Enabled` | `bool` | 2 | 385 |
| `tf3` | `timeframe` | 6 | 386 |
| `tf3Weight` | `int` | 1 | 387 |
| `tf4Enabled` | `bool` | 2 | 389 |
| `tf4` | `timeframe` | 6 | 390 |
| `tf4Weight` | `int` | 1 | 391 |
| `tf5Enabled` | `bool` | 2 | 393 |
| `tf5` | `timeframe` | 6 | 394 |
| `tf5Weight` | `int` | 1 | 395 |
| `emaLength` | `int` | 1 | 397 |
| `swingLength` | `int` | 10 | 398 |
| `obLookback` | `int` | 4 | 399 |
| `fvgLookback` | `int` | 3 | 400 |
| `atrAvgLength` | `int` | 1 | 401 |
| `biasUseStruct` | `bool` | 2 | 403 |
| `biasUseOB` | `bool` | 2 | 404 |
| `biasUseFVG` | `bool` | 2 | 405 |
| `biasUseEMA` | `bool` | 2 | 406 |
| `biasUseSwing` | `bool` | 2 | 407 |

### GRP_VIS

| Variable | Type | Downstream refs | Line |
|---|---:|---:|---:|
| `showOB` | `bool` | 1 | 412 |
| `showFVG` | `bool` | 1 | 413 |
| `showSwingLabels` | `bool` | 1 | 414 |
| `showSwingLines` | `bool` | 1 | 415 |
| `plotPDHL` | `bool` | 1 | 416 |
| `plotPWHL` | `bool` | 1 | 417 |
| `plotPMHL` | `bool` | 1 | 418 |
| `showEMA` | `bool` | 1 | 419 |
| `showSatsLine` | `bool` | 1 | 420 |
| `visualMode` | `string` | 3 | 421 |
| `showSetupWarnings` | `bool` | 2 | 422 |
| `showSniperEntries` | `bool` | 4 | 423 |
| `showUltraEntries` | `bool` | 2 | 424 |
| `showRiskLines` | `bool` | 2 | 425 |
| `showMiniStatus` | `bool` | 1 | 426 |
| `miniStatusPosition` | `string` | 4 | 427 |
| `obExtend` | `int` | 1 | 429 |
| `fvgExtend` | `int` | 1 | 430 |
| `levelExtend` | `int` | 10 | 431 |
| `labelOffset` | `int` | 4 | 432 |

### GRP_HTFLVL

| Variable | Type | Downstream refs | Line |
|---|---:|---:|---:|
| `showHtfKeyLevels` | `bool` | 2 | 437 |
| `htfKeyTf1` | `timeframe` | 1 | 438 |
| `htfKeyTf2` | `timeframe` | 1 | 439 |
| `htfKeyColor1` | `color` | 8 | 440 |
| `htfKeyColor2` | `color` | 8 | 441 |
| `showHtfSwingHL` | `bool` | 1 | 442 |
| `showHtfPoiLevels` | `bool` | 1 | 443 |
| `showHtfKeyLabels` | `bool` | 1 | 444 |
| `requireKeyLevelTouch` | `bool` | 1 | 445 |
| `keyLevelTouchAtrBuffer` | `float` | 1 | 446 |

### GRP_SATS

| Variable | Type | Downstream refs | Line |
|---|---:|---:|---:|
| `satsPreset` | `string` | 2 | 993 |
| `atrLenInput` | `int` | 2 | 994 |
| `baseMultInput` | `float` | 2 | 995 |
| `sourceInput` | `source` | 4 | 996 |
| `useAdaptiveInput` | `bool` | 1 | 997 |
| `erLengthInput` | `int` | 2 | 998 |
| `adaptStrengthInput` | `float` | 1 | 999 |
| `atrBaselineLenInput` | `int` | 1 | 1000 |
| `useTqiInput` | `bool` | 4 | 1001 |
| `qualityStrengthInput` | `float` | 2 | 1002 |
| `qualityCurveInput` | `float` | 1 | 1003 |
| `multSmoothInput` | `bool` | 2 | 1004 |
| `useAsymBandsInput` | `bool` | 1 | 1005 |
| `asymStrengthInput` | `float` | 2 | 1006 |
| `useEffAtrInput` | `bool` | 1 | 1007 |
| `useCharFlipInput` | `bool` | 1 | 1008 |
| `charFlipMinAgeInput` | `int` | 1 | 1009 |
| `charFlipHighInput` | `float` | 1 | 1010 |
| `charFlipLowInput` | `float` | 1 | 1011 |
| `tqiWeightErInput` | `float` | 2 | 1013 |
| `tqiWeightVolInput` | `float` | 2 | 1014 |
| `tqiWeightStructInput` | `float` | 2 | 1015 |
| `tqiWeightMomInput` | `float` | 2 | 1016 |
| `tqiStructLenInput` | `int` | 2 | 1017 |
| `tqiMomLenInput` | `int` | 3 | 1018 |

### GRP_SK

| Variable | Type | Downstream refs | Line |
|---|---:|---:|---:|
| `showSmartKeyLevels` | `bool` | 2 | 1168 |
| `enableSmartKeyFallback` | `bool` | 4 | 1169 |
| `smartKeySourceMode` | `string` | 12 | 1170 |
| `smartKeySelectionMode` | `string` | 2 | 1171 |
| `smartKeyPivotLen` | `int` | 6 | 1172 |
| `smartKeyMaxStored` | `int` | 2 | 1173 |
| `smartKeyMinTouches` | `int` | 10 | 1174 |
| `smartKeyAtrLen` | `int` | 1 | 1175 |
| `smartKeyAtrTolerance` | `float` | 1 | 1176 |
| `smartKeyTouchBuffer` | `float` | 1 | 1177 |
| `smartKeyExtendBars` | `int` | 4 | 1178 |
| `showSmartLabels` | `bool` | 2 | 1179 |
| `useSmartKeyForEntries` | `bool` | 3 | 1181 |
| `useSmartKeyForTP` | `bool` | 2 | 1182 |
| `smartSupportColor` | `color` | 1 | 1184 |
| `smartResistanceColor` | `color` | 1 | 1185 |
| `smartLiquidityColor` | `color` | 4 | 1186 |

### GRP_ENTRY

| Variable | Type | Downstream refs | Line |
|---|---:|---:|---:|
| `manualEnableSetupWarnings` | `bool` | 1 | 1566 |
| `manualEnableOpportunityEntries` | `bool` | 1 | 1567 |
| `manualEnableNormalEntries` | `bool` | 1 | 1568 |
| `manualEnableSniperEntries` | `bool` | 1 | 1569 |
| `manualEnableUltraEntries` | `bool` | 1 | 1570 |
| `manualEnableKeyLevelEntries` | `bool` | 1 | 1571 |
| `showEntryLabelsFinalInput` | `bool` | 1 | 1573 |
| `showHistoricalEntries` | `bool` | 1 | 1574 |
| `entryHistoryBars` | `int` | 1 | 1575 |
| `showTpSlForEntriesFinal` | `bool` | 2 | 1576 |
| `restrictConfirmedEntriesToExecutionTf` | `bool` | 1 | 1578 |
| `maxConfirmedEntryTfMinutes` | `int` | 2 | 1579 |
| `allowHigherTimeframeEntries` | `bool` | 1 | 1580 |

### GRP_RISK

| Variable | Type | Downstream refs | Line |
|---|---:|---:|---:|
| `slMode` | `string` | 4 | 1769 |
| `tpMode` | `string` | 6 | 1770 |
| `slAtrMult` | `float` | 4 | 1771 |
| `tp1RInput` | `float` | 1 | 1772 |
| `tp2RInput` | `float` | 1 | 1773 |
| `tp3RInput` | `float` | 1 | 1774 |
| `dynTpMinScale` | `float` | 2 | 1775 |
| `dynTpMaxScale` | `float` | 1 | 1776 |
| `showRiskForOpportunity` | `bool` | 2 | 1777 |

### GRP_ALERT

| Variable | Type | Downstream refs | Line |
|---|---:|---:|---:|
| `enableAlerts` | `bool` | 6 | 2089 |
| `webhookJson` | `bool` | 6 | 2090 |
| `alertSetup` | `bool` | 2 | 2091 |
| `alertSniper` | `bool` | 2 | 2092 |
| `alertOpportunity` | `bool` | 2 | 2093 |
