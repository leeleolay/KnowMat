nature communications

Article

https://doi.org/10.1038/s41467-025-56267-1

# Active learning framework to optimize process parameters for additive-manufactured Ti-6Al-4V with high strength and ductility

Received: 5 June 2024

Accepted: 9 January 2025

Published online: 22 January 2025

Jeong Ah Lee $ ^{ID} $ $ ^{1,6} $, Jaejung Park $ ^{ID} $ $ ^{2,6} $, Man Jae Sagong $ ^{ID} $ $ ^{1} $, Soung Yeoul Ahn $ ^{1} $, Jung-Wook Cho $ ^{ID} $ $ ^{3} $, Seungchul Lee $ ^{ID} $ $ ^{2} $ & Hyoung Seop Kim $ ^{ID} $ $ ^{1,3,4,5} $

Check for updates

Optimizing process and heat-treatment parameters of laser powder bed fusion for producing Ti-6Al-4V alloys with high strength and ductility is crucial to meet performance demands in various applications. Nevertheless, inherent trade-offs between strength and ductility render traditional trial-and-error methods inefficient. Herein, we present Pareto active learning framework with targeted experimental validation to efficiently explore vast parameter space of 296 candidates, pinpointing optimal parameters to augment both strength and ductility. All Ti-6Al-4V alloys produced with the pinpointed parameters exhibit higher ductility at similar strength levels and greater strength at similar ductility levels compared to those in previous studies. By improving one property without significantly compromising the other, the framework demonstrates efficiency in overcoming the inherent trade-offs. Ultimately, Ti-6Al-4V alloys with ultimate tensile strength and total elongation of 1190 MPa and 16.5%, respectively, are produced. The proposed framework streamlines discovery of optimal processing parameters and promises accelerated development of high-performance alloys.

In the field of additive manufacturing, laser powder bed fusion (LPBF) leads a new era in fabricating complex components. Through precision melting of metal powders in successive layers by a concentrated high-energy laser beam, LPBF, controlled with intricate computer-aided design (CAD) models, is pivotal in producing detailed near-net-shape components $ ^{1-4} $. The ability of LPBF to produce such complex components is particularly pronounced in the fabrication of Ti-6Al-4V alloy components, a material distinguished by its superior mechanical strength $ ^{5,6} $, creep resistance $ ^{7,8} $, corrosion resistance $ ^{9,10} $, and biocompatibility $ ^{11,12} $.

Nevertheless, the broad application of LPBF-manufactured Ti-6Al-4V alloys has encountered a notable strength-ductility compromise. The as-fabricated samples of Ti-6Al-4V alloys comprise acicular  $ \alpha' $ martensite characterized by fine, needle-like structures that exhibit high strength (~1100 MPa) but lower ductility (~8%) $ ^{13-15} $. To address the trade-off between strength and ductility, post-processing techniques have become essential for enhancing ductility by transforming the  $ \alpha' $ phase into a more ductile  $ \alpha + \beta $ two-phase microstructure, even though the ultimate tensile strength (UTS) is often decreased. Therefore, optimizing both the process and post-heat treatment (HT) parameters

to successfully balance strength and ductility is critical for meeting performance demands.

Optimization of strength and ductility can be achieved, considering precise manipulation of processing parameters in LPBF allows control over the microstructural development in Ti-6Al-4V alloys $ ^{16-18} $. Unlike traditional manufacturing techniques, LPBF subjects materials to extreme thermal histories characterized by rapid solidification and cyclic reheating. Therefore, the resulting microstructures are considerably influenced by the processing parameters of LPBF. Several studies $ ^{19-21} $ have reported that higher laser power decreases the cooling rate, potentially leading to coarser martensitic structures or enhanced texture intensity. This effect is attributed to the increased thermal retention in the melt pool, which facilitates the alignment of dendrites parallel to the thermal flux, consequently fostering the development of columnar crystals. Conversely, increasing the scanning speed tends to increase the cooling rate and reduce the temperature gradient in the molten pool, resulting in a transition from a large columnar-like morphology to a small cellular morphology $ ^{22,23} $.

Moreover, various post-HTs have been employed to refine the as-built microstructure and balance the trade-off between strength and ductility. Through sub-transus HT, the as-built microstructure comprising intertwined  $ \alpha' $ martensitic needles within prior- $ \beta $ grains can be refined into an equilibrium phase while preserving the initial microstructure, consequently retaining strength. Super-transus HTs cause considerable growth in columnar prior- $ \beta $ grains, enhancing ductility and partially mitigating the apparent anisotropic deformation behavior $ ^{24} $. Even when HTs are conducted beyond the usual range, such as duplex annealing $ ^{25,26} $, diverse microstructural characteristics can be obtained. Therefore, both LPBF process parameters and post-HT conditions must be considered to comprehensively understand process-property relationships and to optimize mechanical properties of additive manufactured Ti-6Al-4V alloys.

Recently, numerous efforts have been made based on experimental $ ^{[27,28]} $ and computational methods $ ^{[29,30]} $ to understand process-property correlations and, therefore, to find optimal combinations for obtaining materials with superior mechanical properties. Experimentally, a large number of iterative experiments have been conducted based on the design of experiments (DoE) method and, computationally, various properties of Ti-6Al-4V alloys have been explored through simulations to identify combinations that can yield the desired properties of alloys. Additionally, methods to improve the computational efficiency of these computational approaches have also been proposed $ ^{[31]} $. While these experimental and computational studies have successfully produced alloys with the desired mechanical properties, vast number of combinations worth exploring still exist due to the time and resource limitations of both methods $ ^{[32]} $.

To overcome the constraints regarding time and resources and to further investigate the extensive process parameter space of LPBF, data-driven approaches, specifically machine learning (ML), have been applied in the field of additive manufacturing $ ^{32-35} $. The key reason for this success lies in the vast amount of data generated from prior experiments and simulations, addressing the most significant challenge of ML approaches: generating sufficient training data. By utilizing these existing data from prior studies to train ML models, properties of alloys produced under unexplored LPBF process parameters could be expeditiously and relatively accurately predicted. Based on these predictions, focusing efforts on process parameters with the highest potential can significantly reduce the number of experiments or simulations required, saving time and resources. Therefore, many studies have utilized ML in various aspects of additive manufacturing. Specifically, Akbari et al. $ ^{36} $ used ML to predict the yield strength, UTS, and elastic modulus of additively manufactured components, while Zhan et al. $ ^{37} $ developed an ML model to predict the fatigue life of stainless steel 316 L using additive manufacturing process parameters as input features.

In line with the demonstrated usefulness of data-driven approach, various studies in other fields $ ^{38-42} $ have widely utilized active learning, another type of data-driven approach that is particularly specialized for optimizing targeted properties. Unlike traditional ML, active learning involves iterative cycles of prediction and experimentation, using a surrogate model trained on labeled data alongside an acquisition function to select high-uncertainty, unlabeled data points for further testing. This process enables efficient exploration of vast parameter spaces by continuously refining the model, targeting data points with high potential for desired properties. Ultimately, active learning provides a time- and resource-efficient method for identifying data with superior target properties through focused experimentation.

Inspired by the various advantages and achievements of active learning, this study leverages active learning for the efficient and effective exploration of large number of unexplored combinations of LPBF process parameters and HT conditions, aiming to identify those that can produce Ti-6Al-4V alloys with high UTS and total elongation (TE) values simultaneously. The framework of active learning with multiple objectives, the Pareto active learning framework, is established with a Gaussian process regressor (GPR), initially trained with 119 different combinations of LPBF process parameters and HT conditions from previous studies, employed as the surrogate model, and expected hypervolume improvement (EHVI) used as the acquisition function. For every active learning iteration, two new combinations of LPBF process parameters and HT conditions were selected to produce the corresponding Ti-6Al-4V alloy specimens, with their UTS and TE values obtained through tensile tests. Moreover, with a detailed microstructure characterization and analysis of the correlation between process variables and mechanical properties, this study further validates the superior UTS and TE values of Ti-6Al-4V alloy specimens produced with the selected combinations, showing that their microstructures also share similar characteristics with those known to have high UTS and TE, respectively. The proposed Pareto active learning framework whose efficiency and effectiveness are demonstrated throughout this study is expected to enable precise and efficient tailoring of LPBF-fabricated Ti-6Al-4V alloys to meet diverse application requirements.

