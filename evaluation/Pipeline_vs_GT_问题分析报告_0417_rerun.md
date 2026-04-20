# Pipeline vs GT 问题分析报告（0417）

> 评测对象：`data/processed/` 最新推理结果 vs `415反馈/人工修正/` GT 标注
> 生成方式：基于论文标题配对 + 样品级 greedy 匹配 + 字段归一化后的启发式对比

## 1. 总体结论

| 指标 | 数值 |
| --- | --- |
| 对比论文数 | 20 |
| GT 条目总数 | 93 |
| Pipeline 条目总数 | 55 |
| 成功匹配条目 | 45 |
| GT 漏配条目 | 48 |
| Pipeline 多出条目 | 10 |
| 缺失 extraction 输出论文数 | 3 |
| 标题配对最低相似度 | 0.529 |
| 标题配对平均相似度 | 0.964 |

### 结论摘要

- 这批数据 **没有再出现上一版那种整篇论文错配源文档的 P0 问题**。20 篇论文标题配对平均相似度为 `0.964`，最低为 `0.529`，说明 `data/processed` 与 GT 基本是一一对应的。
- 当前主要瓶颈已经从“读错论文”转为“**同一论文内样品拆分与字段标准化不稳定**”。最突出的是 `Sample_ID`、`Key_Params`、`Advanced_Quantitative_Features`、`Main_Phase` 和 `Process_Category`。
- 条目数层面 Pipeline 与 GT 相差 `-38` 条（`55` vs `93`），但这不代表召回更好。偏差里的相当一部分来自 **过拆样品**、**漏掉 reference**，以及部分论文根本没有成功产出 extraction 文件。
- `Reference` 仍然是系统性短板：启发式匹配下统计到 `17` 个 GT reference 条目缺失，集中出现在 `文献(3)`、Paper 1、Paper 4 等论文。
- 本轮还有 `3` 篇论文目录存在但没有生成 extraction 文件，这类样本需要单独看 pipeline 执行链路，不能误判为纯 prompt/schema 问题。

## 2. 高频问题分布

| 问题类型 | 次数 |
| --- | --- |
| sample_id_mismatch | 43 |
| key_params_key_mismatch | 43 |
| aqf_key_mismatch | 39 |
| main_phase_mismatch | 33 |
| composition_element_set_mismatch | 28 |
| property_over_extraction | 26 |
| property_under_extraction | 22 |
| composition_basis_mismatch | 20 |
| key_params_value_mismatch | 19 |
| missing_reference_item | 17 |
| process_category_substantive_mismatch | 14 |
| composition_type_mismatch | 10 |

### 如何解读这些高频问题

- `sample_id_mismatch` 最高，并不全是严重错误；其中一部分只是命名风格不同，但它会显著放大后续匹配难度，也会掩盖真正的字段差异。
- `missing_output_file` 代表目录存在但没有成功产出 extraction JSON，这说明除了抽取质量，当前还存在运行链路/落盘稳定性问题。
- `key_params_key_mismatch` 和 `aqf_key_mismatch` 说明当前 schema 语义还没有完全收敛。很多是“同义不同名”，也有一部分是 Pipeline 过度展开了文中参数或高级表征特征。
- `process_category_substantive_mismatch` 依旧偏高，说明除了词表问题外，还存在真实工艺路线判断错误，尤其在粉末回收、激光熔覆/激光表面处理、混合制造这几类论文里更明显。
- `composition_basis_mismatch` 和 `composition_type_mismatch` 仍在出现，说明 `Nominal`/`Measured` 与 `wt%`/`at%` 的判定规则还不够稳。

## 3. 最值得优先看的论文

