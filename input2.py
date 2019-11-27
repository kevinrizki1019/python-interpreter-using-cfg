from kamarkost import tidurmalam
import kebahagiaan
import rasasenang
import kedamaiaan

KEBAHAGIAAN_INPUT_NAME = "input.jpg"
KESENANGANAN_OUTPUT_NAME = "result.txt"
ISI_HATI = []
for x in range(32,127):
    ISI_HATI.append(x)

def extract_kebahagiaan_from_isi_hati():
    PIPE_ASCII = 124
    
    time_start = time.perf_counter()
    text = pyterseract.image_to_string(Image.open(IMAGE_INPUT_NAME))