## Results and discussion Initial dataset

The workflow of this study is shown in Fig. 1 and proceeds in the order of initial dataset construction, implementation of the Pareto active learning framework, and microstructure analysis. First, the establishment of the initial dataset entailed a detailed description of the process parameters for LPBF and the subsequent HT conditions, as depicted in Fig. 1a. The LPBF process parameters included laser power, scan speed, and volumetric energy density (VED), calculated as

 $$ \mathrm{V E D}(\mathrm{J}/\mathrm{m m}^{3})=\frac{P}{h v t}, $$ 

where P, h, v, and t denote laser power, hatch spacing, scan speed, and layer thickness, respectively. Furthermore, post-HT conditions included parameters such as HT time and temperature. The entire compiled dataset was subjected to consistent furnace cooling, without annealing after the initial HT. A total of 119 combinations of LPBF process parameters and post-HT conditions were extracted from previous studies $ ^{[43-57]} $, and the UTS and TE of Ti-6Al-4V alloys fabricated using each combination were recorded. Utilizing the obtained 119 labeled datasets, the goal was to explore combinations that have not yet been investigated. Thus, a separate unlabeled dataset of 296 unexplored combinations was constructed, aiming to expeditiously and accurately identify combinations that can produce Ti-6Al-4V alloys with high UTS and TE using the Pareto active learning framework. For unexplored combinations, the scan speed and laser power were

Fig. 1 | Schematic of the overall flow. Three components comprising the overall workflow of exploration for Ti-6Al-4V alloys with superior mechanical properties are shown. a Construction of the initial Ti-6Al-4V LPBF dataset incorporating process and HT parameters. b Implementation of the Pareto active learning framework. The proposed active learning framework operated iteratively by selecting two combinations of the LPBF process parameters and post-HT conditions from the unlabeled dataset in each iteration. The two combinations are expected to maximally extend the Pareto front, depicted by yellow lines, which represents an exchange surface where improving one property necessitates compromising the

other. Based on the two combinations, Ti-6Al-4V alloys are fabricated to obtain their UTS and TE values through tensile tests. New data from these tests are added to the labeled dataset to expand the Pareto front, and another two combinations are recommended for testing in a repetitive process. Five iterations were conducted in this study, resulting in experiments on ten new combinations whose UTS and TE values are indicated by red dots. c Microstructure analyses to validate the superior UTS and TE values of Ti-6Al-4V alloy specimens produced with the selected combinations. Source data are provided as Source Data file.

adjusted according to the VED values to prevent the occurrence of keyholes and lack-of-fusion defects $ ^{[58,59]} $. Therefore, the scan speed was set to increase by 50 mm/s from 500 mm/s to 2000 mm/s, while the laser power was configured to increase by 50 W between 100 W and 350 W. For HT conditions, the parameters included a range of temperature and time conditions such as the as-built condition, martensite start temperature (Ms), and  $ \beta $-transus temperature. Consequently, the considered temperatures were 25, 595, 900, and 1050 ^\circC, while the considered HT times were 0 and 2 h.

## Pairwise plot to investigate correlation

Before implementing the Pareto active learning framework, pairwise plots (Fig. 2) were generated using the initial dataset to determine whether combinations of LPBF process parameters and post-HT

Fig. 2 | Pairwise plot and distribution demonstrating correlations between five input parameters and two mechanical properties. a Correlations between five input parameters and UTS (in pink) and correlations between them and TE (in blue). The individual effects of each parameter were visualized without holding other parameters constant, due to the inherent variability and interdependencies within the initial dataset, which comprises data from multiple studies and experimental conditions. The shaded areas represent the distribution of data points, illustrating

the variability and spread within each dataset. The solid lines indicate the fitted trends derived from linear regression of the distributions, capturing the overall relationship between variables. b Distribution of all Ti-6Al-4V samples in the initial dataset marked in gray, that of those with the top 10% of TE marked in blue, and that of those with the top 10% of UTS marked in red based on the values of laser power, HT temperature, and HT time. Source data are provided as Source Data file.

conditions that can produce Ti-6Al-4V alloys with high UTS and TE could be designed based solely on the pairwise relationships between each parameter and mechanical properties, and to understand the individual effects of LPBF process parameters and post-HT conditions on UTS and TE. In the pairwise plot of Fig. 2a, an inverse correlation between UTS and laser power, HT temperature, and HT time was observed, whereas a direct correlation with TE was observed for the three parameters. These relationships are further elucidated in Fig. 2b. Corroborating the trends identified in Fig. 2a, the Ti-6Al-4V samples with the top 10% TE values were fabricated with high values for all three parameters, whereas those with the top 10% UTS were fabricated with low values. Through the pairwise plot, it was observed that laser power, HT temperature, and HT time exhibit an inverse correlation with UTS and a direct correlation with TE, and a discussion regarding why each of these parameters shows this type of relationship, based on previously established insights, can be found in the Supplementary Note 1. Unlike laser power, HT temperature, and HT time, scan speed and VED did not show consistent trends in their effects on UTS and TE. Therefore, the analysis in this section focused on the parameters that showed clear and discernible patterns.

However, it was impossible to design combinations of LPBF process parameters and post-HT conditions that can produce Ti-6Al-4V alloys with high UTS and TE based on the correlations identified from the pairwise plots. First, to understand the pure effect of a single parameter on mechanical properties, the other parameters excluding that parameter need to be fixed. However, since the analysis was conducted based on the initial dataset, this was not possible; determining such pure effects would require multiple additional experiments, demanding significant time and resources. Second, because all three parameters, laser power, post-HT temperature, and post-HT time, showed a tendency where increasing UTS led to a decrease in TE, it was very difficult to achieve high values for both UTS and TE through pairwise correlations. To simultaneously increase UTS and TE, certain parameters would need to be set low to enhance UTS, but it was unclear which parameters to adjust and by how much. This implies that it is essential to consider synergistic effects between them for fabricating Ti-6Al-4V alloys with both high UTS and TE. Therefore, instead of relying solely on one-to-one relationships, an active learning framework was employed to consider the synergistic effects, thereby overcoming the limitations of conventional analytical methods.

## Pareto active learning framework

The Pareto active learning framework proposed in this study proceeds according to the following steps, with an overview of the framework presented in Fig. 3.

## 1. The surrogate model, GPR, is trained with a labeled training dataset to learn the relationship between the three types of LPBF

Fig. 3 | Overview of the Pareto active learning framework proposed in this study. The steps are iteratively repeated to find a combination that achieves both high ultimate tensile strength and total elongation in a Ti-6Al-4V alloy. Source data are provided as Source Data file.

process parameters, two types of post-HT conditions, and the mechanical properties, specifically UTS and TE.

## 2. The trained GPR is used to make predictions for combinations of LPBF process parameters and post-HT conditions that have not yet been experimentally verified for their UTS and TE. This step yields predictions for UTS and TE values of the unlabeled dataset, along with the uncertainty of each prediction.

## 3. The acquisition function, specifically EHVI, uses these values to calculate EHVI values for the unlabeled combinations.

## 4. Two unlabeled combinations with the highest EHVI values are selected to fabricate specimens using those LPBF process parameters and post-HT conditions. Tensile tests are then conducted on the produced specimens to obtain their actual UTS and TE values.

## 5. Newly acquired data from the experiments are added to the labeled training dataset for the next iteration.

## 6. The process starts again from Step 1 with the updated training dataset and repeats until the predefined condition is satisfied; in this study, the stopping condition is defined as when both selected combinations in an iteration fail to expand the Pareto front.