| 论文 | GT | Pred | 漏配 | 多出 | 主要问题 |
| --- | --- | --- | --- | --- | --- |
| Powder recycling for electron beam powder bed_fixed | 15 | 0 | 15 | 0 | missing_output |
| Additive manufacturing Ti-22Al-25 Nb alloy wit | 9 | 0 | 9 | 0 | missing_output |
| 文献 (3)人工修正结果 | 8 | 1 | 7 | 0 | missing_reference_item:5 / missing_target_item:2 / sample_id_mismatch:1 / process_category_vocab_mismatch:1 |
| 文献2-人工修正结果 | 5 | 6 | 2 | 3 | sample_id_mismatch:3 / composition_value_mismatch:3 / key_params_key_mismatch:3 / aqf_key_mismatch:3 |
| 文献 (2)人工修正结果_fixed | 1 | 5 | 0 | 4 | extra_reference_item:3 / sample_id_mismatch:1 / process_category_vocab_mismatch:1 / composition_basis_mismatch:1 |
| 文献 (1)人工修正结果 | 4 | 5 | 1 | 2 | sample_id_mismatch:3 / composition_basis_mismatch:3 / key_params_key_mismatch:3 / main_phase_mismatch:3 |
| Peculiar microstructural evolution and tensile | 6 | 3 | 3 | 0 | composition_element_set_mismatch:3 / key_params_key_mismatch:3 / aqf_key_mismatch:3 / main_phase_mismatch:2 |
| 1-Additively manufactured heterogeneous precipitation-strengthened high-entropy alloys with high strength and ductility | 4 | 2 | 2 | 0 | sample_id_mismatch:2 / key_params_key_mismatch:2 / key_params_value_mismatch:2 / aqf_key_mismatch:2 |
| 3-Nanotwinned precipitates induced ultra-strong AlCoCrFeNi2.1 eutectic high-entropy alloy through additive manufacturing_fixed | 3 | 3 | 1 | 1 | sample_id_mismatch:2 / process_category_substantive_mismatch:2 / composition_element_set_mismatch:2 / key_params_key_mismatch:2 |
| 4-Highly printable, strong, and ductile ordered intermetallic alloy_1 | 4 | 2 | 2 | 0 | sample_id_mismatch:2 / key_params_key_mismatch:2 / key_params_value_mismatch:2 / main_phase_mismatch:2 |

### 重点观察

- 凡是 `missing_output` 的论文，应优先检查 extraction 节点是否中断、写文件路径是否异常、或后处理是否提前失败；这类问题不应该继续用 prompt 调参去掩盖。
- `文献3-人工修正结果`：Pipeline 输出 `10` 条，GT 只有 `2` 条，且多出的 `8` 条几乎都是 reference/中间态被独立拆出，属于明显过拆。
- `文献2-人工修正结果`：同时存在额外 target、样品错配、参数键不统一和 AQF 过度展开，说明 prompt 对“哪些状态该独立成条目”仍缺硬约束。
- `Powder recycling for electron beam powder bed_fixed`：条目数接近，但字段差异非常密集，说明这篇主要不是漏提，而是 **标准化失败**。
- `4-Highly printable...`：少了两个 GT reference，又出现参数值和主相不一致，是“reference 召回不足 + 样品匹配偏移”的典型例子。

## 4. 分层问题分析

### 4.1 样品层：拆分与命名还不稳定

- 典型表现：`sample_id_mismatch = 43`，`extra_target_item = 6`，`extra_reference_item = 4`，`missing_reference_item = 17`。
- 这说明当前 prompt 已能识别更多状态，但还没有稳定学会“何时必须拆、何时不能拆、拆完后该如何命名”。
- 中文论文里尤其明显，常见模式是把对照铸态、粉末态、文献 benchmark、热处理中间态都拆成新的 target。

代表样例：
- `paper`=1-Additively manufactured heterogeneous precipitation-strengthened high-entropy alloys with high strength and ductility, `gt_id`=Ref18_Fe28Co29.5Ni27.5Al8.5Ti6.5, `role`=reference, `proc`=Laser Powder Bed Fusion (L-PBF)
- `paper`=1-Additively manufactured heterogeneous precipitation-strengthened high-entropy alloys with high strength and ductility, `gt_id`=Ref36_CoCrNi94Al3Ti3, `role`=reference, `proc`=Laser Powder Bed Fusion (L-PBF)
- `paper`=4-Highly printable, strong, and ductile ordered intermetallic alloy_1, `gt_id`=Ref_Ni3Al_LPBF, `role`=reference, `proc`=Laser Powder Bed Fusion (LPBF)
- `paper`=4-Highly printable, strong, and ductile ordered intermetallic alloy_1, `gt_id`=Ref_TiAl_AM, `role`=reference, `proc`=Additive Manufacturing
- `paper`=Effect of building direction on the microstructure_fixed, `gt_id`=Cast_Reference, `role`=reference, `proc`=Casting
- `paper`=Peculiar microstructural evolution and tensile, `gt_id`=Cast_48-2-2_RT_ref, `role`=reference, `proc`=Casting
- `paper`=文献 (1)人工修正结果, `pred_id`=ML-Optimized_LPBF, `role`=target, `proc`=Laser Powder Bed Fusion (LPBF) + Heat Treatment
- `paper`=文献 (1)人工修正结果, `pred_id`=Control_NoNi_LaserScanned, `role`=target, `proc`=Laser Powder Bed Fusion (LPBF)
- `paper`=文献 (2)人工修正结果_fixed, `pred_id`=FVS0812_TiB2_LPBF_ThermalExposed, `role`=target, `proc`=Laser Powder Bed Fusion (LPBF) + Post-Processing
- `paper`=文献2-人工修正结果, `pred_id`=Ingot_#1_LaserGlazing, `role`=target, `proc`=Laser Glazing
- `paper`=文献2-人工修正结果, `pred_id`=Ingot_#2_LaserGlazing, `role`=target, `proc`=Laser Glazing
- `paper`=文献2-人工修正结果, `pred_id`=Ingot_#3_LaserGlazing, `role`=target, `proc`=Laser Glazing

