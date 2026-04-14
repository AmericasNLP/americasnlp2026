MODEL="Qwen/Qwen3-VL-8B-Instruct"
TRANSLATION_CHECKPOINT="submission_3.pt"

# wixarika
python baseline/caption_generation.py --model $MODEL --language wixarika
python baseline/americasnlp-2023-sheffield/translate.py --checkpoint $TRANSLATION_CHECKPOINT  --input baseline/output/wixarika_spanish_captions.txt --output baseline/output/wixarika_translated_captions.txt --src spa_Latn --tgt hch_Latn 


# bribri
python baseline/caption_generation.py --model $MODEL --language bribri
python baseline/americasnlp-2023-sheffield/translate.py --checkpoint $TRANSLATION_CHECKPOINT  --input baseline/output/bribri_spanish_captions.txt --output baseline/output/bribri_translated_captions.txt --src spa_Latn --tgt bzd_Latn


## guarani
python baseline/caption_generation.py --model $MODEL --language guarani
python baseline/americasnlp-2023-sheffield/translate.py --checkpoint $TRANSLATION_CHECKPOINT  --input baseline/output/guarani_spanish_captions.txt --output baseline/output/guarani_translated_captions.txt --src spa_Latn --tgt grn_Latn


## nahuatl
python baseline/caption_generation.py --model $MODEL --language nahuatl
python baseline/americasnlp-2023-sheffield/translate.py --checkpoint $TRANSLATION_CHECKPOINT  --input baseline/output/nahuatl_spanish_captions.txt --output baseline/output/nahuatl_translated_captions.txt --src spa_Latn --tgt nah_Latn


## maya
python baseline/caption_generation.py --model $MODEL --language maya
#python baseline/americasnlp-2023-sheffield/translate.py --checkpoint $TRANSLATION_CHECKPOINT  --input baseline/output/maya_spanish_captions.txt --output baseline/output/maya_translated_captions.txt --src spa_Latn --tgt yua_Latn


# Eval
echo "=== Evaluating: Wixarika ==="
python baseline/eval.py --dataframe baseline/output/wixarika_spanish_captions.jsonl --translations baseline/output/wixarika_translated_captions.txt
echo "=== Evaluating: Bribri ==="
python baseline/eval.py --dataframe baseline/output/bribri_spanish_captions.jsonl --translations baseline/output/bribri_translated_captions.txt
echo "=== Evaluating: Guarani ==="
python baseline/eval.py --dataframe baseline/output/guarani_spanish_captions.jsonl --translations baseline/output/guarani_translated_captions.txt
echo "=== Evaluating: Nahuatl ==="
python baseline/eval.py --dataframe baseline/output/nahuatl_spanish_captions.jsonl --translations baseline/output/nahuatl_translated_captions.txt
echo "=== Evaluating: Maya ==="
python baseline/eval.py --dataframe baseline/output/maya_spanish_captions.jsonl --translations baseline/output/maya_translated_captions.txt