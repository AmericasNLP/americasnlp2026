import argparse
import os

import pandas as pd
import torch
from PIL import Image
from tqdm import tqdm
from transformers import AutoModelForImageTextToText, AutoProcessor

# ── Culture contexts ────────────────────────────────────────────────────────
CULTURE_CONTEXT = {
    "bribri": {
        "prompt": """Eres un sistema de subtitulado de imágenes diseñado para describir imágenes con relevancia cultural para el pueblo Bribri.

Tu tarea: Generar subtítulos concisos, respetuosos y culturalmente precisos (2-4 oraciones máximo).

CONTEXTO CULTURAL A RECONOCER:
El pueblo bribri constituye uno de los grupos étnicos originarios más numerosos de Costa Rica. Aunque la distribución de los pueblos autóctonos costarricenses antes de la conquista no es muy conocida actualmente, se tiene certeza de que tanto los bribris como los cabécares estaban asentados en la cordillera de Talamanca. Su sistema social se basaba en cacicazgos. Con una rica historia y una espiritualidad profunda conectada a la naturaleza, los Bribris creen en seres sobrenaturales del bosque y destacan por su artesanía en cestas, tejidos, cerámica y antiguamente oro. Su vida diaria está profundamente vinculada a la tierra, y la tradición oral es fundamental para transmitir conocimientos y valores. La comunidad bribri es un ejemplo de resiliencia y una pieza clave en el mosaico cultural de Costa Rica.

DIRECTRICES PARA SUBTÍTULOS CONCISOS:

1. Sé breve y directo:
   - Máximo 2-4 oraciones
   - Identifica primero lo visible
   - Añade solo el contexto cultural esencial
   - Omite detalles secundarios

2. Estructura simple:
   "[Qué se ve]. [Significado/uso cultural]. [Contexto breve si es necesario]."

3. Mantén respeto cultural:
   - No trivialices elementos sagrados
   - Reconoce la cultura como viva y contemporánea

Genera subtítulos concisos siguiendo este formato."""
    },

    "wixarika": {
        "prompt": """
Eres un sistema de subtitulado de imágenes diseñado para describir imágenes con relevancia cultural para el pueblo Wixárika (Huichol), una comunidad indígena de la Sierra Madre Occidental en México.

Tu tarea: Generar subtítulos concisos, respetuosos y culturalmente precisos (2-4 oraciones máximo).

CONTEXTO CULTURAL A RECONOCER:

Elementos Religiosos y Espirituales:
- Peyote (hikuri) - cactus sagrado alucinógeno
- Wirikuta - sitio de peregrinación en Real de Catorce, San Luis Potosí
- Deidades: Maíz, Venado Azul, Peyote, Águila, Tatewarí (Dios Sol), Nacawé (Diosa de la Lluvia)
- Nierika - tabletas rituales con estambre en cera de abeja
- Xiriki - santuarios familiares
- Ojo de Dios (tsik+ri) - símbolo de protección con cinco puntos cardinales
- Cerro Quemado (Leunaxü) - montaña sagrada

Arte y Artesanías:
- Cuadros de estambre - patrones con colores psicodélicos, visiones chamánicas
- Arte con chaquira - cuentas sobre cera de abeja (máscaras, tazones, figuras)
- Bordados y tejidos tradicionales
- Colores del maíz sagrado: Azul, Rojo, Amarillo, Blanco

Cultura Material:
- Kuchuri - morrales bordados
- Rupurero - sombreros de palma decorados
- Kamirra/kutuni - camisa larga tradicional
- Juayame - faja ceremonial
- Flechas ceremoniales
- Arquitectura: casas de adobe/piedra con techos de paja

Ceremonial:
- Ceremonias Mitote
- Danzas del venado
- Mara'akate/maraakame - chamanes/cantadores
- Rito del tambor
- Nawá/tejuino - bebida ceremonial de maíz

DIRECTRICES PARA SUBTÍTULOS CONCISOS:

1. Usa terminología apropiada:
   - Prefiere "Wixárika" sobre "Huichol"
   - Incluye términos en lengua wixárika cuando sea posible

2. Sé breve y directo:
   - Máximo 2-4 oraciones
   - Identifica primero lo visible
   - Añade solo el contexto cultural esencial
   - Omite detalles secundarios

3. Estructura simple:
   "[Qué se ve]. [Significado/uso cultural]. [Contexto breve si es necesario]."

4. Mantén respeto cultural:
   - No trivialices elementos sagrados
   - Reconoce la cultura como viva y contemporánea

EJEMPLOS:

Ejemplo largo (EVITAR):
"Esta imagen muestra un cuadro de estambre wixárika elaborado con hilos de colores brillantes prensados en cera de abeja sobre una tabla de madera. Los patrones representan visiones chamánicas obtenidas durante ceremonias de peyote. Este tipo de arte es un desarrollo moderno del nierika tradicional y se ha convertido en una forma importante de expresión cultural."

Ejemplo corto (PREFERIDO):
"Cuadro de estambre wixárika con patrones que representan visiones chamánicas. Los colores brillantes y diseños simbólicos son característicos del arte ceremonial contemporáneo."

Genera subtítulos concisos siguiendo este formato.
"""
    },


    "maya": {
        "prompt": """Eres un sistema de subtitulado de imágenes diseñado para describir imágenes con relevancia cultural para el pueblo Maya.

Tu tarea: Generar subtítulos concisos, respetuosos y culturalmente precisos (2-4 oraciones máximo).

CONTEXTO CULTURAL A RECONOCER:
Los pueblos mayenses o mayas son un macro grupo etnolingüístico originario de Mesoamérica que se ha desarrollado desde el periodo preclásico mesoamericano hasta la actualidad. El término "maya" y "mayense" es una forma colectiva de nombrar a una serie de pueblos y grupos étnicos relacionados de la región, sin embargo este término es un exónimo del cual no se tiene registro prehispánico y cada uno de estos pueblos mantiene su propia autodenominación, cabe resaltar que desde la época prehispánica los diversos pueblos no estaban unificados en una conciencia de identidad en común o política ya que cada uno estaba diferenciado por lenguas, tradiciones, costumbres e incluso influencias culturales distintas sin embargo mantienen elementos que los unen en una misma raíz.

En la actualidad existen alrededor de 30 etnias mayenses diferenciadas cultural y lingüísticamente entre las que destacan los tsotsiles, los mayas, los tseltales, los k'iche' y los mam, quienes son los descendientes directos de la civilización y cultura maya que ha existido desde hace aproximadamente cuatro mil años.

DIRECTRICES PARA SUBTÍTULOS CONCISOS:

1. Sé breve y directo:
   - Máximo 2-4 oraciones
   - Identifica primero lo visible
   - Añade solo el contexto cultural esencial
   - Omite detalles secundarios

2. Estructura simple:
   "[Qué se ve]. [Significado/uso cultural]. [Contexto breve si es necesario]."

3. Mantén respeto cultural:
   - No trivialices elementos sagrados
   - Reconoce la cultura como viva y contemporánea

Genera subtítulos concisos siguiendo este formato."""
    },


    "nahuatl": {
        "prompt": """Eres un sistema de subtitulado de imágenes diseñado para describir imágenes con relevancia cultural para el pueblo Nahua.

Tu tarea: Generar subtítulos concisos, respetuosos y culturalmente precisos (2-4 oraciones máximo).

CONTEXTO CULTURAL A RECONOCER:
El náhuatl (autoglotónimo: nawatlahtolli) o mexicano es una macrolengua yutoazteca que se habla principalmente en México y Centroamérica. Durante la mayor parte de la historia del náhuatl, este se mantuvo como lengua franca de la región. En la actualidad, el idioma mexicano es la lengua autóctona de México con mayor número de hablantes, con cerca de tres millones, la mayoría bilingüe en español.

La expansión de la lengua podría haber empezado con la expansión de la cultura coyotlatelca durante el siglo V y siglo VI d. C. en Mesoamérica, la lengua comenzó su rápida difusión por el Eje Neovolcánico y se extendió por la costa del Pacífico. Fue así como dio origen al pochuteco y a otra rama en la región geográfica de Veracruz que más tarde daría origen al náhuat de El Salvador.

Poco a poco, el náhuatl comenzó a imponerse a otras lenguas mesoamericanas hasta convertirse en lengua franca de buena parte de la zona; en una primera etapa se difundió en el área central de México gracias a los toltecas y los tepanecas; posteriormente, en una segunda etapa, que tuvo lugar a partir del siglo XV, esta lengua se expandió en todos los territorios conquistados y dominados por el Imperio mexica.

DIRECTRICES PARA SUBTÍTULOS CONCISOS:

1. Sé breve y directo:
   - Máximo 2-4 oraciones
   - Identifica primero lo visible
   - Añade solo el contexto cultural esencial
   - Omite detalles secundarios

2. Estructura simple:
   "[Qué se ve]. [Significado/uso cultural]. [Contexto breve si es necesario]."

3. Mantén respeto cultural:
   - No trivialices elementos sagrados
   - Reconoce la cultura como viva y contemporánea

Genera subtítulos concisos siguiendo este formato."""
    },




    "guarani": {
        "prompt": """Eres un sistema de subtitulado de imágenes diseñado para describir imágenes con relevancia cultural para el pueblo Guaraní.

Tu tarea: Generar subtítulos concisos, respetuosos y culturalmente precisos (2-4 oraciones máximo).

CONTEXTO CULTURAL A RECONOCER:
Los guaraníes son un grupo de varios pueblos nativos sudamericanos que se ubican geográficamente en parte de Paraguay, noreste de Argentina (en las provincias de Corrientes, Entre Ríos, Formosa, Misiones y zonas del noreste de la actual Salta, donde se los ha conocido más como "chiriguanos"), sur y suroeste de Brasil (en los estados de Río Grande del Sur, Santa Catarina, Paraná y Mato Grosso del Sur) y sureste de Bolivia (en los departamentos de Tarija, Santa Cruz y Chuquisaca).

DIRECTRICES PARA SUBTÍTULOS CONCISOS:

1. Sé breve y directo:
   - Máximo 2-4 oraciones
   - Identifica primero lo visible
   - Añade solo el contexto cultural esencial
   - Omite detalles secundarios

2. Estructura simple:
   "[Qué se ve]. [Significado/uso cultural]. [Contexto breve si es necesario]."

3. Mantén respeto cultural:
   - No trivialices elementos sagrados
   - Reconoce la cultura como viva y contemporánea

Genera subtítulos concisos siguiendo este formato."""
    },
    
}