### 4.2 工艺层：词表问题和真实误判并存

- `process_category_vocab_mismatch = 10` 说明一部分只是 GT 与 Pipeline 表达方式不同，例如 `Laser Powder Bed Fusion` vs `Laser Powder Bed Fusion (LPBF)`。
- 更关键的是 `process_category_substantive_mismatch = 14`，这部分是真错，不是格式差异。
- 误判高发场景：
- 把 `Laser Glazing` 样品和 `LPBF + T6` 样品混到一起。
- 把 `Casting` 或 `Wrought` 的参考样品误当成 AM 基准样品。
- 在 hybrid / UAM / 后处理论文中，只抓住了 `LPBF`，没守住更完整的路线标签。

代表样例：
- `paper`=3-Nanotwinned precipitates induced ultra-strong AlCoCrFeNi2.1 eutectic high-entropy alloy through additive manufacturing_fixed, `gt_id`=EHEA_PBF-LB_AsBuilt, `pred_id`=AlCoCrFeNi2.1_PBF-LB_AB, `pred_proc`=Laser Powder Bed Fusion (LPBF)
- `paper`=3-Nanotwinned precipitates induced ultra-strong AlCoCrFeNi2.1 eutectic high-entropy alloy through additive manufacturing_fixed, `gt_id`=EHEA_PBF-LB_Annealed, `pred_id`=AlCoCrFeNi2.1_PBF-LB_AA600C_8h, `gt_proc`=Laser Powder Bed Fusion (PBF-LB) + Annealing, `pred_proc`=Laser Powder Bed Fusion (LPBF) + Heat Treatment
- `paper`=Peculiar microstructural evolution and tensile, `gt_id`=Cast_48-2-2_RT_ref, `pred_id`=Ti-44Al-4Cr_raw_powder, `gt_proc`=Casting, `pred_proc`=Powder Metallurgy
- `paper`=文献 (1)人工修正结果, `gt_id`=AM_Al-Er-Zr-Ni_As-built, `pred_id`=ML-Optimized_Cast, `gt_proc`=Laser Powder Bed Fusion, `pred_proc`=Casting + Heat Treatment
- `paper`=文献 (1)人工修正结果, `gt_id`=Reference_Alloy_1, `pred_id`=Benchmark_PrintableAl, `gt_proc`=Laser Scanning, `pred_proc`=Laser Powder Bed Fusion (LPBF) + Heat Treatment
- `paper`=文献 (4)人工修正结果, `gt_id`=LPBF_UAM_As_built, `pred_id`=LPBF, `gt_proc`=Hybrid Additive Manufacturing (LPBF + UAM), `pred_proc`=Laser Powder Bed Fusion (LPBF)
- `paper`=Effect of building direction on the microstructure_fixed, `gt_id`=EBM_θ0, `pred_id`=Ti48Al2Cr2Nb_θ0, `gt_proc`=Additive Manufacturing - Electron Beam Melting, `pred_proc`=Electron beam melting (EBM)
- `paper`=Effect of building direction on the microstructure_fixed, `gt_id`=EBM_θ45, `pred_id`=Ti48Al2Cr2Nb_θ45, `gt_proc`=Additive Manufacturing - Electron Beam Melting, `pred_proc`=Electron beam melting (EBM)
- `paper`=Effect of building direction on the microstructure_fixed, `gt_id`=EBM_θ90, `pred_id`=Ti48Al2Cr2Nb_θ90, `gt_proc`=Additive Manufacturing - Electron Beam Melting, `pred_proc`=Electron beam melting (EBM)
- `paper`=文献 (2)人工修正结果_fixed, `gt_id`=FVS0812_TiB2_As-printed, `pred_id`=FVS0812_TiB2_LPBF_AsPrinted, `gt_proc`=Laser Powder Bed Fusion, `pred_proc`=Laser Powder Bed Fusion (LPBF)

