#!/usr/bin/env python3
"""
Usage:
    python evaluate_chrf.py --dataframe data.csv --translations wixarika_generated_captions.txt
"""

import argparse
import pandas as pd
from sacrebleu.metrics import CHRF


def chrf_score(ground_truth: str, generated_text: str) -> float:
    chrf = CHRF(word_order=2)
    return chrf.sentence_score(generated_text, [ground_truth]).score


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataframe", required=True)
    parser.add_argument("--translations", required=True)
    args = parser.parse_args()

    df = pd.read_json(args.dataframe, lines=True)

    with open(args.translations, "r", encoding="utf-8") as f:
        translated_captions = [line.strip() for line in f.readlines()]

    print(f"Number of translations: {len(translated_captions)}")
    print(f"Number of rows in dataframe: {len(df)}")
    assert len(translated_captions) == len(df), "Mismatch between translations and dataframe rows!"

    df["generated_caption"] = translated_captions

    df["chrf_score"] = df.apply(
        lambda row: chrf_score(row["target_caption"], row["generated_caption"]),
        axis=1,
    )

    print(f"Mean chrF++ score: {df['chrf_score'].mean():.2f}")


if __name__ == "__main__":
    main()