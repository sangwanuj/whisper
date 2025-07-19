from faster_whisper.utils import download_model

model_names = ["tiny", "base", "large-v3", "turbo", "hi-large-v3"]

ALIAS_MAP = {
    "hi-large-v3": "ARTPARK-IISc/whisper-large-v3-vaani-hindi"
}

def download_model_weights(selected_model):
    actual = ALIAS_MAP.get(selected_model, selected_model)
    print(f"Downloading alias='{selected_model}' → actual='{actual}' …")
    download_model(actual, cache_dir=None)
    print(f"Finished downloading alias='{selected_model}'.")

for name in model_names:
    download_model_weights(name)

print("Finished downloading all models.")
