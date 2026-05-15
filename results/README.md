# Results of the Shared Task

A huge thank you to all the teams that participated and made this shared task a success! In total, **8 teams** took part, submitting **69 systems** across all languages.

As announced, evaluation followed a two-stage process: systems were first ranked by an automatic metric (**chrF++**), and the **top 5 systems per language** (one per team, taking each team's best-scoring system) then advanced to human evaluation.

📊 **Automatic metric results:** [results/automatic_metric](https://github.com/AmericasNLP/americasnlp2026/tree/main/results/automatic_metric)

🏆 **Per-language winners:** [results/README.md#per-language-winners](https://github.com/AmericasNLP/americasnlp2026/blob/main/results/README.md#per-language-winners)

🥇 **Overall winner:** To recognize the team that performed strongly across *all* languages, we also computed an overall winner based on points earned across the five language rankings — see [results/README.md#overall-winner](https://github.com/AmericasNLP/americasnlp2026/blob/main/results/README.md#overall-winner).


# Per-Language Winners

Each image was shown alongside the 5 captions, and each caption was rated on a 1–5 scale (see the [annotation guidelines](https://github.com/AmericasNLP/americasnlp2026/tree/main/results/annotation_guideline/README.md)). When multiple annotators rated the same example, their scores were averaged per example before computing the overall mean. All test-set samples received at least one annotation, except for Wixarika, where 50 samples (≈25%) were annotated.

Further details on the human annotation procedure will be provided in the shared task description paper.

## 🏆 Guarani — Winner: **IUHoosiers**

| Rank | Team | Version | N Ratings | N Images | Mean Rating |
|------|------|---------|-----------|----------|-------------|
| 🥇 1 | IUHoosiers | 4 | 228 | 101 | 3.448 |
| 🥈 2 | gators | 0 | 228 | 101 | 3.390 |
| 🥉 3 | usp | 0 | 228 | 101 | 2.410 |
| 4 | NAIST | 0 | 228 | 101 | 1.978 |
| 5 | Mila | 1 | 228 | 101 | 1.764 |

## 🏆 Maya — Winner: **Mila**

| Rank | Team | Version | N Ratings | N Images | Mean Rating |
|------|------|---------|-----------|----------|-------------|
| 🥇 1 | Mila | 3 | 212 | 212 | 3.203 |
| 🥈 2 | gators | 0 | 212 | 212 | 3.175 |
| 🥉 3 | yaduha | 0 | 212 | 212 | 2.892 |
| 4 | NAIST | 0 | 212 | 212 | 1.934 |
| 5 | InclusionVLM | 0 | 212 | 212 | 1.108 |

## 🏆 Nahuatl — Winner: **yaduha**

| Rank | Team | Version | N Ratings | N Images | Mean Rating |
|------|------|---------|-----------|----------|-------------|
| 🥇 1 | yaduha | 0 | 200 | 200 | 3.465 |
| 🥈 2 | gators | 0 | 200 | 200 | 3.375 |
| 🥉 3 | Mila | 2 | 200 | 200 | 1.560 |
| 4 | NAIST | 0 | 200 | 200 | 1.220 |
| 5 | InclusionVLM | 0 | 200 | 200 | 1.185 |

## 🏆 Wixarika — Winner: **NAIST**

| Rank | Team | Version | N Ratings | N Images | Mean Rating |
|------|------|---------|-----------|----------|-------------|
| 🥇 1 | NAIST | 0 | 201 | 201 | 3.79 |
| 🥈 2 | gators_v1 | 0 | 201 | 201 | 2.90 |
| 🥉 3 | 6fanle | 0 | 201 | 201 | 2.48 |
| 4 | InclusionVLM | 0 | 201 | 201 | 2.33 |
| 5 | Mila | 2 | 201 | 201 | 2.21 |

## 🏆 Bribri — Winner: **yaduha**

| Rank | Team | Version | N Ratings | N Images | Mean Rating |
|------|------|---------|-----------|----------|-------------|
| 🥇 1 | yaduha | 0 | 320 | 267 | 2.895 |
| 🥈 2 | gators | 1 | 320 | 267 | 2.758 |
| 🥉 3 | NAIST | 0 | 320 | 267 | 2.219 |
| 4 | Mila | 0 | 320 | 267 | 1.994 |
| 5 | usp | 0 | 320 | 267 | 1.086 |

---

# Overall Winner

## 🏆 Overall Winner: **gators**

| Rank | Team | Total Points |
|------|------|--------------|
| 🥇 1 | **gators** | **20** |
| 2 | NAIST | 14 |
| 3 | yaduha | 13 |
| 4 | Mila | 12 |
| 5 | IUHoosiers | 5 |
| 6 | usp | 4 |
| 7 | InclusionVLM | 4 |
| 8 | 6fanle | 3 |

## How the ranking was made

Points were awarded based on each team's rank (during human evaluation) within a culture:

- 🥇 1st place → **5 points**
- 🥈 2nd place → **4 points**
- 🥉 3rd place → **3 points**
- 4th place → **2 points**
- 5th place → **1 point**
- 6th place and below (no human evaluation) → **0 points**

A team's **total points** are the sum of points earned across all five languages (Guarani, Maya, Nahuatl, Wixarika, Bribri).