As aforementioned, the two most crucial components in the active learning framework are the surrogate model and acquisition function, with GPR and EHVI utilized for each component, respectively. Details regarding GPR (i.e., hyperparameters and kernel functions) and the mathematical expression of EHVI are provided in the Method section, while descriptions of the concepts of GPR and EHVI, as well as the reasons for their use in this study, are provided in the Supplementary Note 2. Also, to validate that EHVI is the most suitable acquisition function for the Pareto active learning framework of this study, comparative tests were conducted under conditions specified in Supplementary Note 3. As a result, it was confirmed that EHVI could identify data that could expand the Pareto front more expeditiously and accurately than the other three compared acquisition functions, and therefore EHVI was utilized in this study; the results of the comparative tests can also be found in Supplementary Note 3.

## Active learning iterations

The Pareto active learning framework in this study began with training a GPR on an initial dataset of 119 parameter combinations. In the first iteration, two new combinations were selected from an unexplored dataset of 296, and three specimens for each combination were fabricated and tested, with average UTS and TE values recorded (Table 1 and Supplementary Fig. 1). These selections successfully expanded the Pareto fronts of the initial 119 combinations, thereby increasing the enclosed hypervolume, as shown in Fig. 4a. To be more specific, among the 119 combinations, the highest TE in the alloys with a UTS of ~1060 MPa was 14%. However, a single experiment enabled the identification of LPBF process parameters and post-HT conditions that fabricated a Ti-6Al-4V alloy with a 4.3% point increase in TE. Similarly, whereas the highest UTS among alloys with ~18% of TE was 945 MPa, the combination identified in the first iteration resulted in a UTS of 1061 MPa, enhancing the UTS by 116 MPa. Hence, the framework accurately pinpointed the combinations capable of fabricating Ti-6Al-4V alloys with higher TE at comparable UTS levels and vice versa, thus demonstrating the possibility of improving one property without significantly compromising the other. The second iteration followed a similar process, updating the GPR with 121 data points, including two new data points from the first iteration, and selecting two more combinations from the remaining 294. The iteration also successfully expands the Pareto front, as shown in Fig. 4b. Considering TE, UTS was maintained at ~1200 MPa while achieving a 4.1% point increase in TE compared with the 121 training dataset. Furthermore, regarding UTS, while maintaining TE at around 12%, UTS was increased by 120 MPa. The third iteration further expanded the Pareto front as presented in Fig. 4c, identifying combinations that resulted in Ti-6Al-4V alloys with a 3.5% point increase in TE and a 125 MPa improvement in UTS compared with the updated training dataset comprising known 123 combinations. In the 4th iteration, the 4-1 sample, selected for having the highest EHVI value, was able to increase the Pareto front by 1.2% in terms of TE and 69.3 MPa in terms of UTS compared to the training dataset of 125 combinations. However, the 4-2 sample, selected for

Table 1 | Combinations of LPBF process parameters and post-HT conditions selected by the framework as iterations proceeded, and the corresponding UTS and TE values obtained through tensile tests

<table border="1" style="margin: auto; word-wrap: break-word;"><tr><td rowspan="2">Iteration and Sample Number</td><td colspan="5">Printing Parameters</td><td colspan="2">Measured Properties</td></tr><tr><td style="text-align: center; word-wrap: break-word;">Laser Power (W)</td><td style="text-align: center; word-wrap: break-word;">Scan Speed (mm/s)</td><td style="text-align: center; word-wrap: break-word;">Heating Temperature (^\circC)</td><td style="text-align: center; word-wrap: break-word;">Heating Time (h)</td><td style="text-align: center; word-wrap: break-word;">Volumetric Energy Density (J/mm $ ^{3} $)</td><td style="text-align: center; word-wrap: break-word;">Ultimate Tensile Strength (MPa)</td><td style="text-align: center; word-wrap: break-word;">Total Elongation (%)</td></tr><tr><td style="text-align: center; word-wrap: break-word;">1</td><td style="text-align: center; word-wrap: break-word;">250</td><td style="text-align: center; word-wrap: break-word;">1100</td><td style="text-align: center; word-wrap: break-word;">900</td><td style="text-align: center; word-wrap: break-word;">2</td><td style="text-align: center; word-wrap: break-word;">94.69</td><td style="text-align: center; word-wrap: break-word;">1061 \pm 27.5</td><td style="text-align: center; word-wrap: break-word;">18.3 \pm 1.5</td></tr><tr><td style="text-align: center; word-wrap: break-word;">1-2</td><td style="text-align: center; word-wrap: break-word;">250</td><td style="text-align: center; word-wrap: break-word;">1150</td><td style="text-align: center; word-wrap: break-word;">900</td><td style="text-align: center; word-wrap: break-word;">2</td><td style="text-align: center; word-wrap: break-word;">90.57</td><td style="text-align: center; word-wrap: break-word;">1065 \pm 17.0</td><td style="text-align: center; word-wrap: break-word;">16.3 \pm 2.0</td></tr><tr><td style="text-align: center; word-wrap: break-word;">2</td><td style="text-align: center; word-wrap: break-word;">200</td><td style="text-align: center; word-wrap: break-word;">2000</td><td style="text-align: center; word-wrap: break-word;">595</td><td style="text-align: center; word-wrap: break-word;">2</td><td style="text-align: center; word-wrap: break-word;">41.66</td><td style="text-align: center; word-wrap: break-word;">1221 \pm 18.0</td><td style="text-align: center; word-wrap: break-word;">12.9 \pm 0.2</td></tr><tr><td style="text-align: center; word-wrap: break-word;">2-2</td><td style="text-align: center; word-wrap: break-word;">200</td><td style="text-align: center; word-wrap: break-word;">1950</td><td style="text-align: center; word-wrap: break-word;">595</td><td style="text-align: center; word-wrap: break-word;">2</td><td style="text-align: center; word-wrap: break-word;">42.73</td><td style="text-align: center; word-wrap: break-word;">1209 \pm 8.0</td><td style="text-align: center; word-wrap: break-word;">12.2 \pm 2.1</td></tr><tr><td style="text-align: center; word-wrap: break-word;">3</td><td style="text-align: center; word-wrap: break-word;">200</td><td style="text-align: center; word-wrap: break-word;">1850</td><td style="text-align: center; word-wrap: break-word;">595</td><td style="text-align: center; word-wrap: break-word;">2</td><td style="text-align: center; word-wrap: break-word;">45.04</td><td style="text-align: center; word-wrap: break-word;">1186 \pm 9.0</td><td style="text-align: center; word-wrap: break-word;">16.4 \pm 0.7</td></tr><tr><td style="text-align: center; word-wrap: break-word;">3-2</td><td style="text-align: center; word-wrap: break-word;">200</td><td style="text-align: center; word-wrap: break-word;">1900</td><td style="text-align: center; word-wrap: break-word;">595</td><td style="text-align: center; word-wrap: break-word;">2</td><td style="text-align: center; word-wrap: break-word;">43.85</td><td style="text-align: center; word-wrap: break-word;">1190 \pm 12.4</td><td style="text-align: center; word-wrap: break-word;">16.5 \pm 1.3</td></tr><tr><td style="text-align: center; word-wrap: break-word;">4</td><td style="text-align: center; word-wrap: break-word;">200</td><td style="text-align: center; word-wrap: break-word;">1700</td><td style="text-align: center; word-wrap: break-word;">595</td><td style="text-align: center; word-wrap: break-word;">2</td><td style="text-align: center; word-wrap: break-word;">49.01</td><td style="text-align: center; word-wrap: break-word;">1130 \pm 13.0</td><td style="text-align: center; word-wrap: break-word;">17.6 \pm 0.5</td></tr><tr><td style="text-align: center; word-wrap: break-word;">4-2</td><td style="text-align: center; word-wrap: break-word;">250</td><td style="text-align: center; word-wrap: break-word;">1750</td><td style="text-align: center; word-wrap: break-word;">595</td><td style="text-align: center; word-wrap: break-word;">2</td><td style="text-align: center; word-wrap: break-word;">47.61</td><td style="text-align: center; word-wrap: break-word;">1136 \pm 4.0</td><td style="text-align: center; word-wrap: break-word;">14.7 \pm 2.2</td></tr><tr><td style="text-align: center; word-wrap: break-word;">5</td><td style="text-align: center; word-wrap: break-word;">150</td><td style="text-align: center; word-wrap: break-word;">1500</td><td style="text-align: center; word-wrap: break-word;">595</td><td style="text-align: center; word-wrap: break-word;">2</td><td style="text-align: center; word-wrap: break-word;">41.66</td><td style="text-align: center; word-wrap: break-word;">1207 \pm 10.2</td><td style="text-align: center; word-wrap: break-word;">12.9 \pm 1.2</td></tr><tr><td style="text-align: center; word-wrap: break-word;">5-2</td><td style="text-align: center; word-wrap: break-word;">350</td><td style="text-align: center; word-wrap: break-word;">1450</td><td style="text-align: center; word-wrap: break-word;">0</td><td style="text-align: center; word-wrap: break-word;">0</td><td style="text-align: center; word-wrap: break-word;">100.0</td><td style="text-align: center; word-wrap: break-word;">1214 \pm 21.5</td><td style="text-align: center; word-wrap: break-word;">8.64 \pm 1.4</td></tr></table>

