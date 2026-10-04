# ComfyUI-MasterAudioSaver

A studio-grade audio export and real-time canvas preview node for ComfyUI.

Designed for professional audio post-production, AI voice pipelines, and VFX sound workflows, this node bypasses the compressed or truncated audio exports of standard utilities. It writes pristine, uncompressed **32-bit float WAV** masters or high-fidelity **320kbps MP3s** directly to customizable export directories, while simultaneously generating an integrated in-canvas audio player for instant playback.

---

## Features

- **Mastering-Grade 32-Bit Float WAV:** Exports full uncompressed IEEE 32-bit floating point PCM audio masters without clipping or bit-depth quantization artifacts.
- **320kbps MP3 Encoding:** Direct high-bitrate MP3 compression powered by `torchaudio` for lightweight web and delivery exports.
- **Arbitrary Directory Routing:** Output audio directly to external project folders, shared network shares, or DAW hotfolders via custom absolute paths, with automatic fallback to ComfyUI's default output directory.
- **In-Canvas Interactive Audio Preview:** Automatically generates an interactive waveform audio player directly on the node inside the ComfyUI canvas upon queue execution.
- **Pipeline Pass-Through String:** Outputs the resolved absolute file path string to feed downstream automation, FFmpeg muxers, or asset-tracking nodes.

---

## Installation

1. Navigate to your ComfyUI custom nodes directory:
    cd ComfyUI/custom_nodes

2. Clone this repository:
    git clone https://github.com/harsh-shrivas/ComfyUI-MasterAudioSaver.git

3. Install required dependencies:
    pip install soundfile torchaudio

4. Restart ComfyUI.

---

## Usage

- **Category:** `Audio Processing`
- **Node Name:** `Master Audio Saver & Preview`
- **Workflow:**
  1. Route any ComfyUI `AUDIO` connection (waveform + sample rate) into the `audio` input pin.
  2. *(Optional)* Specify an absolute destination folder in `export_directory` (e.g., `Path\To\Destination\Folder`). Leaving this blank defaults to `ComfyUI/output`.
  3. Set your target filename in `filename_prefix`. Leaving this blank defaults to `Master_VO`.
  4. Select your export format: `wav (32-bit float)` or `mp3 (320kbps)`.
  5. Click **Queue Prompt**. The exported file will be written to disk, and the embedded audio player will populate directly on the node face for instant review.

---

## Inputs & Outputs

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| **audio** | `AUDIO` (Input) | *Required* | Raw audio dictionary containing waveform tensor and sample rate |
| **export_directory** | `STRING` (Input) | `""` | Destination path for the exported master file (supports absolute paths) |
| **filename_prefix** | `STRING` (Input) | `""` | Base name for the audio file (without extension) |
| **format** | `COMBO` (Input) | `wav (32-bit float)` | Audio encoding format: `wav (32-bit float)` or `mp3 (320kbps)` |
| **filepath** | `STRING` (Output) | — | Absolute file path of the saved master audio file |

---

## License

MIT License. Free to use, modify, and integrate into studio pipelines and commercial workflows.