### 4.3 成分层：来源、单位制、余量填充仍有残留错误

- `composition_basis_mismatch = 20`：说明模型仍会把 GT 的 measured 结果回落成 nominal，或者在 GT 未单列成分时主动补 nominal。
- `composition_type_mismatch = 10`：最典型的是 LAAM 论文里 GT 用 `at%`，Pipeline 输出成 `wt%`。
- `composition_value_mismatch = 5`：不仅是数值抽错，也包括 `Bal.` 元素回填不正确带来的主元素偏大问题。

代表样例：
- `paper`=1-Additively manufactured heterogeneous precipitation-strengthened high-entropy alloys with high strength and ductility, `gt_id`=Co47Ni28Cr16Fe3Al3Ti3_HT800C4h, `pred_id`=CoNiCrFeAlTi_DED_HT_STEP_12, `gt_basis`=nominal, `pred_basis`=measured
- `paper`=5-In situ tuning of FCC–BCC dual phase and mechanical properties in multi-principal element alloys via laser-aided additive manufacturing_fixed, `gt_id`=CoCrNi_Al0.6TiFe_0.1_LAAM, `pred_id`=CoCrNi(Al0.6TiFe)0.1, `pred_basis`=nominal
- `paper`=5-In situ tuning of FCC–BCC dual phase and mechanical properties in multi-principal element alloys via laser-aided additive manufacturing_fixed, `gt_id`=CoCrNi_Al0.6TiFe_0.2_LAAM, `pred_id`=CoCrNi(Al0.6TiFe)0.2, `pred_basis`=nominal
- `paper`=5-In situ tuning of FCC–BCC dual phase and mechanical properties in multi-principal element alloys via laser-aided additive manufacturing_fixed, `gt_id`=CoCrNi_Al0.6TiFe_0.3_LAAM, `pred_id`=CoCrNi(Al0.6TiFe)0.3, `pred_basis`=nominal
- `paper`=5-In situ tuning of FCC–BCC dual phase and mechanical properties in multi-principal element alloys via laser-aided additive manufacturing_fixed, `gt_id`=CoCrNi_Al0.6TiFe_0.4_LAAM, `pred_id`=CoCrNi(Al0.6TiFe)0.4, `pred_basis`=nominal
- `paper`=1-Additively manufactured heterogeneous precipitation-strengthened high-entropy alloys with high strength and ductility, `gt_id`=Co47Ni28Cr16Fe3Al3Ti3_HT800C4h, `pred_id`=CoNiCrFeAlTi_DED_HT_STEP_12, `key`=Al, `gt`=3.0, `pred`=6.1
- `paper`=5-In situ tuning of FCC–BCC dual phase and mechanical properties in multi-principal element alloys via laser-aided additive manufacturing_fixed, `gt_id`=CoCrNi_LAAM, `pred_id`=CoCrNi, `key`=Cr, `gt`=33.33, `pred`=30.14
- `paper`=文献2-人工修正结果, `gt_id`=Ingot_4_Laser_Glazed, `pred_id`=Ingot_#4_LaserGlazing, `key`=Sc, `gt`=0.2, `pred`=0.8
- `paper`=文献2-人工修正结果, `gt_id`=LPBF_As_Fabricated, `pred_id`=Al-Cu-Li-Sc-Zr_LPBF_AsFabricated, `key`=Sc, `gt`=0.19, `pred`=0.97
- `paper`=文献2-人工修正结果, `gt_id`=LPBF_T6, `pred_id`=Ingot_#5_LaserGlazing, `key`=Li, `gt`=1.12, `pred`=1.25

### 4.4 参数层：schema 漂移比纯漏提更严重

