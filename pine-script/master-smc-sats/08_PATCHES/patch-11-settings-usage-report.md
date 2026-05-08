# Patch 11 — Settings Usage Report

Generated from:
```text
pine-script/master-smc-sats/03_MASTER_CANDIDATES/master-smc-sats-ravi-custom-01-v1.6-theme-engine-candidate.pine
```

Total input variables found: **167**

## Interpretation
- Downstream refs = how many times the input variable appears after its declaration.
- A value of 0 means the setting may be disconnected or only used indirectly. Review manually before deleting.
- This report understands multiline Pine inputs and attempts basic classification.

## Summary
- Inputs requiring manual connectivity review: **0**
- Groups found: **10**

## Inputs by group

### GRP_THEME — 02 Theme Engine
| Variable | Title | Type | Downstream refs | Class | Line |
|---|---|---:|---:|---|---:|
| `themePreset` | Night | `string` | 12 | Theme-only | 74 |
| `themeIntensity` | Standard | `string` | 2 | Theme-only | 97 |
| `themeZoneTransparency` |  | `int` | 4 | Theme-only | 103 |
| `themePanelTransparency` |  | `int` | 2 | Theme-only | 104 |
| `manualBullColor` |  | `color` | 1 | Theme-only | 106 |
| `manualBearColor` |  | `color` | 1 | Theme-only | 107 |
| `manualNeutColor` |  | `color` | 1 | Theme-only | 108 |
| `manualSlColor` |  | `color` | 1 | Theme-only | 109 |
| `manualTpColor` |  | `color` | 1 | Theme-only | 110 |

### GRP_MASTER — 01 Master / Entry Filters
| Variable | Title | Type | Downstream refs | Class | Line |
|---|---|---:|---:|---|---:|
| `masterPreset` | Custom 01 - XAUUSD Sniper Scalping | `string` | 10 | Logic / engine | 263 |
| `manualMinTqi` |  | `float` | 2 | Logic / engine | 278 |
| `manualUltraTqi` |  | `float` | 2 | Logic / engine | 279 |
| `manualMinEr` |  | `float` | 2 | Logic / engine | 280 |
| `manualKillzoneOnly` |  | `bool` | 2 | Logic / engine | 281 |
| `manualSweepReq` |  | `bool` | 1 | Logic / engine | 282 |
| `manualBlockLowVol` |  | `bool` | 1 | Logic / engine | 283 |
| `manualBlockLowAtr` |  | `bool` | 1 | Logic / engine | 284 |
| `manualSatsLookback` |  | `int` | 2 | Logic / engine | 285 |
| `setupSweepLookback` |  | `int` | 2 | Logic / engine | 288 |
| `setupCooldownBars` |  | `int` | 2 | Logic / engine | 289 |
| `showCounterTrendSetups` |  | `bool` | 2 | Logic / engine | 290 |
| `enableOpportunityMode` |  | `bool` | 2 | Logic / engine | 291 |
| `setupRequiresQuality` |  | `bool` | 1 | Logic / engine | 292 |
| `setupMinTqi` |  | `float` | 1 | Logic / engine | 293 |
| `setupMinEr` |  | `float` | 1 | Logic / engine | 294 |
| `opportunityMinTqi` |  | `float` | 1 | Logic / engine | 295 |
| `opportunityMinEr` |  | `float` | 1 | Logic / engine | 296 |
| `opportunityUsesKZ` |  | `bool` | 1 | Logic / engine | 297 |
| `opportunityUsesVolume` |  | `bool` | 1 | Logic / engine | 298 |
| `zoneRequirement` | OB or FVG | `string` | 2 | Logic / engine | 300 |
| `requireHtfPoiContext` |  | `bool` | 2 | Logic / engine | 303 |
| `htfPoiMode` | 15M or 1H | `string` | 2 | Logic / engine | 304 |
| `htfPoiType` | OB or FVG | `string` | 4 | Logic / engine | 305 |
| `htfPoiOverridesBias` |  | `bool` | 2 | Logic / engine | 306 |
| `requireExecutionZone` |  | `bool` | 2 | Logic / engine | 307 |
| `requireLiquidityConfirmation` |  | `bool` | 2 | Logic / engine | 308 |
| `allowLondon` |  | `bool` | 1 | Logic / engine | 923 |
| `allowNyAm` |  | `bool` | 1 | Logic / engine | 924 |
| `allowNyPm` |  | `bool` | 1 | Logic / engine | 925 |
| `allowAsian` |  | `bool` | 1 | Logic / engine | 926 |
| `allowLunch` |  | `bool` | 1 | Logic / engine | 927 |
| `allowNoKz` |  | `bool` | 2 | Logic / engine | 928 |

