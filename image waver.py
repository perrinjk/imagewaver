from PIL import Image
import numpy as np
import math

def apply_wave_effect(image_path, output_path,):
    # Open the image
    img = Image.open(image_path)
    img = img.convert("RGBA")  # keep transparency
    width, height = img.size

    wavecount = 2 # total wave count
    wave_amplitude_percent = 0.05 # percent of total height that the waves reach
    
    wave_amplitude_pixels = int(height * wave_amplitude_percent * 0.5) # converts wave height to pixels
    wave_period_pixels = 1 / ((1/6) * width) * wavecount # converts wave count to period pixel count

    # increase canvas height to prevent flaps being cut off
    new_height = height + 2 * wave_amplitude_pixels
    wavy_array = np.zeros((new_height, width, 4), dtype=np.uint8)

    # convert image to numpy array
    img_array = np.array(img)

    for x in range(width):
        # calculate the wave offset for the current column
        offset = int(wave_amplitude_pixels * math.sin(wave_period_pixels * x))

        for y in range(height):
            new_y = y + offset + wave_amplitude_pixels  # add wave offset and padding
            
            # only draw pixel if in bounds
            if 0 <= new_y < new_height:
                wavy_array[new_y, x] = img_array[y, x]

    # convert the numpy array back to an image
    wavy_image = Image.fromarray(wavy_array, "RGBA")
    
    # save the wavy image
    wavy_image.save(output_path)
    print(f"Wavy image saved to {output_path}")

# rename both file names for desired effect
apply_wave_effect("AZflag.png", "AZflag_wavy.png")