- `key_params_key_mismatch = 43`，高于 `key_params_value_mismatch = 19`，说明参数层第一优先级不是继续“多抽点参数”，而是先把常见键名收敛。
- Pred-only 高频键包括 `protective_atmosphere`、`layer_thickness_um`、`oxygen_content_ppm`、`acceleration_voltage_kv`，说明 Pipeline 会主动展开很多过程细节。
- GT-only 高频键包括 `powder_bed_preheating_temperature_k`、`spot_size_um`、`aging_temperature_k`、`aging_time_h`，说明后处理参数和少数关键工艺参数仍会漏掉或被换名。

| 键名趋势 | 次数 |
| --- | --- |
| Pred-only `protective_atmosphere` | 16 |
| Pred-only `volumetric_energy_density_j_mm3` | 15 |
| Pred-only `build_plate_temperature_k` | 13 |
| Pred-only `oxygen_content_ppm` | 11 |
| Pred-only `hatch_spacing_um` | 10 |
| Pred-only `laser_power_w` | 7 |
| Pred-only `layer_thickness_um` | 7 |
| Pred-only `scanning_speed_mm_s` | 7 |
| GT-only `spot_size_um` | 7 |
| GT-only `aging_temperature_k` | 3 |
| GT-only `aging_time_h` | 3 |
| GT-only `building_angle_deg` | 3 |
| GT-only `powder_bed_preheating_temperature_k` | 3 |
| GT-only `cooling_medium` | 3 |
| GT-only `cuboid_dimensions_mm` | 2 |
| GT-only `laser_head_increment_mm` | 2 |

代表样例：
- `paper`=1-Additively manufactured heterogeneous precipitation-strengthened high-entropy alloys with high strength and ductility, `gt_id`=Co47Ni28Cr16Fe3Al3Ti3_AP, `pred_id`=CoNiCrFeAlTi_DED_AP, `gt_only`=['cuboid_dimensions_mm', 'laser_head_increment_mm', 'laser_spot_diameter_mm', 'powder_drying_temperature_k', 'powder_drying_time_h', 'powder_feeding_rate_g_min'], `pred_only`=['build_plate_temperature_k', 'powder_feed_rate_g_min', 'spot_diameter_mm']
- `paper`=1-Additively manufactured heterogeneous precipitation-strengthened high-entropy alloys with high strength and ductility, `gt_id`=Co47Ni28Cr16Fe3Al3Ti3_HT800C4h, `pred_id`=CoNiCrFeAlTi_DED_HT_STEP_12, `gt_only`=['aging_temperature_k', 'aging_time_h', 'cuboid_dimensions_mm', 'laser_head_increment_mm', 'laser_spot_diameter_mm', 'powder_drying_temperature_k'], `pred_only`=['build_plate_temperature_k', 'powder_feed_rate_g_min', 'solution_temperature_k', 'solution_time_h', 'spot_diameter_mm']
- `paper`=3-Nanotwinned precipitates induced ultra-strong AlCoCrFeNi2.1 eutectic high-entropy alloy through additive manufacturing_fixed, `gt_id`=EHEA_PBF-LB_AsBuilt, `pred_id`=AlCoCrFeNi2.1_PBF-LB_AB, `pred_only`=['beam_spot_size_um', 'build_plate_temperature_k', 'hatch_spacing_um', 'laser_power_w', 'layer_thickness_um', 'oxygen_content_ppm']
- `paper`=3-Nanotwinned precipitates induced ultra-strong AlCoCrFeNi2.1 eutectic high-entropy alloy through additive manufacturing_fixed, `gt_id`=EHEA_PBF-LB_Annealed, `pred_id`=AlCoCrFeNi2.1_PBF-LB_AA600C_8h, `pred_only`=['build_plate_temperature_k', 'hatch_spacing_um', 'laser_power_w', 'layer_thickness_um', 'oxygen_content_ppm', 'protective_atmosphere']
- `paper`=4-Highly printable, strong, and ductile ordered intermetallic alloy_1, `gt_id`=CCIMA_LPBF_AsPrinted, `pred_id`=CCIMA_as-printed, `gt_only`=['spot_size_um'], `pred_only`=['oxygen_content_ppm']
- `paper`=4-Highly printable, strong, and ductile ordered intermetallic alloy_1, `gt_id`=CCIMA_LPBF_ThermalStabilized, `pred_id`=CCIMA_thermal-stabilized, `gt_only`=['solution_temperature_k', 'solution_time_h'], `pred_only`=['build_plate_temperature_k', 'hatch_spacing_um', 'laser_power_w', 'layer_thickness_um', 'oxygen_content_ppm', 'protective_atmosphere']
- `paper`=1-Additively manufactured heterogeneous precipitation-strengthened high-entropy alloys with high strength and ductility, `gt_id`=Co47Ni28Cr16Fe3Al3Ti3_AP, `pred_id`=CoNiCrFeAlTi_DED_AP, `key`=protective_atmosphere, `gt`=Argon gas, `pred`=Argon
- `paper`=1-Additively manufactured heterogeneous precipitation-strengthened high-entropy alloys with high strength and ductility, `gt_id`=Co47Ni28Cr16Fe3Al3Ti3_HT800C4h, `pred_id`=CoNiCrFeAlTi_DED_HT_STEP_12, `key`=protective_atmosphere, `gt`=Argon gas, `pred`=Argon
- `paper`=3-Nanotwinned precipitates induced ultra-strong AlCoCrFeNi2.1 eutectic high-entropy alloy through additive manufacturing_fixed, `gt_id`=EHEA_PBF-LB_Annealed, `pred_id`=AlCoCrFeNi2.1_PBF-LB_AA600C_8h, `key`=cooling_medium, `gt`=Water quenching, `pred`=Water quench
- `paper`=4-Highly printable, strong, and ductile ordered intermetallic alloy_1, `gt_id`=CCIMA_LPBF_AsPrinted, `pred_id`=CCIMA_as-printed, `key`=protective_atmosphere, `gt`=Ar (<400 ppm O2), `pred`=Argon
- `paper`=4-Highly printable, strong, and ductile ordered intermetallic alloy_1, `gt_id`=CCIMA_LPBF_ThermalStabilized, `pred_id`=CCIMA_thermal-stabilized, `key`=cooling_medium, `gt`=Air cooling, `pred`=Air