### GRP_SMC — 05 SMC Engine
| Variable | Title | Type | Downstream refs | Class | Line |
|---|---|---:|---:|---|---:|
| `tf1Enabled` |  | `bool` | 2 | Logic / engine | 377 |
| `tf1` | 1 | `timeframe` | 6 | Logic / engine | 378 |
| `tf1Weight` |  | `int` | 1 | Logic / engine | 379 |
| `tf2Enabled` |  | `bool` | 2 | Logic / engine | 381 |
| `tf2` | 5 | `timeframe` | 6 | Logic / engine | 382 |
| `tf2Weight` |  | `int` | 1 | Logic / engine | 383 |
| `tf3Enabled` |  | `bool` | 2 | Logic / engine | 385 |
| `tf3` | 15 | `timeframe` | 6 | Logic / engine | 386 |
| `tf3Weight` |  | `int` | 1 | Logic / engine | 387 |
| `tf4Enabled` |  | `bool` | 2 | Logic / engine | 389 |
| `tf4` | 60 | `timeframe` | 6 | Logic / engine | 390 |
| `tf4Weight` |  | `int` | 1 | Logic / engine | 391 |
| `tf5Enabled` |  | `bool` | 2 | Logic / engine | 393 |
| `tf5` | 240 | `timeframe` | 6 | Logic / engine | 394 |
| `tf5Weight` |  | `int` | 1 | Logic / engine | 395 |
| `emaLength` |  | `int` | 1 | Logic / engine | 397 |
| `swingLength` |  | `int` | 10 | Logic / engine | 398 |
| `obLookback` |  | `int` | 4 | Logic / engine | 399 |
| `fvgLookback` |  | `int` | 3 | Logic / engine | 400 |
| `atrAvgLength` |  | `int` | 1 | Logic / engine | 401 |
| `biasUseStruct` |  | `bool` | 2 | Logic / engine | 403 |
| `biasUseOB` |  | `bool` | 2 | Logic / engine | 404 |
| `biasUseFVG` |  | `bool` | 2 | Logic / engine | 405 |
| `biasUseEMA` |  | `bool` | 2 | Logic / engine | 406 |
| `biasUseSwing` |  | `bool` | 2 | Logic / engine | 407 |

### GRP_VIS — 08 Visual Display
| Variable | Title | Type | Downstream refs | Class | Line |
|---|---|---:|---:|---|---:|
| `showOB` |  | `bool` | 1 | Visual-only | 412 |
| `showFVG` |  | `bool` | 1 | Visual-only | 413 |
| `showSwingLabels` |  | `bool` | 1 | Visual-only | 414 |
| `showSwingLines` |  | `bool` | 1 | Visual-only | 415 |
| `plotPDHL` |  | `bool` | 1 | Visual-only | 416 |
| `plotPWHL` |  | `bool` | 1 | Visual-only | 417 |
| `plotPMHL` |  | `bool` | 1 | Visual-only | 418 |
| `showEMA` |  | `bool` | 1 | Visual-only | 419 |
| `showSatsLine` |  | `bool` | 1 | Visual-only | 420 |
| `visualMode` | Clean | `string` | 3 | Visual-only | 421 |
| `showSetupWarnings` |  | `bool` | 2 | Visual-only | 422 |
| `showSniperEntries` |  | `bool` | 4 | Visual-only | 423 |
| `showUltraEntries` |  | `bool` | 2 | Visual-only | 424 |
| `showRiskLines` |  | `bool` | 2 | Visual-only | 425 |
| `showMiniStatus` |  | `bool` | 1 | Visual-only | 426 |
| `miniStatusPosition` | Right of Price | `string` | 4 | Visual-only | 427 |
| `obExtend` |  | `int` | 1 | Visual-only | 429 |
| `fvgExtend` |  | `int` | 1 | Visual-only | 430 |
| `levelExtend` |  | `int` | 10 | Visual-only | 431 |
| `labelOffset` |  | `int` | 4 | Visual-only | 432 |