having the second largest EHVI value, had UTS and TE values positioned within the Pareto front, failing to expand it. Similarly, in the 5th iteration, both of selected combinations failed to expand the Pareto front, indicating that the unexplored combinations capable of expanding the current Pareto front had been depleted. Thus, the stopping criterion was satisfied in the 5th iteration, concluding the active learning iterations. For thorough validation purposes, and to confirm whether depletion had indeed occurred, a 6th iteration was conducted, and an additional experiment was performed on the combination with the largest EHVI value. However, the result also failed to expand the Pareto front, and is reported in the Supplementary Fig. 2 and Supplementary Table 1.

Remarkably, except for the 5-2 sample, the UTS and TE values of the remaining 9 combinations of Ti-6Al-4V alloys, identified by the Pareto active learning framework, not only surpassed those in the initial dataset of 119 combinations used for the framework but also exhibited superior performance compared to the properties of Ti-6Al-4V alloys reported in previous studies on directed energy deposition (DED)-processed and wrought Ti-6Al-4V alloys, as illustrated in Fig. 4f. Consequently, it was demonstrated that the Pareto active learning framework proposed in this study effectively investigated unknown combinations of LPBF process parameters and post-HT conditions, expeditiously and accurately identifying combinations that yielded Ti-6Al-4V alloys with high strength and ductility.

## Interpretation on the selection of the combinations

From the results above, it was observed that the combinations selected in each iteration effectively expanded the Pareto front. The interpretation of why the Pareto active learning framework selected these combinations can be made by examining the predicted UTS and TE values along with their corresponding uncertainties that are provided by the GPR surrogate model and by considering the concept of EHVI. Figure 5 represents the predicted UTS and TE values of the combinations selected during 5 iterations and their corresponding uncertainties. In particular, to visually convey the uncertainty information, probability density functions created based on the predicted values and corresponding uncertainties are also provided, which additionally allowed for the evaluation of the reliability of the GPR surrogate model, as presented in the Supplementary Note 4. The prediction results of the GPR surrogate model on these combinations can be broadly divided into two groups: one with very high prediction uncertainty (e.g., samples 2-1, 2-2, 5-1, 5-2) and another with low uncertainty (e.g., samples 1-1, 1-2, 3-1, 3-2, 4-1, 4-2). First, examining the predicted UTS and TE values of the group with very high uncertainty, they are generally located inside the Pareto front. In other words, considering only the predicted property values or the exploitation concept (selecting combinations with high predicted property values), these combinations are not favorable. However, as explained in the Supplementary Note 5, EHVI considers both exploitation and exploration (selecting combinations with high uncertainty) in a combined manner. In the EHVI equation, the term corresponding to exploration, as visually represented in Supplementary Fig. 19, increases proportionally with the uncertainty value. Therefore, samples with very high uncertainty like 2-1, 2-2, 5-1, and 5-2 were selected because their EHVI values increased from the exploration perspective, based on the idea that combinations with high potential are hidden in unexplored combination spaces. Conversely, in the group with relatively low uncertainty, the predicted UTS and TE values are generally located on the Pareto front line, such as samples 3-1, 3-2, 4-1, and 4-2, or outside the Pareto front line like samples 1-1 and 1-2. In other words, they possess high predicted UTS and TE values, and accordingly, the term corresponding to exploitation in the EHVI equation, as visually represented in Supplementary Fig. 20, increases proportionally, resulting in those combinations to possess high EHVI values. Additionally, because they are not only favorable from the exploitation perspective but also have a certain level of prediction uncertainty, they had further high EHVI values and were thus selected. In summary, the Pareto active learning framework alternates between exploration-favorable selections and exploitation-favorable selections in each iteration, a tendency derived from ability of EHVI to account both exploration and exploitation. This ability of EHVI enabled the identification of combinations that can enhance both UTS and TE, overcoming the inherent trade-off relationship between them.

## Microstructure analysis

After identifying LPBF process parameters and post-HT conditions that could lead to the production of Ti-6Al-4V alloys with high strength and ductility, microstructural analyses were conducted to validate the source of their strength and ductility; aiming to confirm whether the microstructures of the alloys produced in this study simultaneously exhibit the microstructural characteristics of those with high UTS and those with high TE that were respectively identified in previous studies. In this section, the microstructures of one each from samples 1-1, 2-1, 3-1, and 3-2 listed in Table 1 are discussed while discussion regarding those of the 4-1, 5-1, and 6-1 samples are presented in Supplementary Figs. 3–7 and Supplementary Note 6. Furthermore, based on this microstructure analysis, the discussion in Supplementary Note 7 addresses how achieving a balance between UTS and TE was possible.

Fig. 4 | Results of active learning iterations. a First, (b) second, (c) third, (d) fourth, and (e) fifth iterations where yellow diamonds correspond to predicted properties and red triangles correspond to experiment results. f Ashby plot of UTS vs. TE for Ti-6Al-4V alloys from the initial dataset (supplementary data 1), DED-processed, and wrought Ti-6Al-4V samples (supplementary data 2). The shaded regions represent the property space of UTS and TE for different datasets,

illustrating the distribution of data points across various processing methods. The orange region with square markers corresponds to data derived from the initial dataset. The blue region with triangle markers represents data obtained from DED. The green shaded area with pentagon markers indicates data from wrought Ti-6Al-4V samples. Lastly, the red circles denote the optimized properties achieved through the proposed framework. Source data are provided as Source Data file.

Fig. 5 | Predicted UTS and TE values, and probability density function of selected combinations. a First, (b) second, (c) third, (d) fourth, and (e) fifth iterations where yellow diamonds correspond to predicted properties and red triangles correspond to experiment results; the probability density function shown

in blue corresponds to the first sample in each iteration (e.g., 1-1, 2-1, 3-1, 4-1, 5-1), and the one shown in red corresponds to the second sample (e.g., 1-2, 2-2, 3-2, 4-2, 5-2). Source data are provided as Source Data file.

Fig. 6 | Microstructure analyses for strength evolution in 1-1, 2-1, 3-1, and 3-2 samples. a1–d1 Low-magnification EBSD IPF maps of \alpha laths observed in the xz-plane of the LPBF samples. a2–d2 IPF maps of reconstructed prior-\beta phases on the xz-plane corresponding to (a1–d1) where the grain structure of the prior-\beta phase

was reconstructed according to the Burgers orientation relationship $ ^{63} $ based on the local texture of the martensites  $ \alpha $ phase. a3–d3 Contour pole figures of  $ (0001)_{\alpha} $ corresponding to  $ (a1–d1) $. a4–d4 Contour pole figures of  $ (11\bar{2}0)_{\alpha} $ corresponding to  $ (a1–d1) $.