### 4.5 微观组织层：AQF 和 Main_Phase 仍然容易过度解释

- `aqf_key_mismatch = 39` 与 `main_phase_mismatch = 33` 说明当前 prompt 倾向于把论文里的组织解释写得更“丰富”，但未必符合 GT 的收敛粒度。
- AQF 里 Pred-only 最高的是 `Dislocation_Density_m2`、`Lattice_Parameter_nm`、`Fresh_Powder_Percent`、`Yield_Strength_Increase_MPa`，体现出 Pipeline 在做“语义合理扩展”。
- GT-only 最高的是更具体的分相/分区域字段，如 `Dislocation_Density_Deformed_m2`、`FCC_Lattice_Parameter_nm`、`Lamellar_Spacing_nm`。这说明现在的问题不是完全不会提，而是 **抽象层级不一致**。

| AQF 趋势 | 次数 |
| --- | --- |
| Pred-only `Dislocation_Density_m2` | 7 |
| Pred-only `Lattice_Parameter_nm` | 6 |
| Pred-only `Dislocation_Strengthening_Contribution_MPa` | 5 |
| Pred-only `CG_avg_um` | 4 |
| Pred-only `FEG_avg_um` | 4 |
| Pred-only `FEG_fraction_pct` | 4 |
| GT-only `Dislocation_Density_Deformed_m2` | 6 |
| GT-only `FCC_Lattice_Parameter_nm` | 6 |
| GT-only `Alpha2_lamella_thickness_nm` | 3 |
| GT-only `Duplex_region_grain_size_um` | 3 |
| GT-only `Gamma_band_grain_size_um` | 3 |
| GT-only `Gamma_lamella_thickness_nm` | 3 |