### GRP_HTFLVL — 07 HTF Key Levels
| Variable | Title | Type | Downstream refs | Class | Line |
|---|---|---:|---:|---|---:|
| `showHtfKeyLevels` |  | `bool` | 2 | Logic / engine | 437 |
| `htfKeyTf1` | 15 | `timeframe` | 1 | Logic / engine | 438 |
| `htfKeyTf2` | 60 | `timeframe` | 1 | Logic / engine | 439 |
| `htfKeyColor1` |  | `color` | 8 | Logic / engine | 440 |
| `htfKeyColor2` |  | `color` | 8 | Logic / engine | 441 |
| `showHtfSwingHL` |  | `bool` | 1 | Logic / engine | 442 |
| `showHtfPoiLevels` |  | `bool` | 1 | Logic / engine | 443 |
| `showHtfKeyLabels` |  | `bool` | 1 | Logic / engine | 444 |
| `requireKeyLevelTouch` |  | `bool` | 1 | Logic / engine | 445 |
| `keyLevelTouchAtrBuffer` |  | `float` | 1 | Logic / engine | 446 |

### GRP_SATS — 06 SATS Engine
| Variable | Title | Type | Downstream refs | Class | Line |
|---|---|---:|---:|---|---:|
| `satsPreset` | Auto | `string` | 2 | Logic / engine | 993 |
| `atrLenInput` |  | `int` | 2 | Logic / engine | 994 |
| `baseMultInput` |  | `float` | 2 | Logic / engine | 995 |
| `sourceInput` |  | `source` | 4 | Logic / engine | 996 |
| `useAdaptiveInput` |  | `bool` | 1 | Logic / engine | 997 |
| `erLengthInput` |  | `int` | 2 | Logic / engine | 998 |
| `adaptStrengthInput` |  | `float` | 1 | Logic / engine | 999 |
| `atrBaselineLenInput` |  | `int` | 1 | Logic / engine | 1000 |
| `useTqiInput` |  | `bool` | 4 | Logic / engine | 1001 |
| `qualityStrengthInput` |  | `float` | 2 | Logic / engine | 1002 |
| `qualityCurveInput` |  | `float` | 1 | Logic / engine | 1003 |
| `multSmoothInput` |  | `bool` | 2 | Logic / engine | 1004 |
| `useAsymBandsInput` |  | `bool` | 1 | Logic / engine | 1005 |
| `asymStrengthInput` |  | `float` | 2 | Logic / engine | 1006 |
| `useEffAtrInput` |  | `bool` | 1 | Logic / engine | 1007 |
| `useCharFlipInput` |  | `bool` | 1 | Logic / engine | 1008 |
| `charFlipMinAgeInput` |  | `int` | 1 | Logic / engine | 1009 |
| `charFlipHighInput` |  | `float` | 1 | Logic / engine | 1010 |
| `charFlipLowInput` |  | `float` | 1 | Logic / engine | 1011 |
| `tqiWeightErInput` |  | `float` | 2 | Logic / engine | 1013 |
| `tqiWeightVolInput` |  | `float` | 2 | Logic / engine | 1014 |
| `tqiWeightStructInput` |  | `float` | 2 | Logic / engine | 1015 |
| `tqiWeightMomInput` |  | `float` | 2 | Logic / engine | 1016 |
| `tqiStructLenInput` |  | `int` | 2 | Logic / engine | 1017 |
| `tqiMomLenInput` |  | `int` | 3 | Logic / engine | 1018 |