without compromising either; specifically exploring the relationship between process, structure, and property by analyzing how energy density and post-HT temperature (i.e., process) affected the microstructure, and how the resulting microstructure ultimately impacted the mechanical properties.

First, the  $ \alpha $ orientation maps (Fig. 6a1, 6b1, 6c1, 6d1, and Supplementary Fig. 8) revealed that all samples exhibited a fully acicular microstructure, characterized by  $ \alpha $ laths arranged in a Widmanstätten structure $ ^{60} $ comprising elongated  $ \alpha $ laths that formed within the  $ \alpha $-phase matrix. The thickness of these  $ \alpha $ laths, however, varied among the samples, with the 1-1 sample presenting the thickest laths ( $ \sim $2.62  $ \mu $m) and the 2-1 sample the thinnest ( $ \sim $0.71  $ \mu $m) (Supplementary Fig. 9). The 3-1 and 3-2 samples had similar measurements ( $ \sim $0.97 and  $ \sim $0.90  $ \mu $m), representing values slightly higher than that of the 2-1 sample. Because the reduction in the  $ \alpha $ laths thickness contributed to a proliferation of the number of  $ \alpha $ lath interfaces, it can be explicated that the 1-1 sample yielded a lower UTS compared to the other samples, while the 2-1 sample had the highest UTS relative to others. Furthermore, the relatively slower scan speed and higher laser power used for the 1-1 sample resulted in a reduced cooling rate, allowing for more duration for  $ \alpha $ laths growth and coarsening. This slower solidification process led to fewer  $ \alpha $ laths interfaces, which in turn contributed to the lower UTS observed in the 1-1 sample.

Second, the width of the prior- $ \beta $ phase, obtained from the EBSD-IPF maps of the reconstructed prior- $ \beta $ phase (Fig. 6a2, 6b2, 6c2, and 6d2), exhibited a profound interrelation with the thickness of  $ \alpha $ laths. Similar to the thickness, samples with a smaller width of the prior- $ \beta $ phase had higher UTS values, as shown in Supplementary Fig. 9. This phenomenon occurred as larger prior- $ \beta $ grains provided an expanded volume conducive to the nucleation and growth of the phase. Consequently, the width of the prior- $ \beta $ phases influenced the formation of thick  $ \alpha $ laths, and the resulting  $ \alpha $ laths thickness in turn determined the UTS.

Third, PF images (Fig. 6a3, 6b3, 6c3, and 6d3) illustrated that all samples had PF in the  $ (0001)_{\alpha} $ direction parallel to the building direction. On comparing the PF intensities of 2-1, 3-1, and 3-2 samples, which employed low-temperature HT conditions, an orderly increase in PF intensity was identified; the PF intensities increased in the order of 2-1, 3-2, and 3-1 sample. The increased intensity indicates a strong fiber texture, which contributes to anisotropy in the mechanical

Fig. 7 | Microstructure analysis for ductility evolution in 1-1, 2-1, 3-1, and 3-2 samples. a1–d1 SF map of basal slip system  $ \{0001\} < 11\bar{2}0 >_{\alpha} $ corresponding to Fig. 6a1–d1, a2–d2. Frequency distribution of SF values in terms of their size, with

range of SF values corresponding to the basal slip system highlighted in blue, and the overall frequencies within the range denoted inside of the blue rectangle on top-left-corner of each plot. Source data are provided as Source Data file.

properties by limiting slip occurrence. Notably, the impact of PF intensities on the evolution of strength was, however, comparably less than those of  $ \alpha $ lath thickness and prior- $ \beta $ grain width. Additionally, PF in the  $ (11\bar{2}0)_{\alpha} $ direction across all samples (Fig. 6a4, 6b4, 6c4, and 6d4) exhibited a random distribution, contrary to the more uniform distribution observed in the  $ (0001)_{\alpha} $ direction.

Regarding ductility, the Schmid factor (SF) values were evaluated for basal slip ( $ \{0001\}<11\bar{2}0_{\alpha}> $), as shown in Fig. 7a1, 7b1, 7c1, and 7d1

where the basal slip system in \alpha titanium alloys is known to possess the lowest critical resolved shear stress (CRSS) at room temperature, making it the most readily activated slip system during deformation. Accordingly, the frequencies of SF values between 0.4 and 0.5 were compared across all four samples, focusing only on the range of SF values that represented the basal slip system. The SF value distribution for each sample is shown in Fig. 7a2, 7b2, 7c2, and 7d2, with the section of interest highlighted in blue and the percentage of SF values in the range of 0.4 and 0.5. The 1-1 sample exhibited higher SF values than the 2-1 sample, suggesting that the 1-1 sample has easier activation of the slip system than the others samples, thereby possessing better ductility; 54.80% of the total SF values for the 1-1 sample were positioned between 0.4 and 0.5, whereas only 27.26% are for the 2-1 sample. The higher VED in sample 1-1 resulted in slower cooling, which facilitated the transformation to an \alpha+\beta dual-phase microstructure as the material underwent gradual solidification. This phase transformation increased the potential for slip system activation within the grains, particularly in the basal slip system, which was significantly influenced by variations in temperature and cooling rate, leading to enhanced activation. Accordingly, the 1-1 sample exhibited a higher TE value compared to that of the 2-1 sample, which showed signs of localized softening. Such softening in the 2-1 sample could result in premature necking or fracture, preceding significant plastic deformation and, therefore, can culminate in reduced ductility. Moreover, the 3-1 and 3-2 samples, which exhibited TE values between those of 1-1 and 2-1 samples, had frequencies of SF values between 0.4 and 0.5 at 36.80 and 46.38%, respectively; thus, both the values were between those of the 1-1 and 2-1 samples. In addition to the SF analysis, the effects of phase constitution and alloying element partitioning between the \alpha′ and \beta phases on mechanical properties were also examined, and the results are reported in Supplementary Note 8 and Supplementary Figs. 21 and 22.

Hence, through this microstructure analysis, it was confirmed that the samples produced with combinations of LPBF parameters and post-HT conditions selected by the proposed framework not only share microstructural characteristics commonly observed in alloys with high UTS, such as the narrow width of the prior- $ \beta $ phase, which influences the thickness of the formed  $ \alpha $ laths, and the low PF intensity in the  $ (0001)_{\alpha} $ direction, but also exhibit high frequencies of SF values between 0.4 and 0.5, which are also frequently seen in alloys with high TE. In that the samples produced in this study share microstructural characteristics typically observed in both high UTS alloys and high TE alloys, the balance between strength and ductility achieved in this study could be validated.

## Concluding remarks and future directions

In summary, this study was the first to apply a data-driven approach to overcome the inherent trade-offs between strength and ductility in LPBF-fabricated Ti-6Al-4V alloys and to identify combinations of LPBF process parameters and HT conditions that can produce alloys with high UTS and TE. Unlike traditional ML approaches, the proposed Pareto active learning framework considered prediction uncertainty in the selection process, enabling practical exploration of a broad parameter space. Also, by iteratively performing experiments and predictions, it allowed for the optimization of UTS and TE. Specifically, the EHVI acquisition function was instrumental in identifying combinations that could expand the Pareto front by overcoming the trade-off relationship between UTS and TE. Consequently, all ten combinations selected by the Pareto active learning framework across five iterations consistently produced high-performance alloys, achieving high UTS and TE of (1061 MPa, 18.3%), (1130 MPa, 17.6%), (1190 MPa, 16.5%), and (1221 MPa, 12.9%) within only five trials, with the combination producing (1190 MPa, 16.5%) being determined as optimal due to its balanced high UTS and TE values. Additionally, microstructural analysis validated the balance achieved between UTS and TE by confirming that the microstructures of samples produced in the study share the microstructural characteristics of both high UTS alloys and high TE alloys identified in previous studies. In conclusion, the proposed Pareto active learning framework whose ability to optimize both UTS and TE simultaneously was demonstrated throughout this study can be easily adjusted to consider additional LPBF parameters or optimize other properties, making it a valuable tool for future data-driven research. Furthermore, the resulting dataset of 130 combinations of LPBF process parameters and post-HT conditions will provide a strong foundation for ML research on Ti-6Al-4V alloys, accelerating advancements in alloy property optimization.

