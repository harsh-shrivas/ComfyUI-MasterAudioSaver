import os
import random
import soundfile as sf
import torchaudio
import folder_paths

class MasterAudioSaver:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = "output"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "audio": ("AUDIO",),
                "export_directory": ("STRING", {"default": ""}),
                "filename_prefix": ("STRING", {"default": ""}),
                "format": (["wav (32-bit float)", "mp3 (320kbps)"], {"default": "wav (32-bit float)"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("filepath",)
    FUNCTION = "process_audio"
    OUTPUT_NODE = True
    CATEGORY = "Audio Processing"

    def process_audio(self, audio, export_directory, filename_prefix, format):
        waveform = audio["waveform"]
        sample_rate = audio["sample_rate"]
        
        if waveform.ndim == 3:
            waveform = waveform.squeeze(0)

        # Fallback if fields are left blank
        target_dir = export_directory if export_directory.strip() else self.output_dir
        target_prefix = filename_prefix if filename_prefix.strip() else "Master_VO"

        os.makedirs(target_dir, exist_ok=True)
        is_wav = "wav" in format
        ext = "wav" if is_wav else "mp3"
        
        full_custom_path = os.path.join(target_dir, f"{target_prefix}.{ext}")
        
        # SAVE FULL 32-BIT FLOAT UNCOMPRESSED PCM (Matches 15.2MB size)
        if is_wav:
            sf.write(full_custom_path, waveform.cpu().numpy().T, sample_rate, subtype="FLOAT")
        else:
            torchaudio.save(full_custom_path, waveform.cpu(), sample_rate, format="mp3", compression_rate=320)

        # TEMP PREVIEW FOR UI PLAYER
        temp_dir = folder_paths.get_temp_directory()
        preview_file = f"preview_{random.randint(100000, 999999)}.wav"
        preview_path = os.path.join(temp_dir, preview_file)
        sf.write(preview_path, waveform.cpu().numpy().T, sample_rate, subtype="FLOAT")

        return {
            "ui": {
                "audio": [{
                    "filename": preview_file,
                    "type": "temp",
                    "subfolder": ""
                }]
            },
            "result": (full_custom_path,)
        }

NODE_CLASS_MAPPINGS = {"MasterAudioSaver": MasterAudioSaver}
NODE_DISPLAY_NAME_MAPPINGS = {"MasterAudioSaver": "Master Audio Saver & Preview"}