代表样例：
- `paper`=1-Additively manufactured heterogeneous precipitation-strengthened high-entropy alloys with high strength and ductility, `gt_id`=Co47Ni28Cr16Fe3Al3Ti3_AP, `pred_id`=CoNiCrFeAlTi_DED_AP, `gt_only`=['Cell_Size_avg_um'], `pred_only`=['Cellular_Structure_Diameter_avg_um', 'Grain_Size_StdDev_um']
- `paper`=1-Additively manufactured heterogeneous precipitation-strengthened high-entropy alloys with high strength and ductility, `gt_id`=Co47Ni28Cr16Fe3Al3Ti3_HT800C4h, `pred_id`=CoNiCrFeAlTi_DED_HT_STEP_12, `gt_only`=['Cell_Size_avg_um', 'Interior_Volume_Fraction_pct', 'Wall_Volume_Fraction_pct'], `pred_only`=['APB_Energy_mJ_m2', 'Cellular_Structure_Diameter_avg_um', 'Grain_Size_StdDev_um', 'Interior_Volume_Fraction', 'L12_Solvus_Temperature_Interior_C', 'L12_Solvus_Temperature_Wall_C']
- `paper`=3-Nanotwinned precipitates induced ultra-strong AlCoCrFeNi2.1 eutectic high-entropy alloy through additive manufacturing_fixed, `gt_id`=EHEA_PBF-LB_AsBuilt, `pred_id`=AlCoCrFeNi2.1_PBF-LB_AB, `pred_only`=['B2_cell_diameter_nm', 'B2_nanolayer_thickness_nm', 'B2_phase_fraction_pct', 'FCC_nanolayer_thickness_nm', 'FCC_phase_fraction_pct', 'cellular_FCC_nanolayer_thickness_nm']
- `paper`=3-Nanotwinned precipitates induced ultra-strong AlCoCrFeNi2.1 eutectic high-entropy alloy through additive manufacturing_fixed, `gt_id`=EHEA_PBF-LB_Annealed, `pred_id`=AlCoCrFeNi2.1_PBF-LB_AA600C_8h, `gt_only`=['Cellular_B2_Cell_Size_nm', 'Lamellar_B2_Thickness_nm', 'Lamellar_FCC_Thickness_nm', 'NT_FCC_Precipitate_Fraction_pct', 'NT_FCC_Precipitate_Twin_Thickness_avg_nm', 'Needle_Precipitate_Diameter_nm'], `pred_only`=['B2_nanolayer_thickness_AA_nm', 'FCC_nanolayer_thickness_AA_nm', 'Orowan_strengthening_increment_MPa', 'cellular_B2_diameter_AA_nm', 'cellular_colony_precipitate_volume_pct', 'interprecipitate_spacing_B2_nm']
- `paper`=4-Highly printable, strong, and ductile ordered intermetallic alloy_1, `gt_id`=CCIMA_LPBF_ThermalStabilized, `pred_id`=CCIMA_thermal-stabilized, `gt_only`=['APB_Energy_111_mJ_m2', 'C44_Elastic_Constant_GPa', 'Dislocation_Density_35pct_Strain_m2', 'Dislocation_Density_5pct_Strain_m2', 'SISF_Energy_111_mJ_m2'], `pred_only`=['Dislocation_Density_35pct_strain_m2', 'Dislocation_Density_5pct_strain_m2', 'Max_Work_Hardening_Exponent', 'Max_Work_Hardening_Rate_GPa', 'Texture_Index']
- `paper`=5-In situ tuning of FCC–BCC dual phase and mechanical properties in multi-principal element alloys via laser-aided additive manufacturing_fixed, `gt_id`=CoCrNi_LAAM, `pred_id`=CoCrNi, `gt_only`=['Dislocation_Density_Deformed_m2', 'FCC_Lattice_Parameter_nm'], `pred_only`=['Dislocation_Density_m2', 'Lattice_Parameter_nm']
- `paper`=1-Additively manufactured heterogeneous precipitation-strengthened high-entropy alloys with high strength and ductility, `gt_id`=Co47Ni28Cr16Fe3Al3Ti3_HT800C4h, `pred_id`=CoNiCrFeAlTi_DED_HT_STEP_12, `gt_phase`=FCC, `pred_phase`=FCC + L12
- `paper`=3-Nanotwinned precipitates induced ultra-strong AlCoCrFeNi2.1 eutectic high-entropy alloy through additive manufacturing_fixed, `gt_id`=EHEA_PBF-LB_AsBuilt, `pred_id`=AlCoCrFeNi2.1_PBF-LB_AB, `pred_phase`=B2
- `paper`=3-Nanotwinned precipitates induced ultra-strong AlCoCrFeNi2.1 eutectic high-entropy alloy through additive manufacturing_fixed, `gt_id`=EHEA_PBF-LB_Annealed, `pred_id`=AlCoCrFeNi2.1_PBF-LB_AA600C_8h, `gt_phase`=B2, `pred_phase`=B2 + FCC
- `paper`=4-Highly printable, strong, and ductile ordered intermetallic alloy_1, `gt_id`=CCIMA_LPBF_AsPrinted, `pred_id`=CCIMA_as-printed, `pred_phase`=L12
- `paper`=4-Highly printable, strong, and ductile ordered intermetallic alloy_1, `gt_id`=CCIMA_LPBF_ThermalStabilized, `pred_id`=CCIMA_thermal-stabilized, `gt_phase`=L1₂ (ordered FCC), `pred_phase`=L12