As a direction for future research, combining data-driven and physics-based approaches would be promising. While this study was conducted using only a data-driven method due to the relative abundance of Ti-6Al-4V data, exploring recently developed alloys or more diverse types of parameter considered for Ti-6Al-4V present challenges due to limited data availability. In these cases, rather than relying solely on data, additionally utilizing existing physics knowledge and physics-based simulations, as demonstrated in previous studies $ ^{[29,61]} $, could enhance prediction accuracy for alloy properties even under data constraints.

## Methods

## Data preprocessing and active learning method

For the Pareto active learning framework, all data, including 119 initial training data (details in supplementary data 1) and 296 previously unexplored test data, were preprocessed using Standard Scaler from the Python-based scikit-learn package for standardization. When original values were required, an inverse transformation was used to restore them. Additionally, the Pareto active learning framework was built using Python and was modeled using PyTorch. Details regarding GPR and EHVI (e.g., equations and kernel functions) are provided in Table 2, where GPR was specified by its kernel  $ (k(x^{(1)}, x^{(2)})) $ and mean function  $ (\mu(x)) $; the detailed interpretation of EHVI acquisition function is presented in Supplementary Note 5.

## Sample fabrication

For each combination of LPBF process parameters and post-HT conditions selected by the Pareto active learning framework, we fabricated coupon samples of the Ti-6Al-4V alloy using an LPBF machine (Concept Laser M2, GE Additive, USA). The coupon samples were printed with widths, lengths, and heights of 30, 8, and 10 mm, respectively. We used a gas-atomized metallic powder with a nominal composition, as shown in Supplementary Table 2. The Ti_{64} powder was characterized by scanning electron microscopy (SEM), JEOL JSM-7100F. The SEM images of the powders and the corresponding powder size distributions are shown in Supplementary Fig. 12. The process parameters employed in this study are listed in Table 1, with all samples produced using the same layer thickness of 50 \mum, rotation angle of 67^\circ, and hatch distance of 48 \mum. The post-HT conditions utilized in this study are listed in Table 1, and, after the post-HT, all the samples were cooled in a furnace under the argon atmosphere. The density of the specimens, determined via the Archimedes method utilizing XPR 205 (Mettler Toledo, USA), was measured as 4.406 \pm 0.004, 4.407 \pm 0.003, 4.418 \pm 0.007, and 4.412 \pm 0.002 g/cm³ for the 1-1, 2-1, 3-1, and 3-2 samples, respectively. These measurements were consistent with the generally reported values (4.43 g/cm³).

## Electron microscopy characterization

EBSD was employed to conduct microstructural analysis on the xz-plane, with the x-axis aligned with the direction of the powder application and the z-axis corresponding to the build orientation. Before the EBSD examination, specimen surfaces were mechanically polished using a 1200-grit emery paper to achieve the requisite surface finish. EBSD analysis was performed using field emission scanning electron

Table 2 | Details about the surrogate model (Gaussian process regressor) and the acquisition function (expected hypervolume improvement)

| Gaussian process regressor |
| --- |
| GPR( $ \mu(x) $,  $ k(x^{(1)}, x^{(2)}) $) |
| $ \mu(x) $: constant mean function |
| $ k(x^{(1)}, x^{(2)}) = \sigma^{2} \left(1 + \frac{\sqrt{5}d}{l} + \frac{5d^{2}}{3l^{2}}\right) \exp\left(-\frac{\sqrt{5}d}{l}\right) $ (1) |
| Expected hypervolume improvement |
| EHVI =  $ \sum_{i=1}^{N} \Theta(l_{1}^{(i)}, u_{1}^{(i)}, \mu_{1}, \sigma_{1}) \cdot \Psi(l_{2}^{(i)}, l_{2}^{(i)}, \mu_{2}, \sigma_{2}) + \sum_{i=1}^{N} (\Psi(l_{1}^{(i)}, l_{1}^{(i)}, \mu_{1}, \sigma_{1}) - \Psi(l_{1}^{(i)}, u_{1}^{(i)}, \mu_{1}, \sigma_{1})) \cdot \Psi(l_{2}^{(i)}, l_{2}^{(i)}, \mu_{2}, \sigma_{2}) $ (2) |
| $ \Theta(x, y, z, w) = (y - x) \left[1 - \Phi\left(\frac{y - z}{w}\right)\right] $ (3) |
| $ \Psi(x, y, z, w) = w \Phi\left(\frac{y - z}{w}\right) + (z - x) \left[1 - \Phi\left(\frac{y - z}{w}\right)\right] $ (4) |
| $ x^{(1)}, x^{(2)} $: feature vectors |
| d: distance between two vectors  $ x^{(1)} $ and  $ x^{(2)} $ |
| l: length scale where  $ l \sim \text{Gamma}(3.0, 6.0) $ |
| $ \sigma $: output scale where  $ \sigma \sim \text{Gamma}(2.0, 0.15) $ |
| $ l_{1}^{(i)}, l_{2}^{(i)} $: lower bounds of partitioning integration region |
| $ \mu_{1}, \mu_{2} $: mean of predicted values for each objective |
| $ u_{1}^{(i)}, u_{2}^{(i)} $: upper bounds of partitioning integration region |
| $ \sigma_{1}, \sigma_{2} $: standard deviation of predictions for each objective |
| $ \Phi $: standard cumulative probability distribution function |
| $ \phi $: standard probability density function |
| N: number of integration region by partitioning |

microscopy (JSM-7100F, JEOL, Japan), with step sizes of 0.9 µm at 300x magnification and 0.23 µm at 1000x magnification. EBSD analysis was performed in the xz plane. Raw EBSD data were analyzed using orientation imaging microscopy (OIM) software (TSL OIM Analysis 7). EBSD data for the prior-\beta phase was post-processed and visualized using the MTEX package (v. 6.0) $ ^{62} $. The chemical compositions of the specimens were determined by SEM-EDS. The XRD measurement was carried out using Bruker/XRD D8-Advance Davinci instrument applying Cu K\alpha radiation with a wavelength of 0.154 nm. The XRD pattern was obtained between the 2\theta range of 30–90^\circ at the scan rate of 1^\circ min $ ^{-1} $ and the scan interval of 0.02^\circ. The full width at half maximum (FWHM) of selected peaks was measured through single peak fitting, using a Pseudo-Voigt peak approximation.

## Tensile test

Dog-bone-shaped tensile test specimens with a gauge length of 5 mm, gauge width of 2.5 mm, and thickness of 1.0 mm were extracted from the as-built LPBF samples as shown in Supplementary Fig. 13. The specimens were subjected to uniaxial tensile tests at a strain rate of  $ 5 \times 10^{-3} \, s^{-1} $, utilizing an universal testing machine (Instron 1361, Instron, USA). Precise strains were measured during the tensile tests using the digital image correlation method (ARAMIS 12 M, GOM, Germany). All tensile tests were repeated at least three times to obtain reproducible results.

## Data Availability

The raw data generated in this study are available within the article and its supplementary data 1 and 2. There is no restriction on data availability. The same dataset has been deposited in the Figshare repository under the https://doi.org/10.6084/m9.figshare.25971973. Source data are provided with this paper.

## Code availability

All codes are provided separately with this paper and deposited in Code Ocean under the https://doi.org/10.24433/CO.0857013.v1. There is no restriction on code availability.

## References

## 1. McGregor, M., Patel, S., McLachlin, S. & Vlasea, Mihaela Architectural bone parameters and the relationship to titanium lattice

design for powder bed fusion additive manufacturing. Addit. Manuf. 47, 102273 (2021).

## 2. Zhang, H. et al. High throughput in-situ synthesis of Fe-Cr-Ni alloys via laser powder bed fusion: Exploring the microstructure and property evolution. Addit. Manuf. 81, 103996 (2024).