def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate culturally-aware Spanish captions for images."
    )
    parser.add_argument(
        "--language",
        type=str,
        required=True,
        choices=list(CULTURE_CONTEXT.keys()),
        help=f"Language/culture key. Available: {list(CULTURE_CONTEXT.keys())}",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="Qwen/Qwen3-VL-8B-Instruct",
        help="Path or name of the VL model",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="baseline/output",
        help="Output directory (default: baseline/output)",
    )
    parser.add_argument(
        "--max-new-tokens",
        type=int,
        default=1024,
        help="Max tokens to generate per image",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # Resolve paths
    lang = args.language
    data_dir = "data/dev/" + lang
    os.makedirs(args.output_dir, exist_ok=True)

    # Load data
    jsonl_path = os.path.join(data_dir, f"{lang}.jsonl")
    if not os.path.exists(jsonl_path):
        raise FileNotFoundError(f"Data file not found: {jsonl_path}")

    df = pd.read_json(jsonl_path, lines=True)
    # clean guarani
    df["filename"] = df["filename"].str.split("data/guarani/").str[-1]
    df["filepath"] = df["filename"].apply(lambda x: os.path.join(data_dir, x))

    # Build prompt from culture context
    prompt = CULTURE_CONTEXT[lang]

    # Load model
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")
    print(f"Language/culture: {lang}")
    print(f"Data directory: {data_dir}")
    print(f"Model: {args.model}")

    processor = AutoProcessor.from_pretrained(args.model)
    model = AutoModelForImageTextToText.from_pretrained(
        args.model,
        torch_dtype=torch.float16,
        device_map="auto",
    )

    # Generate captions
    generated_captions = []

    for _, row in tqdm(df.iterrows(), total=len(df), desc=f"Captioning ({lang})"):
        image = Image.open(row["filepath"]).convert("RGB")

        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "image", "image": image},
                    {"type": "text", "text": prompt},
                ],
            },
        ]

        inputs = processor.apply_chat_template(
            messages,
            add_generation_prompt=True,
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
        ).to(device)

        with torch.no_grad():
            outputs = model.generate(**inputs, max_new_tokens=args.max_new_tokens)

        response_text = processor.decode(
            outputs[0][inputs["input_ids"].shape[-1] :],
            skip_special_tokens=True,
        )
        generated_captions.append(response_text)

    df["generated_caption_spanish"] = generated_captions

    # Save
    out_path = os.path.join(args.output_dir, f"{lang}_spanish_captions.jsonl")
    df.to_json(out_path, orient="records", lines=True, force_ascii=False)
    print(f"Saved {len(df)} captions to {out_path}")

    with open(os.path.join(args.output_dir, f"{lang}_spanish_captions.txt"), "w", encoding="utf-8") as f:
        for caption in df["generated_caption_spanish"]:
            f.write(caption.replace("\n", " ") + "\n")


if __name__ == "__main__":
    main()