### 4.6 性能层：同时存在过提和漏提

- `property_over_extraction = 26`，`property_under_extraction = 22`，说明性能字段已经不是简单的召回不足，而是 **边界不稳**。
- Pred-only 高频属性里出现 `Aluminum_Content`、`Chromium_Content`、`Niobium_Content`，说明 Pipeline 仍会把局部成分或分析量误当成性能属性。
- GT-only 里除了常规拉伸指标，还出现整组腐蚀指标，说明复杂表征论文的 property schema 仍不够稳。

| Property 趋势 | 次数 |
| --- | --- |
| Pred-only `Ultimate_Tensile_Strength` | 5 |
| Pred-only `Work_Hardening_Rate` | 5 |
| Pred-only `Elongation_Total` | 4 |
| Pred-only `Yield_Strength` | 3 |
| Pred-only `Hardness_Vickers` | 3 |
| Pred-only `Vickers_Hardness` | 3 |
| GT-only `Hardness_HV` | 10 |
| GT-only `Elongation_Total` | 8 |
| GT-only `Ultimate_Tensile_Strength` | 6 |
| GT-only `Yield_Strength` | 3 |
| GT-only `Elongation_Uniform` | 3 |
| GT-only `Work_Hardening_Exponent_Max` | 1 |

## 5. 下一步优化建议

### P0：先稳住样品边界和 reference 召回

- 在 prompt 中单独加入“**只有当成分、工艺路线、后处理状态或论文明确比较对象发生变化时，才拆成独立 item**”的硬约束。
- 对 `Reference` 增加更强规则：凡出现 `compared with`、`benchmark`、`reference alloy`、`conventional alloy`、`cast counterpart`、`wrought counterpart` 时，优先检查是否需要新增 `Role=Reference` 条目。
- 为 `Sample_ID` 增加运行后标准化模板，优先拼接 `alloy + process + state`，减少自由命名。

### P1：把 schema 归一化前移，而不是完全依赖 LLM 自觉输出

- 在后处理中建立参数键名映射白名单，统一 `hatch distance -> hatch spacing`、`beam diameter -> spot size`、`pre-heating temperature C -> build plate temperature K` 之类的常见变体。
- 对 `Composition_Type` 和 `Nominal/Measured` 增加冲突校验；若 measured 缺失但文字只给 nominal，禁止模型擅自补 measured。
- 对 AQF 做字段粒度约束：优先保留定量字段，避免把解释性组织结论或派生强度提升量无限扩展成新键。

### P1：给高风险论文类型加专门护栏

- `Powder recycling / raw powder / fresh powder / reused powder` 论文：强制区分粉末状态样品与成形件样品，防止 reference 过拆。
- `Hybrid AM / UAM / glazing / cladding` 论文：工艺分类必须抓完整短语，不能只保留最常见的 `LPBF` 或 `AM`。
- 含大量 benchmark 对照的中文论文：先做样品表枚举，再补字段，降低“把一句背景综述拆成多个 item”的概率。

## 6. 建议的代码优化顺序

1. 先做 `Sample_ID/Role/Reference` 的 prompt 收紧和后处理归一化。
2. 再做 `Key_Params` 键名映射与单位转换白名单。
3. 然后收紧 `AQF/Main_Phase` 粒度，减少过解释。
4. 最后再针对 `Powder recycling`、`Hybrid AM`、中文 benchmark 论文补 few-shot 或规则示例。

## 7. 备注

- 这份报告是启发式对比，不等同于严格评测分数；但它非常适合指导下一轮 prompt/schema 优化，因为它把问题拆到了“样品边界 / 工艺分类 / 参数标准化 / 组织粒度”四个可行动层面。
- 若要进一步量化每条规则的收益，下一步建议直接挑 `文献2`、`文献3`、`Powder recycling`、`4-Highly printable` 这四篇做 targeted ablation，对比修改前后 item 数和字段差异数。