## 3. Lee, J. A., Sagong, M. J., Jung, J., Kim, E. S. & Kim, H. S. Explainable machine learning for understanding and predicting geometry and defect types in Fe-Ni alloys fabricated by laser metal deposition additive manufacturing. J. Mater. Res. Technol. 22, 413–423 (2023).

## 4. Xu, J., Kontis, P., Peng, R. L. & Moverare, J. Modelling of additive manufacturability of nickel-based superalloys for laser powder bed fusion. Acta Mater 240, 118307 (2022).

## 5. Rani, S. U., Kesavan, D. & Kamaraj, M. Evaluation of influence of microstructural features of LPBF Ti-6Al-4 V on mechanical properties for an optimal strength and ductility. J. Alloys Compd. 960, 170575 (2023).

6. Zhang, W. et al. The reverse transformation mechanism of  $ \beta $ phase and its stability of Ti-6Al-4V alloy fabricated via laser powder bed fusion. Mater. Des. 241, 112926 (2024).

## 7. Zhou, Z., Liu, Y., Liu, X. & Wu, L. High-temperature tensile and creep properties of TiB-reinforced Ti6Al4V composite fabricated by laser powder bed fusion. Mater. Charact. 200, 112859 (2023).

## 8. Sanchez, S. et al. The creep behaviour of nickel alloy 718 manufactured by laser powder bed fusion. Mater. Des. 204, 109647 (2021).

## 9. Qin, P. et al. Corrosion and passivation behavior of laser powder bed fusion produced Ti-6Al-4V under various prior plastic deformation strains. Corros. Sci. 230, 111919 (2024).

## 10. Becker, T. H., Kumar, P. & Ramamurty, U. Fracture and fatigue in additively manufactured metals. Acta Mater 219, 117240 (2021).

## 11. Li, Z., Chuzenji, M. & Mizutani, M. Compression and fatigue performance of Ti6Al4V materials with different uniform and gradient porous structures. Mater. Sci. Eng. A 873, 145030 (2023).

## 12. Ataee, A., Li, Y. & Wen, C. A comparative study on the nanoindentation behavior, wear resistance and in vitro biocompatibility of SLM manufactured CP-Ti and EBM manufactured Ti64 gyroid scaffolds. Acta Biomater 97, 587–596 (2019).

## 13. Wu, X. et al. Microstructures of laser-deposited Ti–6Al–4V. Mater. Des. 25, 137–144 (2004).

## 14. Thijs, L., Verhaeghe, F., Craeghs, T., Humbeeck, J. V. & Kruth, J.-P. A study of the microstructural evolution during selective laser melting of Ti–6Al–4V. Acta Mater 58, 3303–3312 (2010).

## 15. Simonelli, M., Tse, Y. Y. & Tuck, C. Effect of the build orientation on the mechanical properties and fracture modes of SLM Ti-6Al-4V. Mater. Sci. Eng. A 616, 1–11 (2014).

## 16. Pathania, A., Subramaniyan, A. K. & Nagesha, B. K. Influence of post-heat treatments on microstructural and mechanical properties of LPBF-processed Ti6Al4V alloy. Prog. Addit. Manuf. 7, 1323–1343 (2022).

## 17. Lakroune, Y. et al. Microstructural evolution during post heat treatment of the Ti–6Al–4V alloy manufactured by laser powder bed fusion. J. Mater. Res. Technol. 23, 1980–1994 (2023).

## 18. Levkulich, N. C. et al. The effect of process parameters on residual stress evolution and distortion in the laser powder bed fusion of Ti-6Al-4V. Addit. Manuf. 28, 475–484 (2019).

## 19. Zhou, J., Wang, Y., Zhi, G. & He, L. Effect of laser power on anisotropic microstructure and mechanical behavior of biomedical Ti-35Nb-15Zr (at%) alloy fabricated by laser powder bed fusion. Met. Mater. Int. 30, 240–252 (2024).

## 20. Zhang, X., Mao, B., Mushongera, L., Kundin, J. & Liao, Y. Laser powder bed fusion of titanium aluminides: an investigation on site-specific microstructure evolution mechanism. Mater. Des. 201, 109501 (2021).

## 21. Li, S., Lan, X., Wang, Z. & Mei, S. Microstructure and mechanical properties of Ti-6.5Al-2Zr-Mo-V alloy processed by laser powder bed fusion and subsequent heat treatments. Addit. Manuf. 48, 102382 (2021).

## 22. Guo, W. et al. Effect of laser scanning speed on the microstructure, phase transformation and mechanical property of NiTi alloys fabricated by LPBF. Mater. Des. 215, 110460 (2022).

## 23. Chen, Q., Xu, L., Zhao, L., Hao, K. & Han, Y. Effect of scanning speed on microstructure and mechanical properties of as-printed Ti-22Al-25Nb intermetallic by laser powder bed fusion. Mater. Sci. Eng. A 885, 145652 (2023).

## 24. Bourell, D. et al. Materials for additive manufacturing. CIRP Ann 66, 659–681 (2017).

## 25. Tao, X. et al. Electron beam freeform fabrication of Ti6Al4V alloy and the role of post-heat treatment in the microstructure, texture, and mechanical properties. J. Alloys Compd. 954, 170212 (2023).

## 26. Macallister, N., Vanmeensel, K. & Becker, T. H. Fatigue crack growth parameters of Laser Powder Bed Fusion produced Ti-6Al-4V. Int. J. Fatigue 145, 106100 (2021).

## 27. Zhang, K. et al. Microstructure control by heat treatment for better ductility and toughness of Ti-6Al-4V produced by laser powder bed fusion. Aust. J. Mech. Eng. 19, 680–691 (2021).

## 28. Du, X., Simonelli, M., Murray, J. W. & Clare, A. T. Facile manipulation of mechanical properties of Ti-6Al-4V through composition tailoring in laser powder bed fusion. J. Alloys Compd. 941, 169022 (2023).

## 29. Nitzler, J., Meier, C., Müller, K. W., Wall, W. A. & Hodge, N. E. A novel physics-based and data-supported microstructure model for part-scale simulation of laser powder bed fusion of Ti-6Al-4V. Adv. Model. Simul. Eng. Sci. 8, 16 (2021).

## 30. Verma, R., Kumar, P., Jayaganthan, R. & Pathak, H. Extended finite element simulation on tensile, fracture toughness and fatigue crack growth behaviour of additively manufactured Ti6Al4V alloy. Theor. Appl. Fract. Mech. 117, 103163 (2022).

## 31. Proell, S. D., Brotz, J., Kronbichler, M., Wall, W. A. & Meier, C. A highly efficient computational approach for part-scale microstructure predictions in Ti-6Al-4V additive manufacturing. arXiv https://doi.org/10.48550/arXiv.2402.17580 (2024).

## 32. Zhang, J., Yin, C., Xu, Y. & Sing, S. L. Machine learning applications for quality improvement in laser powder bed fusion: A state-of-the-art review. Int. J. AI Mater. Des. 1, 26–43 (2024).

## 33. Guirguis, D., Tucker, C. & Beuth, J. Accelerating process development for 3D printing of new metal alloys. Nat. Commun. 15, 582 (2024).

## 34. Song, W. et al. A new approach to design advanced superalloys for additive manufacturing. Addit. Manuf. 84, 104098 (2024).

## 35. Zhang, X. et al. Machine learning-driven 3D printing: a review. Appl. Mater. Today 39, 102306 (2024).

## 36. Akbari, P., Zamani, M. & Mostafaei, A. Machine learning prediction of mechanical properties in metal additive manufacturing. Addit. Manuf. 91, 104320 (2024).

## 37. Zhan, Z. & Li, H. Machine learning based fatigue life prediction with effects of additive manufacturing process parameters for printed SS 316. L. Int. J. Fatigue 142, 105941 (2021).

## 38. Min, K. & Cho, E. Accelerated discovery of potential ferroelectric perovskite via active learning. J. Mater. Chem. C 8, 7866–7872 (2020).