### GRP_SK — 07 Smart Key Levels
| Variable | Title | Type | Downstream refs | Class | Line |
|---|---|---:|---:|---|---:|
| `showSmartKeyLevels` |  | `bool` | 2 | Logic / engine | 1168 |
| `enableSmartKeyFallback` |  | `bool` | 4 | Logic / engine | 1169 |
| `smartKeySourceMode` | Current + HTF1 + HTF2 | `string` | 12 | Logic / engine | 1170 |
| `smartKeySelectionMode` | Nearest | `string` | 2 | Logic / engine | 1171 |
| `smartKeyPivotLen` |  | `int` | 6 | Logic / engine | 1172 |
| `smartKeyMaxStored` |  | `int` | 2 | Logic / engine | 1173 |
| `smartKeyMinTouches` |  | `int` | 10 | Logic / engine | 1174 |
| `smartKeyAtrLen` |  | `int` | 1 | Logic / engine | 1175 |
| `smartKeyAtrTolerance` |  | `float` | 1 | Logic / engine | 1176 |
| `smartKeyTouchBuffer` |  | `float` | 1 | Logic / engine | 1177 |
| `smartKeyExtendBars` |  | `int` | 4 | Logic / engine | 1178 |
| `showSmartLabels` |  | `bool` | 2 | Logic / engine | 1179 |
| `useSmartKeyForEntries` |  | `bool` | 3 | Logic / engine | 1181 |
| `useSmartKeyForTP` |  | `bool` | 2 | Logic / engine | 1182 |
| `smartSupportColor` |  | `color` | 1 | Logic / engine | 1184 |
| `smartResistanceColor` |  | `color` | 1 | Logic / engine | 1185 |
| `smartLiquidityColor` |  | `color` | 4 | Logic / engine | 1186 |

### GRP_ENTRY — 04 Entry Workflow
| Variable | Title | Type | Downstream refs | Class | Line |
|---|---|---:|---:|---|---:|
| `entryWorkflowMode` | Market Structure Only | `string` | 7 | Logic / engine | 1552 |
| `manualEnableSetupWarnings` |  | `bool` | 1 | Logic / engine | 1566 |
| `manualEnableOpportunityEntries` |  | `bool` | 1 | Logic / engine | 1567 |
| `manualEnableNormalEntries` |  | `bool` | 1 | Logic / engine | 1568 |
| `manualEnableSniperEntries` |  | `bool` | 1 | Logic / engine | 1569 |
| `manualEnableUltraEntries` |  | `bool` | 1 | Logic / engine | 1570 |
| `manualEnableKeyLevelEntries` |  | `bool` | 1 | Logic / engine | 1571 |
| `showEntryLabelsFinalInput` |  | `bool` | 1 | Logic / engine | 1573 |
| `showHistoricalEntries` |  | `bool` | 1 | Logic / engine | 1574 |
| `entryHistoryBars` |  | `int` | 1 | Logic / engine | 1575 |
| `showTpSlForEntriesFinal` |  | `bool` | 2 | Logic / engine | 1576 |
| `restrictConfirmedEntriesToExecutionTf` |  | `bool` | 1 | Logic / engine | 1578 |
| `maxConfirmedEntryTfMinutes` |  | `int` | 2 | Logic / engine | 1579 |
| `allowHigherTimeframeEntries` |  | `bool` | 1 | Logic / engine | 1580 |

### GRP_RISK — 09 Risk / TP / SL
| Variable | Title | Type | Downstream refs | Class | Line |
|---|---|---:|---:|---|---:|
| `slMode` | Hybrid | `string` | 4 | Risk-only | 1769 |
| `tpMode` | Hybrid R + Liquidity | `string` | 6 | Risk-only | 1770 |
| `slAtrMult` |  | `float` | 4 | Risk-only | 1771 |
| `tp1RInput` |  | `float` | 1 | Risk-only | 1772 |
| `tp2RInput` |  | `float` | 1 | Risk-only | 1773 |
| `tp3RInput` |  | `float` | 1 | Risk-only | 1774 |
| `dynTpMinScale` |  | `float` | 2 | Risk-only | 1775 |
| `dynTpMaxScale` |  | `float` | 1 | Risk-only | 1776 |
| `showRiskForOpportunity` |  | `bool` | 2 | Risk-only | 1777 |

### GRP_ALERT — 10 Alerts
| Variable | Title | Type | Downstream refs | Class | Line |
|---|---|---:|---:|---|---:|
| `enableAlerts` |  | `bool` | 6 | Alert-only | 2089 |
| `webhookJson` |  | `bool` | 6 | Alert-only | 2090 |
| `alertSetup` |  | `bool` | 2 | Alert-only | 2091 |
| `alertSniper` |  | `bool` | 2 | Alert-only | 2092 |
| `alertOpportunity` |  | `bool` | 2 | Alert-only | 2093 |
