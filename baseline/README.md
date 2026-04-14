# Baseline: Zero-Shot VLM + Machine Translation

This folder contains the initial baseline system for the **AmericasNLP 2026 Shared Task on Cultural Image Captioning for Indigenous Languages**.

**[Open the notebook in Google Colab](https://colab.research.google.com/drive/1fexxQ2RPeQcetl_34i52l7BcFBqN_fqW?usp=sharing)**

## Approach

The baseline follows a two-stage **generate-then-translate** pipeline:

1. **Image Captioning in Spanish** — A Vision-Language Model ([Qwen3-VL-8B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct)) generates a culturally-informed caption in Spanish using a detailed prompt that includes Wixárika cultural context (religious elements, art, ceremonies, material culture, etc.).
2. **Translation to the Target Language** — The Spanish caption is translated into Wixárika using [Sheffield's winning submission](https://aclanthology.org/2023.americasnlp-1.21/) from the AmericasNLP 2023 Shared Task on Machine Translation into Indigenous Languages.

## Results on dev set

| Language  | chrF++ |
|-----------|--------|
| Wixárika  | 17.77  |
| Bribri    |  7.57  |
| Guaraní   | 20.82  |
| Nahuatl   | 11.53  |
| Maya   | --  |

### Why Spanish as an Intermediate Language?

Existing machine translation resources for Indigenous languages of the Americas are primarily paired with Spanish. Using Spanish as a pivot allows the baseline to leverage available MT systems.

## Culturally-Informed Prompting

Rather than using a generic captioning prompt, the baseline provides the VLM with rich cultural context about the Wixárika people, including:

- Religious and spiritual elements
- Traditional art and crafts
- Material culture
- Ceremonial practices

As a simple baseline, the cultural context used in the prompt was obtained from the [Wikipedia entry for the Wixárika (Huichol) people](https://es.wikipedia.org/wiki/Huichol). This helps the model generate more culturally appropriate descriptions rather than generic image captions.

## Evaluation

Generated captions are evaluated using **ChrF++**, the primary ranking metric for the shared task, which is convenient since it can be computed automatically without human annotators. This baseline uses ChrF++ to evaluate the generated Wixárika captions against the reference captions in the pilot data. The top 5 systems will additionally undergo human evaluation on adequacy, fluency, faithfulness, and cultural appropriateness to determine the overall winner.

## Running the Baseline

The easiest way to run the baseline is through the [Colab notebook](https://colab.research.google.com/drive/1fexxQ2RPeQcetl_34i52l7BcFBqN_fqW?usp=sharing). It handles all setup, including cloning repositories, installing dependencies, and downloading the MT checkpoint. The notebook was run using an A100 GPU.


## Running the Baseline for All Languages

We provide a script to run the baseline for all languages.

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 2. Set Up the Translation Model

We use the [Sheffield 2023 submission](https://github.com/edwardgowsmith/americasnlp-2023-sheffield) to the AmericasNLP Translation Shared Task.

Install its dependencies:

```bash
pip install -r baseline/americasnlp-2023-sheffield/requirements.txt
pip install -e baseline/americasnlp-2023-sheffield/fairseq/
```

Download the translation checkpoint:

```bash
wget https://datasets-and-checkpoints.s3.us-east-1.amazonaws.com/americasnlp-2026/submission_3.pt
```

### 3. Run the Baseline

```bash
sh baseline/run_baseline.sh
```

> **Note:** Adjust the model and checkpoint paths in `run_baseline.sh` before running.
> Sheffield translation model does not support Maya, therefore, we do not report any baseline for Maya.