## 39. Flores, R. A. et al. Active learning accelerated discovery of stable iridium oxide polymorphs for the oxygen evolution reaction. Chem. Mater. 32, 5854–5863 (2020).

## 40. Sheng, Y. et al. Active learning for the power factor prediction in diamond-like thermoelectric materials. Npj Comput. Mater. 6, 1–7 (2020).

## 41. Yuan, R. et al. Accelerated discovery of large electrostrains in BaTiO3-based piezoelectrics using active learning. Adv. Mater. 30, 1702884 (2018).

## 42. Kim, H. et al. Active learning platform for accelerating the search for high-voltage cathode materials in an extensive chemical space. J. Phys. Chem. C 127, 18902–18913 (2023).

## 43. Luo, Q., Yin, L., Simpson, T. W. & Beese, A. M. Effect of processing parameters on pore structures, grain features, and mechanical properties in Ti-6Al-4V by laser powder bed fusion. Addit. Manuf. 56, 102915 (2022).

## 44. Zhou, B., Zhou, J., Li, H. & Lin, F. A study of the microstructures and mechanical properties of Ti6Al4V fabricated by SLM under vacuum. Mater. Sci. Eng. A 724, 1–10 (2018).

## 45. Vrancken, B., Thijs, L., Kruth, J.-P. & Van Humbeeck, J. Heat treatment of Ti6Al4V produced by selective laser melting: microstructure and mechanical properties. J. Alloys Compd. 541, 177–185 (2012).

## 46. Kumar, P., Prakash, O. & Ramamurty, U. Micro-and meso-structures and their influence on mechanical properties of selectively laser melted Ti-6Al-4V. Acta Mater 154, 246–260 (2018).

## 47. Liu, J. et al. Achieving Ti6Al4V alloys with both high strength and ductility via selective laser melting. Mater. Sci. Eng. A 766, 138319 (2019).

## 48. Sun, J. et al. The microstructure transformation of selective laser melted Ti-6Al-4V alloy. Mater. Today Commun. 19, 277–285 (2019).

## 50. Khorasani, A., Gibson, I., Goldberg, M. & Littlefair, G. On the role of different annealing heat treatments on mechanical properties and microstructure of selective laser melted and conventional wrought Ti-6Al-4V. Rapid Prototyp. J 23, 295–304 (2017).

## 51. Fousova, M., Vojtech, D., Doubrava, K., Daniel, M. & Lin, C. F. Influence of inherent surface and internal defects on mechanical properties of additively manufactured Ti6Al4V alloy: comparison between selective laser melting and electron beam melting. Materials 11, 537 (2018).

## 52. Wang, D. et al. Densification, tailored microstructure, and mechanical properties of selective laser melted Ti–6Al–4V alloy via annealing heat treatment. Micromachines 13, 331 (2022).

## Article

## 53. Tao, P. et al. Tensile behavior of Ti-6Al-4V alloy fabricated by selective laser melting: effects of microstructures and as-built surface quality. China Foundry 15, 243–252 (2018).

## 54. Hacisalihoğlu, I., Yıldız, F. & Çelik, A. The effects of build orientation and hatch spacing on mechanical properties of medical Ti-6Al-4V alloy manufactured by selective laser melting. Mater. Sci. Eng. A 802, 140649 (2021).

## 55. Yan, X. et al. Effect of heat treatment on the phase transformation and mechanical properties of Ti6Al4V fabricated by selective laser melting. J. Alloys Compd. 764, 1056–1071 (2018).

## 56. Meng, L. X. et al. Effects of defects and microstructures on tensile properties of selective laser melted Ti6Al4V alloys fabricated in the optimal process zone. Mater. Sci. Eng. A 830, 142294 (2022).

## 57. Wei, W.-H. & Shen, J. Effect of laser energy density on microstructures and mechanical properties of selective laser melted Ti-6Al-4V alloy. Int. J. Mater. Res. 109, 437–442 (2018).

## 58. Cao, S., Zou, Y., Lim, C. V. S. & Wu, X. Review of laser powder bed fusion (LPBF) fabricated Ti-6Al-4V: process, post-process treatment, microstructure, and property. Light adv. Manuf. 2, 20 (2021).

## 59. Thapliyal, S. & Mishra, R. S. Chapter Eight - Linking materials systems approach to alloy design and part qualification for laser powder bed fusion additive manufacturing. In Quality Analysis of Additively Manufactured Metals (eds. Kadkhodapour, J., Schmauder, S. & Sajadi, F.) 321–354 (Elsevier, 2023).

60. Gil, F. J., Ginebra, M. P., Manero, J. M. & Planell, J. A. Formation of  $ \alpha $-Widmanstätten structure: effects of grain size and cooling rate on the Widmanstätten morphologies and on the mechanical properties in Ti6Al4V alloy. J. Alloys Compd. 329, 142–152 (2001).

## 61. Hosseini, E., Scheel, P., Müller, O., Molinaro, R. & Mishra, S. Single-track thermal analysis of laser powder bed fusion process: parametric solution through physics-informed neural networks. Comput. Methods Appl. Mech. Eng. 410, 116019 (2023).

## 62. Hielscher, R. & Schaeben, H. A novel pole figure inversion method: specification of the MTEX algorithm. J. Appl. Crystallogr. 41, 1024–1037 (2008).

63. Lonardelli, I. et al. In situ observation of texture evolution during \alpha \rightarrow \beta and \beta \rightarrow \alpha phase transformations in titanium alloys investigated by neutron diffraction. Acta Mater 55, 5718–5727 (2007).

## Acknowledgements

This work was supported by the National Research Foundation of Korea (NRF) grant funded by the Korea government (MSIT) (NRF-2022R1A5A1030054) and by the Nano & Material Technology Development Program through the National Research Foundation of Korea (NRF) funded by Ministry of Science and ICT (RS-2024-00451579).

## Author Contributions

Jeong Ah Lee (J.A. Lee): Methodology, Visualization, Writing-original draft. Jaejung Park (J. Park): Software, Visualization, Writing-original draft. Man Jae Sagong (M.J. Sagong): Investigation, Visualization, Validation. Soung Yeoul Ahn (S.Y. Ahn): Investigation, Visualization. Jung-Wook Cho (J.W. Cho): Validation, Supervision. Seungchul Lee (S. Lee): Writing-review&editing. Hyoung Seop Kim (H.S. Kim): Supervision, Funding acquisition, Writing-review&editing.

## Competing interests

The authors declare no competing interests.

## Additional information

## Supplementary Material

Correspondence and requests for materials should be addressed to Seungchul Lee or Hyoung Seop Kim.

Peer review information Nature Communications thanks Jiayun Shao and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. A peer review file is available.

## Reprints and permissions information is available at http://www.nature.com/reprints

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

© The Author(s) 2025

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

Published online: 22 January 2025
Jeong Ah Lee $ ^{ID} $ $ ^{1,6} $, Jaejung Park $ ^{ID} $ $ ^{2,6} $, Man Jae Sagong $ ^{ID} $ $ ^{1} $, Soung Yeoul Ahn $ ^{1} $, Jung-Wook Cho $ ^{ID} $ $ ^{3} $, Seungchul Lee $ ^{ID} $ $ ^{2} $ & Hyoung Seop Kim $ ^{ID} $ $ ^{1,3,4,5} $

Nature Communications | (2025)16:931

## Results and Discussion

Initial dataset

## Data Availability

## 63. Lonardelli, I. et al. In situ observation of texture evolution during \alpha \rightarrow \beta and \beta \rightarrow \alpha phase transformations in titanium alloys investigated by neutron diffraction. Acta Mater 55, 5718–5727 (2007).

## Author Contributions

## Supplementary Material

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

Results and discussion
Initial dataset

Data availability

63. Lonardelli, I. et al. In situ observation of texture evolution during α → β and β → α phase transformations in titanium alloys investigated by neutron diffraction. Acta Mater 55, 5718–5727 (2007).

Author contributions

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41467-025-56267-1.